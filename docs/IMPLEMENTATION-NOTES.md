# Reference Implementation Notes

These notes record the pinned technical realization behind the first implementation. They are not the portable definition of the architecture.

## Google ADK 2.9.0

The frozen implementation surface identifies the native pieces needed for the reference runtime, including `Workflow`, `FunctionNode`, `JoinNode`, `Context.run_node()`, `RequestInput`, resumability/replay state, retry/timeout/concurrency controls, `SessionService`, `ArtifactService`, events, routes, and state deltas.

The critical realization is that `RequestInput` can represent the runtime boundary of a Cognitive Interrupt: the workflow produces a typed request, stops, and later resumes from a matching external `FunctionResponse`.

**Important:** resumability in the pinned 2.9.0 implementation is experimental/best-effort. This is why kill/restart testing is a hard implementation gate rather than an afterthought.

There is also a contract-validation caveat. The pinned rehydration code fully handles simple shapes but does not implement every nested constraint of arbitrary raw JSON Schema; complex schemas can fall back to partial or skipped validation. Therefore the MCP/bridge boundary MUST validate the complete CognitiveResult using the Engine's own JSON Schema validator before constructing the `FunctionResponse`. `RequestInput.response_schema` remains useful metadata, but it is not the only validator.

## Jev / TypeSafe System One

The frozen semantic surface treats Jev as its own typed judgment system rather than a generative `BaseLlm` replacement.

The useful primitives are:

- Noul
- Choice
- Score

The reference architecture uses Jev through workflow-native adapters, usually as `FunctionNode` wrappers, with sensor packs for multiple independent judgments over the same state.

Jev outputs are predictions or semantic measurements, not automatically Braintrust quality scores.

The frozen Braintrust TypeSafe integration captures the Jev `state` verbatim by default. The reference observation profile therefore sends a state reference/hash while preserving the returned distribution needed for calibration. If native masking cannot enforce that boundary reliably, use an equivalent manual span instead of leaking raw state.

## Braintrust 0.41.0

Braintrust provides the empirical layer: traces, scores, evaluations, datasets, experiments, and comparison across program revisions.

The frozen ADK/Braintrust pair has observability gaps around workflow topology, routes, and some tool boundaries. The reference implementation therefore adds explicit OpenTelemetry spans for:

- workflow/component execution;
- branch decisions;
- Cognitive Interrupt creation;
- Cognitive Interrupt satisfaction;
- resume transitions;
- workflow revision correlation.

The project does not build a new observability backend. It adds only the missing sensors.

## Cross-system invariant

The three systems should not be flattened into peers:

```text
ADK        = executable body / persistent continuation
Jev        = cheap narrow semantic operation inside the body
Braintrust = empirical observation of what the body did and what worked
```

External premium cognition exists outside the runtime and is inserted only at typed Cognitive Interrupt boundaries.


## Evidence boundary

Exact frozen artifact hashes and source paths for these version-specific claims are recorded in [`PROVENANCE.md`](PROVENANCE.md).
