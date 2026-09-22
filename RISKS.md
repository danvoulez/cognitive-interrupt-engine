# Risks, Assumptions, and Mitigations

This document records the architectural assumptions that could invalidate or materially constrain the reference implementation.

## R1. ADK resumability is experimental in the pinned implementation

**Status:** Critical technical dependency.

The reference design depends on durable interrupt/resume behavior. In the pinned ADK 2.9.0 source, resumability is experimental and documented as best-effort.

**Mitigation:**

- pin the exact runtime version;
- acceptance-test kill/restart around every interrupt boundary;
- make side effects idempotent;
- persist all essential state externally;
- treat runtime upgrades as compatibility events requiring the full resumability suite.

The architectural concept is not ADK-specific, but the first implementation is.

## R2. Consumer scheduling is external capacity, not infrastructure we control

**Status:** Economic and latency risk, not correctness dependency.

Scheduled capabilities in consumer products may change limits, timing, or behavior.

**Mitigation:**

- pending interrupts remain durable when a slot is missed;
- support several providers;
- maintain API fallback;
- never make subscription arrival required for correctness;
- measure actual slot reliability over time.

## R3. Braintrust does not natively expose every ADK Workflow boundary in the pinned pair

**Status:** Observability gap.

The reference integration requires explicit spans for workflow nodes, branches, Cognitive Interrupt creation/satisfaction, and some non-native tool boundaries.

**Mitigation:** targeted OpenTelemetry instrumentation. Braintrust remains the storage/evaluation/experiment layer; the project only supplies missing sensors.

## R4. Cold-start calibration is statistically weak

**Status:** Expected bootstrap limitation.

Per-executor empirical distributions and late outcomes require samples that do not exist initially.

**Mitigation:** three regimes:

1. conservative fixed rules + deterministic gates;
2. empirical learning after minimum sample thresholds;
3. calibrated routing only when data is sufficient.

Never pretend that `n=3` is a meaningful distribution.

## R5. Serial cognitive latency can dominate wall-clock time

**Status:** Core planning risk.

Five sequential hourly interrupts can make a small logical workflow take most of a day.

**Mitigation:**

- batch independent semantic questions;
- prepare evidence before premium slots;
- plan around Cognitive Critical Path;
- minimize Serial Interrupt Depth;
- maximize useful deterministic continuation after each premium turn;
- use API when waiting cost exceeds monetary cost.

## R6. Workflow self-modification can cause systemic regressions

**Status:** High-impact capability.

**Mitigation:** immutable revisions and staged promotion:

```text
proposed -> schema-valid -> constructible -> tested -> shadow -> canary -> active
```

Human approval is reserved for high-impact effects rather than every structural change forever.

## R7. Overbuilding infrastructure before proving the primitive

**Status:** Project execution risk.

**Mitigation:** build from a complete blueprint but implement through vertical cycles. The first hard gate is interrupt -> process death -> later external response -> correct resume.

## R8. Handoff quality can silently reintroduce agent-like cost

**Status:** Behavioral risk.

If premium turns return vague prose, future models must reconstruct meaning and continuity leaks back into cognition.

**Mitigation:** typed cognitive result schemas, continuation-complete templates, Jev handoff linting, and Braintrust Handoff Repair metrics.

## R9. Content-addressed identity can be undermined by unstable canonicalization

**Status:** Provenance risk.

**Mitigation:** use one canonicalization profile, pin it, test it across languages, and never include nondeterministic fields in structural identity.

## R10. Cheap routing can reduce quality

**Status:** Economic optimization risk.

**Mitigation:** cost is never optimized independently. Routing considers expected quality, latency, criticality, wait cost, and late outcomes.

## R11. ADK 2.9.0 does not fully validate complex raw JSON Schema on durable resume

**Status:** Contract-integrity risk.

The pinned ADK rehydration path validates simple response shapes, but complex raw JSON Schema handling is partial and may fall back to accepting data that has not been validated against every nested constraint.

**Mitigation:**

- the Engine bridge validates the complete cognitive result against the canonical output schema before creating a resume `FunctionResponse`;
- require `interrupt_id` and `obligation_ref` in the returned result and compare both to the pending obligation;
- treat ADK `response_schema` as runtime/HITL metadata, not the sole contract-enforcement boundary;
- add invalid nested-result fixtures to the PR 2/3 acceptance suite.

## R12. Subscription capacity is governed by provider product constraints

**Status:** External dependency / compliance risk.

The economic design may prefer scheduled capacity already included in a subscription, but it does not assume that every provider permits arbitrary automation, connector access, cadence, or workload volume.

**Mitigation:**

- use only scheduling, connectors, and automation surfaces actually exposed for the account/product in use;
- respect provider terms, rate limits, and product limits;
- keep provider-specific capability declarations versioned and empirical;
- degrade to another compatible executor or metered API when a subscription surface is unavailable;
- never make circumvention of a product limit part of the Engine's correctness model.
