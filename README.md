<div align="center">

# Claude Platform Python Example

**Production-ready Python starter for the Anthropic Claude API**

[![Python](https://img.shields.io/badge/Python-3.14-3776ab?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Anthropic](https://img.shields.io/badge/Anthropic_SDK-latest-cc785c?style=flat-square)](https://docs.anthropic.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](LICENSE)
[![Branch](https://img.shields.io/badge/branch-main-3b82f6?style=flat-square&logo=git&logoColor=white)](https://github.com/Imranalimohammed-AI/claude-platform-python-example)

</div>

---

## Overview

A minimal, production-ready Python starter demonstrating three core Anthropic SDK patterns — single message, streaming, and multi-turn chat — with prompt caching enabled out of the box.

---

## SDK Patterns Demonstrated

| Pattern | Description |
|---------|-------------|
| **Single message** | One-shot completion with a cached system prompt |
| **Streaming** | Print tokens as they arrive using the streaming API |
| **Multi-turn chat** | Full conversation history loop |

---

## Models

| Model ID | Best for |
|----------|----------|
| `claude-opus-4-8` | Most capable, complex reasoning |
| `claude-sonnet-4-6` | Balanced speed + capability (default) |
| `claude-haiku-4-5-20251001` | Fastest, lowest cost |

Change the `MODEL` constant in `main.py` to switch models.

---

## Prompt Caching

All calls use `cache_control: ephemeral` on the system prompt. On repeated calls within the same TTL window, cached tokens are billed at ~10% of standard input price — reducing cost and latency for high-frequency use cases.

---

## Branch Strategy

```
main          ← production, protected (PR-only)
  └── develop ← integration, all PRs target here
        ├── feature/<name>
        ├── fix/<name>
        └── hotfix/<name>
```

---

## Quick Start

```powershell
# Clone
git clone git@github.com:Imranalimohammed-AI/claude-platform-python-example.git
cd claude-platform-python-example

# Create virtual environment
uv venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
uv pip install anthropic python-dotenv

# Set API key
Copy-Item .env.example .env
# Edit .env: replace placeholder with your real key

# Run
python main.py
```

---

## Project Structure

| File | Purpose |
|------|---------|
| `main.py` | Three demo patterns: single, streaming, interactive chat |
| `requirements.txt` | Pinned dependencies |
| `.env.example` | Environment variable template |
| `ARCHITECTURE.md` | API flow and caching reference |

---

## Security

| Control | Implementation |
|---------|---------------|
| API key | `ANTHROPIC_API_KEY` env var or `.env` — never hardcoded |
| `.env` | Excluded from version control |
| User input | Passed as data to API — not interpolated into system prompt |

See [SECURITY.md](SECURITY.md) for the full policy.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for branching strategy and PR guidelines.

## License

MIT © 2026 Imranali Mohammed — see [LICENSE](LICENSE)
