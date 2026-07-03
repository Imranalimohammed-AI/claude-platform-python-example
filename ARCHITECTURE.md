# Architecture — Claude Platform Python Example

## Component overview

```
ClaudePlatformPythonExample/
  main.py
    ├── _make_client()        reads ANTHROPIC_API_KEY from env
    ├── single_message()      one-shot POST /v1/messages
    ├── stream_message()      streaming POST /v1/messages
    └── interactive_chat()    multi-turn loop with history list

  .env / .env.example         API key (never committed)
  requirements.in             source deps: anthropic, python-dotenv
  requirements.txt            pinned deps
```

## Request flow

```
User prompt
  └─► Build messages list [{role, content}, ...]
        └─► anthropic.Anthropic.messages.create()
              └─► POST https://api.anthropic.com/v1/messages
                    Headers: x-api-key, anthropic-version
                    Body:    model, max_tokens, system (cached), messages
                    └─► Response JSON
                          └─► content[0].text  →  printed to stdout
```

## Prompt caching

```
System message block:
  { "type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"} }

First call:  full system-prompt tokens billed  →  cache WRITE
Subsequent:  cache_read_input_tokens billed at ~10%  →  cache HIT
Cache TTL:   5 minutes from last use
```

## Streaming flow

```
client.messages.stream(...)   →  SSE connection kept open
  for chunk in stream.text_stream:
    print(chunk, end="", flush=True)   →  token-by-token output
```

## Multi-turn history

```
history = []
─── turn 1 ──────────────────────────────────
history.append({"role": "user",      "content": user_input})
resp = client.messages.create(..., messages=history)
history.append({"role": "assistant", "content": reply})
─── turn 2 ──────────────────────────────────
(same history list grows; full context sent on every request)
```

## Key decisions

| Decision | Rationale |
|---|---|
| Env var for API key | Prevents accidental secrets in source or logs |
| `cache_control: ephemeral` on system | Cuts repeat-call cost without any code change |
| `python-dotenv` optional | Dev convenience; env var always takes precedence |
| `list[dict]` history | Simplest multi-turn; swap for a database if persistence is needed |
