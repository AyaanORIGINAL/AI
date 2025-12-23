# Admissions Chatbot

This repository contains a small AI-powered admissions chatbot for school admission queries. It supports an OpenAI-backed mode (if `OPENAI_API_KEY` is set) and a rule-based fallback if no API key is available.

Files:

- `admission_chatbot.py` — main CLI/web chatbot entrypoint.
- `requirements.txt` — Python dependencies (optional).

Quick start (CLI):

1. Create a virtual environment and install dependencies (optional):

```bash
python -m venv .venv
source .venv/bin/activate   # on Windows use: .venv\Scripts\activate
pip install -r requirements.txt
```

2. (Optional) Set `OPENAI_API_KEY` to enable AI responses:

```bash
export OPENAI_API_KEY="sk-..."   # Windows (PowerShell): $env:OPENAI_API_KEY = 'sk-...'
```

3. Run the CLI chatbot:

```bash
python admission_chatbot.py
```

Run as a tiny web server (requires Flask):

```bash
python admission_chatbot.py --web
# then POST JSON {"message": "..."} to http://127.0.0.1:5000/chat
```

Behavior:

- If `OPENAI_API_KEY` is present and `openai` is installed, queries are sent to the OpenAI ChatCompletion API.
- Otherwise, a simple rule-based helper answers common admissions questions.

Next steps you might want:

- Hook the bot into your school's admission database for personalized status checks.
- Add richer fallback flows to collect applicant data and export CSVs.
- Integrate with messaging platforms (Slack, MS Teams) or build a web UI.
