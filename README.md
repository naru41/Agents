# Agents

Shared Codex rules for delegating bounded, low-risk work to local Qwen.

## Use in another project

Copy `AGENTS.md` to the project root, or add this repository as a submodule:

```sh
git submodule add https://github.com/naru41/Agents.git .agents
```

For submodule use, add this instruction to the project's root `AGENTS.md`:

```md
Before starting any task, read and follow `.agents/AGENTS.md`.
```

## Solution agent entrypoint

`solution_agent.run(request, dispatch)` accepts a prompt request and returns any JSON-compatible output. The host owns the model/provider and supplies the async `dispatch(system_prompt, request)` callback, so this repository stays provider-independent.
