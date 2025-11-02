#!/usr/bin/env python3
import sys

commit_message = sys.argv[1] if len(sys.argv) > 1 else ""

# Simple validation logic (placeholder for Copilot/OpenAI)
if len(commit_message.split()) < 3:
    print("❌ Commit blocked due to vague message.")
    sys.exit(1)

print("✅ Commit message looks meaningful.")
sys.exit(0)
