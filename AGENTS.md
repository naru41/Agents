# Shared Agent Rules

## Delegate Bounded Tasks to Local Qwen

- Before Codex completes an eligible low-risk task, run `E:\LocalLLM\chat-qwen.ps1 -Prompt <complete-task>` and use its result as the first draft.
- Eligible tasks are data-format conversion; fixtures, mocks, and seed data; first drafts of documentation, changelogs, and API docs; translation and localization; log or text summarization and classification; boilerplate; unit-test drafts from supplied code; mechanical code edits; SQL, regex, and shell snippets; first-pass code review or stack-trace analysis; and QA or acceptance checklists.
- For repository tasks, use Graft first when available and include only the minimal relevant task, constraints, and source spans. Request a concise patch, code block, JSON result, or summary without long reasoning or logs.
- Qwen is text-only through this runner. Codex must inspect its output, apply changes, run relevant validation, and remain responsible for the final result.
- Do not delegate authentication, authorization, cryptography, security decisions, destructive data migrations, production incidents, cross-system architecture, current external API facts, deployment or release actions, destructive Git operations, or final merge review.
- Never use Ollama, `ollama run`, or an Ollama API for delegated or local-model work. If Qwen fails, report the blocker instead of silently falling back.
