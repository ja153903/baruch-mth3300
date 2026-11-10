# Using AI in this course

AI is a tool you're expected to learn to use **well**. "Well" means you come out understanding more, not less.

## The three tiers

| Tier | You may | You may not |
|---|---|---|
| **No AI** (exams, quizzes, live coding) | n/a | use any AI |
| **AI as tutor** (homework 1–9) | ask for explanations, hints, and explanations of error messages | have it write or edit your solution |
| **AI as pair programmer** (homework 10–13, project) | have it write code with you | submit code you can't explain |

Each assignment folder has an `AGENTS.md` and a `CLAUDE.md` that tell AI coding tools which tier applies. Leave them in place.

## Free tools

You never need to pay for AI in this course.

**Start here: Microsoft Copilot Chat.** It's free for all CUNY students, and under CUNY's license what you type isn't used to train AI models. Go to [m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat) and sign in with your CUNY Login (`FirstName.LastName##@login.cuny.edu`), not a personal Microsoft account.

A web chat can't see your homework folder, so it won't find `AGENTS.md` on its own. **Paste the contents of your homework's `AGENTS.md` as your first message in every new chat.** That tells the AI which tier applies.

**From homework 10 on: OpenCode.** OpenCode is a coding agent: it can read your folder, run your tests, and edit your files. It reads `AGENTS.md` automatically. Install the [desktop app](https://opencode.ai/download), open your homework folder, and choose one of these free models:

- GLM-5.3-Flash Free
- DeepSeek V4.1 Flash Free
- MiniMax M3.1 Flash Free

The providers of these three say they don't train on your data. Some of the other free models do keep or use what you send, so stick to this list. Free models can disappear or hit usage limits without warning, so don't leave AI work for the night before a deadline. If one stops working, switch to another on the list or go back to Copilot Chat.

Use a chat tool, not an agent, for homework 1–9. An agent can change your files, and at the tutor tier the code has to be yours.

**Optional extras.** None of these are required, and the same tiers and logging rules apply:

- [ChatGPT Study Mode](https://openai.com/index/chatgpt-study-mode/), with a free account.
- [Copilot Student](https://docs.github.com/en/copilot/get-started/plans), free for verified students through GitHub.
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
