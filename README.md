# Claude Platform Python Example

A minimal, production-ready Python starter for the Anthropic Claude API.

Demonstrates three core SDK patterns:
- **Single message** — one-shot completion with a cached system prompt
- **Streaming** — print tokens as they arrive
- **Multi-turn chat** — full conversation history loop

## Quick start

```powershell
# 1. Activate the shared project venv
cd AI-Vibecoding
.\.venv\Scripts\Activate.ps1

# 2. Install dependencies
uv pip install anthropic python-dotenv

# 3. Set your API key (option A — env var)
$env:ANTHROPIC_API_KEY = "sk-ant-..."

# 3. Set your API key (option B — .env file)
Copy-Item ClaudePlatformPythonExample\.env.example ClaudePlatformPythonExample\.env
# Edit .env and replace sk-ant-api03-YOUR_KEY_HERE with your real key

# 4. Run
python ClaudePlatformPythonExample\main.py
```

## Files

| File | Purpose |
|---|---|
| `main.py` | Three demo patterns: single, streaming, interactive chat |
| `requirements.in` | Source dependencies (edit to add packages) |
| `requirements.txt` | Pinned dependencies |
| `.env.example` | Environment variable template — copy to `.env` |
| `README.md` | This file |
| `ARCHITECTURE.md` | Architecture and API flow reference |

## Available models

Change the `MODEL` constant in `main.py`:

| Model ID | Best for |
|---|---|
| `claude-opus-4-8` | Most capable, complex reasoning |
| `claude-sonnet-4-6` | Balanced speed + capability (default) |
| `claude-haiku-4-5-20251001` | Fastest, lowest cost |

## Prompt caching

All calls use `cache_control: ephemeral` on the system prompt. On repeated calls within the same session the cached tokens are billed at ~10% of standard input price, reducing cost and latency.

## Security notes

- API key is read from the environment only — never hardcoded.
- `.env` is not committed to version control (add it to `.gitignore`).
- All user input is passed as data to the API, not interpolated into the system prompt.
