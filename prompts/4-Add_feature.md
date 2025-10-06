You are my AI development assistant inside a Codev + ai-dev-tasks hybrid project.

Goal:
Add a new feature called "<FEATURE_NAME>" to my existing repository using the SP(IDE)R flow.

Follow these steps carefully:

1. **Specify**
   - Use `ai-dev-tasks/create-prd.md` to write a concise, testable PRD.
   - Save it in `codev/specs/<FEATURE_NAME>/prd.md`.

2. **Plan**
   - Use `ai-dev-tasks/generate-tasks.md` based on the PRD.
   - Create a markdown task list and save it in `codev/plans/<FEATURE_NAME>/tasks.md`.
   - Make sure task IDs follow `T1`, `T2`, etc., and each line starts with `- [ ]`.

3. **Implement**
   - For each task, use `ai-dev-tasks/process-task-list.md`.
   - Produce implementation notes in `codev/impl/<FEATURE_NAME>/T<ID>_<timestamp>.md`.
   - Follow this sequence in PowerShell:
     ```
     python devflow.py --feature <FEATURE_NAME> --next
     python devflow.py --feature <FEATURE_NAME> --done <TaskID>
     ```
   - Implement minimal changes, then move to the next task.

4. **Defend**
   - Write or update the test plan in `codev/defend/<FEATURE_NAME>/test_plan.md`.
   - Add both positive and negative test scenarios.

5. **Evaluate**
   - Run tests locally and summarize results in `codev/evaluate/<FEATURE_NAME>/results.md`.

6. **Review**
   - Add retrospective notes and lessons in `codev/review/<FEATURE_NAME>/retrospective.md`.
   - If any templates or prompts can be improved, suggest edits to `ai-dev-tasks/*.md`.

7. **Git**
   - Use the branch name `feat/<FEATURE_NAME>` and commit convention:
     - `spec(<FEATURE_NAME>): PRD created`
     - `plan(<FEATURE_NAME>): tasks defined`
     - `impl(<FEATURE_NAME>): implemented T<ID>`
     - `test(<FEATURE_NAME>): added tests`
     - `review(<FEATURE_NAME>): retro and improvements`

Deliverables:
- The updated file tree under `codev/` with new folders.
- The filled PRD and tasks files.
- Implementation notes for at least one sample task (T1).
- Suggested test plan and evaluation placeholders.
