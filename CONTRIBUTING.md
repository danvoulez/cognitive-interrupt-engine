# Contributing

This repository is spec-first. Changes should preserve the architectural separation between persistent continuation and transient actors.

## Preferred contribution shape

Contributions should be framed as one of:

- clarification of a portable architectural invariant;
- correction to an implementation mapping;
- executable schema or acceptance test;
- vertical-cycle implementation;
- empirical result that changes routing, cost, or reliability assumptions.

Avoid adding a parallel workflow engine when a native runtime primitive already exists.

## Design questions for every change

- Does this make continuity depend on an actor that can disappear?
- Is this exact work better represented deterministically?
- Is this narrow semantic work better represented by Jev?
- Does an external cognitive contribution return a typed continuation-ready result?
- Does the change increase serial interrupt depth?
- Can repeated reasoning here be templated or compiled into software?
