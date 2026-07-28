# ASD-STE100 for Claude

A Claude Code skill that checks technical writing against [ASD-STE100 Simplified Technical English](https://asd-ste100.org), plus drop-in CLAUDE.md rule sets.

STE is the controlled language used for aerospace and defence maintenance documentation. It restricts grammar and vocabulary so that a procedure means exactly one thing to a technician reading it in a second language, at night, on a wet ramp. The rules are useful well outside aviation — anywhere an instruction being misread is expensive.

## What this does

1. Lints text for sentence length, -ing forms, passive voice, and unapproved vocabulary.
2. Reports every violation with the rule broken and a suggested fix.
3. Rewrites the text to comply.
4. Runs an **independent audit agent** over its own output, with fresh context, to catch what the first pass missed.

Step 4 is the part that makes it trustworthy. A model checking its own rewrite tends to approve it. A second agent that never saw the reasoning does not.

## Style profiles

STE collides with most house style guides in four predictable places. On first run the skill asks which way you want each one resolved, saves the answer to `~/.claude/ste-profile.json`, and never asks again.

| Conflict | STE rule | Common house preference |
|---|---|---|
| Articles and fragments | S-4 — keep full grammar | Drop articles for concision |
| List numbering | X-1 — numbers for sequential steps only | Number everything for easy reference |
| Sentence length | S-1/S-2 — 20 procedural, 25 descriptive | One flat cap |
| Warning placement | C-2 — warning before its step | Action first |

Three presets ship with it:

1. **Strict** — full ASD-STE100, nothing overridden. Use this when output must be certifiable.
2. **Readable** — STE grammar, numbered lists throughout, flat 20-word cap.
3. **Custom** — the skill asks about each conflict one at a time.

Any profile except strict produces STE-derived output, not certifiable ASD-STE100. The skill says so in every report rather than letting you assume otherwise.

## Install

Copy the skill into your Claude Code skills directory:

```bash
cp -r skills/asd-ste100 ~/.claude/skills/
```

Then ask Claude to check something:

```
check this procedure against STE
```

## CLAUDE.md rule sets

If you want Claude writing in STE by default rather than checking after the fact, paste one of these into your `CLAUDE.md`:

1. `claude-md/ste-strict.md` — full STE, 26 rules, no overrides.
2. `claude-md/ste-custom-example.md` — worked example of a profile that overrides three rules for a house style.

The skill and the CLAUDE.md rules serve different jobs. The rules shape what Claude writes. The skill proves it, with a lint pass and an independent audit.

## Repository layout

```
skills/asd-ste100/
  SKILL.md                        skill definition and workflow
  references/writing-rules.md     the STE rules, by category
  references/word-substitutions.md  common unapproved to approved pairs
  references/auditor.md           instructions for the audit agent
  scripts/ste_lint.py             deterministic lint pass
claude-md/
  ste-strict.md                   full STE for CLAUDE.md
  ste-custom-example.md           example profile with overrides
```

## Scope and limits

1. The bundled word list covers common substitutions. It is not the full dictionary, which runs to roughly 900 approved words.
2. Uncertain vocabulary is flagged `word (verify)` rather than guessed at, so you know what still needs a human check.
3. Technical Names and Technical Verbs are exempt from vocabulary checks by design. Part names and maintenance verbs are never simplified.
4. The official specification and dictionary are free from [asd-ste100.org](https://asd-ste100.org). This project is an independent tool and is not affiliated with or endorsed by AeroSpace and Defence Industries Association of Europe.

## Licence

MIT. See [LICENSE](LICENSE).
