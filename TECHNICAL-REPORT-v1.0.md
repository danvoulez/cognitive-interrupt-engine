# Ephemeral Cognition, Persistent Continuation

## A Cognitive Interrupt Architecture for Durable AI Workflows

**Technical report and architectural specification — v1.0.0 (2026-09-22)**  
Dan Voulez

## Abstract

Most agent systems make a language model carry the active process, memory, and
control loop. This report describes a different boundary: deterministic
software owns continuity, while cognition is invoked only when a workflow has
reached a typed semantic gap. The gap becomes a durable Cognitive Interrupt.
The workflow persists its state and obligation, the cognitive actor may
disappear, and a later typed result can resume the continuation without
reconstructing the whole task.

The architecture combines Persistent Continuation with Ephemeral Cognition,
Continuation-Complete Cognition, cycle-aware planning, Jev semantic
operations, Braintrust empirical accounting, and an adaptive cost model. It
also defines a concrete realization boundary for Google ADK 2.9.0, Jev /
TypeSafe System One, and Braintrust 0.41.0. The realization is intentionally
spec-first: the architecture is public in this release, while the
kill/restart/resume reference implementation remains a stated milestone.

## 1. Scope and epistemic boundary

This release freezes the architectural object and its portable contracts. It
does not claim that a production runtime has already completed every durable
resume, provider, credentialed integration, or economic measurement. The
portable definition is in `SPEC.md` and RFC CIR-0001. The version-specific
mapping and its frozen evidence are in `docs/IMPLEMENTATION-NOTES.md` and
`docs/PROVENANCE.md`.

The first implementation gate is deliberately narrow: a workflow must suspend
on a typed interrupt, survive process death, receive a later compatible
answer, validate that answer, and resume the correct continuation. The
repository records this as a future acceptance gate rather than implying that
the spec itself is an implementation receipt.

## 2. Central inversion

The normal agent loop is:

```text
LLM -> decide -> tool -> observe -> decide -> tool -> ...
```

The Cognitive Interrupt loop is:

```text
workflow -> deterministic work -> semantic narrowing -> interrupt
                                                     |
                                             persist and stop
                                                     |
                                             external cognition
                                                     |
workflow <- deterministic continuation <- typed result
```

The external model is therefore a temporary implementation of a missing
function:

```text
missing_function(input) -> typed_output
```

It is not the process and does not own the durable task. This boundary makes
the workflow inspectable, restartable, and able to wait for a compatible
cognitive capability without corrupting state.

## 3. The Cognitive Interrupt primitive

A Cognitive Interrupt is a durable obligation containing an interrupt
identity, an obligation reference, an opaque continuation reference, an input
reference and schema, an output schema, capability requirements, and creation
time. Its result is bound to both the interrupt identity and the obligation
reference. A structurally valid answer for a different obligation is not a
valid resume.

The lifecycle is:

```text
OPEN -> PENDING -> SATISFIED -> CONTINUING
                 |             |
                 +-> EXPIRED    +-> CONTAINED
```

Before resumption, the bridge checks that the interrupt is still pending, the
obligation reference matches, the result satisfies the complete canonical
schema, the interrupt has not already been satisfied or superseded, and the
caller has permission for the capability slot. Runtime-native response
schemas are defense in depth; they are not the only contract boundary.

## 4. Continuation-Complete Cognition

A cognitive turn is complete only when deterministic software can continue
without asking another model to interpret the answer. The result therefore
contains a resolution, artifacts and discoveries, an optional program patch,
the deterministic work now possible, required checks, residual uncertainty,
and a typed handoff. This preserves the distinction between a useful semantic
contribution and an unbounded prose response.

The continuation can reject a result, contain it for review, or apply it after
identity, schema, policy, and deterministic checks. External cognition does
not receive unmediated effect authority.

## 5. Computational classes and planning

The engine separates deterministic computation, narrow semantic computation,
and open-ended external cognition. Jev supplies cheap, typed operations such
as Noul, Choice, Score, and sensor packs. An interrupt is reserved for a gap
that deterministic code cannot close and Jev cannot narrow sufficiently.

Plans are organized into cycles rather than narrative task lists:

```text
deterministic preparation
 -> semantic narrowing
 -> Cognitive Interrupt if necessary
 -> typed resolution
 -> deterministic continuation
 -> checks and evaluation
```

Every prospective interrupt must state why code cannot continue, why Jev is
insufficient, what evidence is prepared, what exact output unblocks the next
cycle, and whether independent questions can be batched. Serial interrupt
depth is a first-class latency measure.

## 6. Empirical and economic architecture

Braintrust is the empirical layer for traces, evaluations, datasets,
experiments, and comparisons across workflow revisions and executors. It is
not the authority boundary and Jev predictions are not automatically quality
scores. Observation must preserve correlation while masking or referencing
semantic state rather than copying secrets or sensitive state into a public
trace.

The cost model tracks more than tokens: total cognitive cost, cost per
successful task, premium dependency, interrupt rate, rescue recurrence,
compilation of rescue work into software, subscription utilization,
deterministic runway, handoff repair cost, serial interrupt depth, and
expected cognitive wait. Routing is adaptive: executions produce evidence,
evidence changes policy, and the next policy is staged rather than silently
mutating a running workflow.

## 7. Concrete reference mapping

The first implementation maps the portable boundary onto three systems:

| System | Responsibility |
| --- | --- |
| Google ADK 2.9.0 | Durable workflow execution, `RequestInput`, sessions, artifacts, and resumability |
| Jev / TypeSafe System One | Narrow semantic operations and sensor packs inside the workflow |
| Braintrust 0.41.0 | Tracing, evaluation, experiments, and longitudinal evidence |

The mapping is intentionally asymmetric. ADK is the executable body and
persistent continuation. Jev is a semantic operation inside that body.
Braintrust observes and evaluates what the body did. Hosted or scheduled
premium cognition appears only at a typed interrupt boundary.

ADK resumability is experimental and best-effort in the pinned version, so
process-death tests are a hard gate. The bridge also validates complete result
schemas because the pinned rehydration path does not enforce every nested
constraint of arbitrary raw JSON Schema. Braintrust instrumentation adds
explicit spans for workflow topology, interrupt creation and satisfaction,
resume transitions, and revision correlation where native instrumentation is
incomplete.

## 8. Security and provenance

Retrieved files, logs, model output, web content, and artifacts are data unless
the current task contract explicitly identifies them as instructions. Secrets
are not placed in content-addressed structural objects or copied into
observability merely for convenience. Workflow revisions are immutable and
promoted through proposed, schema-valid, constructible, tested, shadow,
canary, and active states. Stop and degraded modes preserve inspectable state
and reject new effectful work while capability is unavailable.

Structural identity uses a pinned canonicalization profile. Provider versions,
source paths, and artifact hashes are recorded in `docs/PROVENANCE.md` so
version-specific claims remain bounded and recheckable.

## 9. What v1.0 proves and leaves open

This release proves the shape of the architectural contracts, their examples,
the security and provenance boundaries, the planned vertical implementation
sequence, and local contract tests that do not require live provider access.

It deliberately leaves these as future milestones:

- kill/restart/resume of the reference ADK workflow;
- a real scheduled external turn satisfying an interrupt;
- credentialed Jev/TypeSafe and Braintrust integration;
- empirical calibration, cost curves, and provider routing;
- multi-provider operation and the later maintenance program.

Those limits are part of the release's claim. Future versions accumulate
evidence against this frozen architectural object rather than silently
changing what v1.0 means.

## 10. Citation

Use the metadata in `CITATION.cff` and cite release `v1.0.0` together with
[DOI 10.5281/zenodo.22893166](https://doi.org/10.5281/zenodo.22893166).

## Appendix A — Repository map

- `SPEC.md`: integrated architecture;
- `rfcs/CIR-0001-cognitive-interrupt.md`: portable interrupt protocol;
- `COST.md`: adaptive cost architecture;
- `RISKS.md`: assumptions and mitigations;
- `ROADMAP.md`: vertical implementation sequence;
- `schemas/` and `examples/`: machine-readable contracts;
- `docs/PROVENANCE.md`: frozen evidence boundary;
- `docs/SECURITY-MODEL.md`: effect and prompt-injection boundaries.

## Appendix B — Reference acceptance sequence

The planned evidence sequence is deterministic cycle, durable interrupt,
scheduled external cognition, Jev semantic cycle, task cascade, workflow
evolution, persistent program maintenance, Braintrust learning loop, multiple
premium providers, and the first full program. Each step must end in an
observable event, computation, and persisted result.
