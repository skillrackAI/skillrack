---
name: asd-ste100
description: Check and rewrite text against ASD-STE100 Simplified Technical English (STE). Use whenever the user asks to check, lint, review, or rewrite writing for STE compliance, mentions "STE", "Simplified Technical English", "ASD-STE100", or controlled language, or wants technical documentation (procedures, manuals, warnings, maintenance instructions, work cards) made simpler, clearer, or compliant. Also use for general "check my technical writing" requests on procedural or descriptive documentation.
---

# ASD-STE100 Writing Checker

Check text against ASD-STE100 Simplified Technical English. Produce a numbered violation report, a compliant rewrite, and an independent audit.

STE is a controlled language for technical documentation. It has two parts: writing rules (grammar, style, sentence limits) and a dictionary of approved words, where each approved word carries one meaning and one part of speech. The authoritative specification is free from asd-ste100.org. This skill applies the rules and the best-known dictionary substitutions, and marks uncertain vocabulary as `word (verify)` rather than guessing.

## Step 0 — Load the style profile

STE collides with common house style guides in four predictable places. Rather than guess, this skill reads a saved profile.

Look for a profile at `~/.claude/ste-profile.json`. If it exists, load it, state the profile name in the report header, and go to step 1 without asking anything.

If no profile exists, ask ONE question. Present it exactly like this and wait for a single digit:

```
No STE profile found. Which style?

1. Strict — every STE rule applied. Nothing overridden.
2. Readable — STE grammar, but numbered lists throughout and a 20-word cap everywhere.
3. Custom — I ask about each of the four conflicts, one at a time.
```

For choice 3, ask these four questions one at a time, never batched. Each needs a single digit:

```
1/4 Articles and grammar. STE rule S-4 forbids telegraphic style.
1. Keep articles and full sentences — "Remove the bolt."
2. Drop articles, allow fragments — "Remove bolt."
```

```
2/4 List numbering. STE rule X-1 reserves numbers for sequential steps.
1. STE convention — numbers for steps, letters or dashes for non-sequential items
2. Always numbered — easier to reference, but implies order where none exists
```

```
3/4 Sentence length. STE caps at 20 words procedural, 25 descriptive.
1. STE limits, hard caps
2. 20 words everywhere, hard cap
3. 20 words everywhere, carve-out for root-cause, security, and technical guidance
```

```
4/4 Warning placement. STE rule C-2 puts warnings before the step they guard.
1. Warning before the step — safety convention
2. Action first, warning after — matches action-first house style
```

Write the answers to `~/.claude/ste-profile.json` so the questions never repeat:

```json
{
  "profile": "custom",
  "articles": "keep",
  "lists": "ste",
  "sentence_limit": {"procedural": 20, "descriptive": 25, "carve_out": false},
  "warning_placement": "before"
}
```

Presets map to these values. Strict: articles `keep`, lists `ste`, limits 20/25 no carve-out, warnings `before`. Readable: articles `keep`, lists `numbered`, limits 20/20 no carve-out, warnings `before`.

To change the profile later, the user says "change my STE profile" — delete the file and re-ask.

## Workflow

1. **Classify the text.** Procedural (instructions to do something) or descriptive (explanation, background). Mixed documents: classify per paragraph, because the sentence limits differ.

2. **Run the mechanical lint.** It catches length, -ing forms, passive markers, and known unapproved words deterministically:
   ```bash
   python3 scripts/ste_lint.py --limit 20 <file>
   ```
   Pass the limit from the loaded profile. For text pasted in chat, write it to a temp file first. Script output is candidates, not verdicts — judge each one, and discard any that the profile has overridden.

3. **Read `references/writing-rules.md`.** Check every category: words, noun clusters, verbs, sentences, procedures, descriptive text, safety instructions, punctuation. Skip only the rules the profile overrides.

4. **Check vocabulary** against `references/word-substitutions.md`. Two exemptions matter more than anything else here: Technical Names (nouns for parts, tools, systems, such as "overhead panel") and Technical Verbs (manufacturing and maintenance actions, such as "to drill", "to torque") are always allowed, even when absent from the dictionary. Flagging a real part name as a violation destroys trust in the whole report, so when in doubt, leave it alone.

5. **Write the report** using the template below, then the rewrite.

6. **Independent audit (mandatory).** Spawn a subagent with fresh context. It must see the inputs, never your reasoning. Give it:
   - The original text (file path).
   - The finished report and rewrite (save to a temp file first).
   - Paths to `references/writing-rules.md`, `references/word-substitutions.md`, `references/auditor.md`.
   - The active profile, verbatim.

   Tell it to follow `references/auditor.md` exactly. Run it synchronously. Append its verdict as an `## Audit` section. On FAIL, fix the problems and re-run the audit once. Report the final verdict either way — a hidden FAIL makes the whole report worthless. Where no subagent tool exists, do a self-audit and label it "self-audit, not independent".

## Report template

Use this structure:

```
# STE Check: <name or first words of text>

<one-line verdict, e.g. "14 violations. Rewrite below.">

## Summary
1. Profile: <strict / readable / custom>
2. Text type: <procedural / descriptive / mixed>
3. Sentences checked: <n>
4. Violations found: <n>

## Violations
1. [<category>] "<quoted original>" — <rule broken, one short sentence> — Rewrite: "<fix>"
2. ...

## Compliant rewrite
<full rewritten text>

## Audit
<auditor verdict, appended verbatim>
```

Report rules:

1. Number every violation. Quote the original exactly so the user can find it.
2. Numbering runs sequentially across the whole report. Never restart per section.
3. Category tags: `word`, `verb`, `noun-cluster`, `sentence-length`, `passive`, `-ing form`, `procedure`, `paragraph`, `warning`, `punctuation`.
4. Uncertain vocabulary gets `word (verify)` and a note to check the official dictionary.
5. Long text (more than about two pages): rewrite the worst sections, offer the rest as follow-up.
6. Zero violations: say so, skip the rewrite, still run the audit.
7. Never use markdown blockquotes. Use quotation marks or fenced blocks.
8. Name the profile in every report. On any profile except strict, say which rules were overridden, so nobody mistakes the output for full STE.
9. Never describe output as certified, approved, or endorsed. This is an unofficial tool. Only ASD and the STEMG speak to conformance.

## Rewriting guidance

Do not patch flagged words in place. Restructure, because most violations are symptoms of sentence shape rather than word choice:

1. One instruction per sentence, imperative form.
2. Active voice. Name the doer, or use the imperative.
3. Break long sentences at logical joints. Use vertical lists for step sequences.
4. Split noun clusters of four or more: "runway light connection resistance calibration" becomes "calibration of the resistance on a runway light connection".
5. Warning content is always command first, then reason: "DO NOT TOUCH THE VALVE. THE VALVE IS HOT." Placement follows the profile; this ordering does not.
6. Keep the technical meaning identical. A rewrite that reads better but means something different is a failure, so flag the ambiguity and ask instead of guessing.

Apply the profile to articles, list numbering, sentence limits, and warning placement. Everything else in the rules file applies in every profile.
