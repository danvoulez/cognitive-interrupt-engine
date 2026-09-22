# Vertical Implementation Roadmap

The implementation is derived from a complete architectural blueprint, but code is merged in **closed vertical cycles**, not horizontal infrastructure layers.

## PR 1 — Deterministic Cycle

Deliver:

```text
Typed Task -> ADK Workflow -> deterministic nodes -> Artifact
```

Includes content addressing, Task/Execution identity, persistent ADK session/artifact services, and baseline Braintrust trace correlation.

## PR 2 — Durable Cognitive Interrupt

Deliver:

```text
Workflow -> RequestInput -> persist -> process dies -> resume later
```

This is the fundamental architecture gate.

Acceptance test must kill the process after the interrupt and reconstruct the runner before supplying the typed response. The bridge must reject an invalid nested result before it reaches ADK resume handling.

## PR 3 — Real Scheduled External Cognition

Deliver:

```text
platform schedule -> turn_begin -> typed mission -> external LLM
                  -> turn_end -> ADK resumes -> deterministic continuation
```

A real external provider fills a real interrupt. `turn_end` verifies interrupt identity, Task/obligation identity, and the complete output schema before creating the ADK resume response.

## PR 4 — Jev Semantic Cycle

Deliver:

```text
machine -> Jev sensor pack -> deterministic route
premium result -> Jev continuation lint -> machine
```

## PR 5 — Task Cascade

One execution can create Artifacts, a Patch, and child Tasks. Prove `Task -> Task*`.

## PR 6 — Workflow Evolution

A task can propose a new WorkflowRevision. Validate, construct, test, hash, and stage it without mutating the currently running revision.

## PR 7 — Persistent Program Maintenance

Introduce `maintain_program` as a recurring/persistent Task that manages backlog, deduplication, context compaction, pending interrupts, and structural improvements.

## PR 8 — Braintrust Learning Loop

Add late evaluations, datasets, experiments, Jev calibration, executor comparison, workflow comparison, and cost/continuation metrics.

## PR 9 — Multiple Premium Providers

Allow compatible interrupts to be supplied by more than one external premium system. Begin empirical routing by TaskType and capability.

## PR 10 — First Full Program

Use the local-model/LoRA program as an acceptance test of the complete Engine rather than as the source of architectural discovery.

## Rule for every PR

A PR must end in an observable state transition:

```text
event -> workflow -> computation -> persisted result
```

No PR exists solely because "we will need this infrastructure later."
