# Using AI in this course

AI is a tool you're expected to learn to use **well**. "Well" means you come out understanding more, not less.

## The three tiers

| Tier | You may | You may not |
|---|---|---|
| **No AI** (exams, quizzes) | n/a | use any AI |
| **AI as tutor** (homework 1–9) | ask for explanations, hints, and explanations of error messages | have it write or edit your solution |
| **AI as pair programmer** (homework 10–13, AI build session, project) | have it write code with you | submit code you can't explain |

Each assignment folder has an `AGENTS.md` and a `CLAUDE.md` that tell AI coding tools which tier applies. Leave them in place.

## Free tools

You never need to pay for AI in this course.

**Your main tool: GitHub Copilot in VS Code.** It's free through the GitHub Student Developer Pack (see [`setup.md`](setup.md)). It works inside your editor, so it can see your homework folder and reads `AGENTS.md` automatically. Copilot Chat has modes; use the right one for the tier:

- **Homework 1–9: Ask mode.** It explains and answers questions but doesn't edit your files. At the tutor tier, the code has to be yours.
- **Homework 10–13, the AI build session, and the project: Agent mode.** It can edit files and run your tests.

Copilot gives you a monthly allowance. If you run out, switch to one of the tools below until it resets.

**Backup agent: OpenCode.** OpenCode is another coding agent. Like Copilot, it reads `AGENTS.md` and supports skills and MCP servers, so what you build in this course works in both. Install the [desktop app](https://opencode.ai/download), open your homework folder, and choose one of these free models:

- GLM-5.3-Flash Free
- DeepSeek V4.1 Flash Free
- MiniMax M3.1 Flash Free

The providers of these three say they don't keep or train on your data. Some of OpenCode's other free models do, so stick to this list. Free models can disappear without warning; if one stops working, switch to another on the list.

**For anything private: CUNY Copilot.** [Microsoft Copilot Chat](https://m365.cloud.microsoft/chat), signed in with your CUNY Login (`FirstName.LastName##@login.cuny.edu`), is the only AI tool CUNY licenses, and the only one covered by CUNY's privacy protections. It's a web chat, so it can't see your files: paste your homework's `AGENTS.md` as your first message in every new chat.

**Optional extras.** None of these are required, and the same tiers and logging rules apply:

- [ChatGPT Study Mode](https://openai.com/index/chatgpt-study-mode/), with a free account.
- Claude Code or Codex, if you already pay for Claude or ChatGPT. Both pick up the instructions in each homework folder.
- A free year of Google AI Pro, for US college students 18 or older who sign up by December 31, 2026. **It charges $19.99 a month after the free year unless you cancel.**

Whatever tool you use, don't paste in passwords, your EMPLID, or other personal information.

*Model list and offers last checked November 2026.*

## Prompts that help you learn

| Instead of… | Try… |
|---|---|
| "Fix my code" | "Here's my code, my input, what I expected, and what happened. What concept am I missing?" |
| "Write a function that…" | "I'm planning to solve this by… Is there a flaw in my plan?" |
| "Explain recursion" | "Explain recursion using my `factorial` function, then quiz me on it" |
| Pasting the whole assignment | Pasting the smallest piece that shows your problem |

**Predict first.** Before you ask why code behaves a certain way, write down what you *expected* it to do. The gap between your prediction and the result is the thing you need to learn.

## AI makes mistakes

AI tools sometimes invent functions that don't exist, get edge cases wrong, or sound sure of things that are false. Your tests and the official documentation decide what's true, not the AI.

## The AI log

Every homework includes an `AI_LOG.md`. For each significant session, write down:

```markdown
## Session: <date>, <topic>
- **I asked:** …
- **It said (summary):** …
- **What I did with it:** accepted / changed / rejected, and **why**
```

Logged AI use is **never** penalized. AI use you didn't log is an academic integrity issue.
