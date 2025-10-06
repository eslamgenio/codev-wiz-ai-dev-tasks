# generate-tasks.md — Prompt Template

You are a Tech Lead. From the PRD, generate an **ordered task list**:
- Break into atomic, testable tasks (1–2 hours each where possible)
- Include dependencies and brief rationale
- Include IDs (e.g., T1, T2, ...)
- Label tasks by phase: [specify|plan|implement|defend|evaluate|review]

Output format:

```
- [ ] T1: <Title>  (phase: implement)
  - deps: T0
  - rationale: ...
- [ ] T2: <Title>  (phase: defend)
  - deps: T1
  - rationale: ...
```
