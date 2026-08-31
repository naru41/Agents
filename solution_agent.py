"""Small, provider-agnostic solution-agent contract for host applications."""

import json
from collections.abc import Awaitable, Callable, Mapping
from typing import Any


SYSTEM_PROMPT = (
    "You are an auxiliary solution agent. Complete the request and return the most useful result directly "
    "in the same language as the request. Plain text or JSON is allowed. Do not mention delegation."
)
Dispatch = Callable[[str, dict[str, Any]], Awaitable[Any]]


async def run(request: Mapping[str, Any], dispatch: Dispatch) -> Any:
    """Send one prompt request through the host dispatcher and preserve any JSON-compatible output."""
    prompt = request.get("prompt")
    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError("prompt is required")
    output = await dispatch(SYSTEM_PROMPT, {"prompt": prompt.strip(), "context": request.get("context")})
    if not isinstance(output, str):
        return output
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        return output
