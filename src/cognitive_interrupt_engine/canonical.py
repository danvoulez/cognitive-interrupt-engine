"""Non-normative content identity helpers for the repository examples.

The architecture requires RFC 8785 / JCS for production structural identity.
This module intentionally implements only a restricted JCS-compatible subset so
examples can execute without silently pretending that ``json.dumps`` is a full
JCS implementation.

Supported values:
- null / booleans
- strings
- integers in the IEEE-754 safe integer range
- arrays of supported values
- objects with ASCII string keys and supported values

Floats, non-ASCII object keys, and integers outside the safe range are rejected.
A production implementation MUST use a pinned, tested RFC 8785 implementation.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any

_SAFE_INT_MAX = (1 << 53) - 1


def _validate_demo_value(value: Any, path: str = "$") -> None:
    if value is None or isinstance(value, (bool, str)):
        return
    if isinstance(value, int) and not isinstance(value, bool):
        if not -_SAFE_INT_MAX <= value <= _SAFE_INT_MAX:
            raise ValueError(f"integer outside JCS-safe demo range at {path}")
        return
    if isinstance(value, float):
        raise TypeError(
            f"floats are intentionally unsupported by the demo canonicalizer at {path}; "
            "use a pinned RFC 8785 implementation"
        )
    if isinstance(value, list):
        for index, item in enumerate(value):
            _validate_demo_value(item, f"{path}[{index}]")
        return
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise TypeError(f"object key is not a string at {path}")
            if not key.isascii():
                raise ValueError(
                    f"non-ASCII object key at {path}.{key!r}; demo helper cannot "
                    "guarantee RFC 8785 key ordering"
                )
            _validate_demo_value(item, f"{path}.{key}")
        return
    raise TypeError(f"unsupported JSON value at {path}: {type(value).__name__}")


def canonical_json(value: Any) -> bytes:
    """Return deterministic UTF-8 JSON for the restricted demo profile."""
    _validate_demo_value(value)
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def content_hash(value: Any) -> str:
    """Return a ``sha256:``-prefixed identity for the demo profile."""
    digest = hashlib.sha256(canonical_json(value)).hexdigest()
    return f"sha256:{digest}"
