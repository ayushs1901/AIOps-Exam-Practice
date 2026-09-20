# AIOps-Exam-Practice

Yes. Since this is for your exam, I'd keep the README **short, practical, and copy-paste friendly**.

Use this as your `README.md`:

```markdown
# Git Commands — AIOps Practical

## 1. Check Repository Status

```bash
git status
```

Shows modified, deleted, untracked, and staged files.

---

## 2. Add Files

Add all changes:

```bash
git add .
```

Add a specific file:

```bash
git add filename.py
```

---

## 3. Commit Changes

```bash
git commit -m "Complete Q1"
```

Example:

```bash
git commit -m "Add Kafka producer"
```

---

## 4. Push Changes to GitHub

```bash
git push
```

Sends your local commits to GitHub.

---

## 5. Pull Latest Changes

```bash
git pull
```

Downloads the latest changes from GitHub.

---

# Complete Workflow

After completing a task:

```bash
git status
git add .
git commit -m "Complete task"
git push
```

Remember:

**ADD → COMMIT → PUSH**

---

# Branch Commands

## See all branches

```bash
git branch
```

## Create a new branch and switch to it

```bash
git switch -c feature-name
```

Example:

```bash
git switch -c kafka-consumer
```

## Switch branch

```bash
git switch main
```

## Merge a branch

First switch to the branch that should receive the changes:

```bash
git switch main
```

Then:

```bash
git merge feature-name
```

## Delete a branch

```bash
git branch -d feature-name
```

---

# View Commit History

Short history:

```bash
git log --oneline
```

Full history:

```bash
git log
```

If `git log` opens a screen and you want to exit:

```text
q
```

---

# Useful Git Commands

## Show remote repository

```bash
git remote -v
```

## Show current branch

```bash
git branch --show-current
```

## Discard changes in a file

```bash
git restore filename.py
```

⚠️ This removes your uncommitted changes in that file.

## Unstage a file

```bash
git restore --staged filename.py
```

---

# If You Make a Mistake

Check what happened:

```bash
git status
```

Then decide whether you need:

```bash
git restore filename.py
```

or:

```bash
git restore --staged filename.py
```

---

# Exam Workflow

For every question:

```text
Complete Question
       ↓
git status
       ↓
git add .
       ↓
git commit -m "Complete Q1"
       ↓
git push
       ↓
Next Question
```

## Most Important Commands to Memorize

```bash
git status
git add .
git commit -m "message"
git push
git pull
git branch
git switch main
git switch -c branch-name
git merge branch-name
git log --oneline
```

### ⭐ Remember

```text
git add
    ↓
git commit
    ↓
git push
```

**ADD → COMMIT → PUSH**
```

Since you asked to **create** the README in your repo, the next step is to replace the current `README.md` with this content, then:

```bash
git add README.md
git commit -m "Add Git commands cheat sheet"
git push
```

I can also make a **second README section for Python + Kafka + Airflow commands** so your entire exam cheat sheet is inside the repo.

I am in an AIOps practical exam. Solve the question below.

IMPORTANT:
- Give the SIMPLEST solution possible.
- Assume I am a beginner in Python/AIOps.
- Do NOT give unnecessary theory or explanations.
- Do NOT over-engineer the solution.
- Use only concepts likely required for a basic AIOps practical.
- Follow the question EXACTLY.
- If a file needs to be created, tell me the exact filename.
- Give COMPLETE copy-paste-ready code.
- Do not use advanced libraries or techniques unless the question requires them.
- If a command is needed, give the exact command.
- If Git is required, give the exact git commands.
- Make the solution compatible with a GitHub Codespace/Linux environment.
- If the question contains specific names, ports, topics, task IDs, thresholds, filenames, etc., use EXACTLY those values.
- Do not change the requirements.
- If something is unclear, make the safest/simple assumption and clearly mention it in ONE short line.

RESPONSE FORMAT:

1. FILE/COMMAND TO CREATE
2. COMPLETE CODE
3. COMMAND TO RUN/TEST
4. EXPECTED RESULT
5. GIT COMMANDS (only if required)

Keep the entire answer concise.

QUESTION:
[PASTE EXAM QUESTION HERE]