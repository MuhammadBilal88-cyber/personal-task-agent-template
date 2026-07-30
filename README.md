# Personal Task Agent — Starter Template

Module 3 · Week 4 · Project

An agent that completes a real multi-step task on one command — research a topic,
save notes to a file, and email a summary — **with a leash on**: a human approval
step, full logging, and a hard cap so the loop can't run forever.

The scary parts (the loop, the approval gate, logging, the iteration cap) are
already done. Your job is to fill in a few small TODOs and make it yours.

---

## What's in here

```
personal-task-agent/
  agent.py        # the reason->act->observe loop + approval + logging + cap
  tools.py        # the 3 tools: research, save_note, send_email  (your TODOs)
  config.py       # model, caps, and which tools auto-run vs need approval
  .env.example    # copy to .env and paste your API key
  requirements.txt
  README.md       # you are here
  notes/          # save_note writes here
  logs/           # every run writes an audit log here
```

---

## Setup (about 5 minutes)

1. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Add your API key**
   ```bash
   cp .env.example .env
   ```
   Open `.env` and paste your real key after `ANTHROPIC_API_KEY=`.
   Never commit `.env` — it's already in `.gitignore`.

3. **Run it once** (it works out of the box; the email is a safe dry-run)
   ```bash
   python agent.py "Research the James Webb telescope, save the notes to webb.md, then email a summary to me@example.com"
   ```
   Watch the loop run in your terminal, approve the email when it asks,
   then check the new files in `notes/` and `logs/`.

---

## Your assignment

The template runs, but two tools are only starters. Make it genuinely useful:

- [ ] **Fill in `research()` in `tools.py`.** Right now it just asks the model to
      summarise what it already knows. Make it return *real, useful* notes —
      enable Anthropic's web search in that call, or plug in a search API and
      summarise the results.
- [ ] **Write a good email step.** Make sure the agent turns the saved notes into
      a clean, readable summary in the email body — not a wall of raw text.
- [ ] **Check your permissions.** Look at `AUTO_APPROVE` in `config.py`. Confirm
      that `send_email` is NOT on it (so it always asks first) and decide whether
      anything else should be gated.
- [ ] **(Stretch) Send a real email.** Only if you want to. Keep it behind the
      approval gate. A Gmail MCP connector or a transactional email API is safer
      than raw SMTP.

---

## Definition of done

Your project is done when **all** of these are true:

1. **One command** runs the whole task end to end (research → notes → email).
2. The **email waits for your approval** — typing `n` skips it, `y` sends it.
3. A **log file** in `logs/` shows every tool call, its result, the approval, and
   a timestamp.
4. The **iteration cap** is in place (it is — don't remove it).
5. Your **API key is in `.env`**, not pasted into any `.py` file.

Bring a clean run and its log to the next class — you'll demo it live.

---

## How the guardrails work (so you can explain them)

- **Approval gate** — In `config.py`, `AUTO_APPROVE` lists the tools that run
  without asking. Everything else calls `ask_human()` first and only runs on `y`.
  Least privilege: reading is safe, sending is not.
- **Logging** — `log()` in `agent.py` writes every call, result, and approval to
  both the console and a timestamped file in `logs/`.
- **Iteration cap** — `MAX_ITERATIONS` in `config.py` stops the loop after N turns
  no matter what, so a confused agent can never spend money forever.

---

## Troubleshooting

- **`AuthenticationError`** — your key isn't loaded. Check `.env` exists and has a
  real key, and that you ran `pip install -r requirements.txt` (which installs
  `python-dotenv`).
- **A tool never gets called** — its `description` in `tools.py` is probably too
  vague. Describe it like you're briefing a new teammate.
- **`TypeError` when a tool runs** — your `input_schema` property names must match
  the function's argument names exactly.
- **It loops and stops at the cap** — the model is stuck. Make your goal more
  specific, or check that each tool returns something useful.
