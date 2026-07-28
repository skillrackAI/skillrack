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

1. **Strict** — every rule applied, nothing overridden. Use this when the output has to hold up to review.
2. **Readable** — STE grammar, numbered lists throughout, flat 20-word cap.
3. **Custom** — the skill asks about each conflict one at a time.

Any profile except strict deliberately breaks STE rules, so its output is STE-derived rather than STE. The skill says which profile produced a report rather than letting you assume.

This is an unofficial tool. It does not certify anything, and no output from it should be described as approved or endorsed by ASD. Only ASD and the STEMG speak to what conforms to the specification.

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

1. The bundled word list is a short set of well-known substitutions written for this tool. It is not the ASD dictionary and is no substitute for it.
2. Uncertain vocabulary is flagged `word (verify)` rather than guessed at, so you know what still needs checking against the official dictionary.
3. Technical Names and Technical Verbs are exempt from vocabulary checks by design. Part names and maintenance verbs are never simplified.
4. Rules here are summarised in this project's own words. Read the specification itself for the authoritative text.

## Trademark and copyright

ASD-STE100 and Simplified Technical English are trademarks of ASD, AeroSpace and Defence Industries Association of Europe, Brussels (EU trade mark 017966390). The specification and its dictionary are copyright ASD.

This project is independent and unaffiliated. It is not endorsed, approved, or certified by ASD or the STEMG. The standard is named here only to describe what the tool checks against.

The specification is available at no cost from [asd-ste100.org](https://asd-ste100.org). No part of it is reproduced in this repository, and the dictionary is not redistributed here. Get both from ASD directly.

## Licence

MIT, covering this tool only. See [LICENSE](LICENSE). The licence grants no rights in ASD's specification, dictionary, or trademarks.
