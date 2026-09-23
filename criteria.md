# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
I chose 4 of 5 because each question focuses on a different advice thread,
and one topic may be harder for retrieval even though the answer is present.
The target still requires the system to find useful information for most questions.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
Every answer needs a source so I can verify which thread supports the advice.
This should be achievable because each retrieved chunk includes the source
document metadata.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
I chose 4 of 5 because the out-of-scope questions are unrelated to student
advice and should produce weaker matches. One could still share common words
with a thread and pass the gate.

---

## 4. Chunk Quality

At least 4 of 5 sampled chunks contain a complete advice thread, with no sentence cut off at the beginning or end, and include enough context to understand the question and replies without reading another chunk.


**Why this target:**
Each advice document has a question followed by multiple student replies, so a
useful chunk should preserve that context. I chose 4 of 5 because one sampled
chunk could still be split awkwardly while most should represent a full thread.

---

## 5. Multiple perspectives are represented

For at least 4 of my 5 test questions, the generated answer includes at least two distinct advice points that can each be traced to different replies in the retrieved source thread.

**Why this target:**
The advice threads contain several replies that add different details, such as
different internship timelines or study locations. I chose 4 of 5 because the
system should synthesize multiple perspectives, while one thread may have less
variation or a weaker retrieval result.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
