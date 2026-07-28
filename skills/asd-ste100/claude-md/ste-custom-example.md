# Technical Writing — ASD-STE100 (custom example)

Example of a profile that keeps STE grammar but overrides three rules to match a house style guide. Copy and edit. This profile deliberately breaks STE rules S-4 and X-1, so its output is STE-derived rather than STE.

Scope: procedures, manuals, warnings, work cards, maintenance steps.

## Overrides

1. Articles dropped, fragments allowed. Overrides STE S-4. "Remove bolt." is correct here.
2. All lists numbered, sequential or not. Overrides STE X-1. Numbers make review comments easier to reference.
3. Cap of 20 words for all text, procedural and descriptive. Carve-out: root-cause, security, and technical guidance may exceed the cap when a split would lose meaning. Flag the overrun rather than forcing the split.

## Everything else still applies

4. One instruction per sentence. Imperative: "Remove bolt."
5. Active voice only. Never "bolt should be removed".
6. No -ing forms. Exception: Technical Names ("landing gear", "warning light").
7. Use must, can, will. Never shall, should, may, might.
8. Simple tenses only. Never "has been removed" — use "was removed".
9. Max 3 nouns in a cluster. Break longer with prepositions.
10. Short common words: do, start, stop, use, make sure, before, after, if, to.
11. One word, one meaning. Never vary synonyms for the same thing.
12. No etc., e.g., i.e., and/or. List items or restructure.
13. Technical Names and Technical Verbs always allowed. Never simplify part names.
14. WARNING = injury risk. CAUTION = equipment damage. NOTE = information only.
15. Warnings state command first, then reason. "DO NOT TOUCH VALVE. VALVE IS HOT."
16. Max 6 sentences per paragraph in descriptive text.

Full STE: use `ste-strict.md` instead, or run the skill with the strict profile.
