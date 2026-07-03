#!/usr/bin/env python3
"""
Claude Platform Python Example
================================
Demonstrates the Anthropic Python SDK:
  - Single message completion with prompt caching
  - Streaming response
  - Multi-turn interactive chat

Setup:
    uv pip install anthropic python-dotenv
    $env:ANTHROPIC_API_KEY = "sk-ant-..."   # Windows PowerShell

Usage:
    python main.py
"""

import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent / ".env")
except ImportError:
    pass

try:
    import anthropic
except ImportError:
    print("ERROR: anthropic package not installed.")
    print("  Run: uv pip install anthropic python-dotenv")
    sys.exit(1)

MODEL = "claude-sonnet-4-6"

SYSTEM = (
    "You are a helpful, concise assistant. "
    "Answer questions clearly and accurately."
)


def _make_client() -> anthropic.Anthropic:
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not key:
        print("ERROR: ANTHROPIC_API_KEY is not set.")
        print("  PowerShell: $env:ANTHROPIC_API_KEY = 'sk-ant-...'")
        print("  Or copy .env.example -> .env and add your key.")
        sys.exit(1)
    return anthropic.Anthropic(api_key=key)


def single_message(client: anthropic.Anthropic, prompt: str) -> str:
    """One-shot completion with a cached system prompt."""
    resp = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=[
            {
                "type": "text",
                "text": SYSTEM,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.content[0].text


def stream_message(client: anthropic.Anthropic, prompt: str) -> None:
    """Stream tokens to stdout as they arrive."""
    print("Claude: ", end="", flush=True)
    with client.messages.stream(
        model=MODEL,
        max_tokens=1024,
        system=[
            {
                "type": "text",
                "text": SYSTEM,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        for chunk in stream.text_stream:
            print(chunk, end="", flush=True)
    print()


def interactive_chat(client: anthropic.Anthropic) -> None:
    """Multi-turn chat loop that keeps the full conversation history."""
    history: list[dict] = []
    print(f"\n[Interactive Chat — {MODEL}]")
    print("Type 'quit' or press Ctrl+C to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "bye"):
            print("Goodbye!")
            break

        history.append({"role": "user", "content": user_input})

        resp = client.messages.create(
            model=MODEL,
            max_tokens=2048,
            system=[
                {
                    "type": "text",
                    "text": SYSTEM,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            messages=history,
        )

        reply = resp.content[0].text
        history.append({"role": "assistant", "content": reply})
        print(f"Claude: {reply}")

        u = resp.usage
        cached = getattr(u, "cache_read_input_tokens", 0) or 0
        print(f"  [tokens in={u.input_tokens} cached={cached} out={u.output_tokens}]\n")


def main() -> None:
    client = _make_client()

    print("=== 1. Single message ===")
    answer = single_message(client, "What is prompt caching and why does it save money?")
    print(f"Claude: {answer}\n")

    print("=== 2. Streaming ===")
    stream_message(client, "List three things that make Python popular. One sentence each.")
    print()

    print("=== 3. Interactive chat ===")
    interactive_chat(client)


if __name__ == "__main__":
    main()
