# Security Policy

## Supported Versions
| Version | Supported |
|---------|-----------|
| `main` | ✅ |
| `develop` | ✅ |
| Older | ❌ |

## Reporting
**Do not open public issues for security vulnerabilities.**
Email: imranali.mohammed@cotiviti.com
Response within 48 hours, fix timeline within 7 days.

## Security Controls
| Control | Implementation |
|---------|---------------|
| API key | `ANTHROPIC_API_KEY` env var or `.env` file — never hardcoded |
| `.env` | Excluded from version control via `.gitignore` |
| User input | Passed as data to API — not interpolated into system prompt |
| No logging | API key and conversation content not written to logs or files |
