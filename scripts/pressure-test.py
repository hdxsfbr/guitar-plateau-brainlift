#!/usr/bin/env python3
"""Run the BrainLift POV pressure-test prompt via OpenRouter.
Usage: pressure_test.py <model> <pov_file> <out_prefix>
Reads the API key from ~/.config/agentforge/openrouter_api_key at run time; never prints or saves it."""
import json, os, sys, time, urllib.request
PROMPT = ("Evaluate this education POV: {pov} Where is it weak or unlikely to work? Identify the strongest objection, "
          "the specific constraint behind it, and the evidence needed to resolve it. Give an honest assessment; "
          "do not agree or disagree just because I asked.")
model, pov_file, out = sys.argv[1], sys.argv[2], sys.argv[3]
pov = open(pov_file, encoding='utf-8').read().strip()
prompt = PROMPT.format(pov=pov)
key = open(os.path.expanduser('~/.config/agentforge/openrouter_api_key')).read().strip()
body = {"model": model, "messages": [{"role": "user", "content": prompt}], "max_tokens": 8000, "usage": {"include": True}}
req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=json.dumps(body).encode(),
      headers={"Authorization": "Bearer " + key, "Content-Type": "application/json",
               "X-Title": "guitar-plateau-brainlift pressure test"})
del key
t0 = time.strftime('%Y-%m-%d %H:%M:%S %Z')
resp = json.load(urllib.request.urlopen(req, timeout=600))
t1 = time.strftime('%Y-%m-%d %H:%M:%S %Z')
text = resp["choices"][0]["message"]["content"]
with open(out + '.md', 'w', encoding='utf-8') as f:
    f.write(f"<!-- model requested: {model}; model returned: {resp.get('model')}; started {t0}; finished {t1}; "
            f"usage: {json.dumps(resp.get('usage'))} -->\n\n## Prompt (verbatim)\n\n{prompt}\n\n## Response (verbatim)\n\n{text}\n")
with open(out + '.json', 'w', encoding='utf-8') as f:
    json.dump({"request": {"model": model, "messages": body["messages"], "max_tokens": 8000},
               "started": t0, "finished": t1, "response": resp}, f, ensure_ascii=False, indent=1)
u = resp.get('usage') or {}
print(out, resp.get('model'), 'tokens', u.get('prompt_tokens'), u.get('completion_tokens'), 'cost', u.get('cost'))
