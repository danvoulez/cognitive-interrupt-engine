# Engine de Inteligência Agendada — Especificação Integrada

**Version 1.0-draft · September 2026 · Dan Voulez**

## 1. Definition

The Engine is a **living task-oriented software system** whose continuity is carried by durable workflows while cognition appears only where it is missing.

The system executes everything it already knows how to execute. Narrow semantic uncertainty may be delegated to Jev. Open-ended semantic uncertainty becomes a **Cognitive Interrupt**: a typed obligation plus a persisted continuation.

When a Cognitive Interrupt is emitted, execution can stop completely. No model session, resident agent, or waiting process is required. Later, an external intelligence supplies one typed value. The workflow resumes and deterministic machinery takes possession of the result.

> **Ephemeral Cognition, Persistent Continuation.**

> **Actors are transient. State and obligations persist.**

## 2. Central inversion

Ordinary agent architecture makes the LLM own continuity and invoke deterministic tools.

This architecture makes software own continuity and invoke cognition only at semantic gaps.

```text
known -> known -> Jev -> known -> ??? -> known -> known
                                  ^
                          Cognitive Interrupt
```

The premium model is therefore closer to a temporary implementation of:

```text
missing_function(input) -> typed_output
```

than to a long-running agent.

## 3. Computational classes

The planner chooses among four broad classes of work:

1. **Deterministic computation** for exact transformations.
2. **Jev semantic computation** for narrow probabilistic judgments.
3. **Cognitive Interrupts** for open-ended reasoning that requires scarce cognition.
4. **Physical or external jobs** for long-running work on machines, services, or humans.

A healthy program progressively moves recurring work downward from expensive open cognition into cheaper reusable structure.

## 4. Native runtime

The reference implementation uses Google ADK as the executable substrate. It does not introduce a second workflow engine.

Relevant native primitives include:

- `Workflow`
- `FunctionNode`
- `JoinNode`
- `Context.run_node()`
- `RequestInput`
- resumability and replay state
- `SessionService`
- `ArtifactService`
- retries, timeouts, concurrency, events, routes, and state deltas

The portable architecture does not require ADK specifically, but any alternative runtime must preserve the same durable interrupt/resume semantics.

## 5. Core objects

### Program
Long-lived identity of a project or autonomous body of work.

### ProgramRevision
An immutable executable version referencing a root `WorkflowRevision`, task types, templates, Jev packs, observation policy, and resource bindings.

### Objective
A desired outcome plus measurable progress or completion criteria.

### TaskType
Reusable contract describing input schema, output schema, required capabilities, default workflow, and evaluation strategy.

### Task
The central logical unit of work. Tasks are immutable, typed, composable, and content-addressed.

```yaml
task:
  task_type: sha256:...
  parents: [sha256:...]
  inputs: {...}
  expected_outputs: {...}
  requirements:
    capabilities: [...]
  lifecycle: finite | recurring | persistent
```

### WorkflowRevision
Immutable executable workflow definition. A behaviorally relevant change produces a new revision.

### Template
Reusable structure for tasks, workflows, interrupt contracts, context assembly, handoffs, planning outputs, evaluations, and maintenance cycles.

### Artifact
Durable output such as code, data, models, reports, measurements, or files.

### Execution
A temporal occurrence of work against a specific Task and WorkflowRevision.

### CognitiveInterrupt
A durable typed obligation waiting for compatible cognition.

### Evaluation
Immediate or delayed assessment of an Execution, Artifact, Task, WorkflowRevision, executor, or semantic prediction.

### Patch
A proposed structural change to the program: add/supersede tasks, create/supersede workflows, add dependencies, templates, Jev packs, or routing changes.

### Executor
A capability description for machines, scripts, local models, external premium systems, or humans.

## 6. Content addressing

Structural objects use deterministic canonical serialization and SHA-256 identity.

Preferred rule:

```text
id = sha256(JCS(object))
```

Time does not belong in the identity of immutable structural objects. Time belongs to Executions and Events.

Objects are never silently edited. Evolution is expressed through new objects and explicit lineage such as `supersedes`.

## 7. Task cascade

A Task can produce additional Tasks.

```text
Execution(Task)
   -> Artifacts
   -> Evaluations
   -> Patch
   -> Task*
```

This permits sequential, parallel, conditional, and expansive composition. The expansive case is the core of the living-program behavior: work discovers and materializes new work.

## 8. Cognitive Interrupt

A Cognitive Interrupt records the exact semantic obligation preventing deterministic continuation.

```yaml
cognitive_interrupt:
  interrupt_id: interrupt-...
  obligation_ref: sha256:...   # Task hash
  continuation_ref: continuation:...  # opaque durable handle
  capability_requirements:
    reasoning: deep
    tools: [web]
  input_schema: sha256:...
  input: {...}
  output_schema: sha256:...
  created_at: ...
```

In the ADK realization, this maps to `RequestInput` and later to a `FunctionResponse` carrying the matching interrupt id. The portable `continuation_ref` is resolved by the ADK adapter to the concrete session/invocation/node state; those runtime identifiers are deliberately not part of CIR-0001.

The Engine bridge validates the complete returned contract before creating that resume response. This is an architectural requirement, not something delegated blindly to the runtime's schema handling.

The waiting duration may be milliseconds, hours, or days without changing the architectural semantics.

## 9. Resumability invariant

The first implementation acceptance gate is:

```text
workflow
 -> cognitive interrupt
 -> persisted continuation
 -> process dies
 -> time passes
 -> typed response arrives
 -> process is recreated
 -> same logical invocation resumes
```

All side effects around resumable boundaries must be idempotent. No essential state may exist only in process memory.

## 10. External cognition

External premium systems are not resident agents owned by the Engine. Where a provider exposes scheduled tasks or an equivalent trigger mechanism, that external facility can expose periodic capacity to the Engine.

A scheduled appearance:

1. identifies its capability slot;
2. asks the Engine for a compatible pending Cognitive Interrupt;
3. receives a prepared, minimal, typed contract;
4. performs the open-ended cognitive work;
5. returns a typed result;
6. disappears;
7. leaves the deterministic workflow to process consequences.

## 11. Continuation-Complete Cognition

A premium turn is not complete merely because it answered the immediate question. It must leave the deterministic continuation in a usable state after the model disappears.

A strong cognitive result includes:

```yaml
cognitive_result:
  interrupt_id: interrupt-...
  obligation_ref: sha256:...
  resolution: {...}
  artifacts: [...]
  discoveries: [...]
  program_patch:
    tasks: [...]
    dependencies: [...]
    workflows: [...]
    templates: [...]
    jev_packs: [...]
  deterministic_continuation:
    now_possible: [...]
    required_checks: [...]
  residual_uncertainty:
    - question: ...
      capability_required: ...
  handoff:
    preserve: [...]
```

The primary handoff is to software, not to another model.

## 12. Deterministic Runway

**Deterministic Runway** is the useful work that can occur after a cognitive contribution before another open-ended Cognitive Interrupt is required.

A short runway caused by vague output or missing structure is a handoff failure. A long runway is not automatically optimal, but unnecessary repeated cognition is wasteful.

## 13. Jev as semantic instruction set

Jev is not an agent and should not masquerade as a generative LLM. It provides low-cost typed semantic operations inside workflows.

The main primitives are:

- **Noul** for yes/no probability.
- **Choice** for a distribution over finite alternatives.
- **Score** for ordered rubric judgments.

Typical questions:

```text
is_duplicate?
does_this_address_the_task?
which_failure_class?
which_executor_fits?
how_complete?
does_this_require_premium?
```

Several independent questions over the same state should be batched into **sensor packs**.

## 14. Cycle-aware planning

Planning is central because Task boundaries must align with the actual computational cycle.

The planner must ask:

```text
What can run deterministically now?
Where is narrow semantic judgment enough?
Where will open cognition be missing?
What must be prepared before that interrupt?
What typed result must the interrupt return?
What deterministic work becomes possible afterward?
Can multiple cognitive questions be batched into one visit?
How many serial cognitive waits lie on the critical path?
```

Planning therefore designs the **cognitive topology** of the program, not merely a list of tasks.

## 15. Semantic Debt

Semantic Debt is avoidable ambiguity that forces later cognition to reconstruct the meaning of previous work.

Bad:

```text
LLM A -> vague prose -> LLM B reconstructs context -> LLM C clarifies
```

Good:

```text
LLM -> typed durable result -> deterministic continuation
```

Templates, typed outputs, context assembly, and continuation contracts exist partly to minimize Semantic Debt.

## 16. Templates

Repeated structure should be aggressively templated:

- TaskTypes
- workflow fragments
- Cognitive Interrupt contracts
- Jev packs
- planning outputs
- context builders
- handoffs
- evaluations
- machine jobs
- failure recovery
- maintenance cycles

Templating is the mechanism by which previously paid cognition becomes reusable capital.

## 17. Braintrust as empirical memory

Braintrust does not execute the program. It observes what happened and supports longitudinal learning.

Every relevant trace should correlate to:

```text
program_revision
workflow_hash
task_hash
task_type
execution_id
executor
interrupt_id
slot_id
jev_pack_hash
artifact_hashes
```

The system should be able to answer not only which model produced an answer, but which exact software revision produced the surrounding behavior.

## 18. Evaluations

Evaluations may be immediate or delayed. Delayed evaluation is particularly important because an apparently good cognitive contribution may later prove harmful, useless, or unexpectedly valuable.

Braintrust supports comparison across:

- TaskType × executor
- WorkflowRevision × outcome
- JevPack × calibration
- Template × quality
- placement of cognition × cost/latency/outcome

Production output does not automatically become ground truth.

## 19. Compile cognition into software

A central learning loop is:

```text
premium cognition
 -> repeated pattern discovered
 -> Template / Workflow / JevPack / deterministic function
 -> future premium interrupt eliminated or narrowed
```

Maturity is therefore visible as a changing computational boundary: more exact code and narrow semantic operations, fewer broad premium gaps.

## 20. Scheduling

There are two calendars.

### Capability calendar
Configured in external platforms. It changes rarely and expresses availability of cognition.

### Work calendar
Maintained by the program. It changes frequently and expresses which work should be ready for which future capability windows.

A scheduled platform event is a **capability pulse**, not a hard-coded task assignment.

## 21. MCP bridge

The bridge between external platforms and durable continuations should remain thin.

Conceptually:

```text
turn_begin(slot_id)
turn_end(interrupt_id, typed_result)
```

Internally, the ADK realization maps this to `RequestInput` / resume semantics. Before constructing a resume response, the bridge MUST validate the full result against the Engine's output contract and bind it to the expected interrupt and obligation. The bridge does not host an agent loop.

## 22. Program maintenance

`maintain_program` is a persistent Task like any other. Its object happens to be the program itself.

It can inspect backlog, deduplicate work, compact context, review pending interrupts, analyze Braintrust evidence, create or supersede Tasks, and propose new WorkflowRevisions.

Meta-work is ordinary work whose subject is other work.

## 23. Workflow evolution

A running workflow revision is immutable. A Task may propose a new revision, but the invocation that began under `W17` completes under `W17`. Future work may use `W18`.

Promotion of workflow revisions should be staged:

```text
proposed -> schema-valid -> constructible -> tested -> shadow -> canary -> active
```

High-impact external effects may require human gates. Low-risk changes can eventually promote automatically after evidence is sufficient.

## 24. Security principle

The important boundary is not that cognition may only "judge." External cognition may design, code, plan, and propose structural changes. The stronger invariant is:

> **Cognition produces typed results; durable software owns their application.**

Unmediated side effects are avoided. Validation, tests, policies, and workflow transitions interpret the cognitive contribution after the model is gone.

## 25. Architectural metrics

The Engine should track at least:

- Continuation Readiness
- Deterministic Runway
- Semantic Debt
- Interrupt Rate
- Serial Interrupt Depth
- Expected Cognitive Wait
- Cognitive Compression
- Handoff Repair Rate
- Premium Dependency
- API Rescue Rate
- Rescue Recurrence
- Rescue Compilation Rate

## 26. Final statement

The Engine is a durable program whose state, tasks, and continuations persist while computation appears only when needed.

Google ADK executes the durable workflow. Jev supplies narrow semantic operations. External premium systems satisfy open Cognitive Interrupts. Braintrust records the empirical consequences so the program can improve its planning, routing, templates, and cognitive placement over time.

The target trajectory is:

```text
expensive cognition
 -> experience
 -> reusable structure
 -> cheap repeatability
```

Four sentences summarize the architecture:

> **The intelligence exists only in the gaps.**

> **The process carries the thinker forward, not the other way around.**

> **Premium cognition must leave deterministic continuation behind.**

> **Repeated cognition should eventually compile into software.**
