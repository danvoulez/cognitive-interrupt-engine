# Provenance of the Reference Mapping

The portable Cognitive Interrupt architecture is independent of any one framework. The concrete ADK/Jev/Braintrust claims in this repository were checked against a frozen design corpus dated **2026-09-20**.

## Frozen artifacts

| Artifact | SHA-256 |
|---|---|
| `adk-metabolize-canonical.zip` | `c03c4817e03e0934b6e47029704b3113fa8915476ec4e68a6333f8afa19210db` |
| `adk-python-source.zip` | `e84bdffb56fc6c5cfa7ebbc32397862e1dd5e1ace05eed20f87dc21b953dc56c` |
| `semantic-metabolize-canonical.zip` | `24527bf93ec55c18d17f6f6e1ba35f1d086fc08113434f98deda3e7c7d33e44c` |
| `braintrust-metabolize-canonical.zip` | `1ed9b589915298107a01bbcf07c39efd55113b8a294009d895a7ff456937be14` |

The enclosing handoff archive used during the repository audit had SHA-256:

```text
dd39e8431e892c98fecf8b9aac75f5ef7dcd56bc4ea5caa3384a992b0dc0a292
```

These hashes are evidence identifiers, not dependencies that must ship with the repository.

## Version boundary

The concrete mapping was checked against:

- Google ADK **2.9.0** source contained in the frozen handoff;
- Jev **`jev-1.13.0`**, TypeSafe API **0.2.0**, snapshot dated 2026-09-20;
- Braintrust Python SDK **0.41.0**;
- Braintrust TypeSafe integration contract requiring `typesafe-sdk >= 0.6.0` in the frozen mapping.

## Claims rechecked during repository audit

### ADK

Source paths in the frozen ADK tree establish that:

- `events/request_input.py` defines `RequestInput` with `interrupt_id`, `payload`, `message`, and `response_schema`;
- `workflow/_function_node.py` passes `RequestInput` through as workflow control flow;
- `workflow/_workflow.py` checkpoints waiting nodes and preserves interrupt ids in resumable execution;
- `runners.py` reconstructs resume inputs from function responses and resolves them to an existing invocation;
- `apps/_configs.py` marks `ResumabilityConfig` experimental and documents best-effort, at-least-once resumption with loss of in-memory state;
- `workflow/utils/_rehydration_utils.py` validates simple response schemas but explicitly falls back or skips full validation for complex raw JSON Schema shapes. The Engine therefore validates the full output contract itself before resumption.

### Jev

The frozen ADK/Jev pair map establishes:

- Jev is not mapped to ADK `BaseLlm`;
- Noul, Choice, and Score are separate semantic primitives;
- Noul has no confidence field;
- several questions can share one state in a sensor-pack request;
- routing remains owned by the host workflow after semantic judgment.

### Braintrust

The frozen Braintrust pair maps establish for **Braintrust 0.41.0 + ADK 2.9.0**:

- native ADK instrumentation does not observe `google.adk.workflow` graph/node/edge/route semantics;
- both non-MCP ADK tool patch targets miss the pinned ADK source;
- targeted OpenTelemetry spans are therefore required for those gaps;
- the TypeSafe integration places semantic predictions in output rather than Braintrust scores;
- native TypeSafe observation captures state verbatim unless the application applies an explicit masking/reference policy.

## Epistemic boundary

These are version-bounded implementation facts, not eternal properties of ADK, Jev, or Braintrust. Upgrading any pinned system requires rerunning the relevant compatibility checks before deleting or changing a fallback.
