# The Unofficial Guide

Name: Prerana Bajracharya
Corpus: `advice_threads`

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

This project builds a searchable unofficial guide from the `advice_threads`
corpus, which contains student questions and replies about college life. It
can answer specific questions about internships, laptops, roommates, study
locations, and communicating with professors. The system retrieves the most
relevant advice thread, checks whether the match is strong enough, and then
generates an answer using the retrieved documents. Answers include the source
filename, and unrelated questions are rejected when the relevance gate does
not find enough information.

## Chunking Strategy

**Chunk size:** One complete advice thread per chunk; there is no fixed character limit.
**Overlap:** 0 characters.

I chose this strategy because the advice_threads documents are short and each document contains one question followed by several replies. Keeping each thread together preserves the different perspectives and prevents a reply from being separated from the question it answers.

## Sample Chunks

**Chunk 1** — source: `thread_bike_commute.txt#0` — produced by: `chunker.py::split_documents`

```
THREAD: Is a bike worth it for a 20 minute walk commute?

--- reply 1 (14 votes) ---
Yeah. Cuts an 18 minute walk to about 6. The thing nobody mentions is storage — covered bike parking exists at three buildings and is full by 9am at all three.

--- reply 2 (9 votes) ---
Counterpoint, I sold mine. Between November and March the paths are either icy or salted and salt destroys a drivetrain in one season.

--- reply 3 (22 votes) ---
Both true. I keep a cheap bike for September to November and walk the rest of the year. Total cost was about $120 for the bike and I don't care what happens to it.

--- reply 4 (5 votes) ---
If you do get one, the campus does free registration and it's the only reason I got mine back after it was taken.
```

**Chunk 2** — source: `thread_first_gen.txt#0` — produced by: `chunker.py::split_documents`

```
THREAD: Anything specific for first-generation students?

--- reply 1 (33 votes) ---
The advising office has a specific programme and it is genuinely good, but it is opt-in and badly publicised. Ask for it by name.

--- reply 2 (41 votes) ---
The thing I'd say: the unwritten rules are the hard part, not the coursework. Ask about the unwritten rules explicitly. People are happy to explain them and nobody volunteers them.

--- reply 3 (16 votes) ---
Emergency fund for textbooks and travel exists and is not means-tested beyond a short form.
```

**Chunk 3** — source: `thread_laptop_specs.txt#0` — produced by: `chunker.py::split_documents`

```
THREAD: How much laptop do I actually need for CS courses?

--- reply 1 (31 votes) ---
Less than the recommended spec page says. 16GB of RAM is the one number worth paying for; everything else you'll never notice.

--- reply 2 (18 votes) ---
Adding: the lab machines exist and are better than anything you'll buy. For the heavy assignments people just use those.

--- reply 3 (12 votes) ---
I did two years on an 8GB machine and it was fine until the last project, at which point it very much wasn't. 16 is the answer.
```

**Chunk 4** — source: `thread_office_hours_etiquette.txt#0` — produced by: `chunker.py::split_documents`

```
THREAD: Is it weird to go to office hours with no specific question?

--- reply 1 (44 votes) ---
No, and this is the single most common thing first years get wrong. 'I'm following the lectures but I don't feel like I understand the shape of it' is a completely normal thing to say.

--- reply 2 (29 votes) ---
They're usually empty. You are doing the instructor a favour by turning up.

--- reply 3 (18 votes) ---
If it helps, treat it as a standing appointment. Go every week for a month and it stops feeling like a thing.
```

**Chunk 5** — source: `thread_professor_email.txt#0` — produced by: `chunker.py::split_documents`

```
THREAD: Do professors actually answer email?

--- reply 1 (21 votes) ---
Varies enormously. General rule I've found: if the syllabus states a response window, it's honoured. If it doesn't, assume 48 hours and don't panic before then.

--- reply 2 (33 votes) ---
Office hours are dramatically more effective than email for anything that takes more than two sentences to answer. They're also usually empty.

--- reply 3 (15 votes) ---
Empty office hours is the biggest unused resource here and I say that having wasted a year not going.
```

## Sample Answer

**Question:** When should students start looking for a summer internship?

**Answer:** Students should start looking for a summer internship earlier than
feels reasonable, as large employers close applications in October and November
for the following summer. Smaller and local employers hire in February and
March if students miss the autumn recruiting period. Source:
`thread_internship_timing.txt`.

```
Best distance: 0.267
Cutoff: 0.6
```

**My relevance cutoff:** 0.6

The five in-corpus questions had best distances from 0.2790 to 0.4037. The
five out-of-scope questions had best distances from 0.8280 to 0.9479. I placed
the cutoff at 0.6, in the gap between the two groups.

| Question | In corpus? | Best distance |
|---|---|---|
| When should students start looking for a summer internship, and how does timing differ between large and local employers? | Yes | 0.2790 |
| What laptop specification do students say matters most for CS courses, and what alternatives are available for demanding assignments? | Yes | 0.2918 |
| What steps do students recommend taking when a roommate situation is not working? | Yes | 0.2872 |
| What study locations do students recommend besides the library, and what are the advantages of each? | Yes | 0.4037 |
| When should students email professors, and when are office hours a better option? | Yes | 0.3006 |
| What is the capital of Mongolia? | No | 0.9479 |
| How do I change the oil in a diesel engine? | No | 0.9299 |
| Who won the 1994 World Cup? | No | 0.9517 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.8280 |
| How do I write a for loop in Rust? | No | 0.8712 |

## How I Used AI

**1.** I asked AI to review my five test questions and acceptance criteria for
Milestone 2 and identify whether each one had a measurable target. It pointed
out that the chunk-quality and multiple-perspectives criteria needed clearer
ways to judge them, so I rewrote those criteria to specify 4 of 5 and describe
what counts as a complete chunk or distinct advice point.

**2.** I asked AI to suggest a chunking strategy for the short question-and-
reply documents in `advice_threads`. It suggested keeping each complete thread
together instead of using fixed character windows, so I implemented
`chunker.py::split_documents` with one document per chunk and zero overlap. I
then re-indexed the corpus, inspected the distances, and used the measured gap
between in-scope and out-of-scope questions to document a `0.6` cutoff.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunk quality | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Multiple perspectives are represented | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

**Evidence:** The following excerpts are from
`results/run_2026-09-23_2059_before.md`. Retrieval was produced by
`store.py::search`, chunking by `chunker.py::split_documents`, the gate by
`gate.py::check`, and answers by `generate.py::answer_from_chunks`.

**Criterion 1 — Retrieved chunk contains the answer:**

```text
Sources retrieved: thread_commuting.txt, thread_first_gen.txt,
thread_internship_timing.txt, thread_professor_email.txt,
thread_roommate_conflict.txt

Students should start looking for a summer internship earlier than feels
reasonable. Large employers close their applications in October and November,
whereas smaller and local places hire later, in February and March.
```

The relevant source thread was present for each of the five questions in all
three runs, giving 5/5 each time. This criterion measures the retrieved chunk,
not the scorer's exact keyword match in the generated answer. In particular,
`thread_professor_email.txt` contains "assume 48 hours," so the retrieval
criterion is met even though the earlier scorer expected `48 hours` and the
generated answer used `48-hour`.

**Criterion 2 — Every answer names a source:**

```text
According to the documents, you should wait 48 hours for a response to an
email unless the syllabus states a response window. Office hours are
dramatically more effective than email for anything that takes more than two
sentences to answer.

Source: `thread_professor_email.txt`
```

All five generated answers named at least one source in each run, giving 5/5.

**Criterion 3 — Gate stops out-of-corpus questions:**

```text
Out-of-scope questions refused: 5 of 5
Capital of Mongolia: 0.948 — refused
Diesel engine oil: 0.930 — refused
1994 World Cup: 0.952 — refused
Ibuprofen dosage: 0.828 — refused
Rust for loop: 0.871 — refused
```

The gate refused 5/5 out-of-corpus questions, exceeding the target of 4/5.

**Criterion 4 — Chunk quality:**

```text
Chunk 3 — source: thread_laptop_specs.txt#0
THREAD: How much laptop do I actually need for CS courses?

16GB of RAM is the one number worth paying for; everything else you'll never
notice. The lab machines exist and are better than anything you'll buy.
```

The five sampled chunks in the README each preserved a complete advice thread,
including its question and replies, so this was scored 5/5 in every run.

**Criterion 5 — Multiple perspectives are represented:**

```text
Run 1, professor-email question:
According to thread_professor_email.txt, you should check the syllabus for a
response window, but otherwise, assume a 48-hour response time.
Office hours are dramatically more effective than email for anything that
takes more than two sentences to answer.
Source: thread_professor_email.txt
```

All three answers included both advice points: the 48-hour email response
window and the recommendation to use office hours for questions taking more
than two sentences. Each run therefore scored 5/5.

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MET | All five questions had a retrieved chunk containing the relevant answer in all three runs, exceeding the target of 4/5. |
| 2 | Every answer names a source | MET | Every generated answer named at least one source document in all three runs, meeting the target of 5/5. |
| 3 | The relevance gate stops out-of-corpus questions | MET | The gate refused all five out-of-corpus questions, exceeding the target of 4/5. |
| 4 | Chunk quality | MET | All five sampled chunks preserved a complete advice thread with its question and replies, meeting the target of 4/5. |
| 5 | Multiple perspectives are represented | MET | Each answer included at least two distinct advice points traceable to the retrieved advice thread, meeting the target of 4/5 in every run. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
