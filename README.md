# Skillrack

Skills for [Claude Code](https://claude.com/claude-code). One clone gets the lot; copy the ones you want.

## Skills

| Skill | What it does |
|---|---|
| [asd-ste100](skills/asd-ste100) | Checks technical writing against ASD-STE100 Simplified Technical English, with configurable style profiles and an independent audit pass. |

## Install

Clone, then copy the skills you want into your Claude Code skills directory:

```bash
git clone https://github.com/skillrackAI/skillrack.git
```

```bash
cp -r skillrack/skills/asd-ste100 ~/.claude/skills/
```

Each skill has its own README with usage and options. Nothing here depends on anything else here, so take one skill or all of them.

## What makes a skill worth adding here

Two things, held to consistently:

1. **Deterministic work goes in a script.** Anything a model would otherwise redo from scratch on every run — counting, matching, parsing, rewriting a file in place — belongs in code. It costs less, it gives the same answer twice, and it frees the model for the judgment calls.

2. **The model checks its own work with fresh eyes.** A model reviewing its own output in the same context approves it. A second pass that never saw the reasoning does not. Where a skill produces something a user has to trust, that second pass is the difference between a tool and a suggestion.

## Licence

MIT. See [LICENSE](LICENSE).

Individual skills may reference external standards or specifications. Those remain the property of their owners, and each skill's README says what it is and is not. Nothing here is endorsed by or affiliated with the bodies that publish those standards.
