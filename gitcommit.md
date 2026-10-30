# Git Commit Automation Instruction

When this file is referenced or invoked by the user, the AI assistant must automatically stage, commit, and push all recent changes using a meaningful, concise, and well-structured commit message.

---

### Workflow for the AI Assistant

1. **Inspect Changes**:
   - Check modified and untracked files with `git status -s`
   - Review file changes using `git diff --cached` or `git diff` to formulate an accurate summary.

2. **Generate Readable Commit Message**:
   - Follow standard Conventional Commit syntax:
     - `feat:` for new features
     - `fix:` for bug fixes
     - `refactor:` for code restructuring
     - `chore:` for configuration, build, or tooling changes
   - Summarize the changes clearly in imperative mood (e.g., `feat: implement admin authentication system with middleware and brute-force throttling`).

3. **Execute Git Commands**:
   Run the following sequence in the project root:
   ```bash
   git add .
   git commit -m "<type>(<scope>): <clear readable description of changes>"
   git push -u origin main
   ```

4. **Confirm**:
   Output the commit hash, message, and push status to the user.

---

### Manual Execution Helper

If running manually in PowerShell / Terminal:

```bash
git add .
git commit -m "feat(auth): implement admin authentication with AdminAuthentication middleware and brute-force protection"
git push -u origin main
```
