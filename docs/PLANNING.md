# Cycle-Aware Planning Discipline

Planning is not the production of a narrative task list. It is the design of an executable cognitive topology.

## 1. Plan around cycles

A plan should identify:

```text
deterministic preparation
 -> semantic narrowing
 -> Cognitive Interrupt if necessary
 -> typed resolution
 -> deterministic continuation
 -> jobs/tests/evaluation
 -> next interrupt only if residual uncertainty remains
```

Task boundaries that ignore these transitions produce latency, Semantic Debt, and wasted premium windows.

## 2. Every prospective interrupt must answer six questions

1. Why can deterministic software not continue?
2. Why is Jev insufficient?
3. What evidence can be prepared before cognition arrives?
4. What exact typed output will unblock the continuation?
5. What deterministic work becomes possible immediately afterward?
6. Can this interrupt be combined with another independent open question to reduce serial waits?

## 3. Cognitive Critical Path

The planner must reason about **serial interrupt depth**, not only DAG dependencies.

Two plans can contain identical Tasks but radically different wall-clock latency:

```text
Plan A: interrupt -> interrupt -> interrupt -> interrupt
Plan B: one interrupt -> four deterministic branches -> optional final interrupt
```

Prefer the second when semantics permit.

## 4. Prepared workstation rule

A premium executor should arrive to:

- resolved input references;
- relevant files already selected;
- logs and metrics already collected;
- jobs already finished where possible;
- minimal context assembled;
- explicit uncertainty;
- response schema;
- clear done criteria.

Premium cognition should not spend scarce windows on deterministic housekeeping.

## 5. Continuation-Complete output

The planner must specify not only what the model should solve but what the next deterministic cycle requires.

A premium task is incomplete if the answer is correct but the workflow cannot continue without asking another model to interpret it.

## 6. Templating

Planning templates should encode recurring cycle shapes such as:

```text
collect -> classify -> investigate -> verify
```

```text
generate -> deterministic test -> Jev semantic check -> repair if needed
```

```text
machine evidence -> premium interpretation -> machine materialization
```

The goal is to make good cycle structure reusable rather than rediscovered.
