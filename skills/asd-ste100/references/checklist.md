# Common Errors — Fast Triage

`writing-rules.md` is organised by category, which is right for a full sweep but wrong for a first pass. This file is ordered by how often each problem actually appears, so a quick read down the list catches most of what is wrong with a document before the systematic check begins.

Rule IDs in brackets point back to `writing-rules.md`.

## The frequent ten

1. **Sentence over the limit.** [S-1, S-2] The single most common failure, and usually the cause of several others — long sentences are where passives, gerunds, and multiple instructions hide. Fix this first and the count drops on its own.

2. **Passive voice in a procedure.** [V-3] "The bolt should be removed" leaves the doer unstated. A technician needs to know the instruction is for them. Convert to the imperative.

3. **-ing forms.** [V-2] "Removing the pump requires disconnecting the connector." Two gerunds, no instruction. Becomes: "Disconnect the connector. Remove the pump." Watch for Technical Names — "landing gear" is not a violation.

4. **shall / should / may / might.** [V-4, V-5] These blur requirement, recommendation, and permission. In documentation someone works from, that ambiguity is the whole problem. Use must, can, will.

5. **Long words with short equivalents.** [W-1] perform, utilize, ensure, commence, terminate, prior to, subsequent to, in order to. High-frequency, easy to fix, and worth catching early because they cluster — a writer who uses one usually uses several.

6. **More than one instruction per sentence.** [S-3] "Remove the panel and disconnect the connector and drain the reservoir." Three actions, one sentence, no way to track which are done. Split into steps.

7. **Steps buried in prose.** [S-5, P-3] A paragraph containing "then", "next", "after that" is a numbered list that has not been written as one. Nobody reads a procedure straight through; they scan for the step they are on, and prose hides it.

8. **Noun cluster of four or more.** [N-1] "runway light connection resistance calibration" — the reader has to guess what modifies what. Break it with prepositions.

9. **Complex tenses.** [V-6] "has been removed", "had been installed", "will have been checked". Simple past, present, or future carries the same meaning with less to parse.

10. **Warning in the wrong place or at the wrong level.** [C-1, C-2] A warning after its step has already failed. A CAUTION used for an injury risk understates it. Check placement and level together — these are the errors with real consequences.

## Also worth a look

11. **Vague openings.** [S-7] "There are three bolts that hold the panel" → "Three bolts hold the panel."
12. **etc. / e.g. / i.e. / and-or.** [W-6] List the items, or write the sentence again.
13. **Synonym drift.** [W-4, W-5] The same part called a "connector" in step 3 and a "plug" in step 7. The reader cannot tell whether these are two things.
14. **Condition after the command.** [S-6] "Open the valve if the pressure is more than 100 psi" makes the reader act, then reconsider. Put the condition first.
15. **Telegraphic style.** [S-4] "Remove bolt." Only a violation in profiles that keep articles. Check the profile before flagging.

## Errors the checker makes

Worth a separate pass, because a report full of false positives gets discarded whole, and then none of the real findings land either.

16. **Flagging a Technical Name.** [W-2] "overhead panel", "circuit breaker", "main gear door" are correct as written. Never simplify a part, tool, system, or document name. When unsure whether something is a part name, leave it alone — a missed finding costs less than a wrong one.

17. **Flagging a Technical Verb.** [W-3] drill, ream, torque, calibrate, swage, lockwire. These are approved regardless of how technical they look.

18. **Flagging an -ing word inside a Technical Name.** [V-2] landing gear, warning light, bearing housing, wiring loom.

19. **Guessing at vocabulary.** Anything not on the known list gets `word (verify)`, not a confident verdict. The bundled list is a fraction of the dictionary, and false confidence about a word being unapproved is worse than saying you do not know.

20. **Applying an overridden rule.** Check the profile before reporting articles, list numbering, sentence limits, or warning placement. Reporting a violation the user explicitly turned off reads as not having listened.

21. **Changing the meaning to fix the grammar.** A rewrite that reads better but says something different is a failure, not a fix. Flag the ambiguity and ask.
