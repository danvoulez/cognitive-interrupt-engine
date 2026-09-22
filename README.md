# Ephemeral Cognition, Persistent Continuation

**A Cognitive Interrupt Architecture for Durable AI Workflows**

> The intelligence exists only in the gaps.

Most agent systems make the model own continuity and call deterministic tools along the way. This project inverts that relationship: **durable software owns continuity, while cognition is invoked only where the workflow cannot continue without a semantic value.**

```text
RUN -> RUN -> JEV -> RUN -> COGNITIVE INTERRUPT -> SUSPEND
                                             ... hours later ...
external intelligence -> typed result -> RESUME -> RUN -> RUN
```

The external LLM is not the process. It is a temporary implementation of a missing function:

```text
missing_function(input) -> typed_output
```

The workflow persists before and after it. The intelligence does not.

## Core principles

- **Persistent Continuation, Ephemeral Cognition.** Actors are transient; state and obligations persist.
- **Cognitive Interrupts.** Open-ended semantic gaps become durable, typed obligations that may be resolved hours or days later.
- **Continuation-Complete Cognition.** A premium turn must leave behind a result the deterministic continuation can consume after the model disappears.
- **Typed, content-addressed work.** Tasks, workflows, templates, packs, patches, and artifacts are immutable and identified by content.
- **Cycle-aware planning.** Project decomposition is designed around deterministic stretches, semantic operations, cognitive interrupts, and resumptions.
- **Compile cognition into software.** Recurring premium reasoning should progressively become deterministic code, templates, Jev packs, or local capability.
- **Adaptive economics.** Cost is part of planning and routing from day one; premium API is a backstop, not necessarily the steady-state fuel.

## Concrete realization

The current reference architecture maps these ideas onto three systems:

| System | Role |
|---|---|
| **Google ADK 2.9.0** | Durable workflow runtime, `RequestInput`, resumability, sessions, artifacts, native workflow execution |
| **Jev / TypeSafe System One** | Cheap narrow semantic computation through Noul, Choice, Score, and sensor packs |
| **Braintrust 0.41.0** | Empirical memory: tracing, evaluations, experiments, and longitudinal evidence for calibration/comparison |

External premium models are **not hosted agents**. Where an external provider exposes scheduled tasks or an equivalent trigger mechanism, that facility can provide periodic cognitive capacity. A waiting Cognitive Interrupt is matched to a compatible appearance, receives one typed contribution, then the workflow resumes.

## Repository map

```text
SPEC.md                         Formal integrated architecture
COST.md                         Adaptive cost architecture
RISKS.md                        Critical assumptions and failure modes
AUDIT.md                        Re-check results, corrections, and unproven claims
ROADMAP.md                      Cycle-oriented implementation plan
docs/PLANNING.md                Cycle-aware planning discipline
docs/IMPLEMENTATION-NOTES.md    ADK / Jev / Braintrust realization notes
docs/PROVENANCE.md              Frozen evidence/version boundary for those mappings
docs/SECURITY-MODEL.md          Security assumptions and effect boundaries
rfcs/CIR-0001-cognitive-interrupt.md
                                Portable Cognitive Interrupt primitive
schemas/                        Draft machine-readable contracts
examples/minimal-cycle.yaml     Minimal vertical-cycle example
examples/cognitive-interrupt.json / cognitive-result.json
                                Concrete contract fixtures
src/                            Tiny content-addressing reference helpers
tests/                          Contract tests for the helpers
CITATION.cff                    Citation metadata for GitHub / Zenodo
```

## The architectural inversion

Traditional agent loop:

```text
LLM -> decide -> tool -> observe -> decide -> tool -> ...
```

Cognitive Interrupt architecture:

```text
workflow -> deterministic -> Jev -> deterministic -> INTERRUPT
                                                    |
                                                    v
                                                persist + stop
                                                    |
                                             external cognition
                                                    |
                                                    v
workflow <- deterministic continuation <- typed result
```

**The process carries the thinker forward, not the other way around.**

## Status

Release **v1.0.0** is an architectural technical report and specification. The architecture is intentionally separated from the pinned implementation details so the Cognitive Interrupt model can survive changes in any particular runtime. The first implementation gate is deliberately small: prove that a workflow can suspend on a typed cognitive interrupt, lose its process, receive a scheduled external answer later, and resume correctly. That kill/restart/resume gate remains a future reference-implementation milestone.

See [ROADMAP.md](ROADMAP.md) for the vertical PR sequence and [docs/PROVENANCE.md](docs/PROVENANCE.md) for the frozen evidence behind version-specific implementation claims.

## Citation

If you use or discuss this architecture, cite release `v1.0.0` using [`CITATION.cff`](CITATION.cff) and [DOI 10.5281/zenodo.22893166](https://doi.org/10.5281/zenodo.22893166).

## Author

Dan Voulez, 2026.
