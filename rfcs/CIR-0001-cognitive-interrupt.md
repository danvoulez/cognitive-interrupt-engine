# CIR-0001: Cognitive Interrupts and Persistent Continuations

**Status:** Draft  
**Category:** Architecture / Protocol  
**Version:** 0.1

## Abstract

A Cognitive Interrupt is a durable typed obligation emitted when a persistent workflow cannot continue without open-ended semantic computation. The workflow serializes enough continuation state to stop completely. A compatible external cognitive executor may satisfy the obligation later by returning a typed result. The workflow then resumes without requiring the original cognitive actor or process to survive.

## Motivation

Conventional agent loops entangle cognition and control. The model interprets state, chooses actions, observes results, and carries continuity. This makes waiting, context, cost, and failure recovery properties of the cognitive actor.

Cognitive Interrupts invert the relationship: software owns control and persistence; cognition supplies missing semantic values.

## Core invariant

> Actors are transient. State and obligations persist.

## Logical contract

```text
create_interrupt(obligation_ref, input, output_schema, capability_requirements, continuation_ref)
    -> interrupt_id

satisfy_interrupt(interrupt_id, obligation_ref, typed_output)
    -> validate -> resume(continuation_ref, typed_output)
```

The implementation MUST support a period during which no cognitive actor or workflow process remains active.

## Required fields

A portable interrupt envelope contains at least:

```yaml
interrupt_id: execution-specific identifier
obligation_ref: content-addressed Task or equivalent
continuation_ref: opaque durable reference to the suspended continuation
capability_requirements: {...}
input_schema: schema reference
input: ...
output_schema: schema reference
created_at: timestamp
```

Lifecycle state such as `waiting`, `claimed`, `satisfied`, `expired`, or `superseded` SHOULD be recorded in an event log or runtime index rather than by mutating the interrupt envelope itself.

The reference JSON Schema is [`schemas/cognitive-interrupt.schema.json`](../schemas/cognitive-interrupt.schema.json).

## Semantics

1. Creating an interrupt MUST NOT imply that a cognitive executor is currently available.
2. A waiting interrupt MUST survive process termination.
3. A submitted result MUST identify both the `interrupt_id` and the `obligation_ref` it satisfies.
4. The returned value MUST be validated against the complete output contract before it is accepted as resume input.
5. The workflow MUST resume from the persisted continuation rather than reconstructing logical state from model prose.
6. Side effects around replay/resume boundaries MUST be idempotent or otherwise protected against duplicate execution.
7. The cognitive executor MAY disappear immediately after supplying its result.
8. A missed external capacity window MUST NOT invalidate the continuation.
9. An implementation MAY match one interrupt to multiple compatible providers, but only one accepted result should satisfy a given obligation unless the workflow explicitly models ensembles.

## Continuation-Complete Cognition

A result is continuation-complete when it supplies not only a plausible answer but enough typed structure for the non-cognitive workflow to continue correctly after the executor disappears.

The result contract SHOULD make residual uncertainty explicit instead of smuggling it into narrative prose.

## Capability supply

Capability may come from:

- scheduled premium systems where the provider exposes suitable scheduling and tool access;
- metered APIs;
- local models;
- humans;
- future specialist services.

The interrupt contract should describe required capabilities rather than hard-code a provider unless the provider itself is semantically relevant.

## Economics

Scheduled subscription capacity may be preferred economically when available, but MUST NOT be a correctness dependency. Metered API may act as overflow or recovery supply.

## Reference mapping: Google ADK 2.9.0

In the current reference implementation:

```text
Cognitive Interrupt -> RequestInput
Typed resolution     -> FunctionResponse with matching interrupt id
Persistent state     -> ADK SessionService / event history
Workflow             -> ADK Workflow
```

The ADK adapter resolves the portable `continuation_ref` to the concrete ADK session/invocation/node state. Those identifiers are implementation details, not part of CIR-0001.

`RequestInput.response_schema` is useful for communicating the expected response shape, but the Engine bridge MUST perform its own complete contract validation before creating the resume `FunctionResponse`. The pinned ADK 2.9.0 rehydration path performs only partial validation for complex raw JSON Schemas, so CIR-0001 correctness cannot rely on that validator alone.

This mapping is implementation-specific. CIR-0001 is intended to remain meaningful independently of ADK.
