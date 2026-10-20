import re
# v0.2 詞表：補上單獨的 AI / IA / KI / 人工智能 等（第一輪漏檢的 4 串均因此）
AI_LEX = re.compile(r'\b(ai|a\.i\.|ia|ki|geo|aeo|llmo|gpt\w*|chatgpt|openai|perplexity|gemini|claude|copilot|llms?|ai overviews?|aio|'
                    r'sge|generative|answer engines?|llms\.txt|oai-searchbot|gptbot|perplexitybot|claudebot|google-extended|'
                    r'searchgpt|cited|citations?|grok|deepseek|chatbots?|language models?)\b|人工智能|人工智慧|大模型', re.I)
