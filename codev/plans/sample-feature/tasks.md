# Tasks — Sample Feature

> Generated from PRD using `ai-dev-tasks/generate-tasks.md`

- [ ] T1: Scaffold feature module (phase: implement)
  - deps: 
  - rationale: Set baseline structure for code & tests
- [ ] T2: Implement core logic (phase: implement)
  - deps: T1
  - rationale: Business logic with input validation
- [ ] T3: Unit tests for core logic (phase: defend)
  - deps: T2
  - rationale: Ensure correctness and cover edge cases
- [ ] T4: Wire UI/CLI (phase: implement)
  - deps: T2
  - rationale: Basic interface integration
- [ ] T5: Integration test (phase: evaluate)
  - deps: T3, T4
  - rationale: End-to-end validation
- [ ] T6: Review & lessons (phase: review)
  - deps: T5
  - rationale: Retro and prompt/template improvements
