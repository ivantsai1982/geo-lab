"""S5-1: embed every non-ad claim (F14) with OpenAI text-embedding-3-small.
Keys are read from a file outside the project (path in env GEO_KEYS); never stored in the repo.
Output: data/full/s5/claims.jsonl (id, author, thread, level, topic, claim), claims_emb.npy
"""
import json, os, sqlite3, time, requests, numpy as np, sys
sys.stdout.reconfigure(encoding="utf-8")
R = "G:/學習雜亂/GEO學習/"; OUT = R + "data/full/s5/"; os.makedirs(OUT, exist_ok=True)
K = json.load(open(os.environ["GEO_KEYS"], encoding="utf-8"))
F = {o["id"]: o for o in map(json.loads, open(R + "data/full/s2/final_items.jsonl", encoding="utf-8"))}
d = json.load(open(R + "data/full/s4/softad_flags.json", encoding="utf-8"))
fl, rep = d["flags"], set(d["reposts"])
db = sqlite3.connect(R + "data/reddit.db")
meta = {}
for pid, a in db.execute("select id, author from posts"): meta["p_" + pid] = (a, pid)
for cid, a, pid in db.execute("select id, author, post_id from comments"): meta["c_" + cid] = (a, pid)

rows = []
for i, o in F.items():
    c = (o.get("F14") or "無").strip()
    if c == "無" or o["未決"] or i in fl or i in rep: continue
    a, t = meta[i]
    rows.append({"id": i, "author": a, "thread": t, "level": o["level"], "topic": o["F13"], "claim": c})
print("claims", len(rows))

embs = []
for s in range(0, len(rows), 500):
    batch = [r["claim"] for r in rows[s:s + 500]]
    for attempt in range(5):
        r = requests.post("https://api.openai.com/v1/embeddings", headers={"Authorization": "Bearer " + K["openai"]},
                          json={"model": "text-embedding-3-small", "input": batch}, timeout=120)
        if r.ok: break
        time.sleep(5 * (attempt + 1))
    r.raise_for_status()
    embs += [x["embedding"] for x in sorted(r.json()["data"], key=lambda x: x["index"])]
    print(s + len(batch), end=" ", flush=True)
E = np.array(embs, dtype=np.float32)
E /= np.linalg.norm(E, axis=1, keepdims=True)
np.save(OUT + "claims_emb.npy", E)
with open(OUT + "claims.jsonl", "w", encoding="utf-8") as w:
    for r in rows: w.write(json.dumps(r, ensure_ascii=False) + "\n")
print("\nsaved", E.shape)
