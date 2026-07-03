# Contributing to Claude Platform Python Example

## Branching Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Production-ready, protected — PR-only |
| `develop` | Integration — all PRs target here |
| `feature/<name>` | New features from `develop` |
| `fix/<name>` | Bug fixes from `develop` |
| `hotfix/<name>` | Critical fixes from `main` |

## Workflow
1. `git checkout -b feature/your-feature develop`
2. Commit with clear messages
3. Open PR targeting `develop`

## Commit Format
```
type(scope): short description
Types: feat | fix | docs | style | refactor | test | chore | security
```

## Security Requirements
- API key must come from `ANTHROPIC_API_KEY` env var or `.env` file only
- Never hardcode API keys in source, tests, or examples
- `.env` must remain in `.gitignore`
- See [SECURITY.md](SECURITY.md)
