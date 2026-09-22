# Repository Audit

**Audit date:** 2026-09-22  
**Scope:** internal consistency, frozen-source claims, contract schemas, packaging, publication hygiene.

## Result

The central architecture remains coherent after re-checking the frozen ADK/Jev/Braintrust corpus. No contradiction was found in the core model:

```text
persistent workflow
 -> cognitive gap
 -> durable interrupt
 -> no resident cognition required
 -> typed external resolution
 -> deterministic resume
```

The audit did find and repair several publication-critical issues.

## Corrections made

1. **Resume validation boundary clarified.** ADK 2.9.0 does not fully enforce arbitrary complex raw JSON Schema during durable rehydration. The Engine bridge now explicitly owns complete result validation before constructing a resume `FunctionResponse`.
2. **Interrupt/result identity bound end-to-end.** `CognitiveResult` now carries both `interrupt_id` and `obligation_ref`, preventing a structurally valid result from being silently applied to the wrong pending obligation.
3. **Portable RFC decoupled from ADK runtime identifiers.** `continuation_ref` is an opaque durable handle. ADK session/invocation/node identifiers are adapter details, not CIR-0001 fields.
4. **RFC and JSON Schemas aligned.** The portable contract and machine-readable fixtures now use the same field model.
5. **Placeholder schema identifiers removed.** Draft schemas now use stable URN identifiers rather than `example.invalid`.
6. **Content-addressing helper made explicitly non-normative.** The executable demo refuses values for which it cannot honestly claim interoperability and points production implementations to a pinned RFC 8785/JCS implementation.
7. **Security model restored.** Result validation, least privilege, prompt-injection boundaries, observability privacy, staged workflow promotion, stop/degraded modes, and Jev state-reference policy are now explicit.
8. **Frozen-source provenance added.** Version-specific ADK/Jev/Braintrust claims now have artifact digests and source-boundary notes in `docs/PROVENANCE.md`.
9. **Economic metrics expanded.** The cost appendix now tracks rescue recurrence/compilation, premium dependency, cognitive compression, serial interrupt depth, and related adaptive measures.
10. **Unchosen license removed.** No reuse license is asserted until the author explicitly selects one before publication.
11. **Premature release metadata removed.** `CITATION.cff` no longer claims a release date before a public release exists.
12. **Provider scheduling claim narrowed.** Scheduled subscription capacity is described only where the provider actually exposes suitable scheduling/tool surfaces, and remains an economic preference rather than a correctness dependency.
13. **CI and repository tests added.** GitHub Actions now runs the local contract suite.

## Frozen-source claims rechecked

Against the frozen 2026-09-20 corpus:

- Google ADK source identifies version **2.9.0**.
- `RequestInput` carries `interrupt_id`, `payload`, `message`, and `response_schema`.
- Workflow/FunctionNode handling converts `RequestInput` into an interrupt and preserves waiting state for resumable execution.
- Runner resume input is reconstructed from matching function responses.
- `ResumabilityConfig` is explicitly **experimental**, best-effort, and at-least-once on resume; in-memory state may be lost.
- Jev is not mapped to ADK `BaseLlm`; Noul, Choice, and Score remain distinct primitives.
- Noul has no confidence field in the pinned direct TypeSafe contract.
- Sensor-pack semantics evaluate several questions over one state/request.
- Braintrust 0.41.0 does not natively patch ADK workflow graph/node/edge/route semantics.
- Both non-MCP ADK tool patch targets miss ADK 2.9.0 in the frozen Braintrust mapping.
- Braintrust's TypeSafe integration records semantic answers in output, not as quality scores, and captures state verbatim unless masking/reference policy is applied.

Exact artifact hashes are in `docs/PROVENANCE.md`.

## Executable checks

The audited tree passes:

```text
9 pytest tests
3 JSON Schemas checked as Draft 2020-12
2 concrete contract fixtures validated
Markdown local-link integrity check
YAML parse checks for CITATION.cff, issue form, and minimal cycle
Editable/package import check
Wheel build without network/build isolation
```

## What is not yet proven

This repository remains **spec-first**. The following are deliberately not claimed as completed:

- no live kill/restart ADK Cognitive Interrupt prototype has been implemented in this repository yet;
- no real scheduled consumer-platform turn has satisfied an interrupt end-to-end yet;
- no live Jev/TypeSafe or Braintrust credentialed integration test is included here;
- no empirical cost curve, routing policy, calibration result, or LoRA program result exists yet;
- CIR-0001 is a draft architectural protocol, not a standards-body specification.

Those are implementation/empirical milestones in `ROADMAP.md`, not hidden assumptions.

## Release blockers

Before the first public GitHub/Zenodo release:

1. choose the reuse license explicitly;
2. add the final repository URL to citation metadata;
3. decide whether v1.0 denotes the architecture paper/spec or the first working reference implementation;
4. rerun the suite from the tagged release artifact;
5. if a DOI is reserved, add it to the paper/repository metadata before final archival publication.
