# Security Model

The architecture assumes cognitive outputs are useful but untrusted inputs. A model may design, code, classify, plan, or propose structural change, but durable software mediates application of the result.

## 1. No unmediated cognitive side effects

A CognitiveResult is data first.

```text
external cognition
 -> typed result
 -> identity + schema validation
 -> deterministic checks / policy / Jev where appropriate
 -> side effect
```

The external cognitive actor does not need to remain present while consequences are applied.

## 2. Resume integrity

Before an external result may resume a continuation, the bridge verifies:

- the `interrupt_id` is currently pending;
- the returned `obligation_ref` matches the expected Task/obligation;
- the result validates against the complete canonical output schema;
- the interrupt has not already been satisfied, expired, or superseded;
- the caller is permitted to satisfy the selected capability slot.

Runtime-native response-schema handling is defense in depth, not the sole validation boundary.

## 3. Least-privilege execution

External cognition receives only the tools required by the current obligation. Machine workers should expose registered JobTypes rather than an unrestricted shell by default.

Dangerous operations, destructive effects, high spend, publication, credential changes, or other constitution-defined effects may require deterministic policy or human approval.

## 4. Prompt-injection boundary

Retrieved files, logs, model outputs, web content, and artifacts are data unless the current Task contract explicitly identifies them as instructions. Context assembly should preserve that distinction.

## 5. Secrets and observability

Secrets are not content-addressed into public structural objects and should not be copied into Braintrust merely for convenience.

For Jev/TypeSafe observation, the preferred profile is:

```text
semantic state        -> reference/hash
semantic distribution -> capture
```

The frozen Braintrust 0.41.0 TypeSafe integration captures `state` verbatim by default. The reference implementation must therefore apply masking/reference policy or replace that boundary with an equivalent manual span.

Session/user identifiers should be hashed or omitted according to the observation profile.

## 6. Workflow evolution

Workflow revisions are immutable. Self-modification means proposing a new revision, not mutating the running one.

Promotion is staged:

```text
proposed -> schema-valid -> constructible -> tested -> shadow -> canary -> active
```

Rollback remains possible because previous revisions continue to exist.

## 7. Stop and degraded modes

The implementation should provide a durable stop state that rejects new external turns and prevents new effectful jobs while preserving inspectable state.

Loss of premium cognition should degrade capability, not corrupt state. Waiting Cognitive Interrupts remain pending until compatible capability returns or policy escalates them to another executor.
