#!/usr/bin/env python3
"""Mechanical ASD-STE100 lint. Flags CANDIDATES for review, not verdicts.

Checks: sentence length, -ing forms, passive-voice markers, known
unapproved words/phrases, telegraphic "etc./e.g./i.e./and-or", and
4+ noun-cluster heuristics are left to the model (needs POS judgment).

Usage: ste_lint.py --type {procedural,descriptive} FILE
"""
import argparse
import re
import sys

UNAPPROVED_PHRASES = {
    "prior to": "before",
    "subsequent to": "after",
    "in order to": "to",
    "in the event of": "if",
    "in the event that": "if",
    "with regard to": "about",
    "in excess of": "more than",
    "carry out": "do",
    "comply with": "obey",
    "make sure that": None,  # approved; listed to avoid false hit on 'ensure' logic
    "and/or": '"X, or Y, or both"',
}

UNAPPROVED_WORDS = {
    "perform": "do", "performs": "do", "performed": "did/done", "accomplish": "do",
    "commence": "start", "commences": "start", "commenced": "started",
    "initiate": "start", "initiated": "started",
    "terminate": "stop", "terminated": "stopped", "cease": "stop",
    "utilize": "use", "utilizes": "use", "utilized": "used", "employ": "use",
    "ensure": "make sure", "ensures": "make sure", "verify": "make sure",
    "rectify": "correct", "indicate": "show", "indicates": "shows",
    "demonstrate": "show", "fabricate": "make", "retain": "keep", "retained": "kept",
    "subsequent": "later/next", "requires": "needs", "required": "needed/necessary",
    "assist": "help", "attempt": "try", "obtain": "get", "notify": "tell",
    "shall": "must", "should": "must", "may": "can", "might": "can",
    "whilst": "while", "concerning": "about", "additional": "more",
    "entire": "all/complete", "identical": "the same", "adequate": "enough (verify)",
    "sufficient": "enough (verify)", "frequently": "often",
    "etc": "list the items", "e.g": "for example", "i.e": "say it directly",
}

# -ing words commonly part of Technical Names; do not flag.
ING_ALLOWLIST = {
    "landing", "warning", "bearing", "coupling", "fitting", "housing",
    "wiring", "mounting", "packing", "rigging", "grounding", "shielding",
    "during",  # not a verb form
}

PASSIVE_RE = re.compile(
    r"\b(is|are|was|were|be|been|being)\s+(\w+ed|shown|done|made|put|set|held|kept|cut|torn|worn|broken|drawn|given|taken|found)\b",
    re.IGNORECASE,
)


def sentences(text):
    # naive splitter; good enough for lint candidates
    parts = re.split(r"(?<=[.!?])\s+", text.replace("\n", " "))
    return [p.strip() for p in parts if p.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--type", choices=["procedural", "descriptive"], default="procedural")
    ap.add_argument("--limit", type=int, default=None,
                    help="Word cap per sentence. Overrides --type. Take this from the style profile.")
    ap.add_argument("file")
    args = ap.parse_args()

    limit = args.limit if args.limit else (20 if args.type == "procedural" else 25)
    text = open(args.file, encoding="utf-8").read()
    findings = []

    for i, s in enumerate(sentences(text), 1):
        words = re.findall(r"[A-Za-z][A-Za-z'/-]*", s)
        if len(words) > limit:
            findings.append((i, "sentence-length", f"{len(words)} words (limit {limit})", s))

        low = s.lower()
        for phrase, repl in UNAPPROVED_PHRASES.items():
            if repl and phrase in low:
                findings.append((i, "word", f'"{phrase}" -> {repl}', s))

        for w in words:
            lw = w.lower().rstrip(".")
            if lw in UNAPPROVED_WORDS:
                findings.append((i, "word", f'"{w}" -> {UNAPPROVED_WORDS[lw]}', s))
            if lw.endswith("ing") and len(lw) > 5 and lw not in ING_ALLOWLIST:
                findings.append((i, "-ing form", f'"{w}" (allowed only in Technical Names)', s))

        m = PASSIVE_RE.search(s)
        if m:
            findings.append((i, "passive", f'"{m.group(0)}"', s))

    if not findings:
        print("No mechanical findings. Manual rule check still required.")
        return

    print(f"{len(findings)} candidate finding(s) — review each; Technical Names/Verbs are exempt.\n")
    for n, (i, cat, detail, s) in enumerate(findings, 1):
        snippet = s if len(s) <= 90 else s[:87] + "..."
        print(f"{n}. [sent {i}] [{cat}] {detail}\n   > {snippet}")


if __name__ == "__main__":
    sys.exit(main())
