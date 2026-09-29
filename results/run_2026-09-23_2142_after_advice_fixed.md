# Run log — after_advice_fixed

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `advice_threads` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-09-23 21:42

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| When should students start looking for a summer internship, and how does timing differ between large and local employers? | pass | pass | pass |
| What laptop specification do students say matters most for CS courses, and what alternatives are available for demanding assignments? | pass | pass | pass |
| What steps do students recommend taking when a roommate situation is not working? | pass | pass | pass |
| What study locations do students recommend besides the library, and what are the advantages of each? | pass | pass | pass |
| When should students email professors, and when are office hours a better option? | pass | fail | pass |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.948 | refused |
| How do I change the oil in a diesel engine? | 0.930 | refused |
| Who won the 1994 World Cup? | 0.952 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.828 | refused |
| How do I write a for loop in Rust? | 0.871 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### When should students start looking for a summer internship, and how does timing differ between large and local employers? — run 1

- Best distance: 0.2790 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_internship_timing.txt, thread_professor_email.txt, thread_roommate_conflict.txt

```
Students should start looking for a summer internship earlier than feels reasonable, as large employers close applications in October and November for the following summer. In contrast, smaller and local places hire later, specifically in February and March. 

Source: thread_internship_timing.txt
```

### When should students start looking for a summer internship, and how does timing differ between large and local employers? — run 2

- Best distance: 0.2790 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_internship_timing.txt, thread_professor_email.txt, thread_roommate_conflict.txt

```
Students should start looking for a summer internship earlier than feels reasonable, as large employers close their applications in October and November for the following summer (*thread_internship_timing.txt*). In contrast, smaller and local places hire later, in February and March (*thread_internship_timing.txt*).
```

### When should students start looking for a summer internship, and how does timing differ between large and local employers? — run 3

- Best distance: 0.2790 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_internship_timing.txt, thread_professor_email.txt, thread_roommate_conflict.txt

```
Students should start looking for a summer internship earlier than feels reasonable, as large employers close their applications in October and November for the following summer (*thread_internship_timing.txt*). In contrast, smaller and local places hire later, in February and March (*thread_internship_timing.txt*).
```

### What laptop specification do students say matters most for CS courses, and what alternatives are available for demanding assignments? — run 1

- Best distance: 0.2918 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_laptop_specs.txt, thread_pass_fail.txt, thread_printing.txt, thread_textbook_editions.txt

```
According to the documents, 16GB of RAM is the laptop specification worth paying for. For heavy assignments, students can use the lab machines, which exist and are better than anything you can buy. 

Source: `thread_laptop_specs.txt`
```

### What laptop specification do students say matters most for CS courses, and what alternatives are available for demanding assignments? — run 2

- Best distance: 0.2918 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_laptop_specs.txt, thread_pass_fail.txt, thread_printing.txt, thread_textbook_editions.txt

```
According to thread_laptop_specs.txt, 16GB of RAM is the specification worth paying for. For heavy assignments, students can use the lab machines, which are better than anything you can buy.
```

### What laptop specification do students say matters most for CS courses, and what alternatives are available for demanding assignments? — run 3

- Best distance: 0.2918 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_laptop_specs.txt, thread_pass_fail.txt, thread_printing.txt, thread_textbook_editions.txt

```
According to thread_laptop_specs.txt, 16GB of RAM is the specification worth paying for. For heavy assignments, the lab machines exist and are better than anything you can buy, and people just use those.
```

### What steps do students recommend taking when a roommate situation is not working? — run 1

- Best distance: 0.2872 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_group_project.txt, thread_late_work.txt, thread_roommate_conflict.txt, thread_study_spots.txt

```
Students recommend talking to your Resident Advisor (RA) early, framing it as needing help to sort things out rather than asking to move (thread_roommate_conflict.txt). It is also recommended to write down specific details before your meeting rather than just saying it is not working (thread_roommate_conflict.txt).
```

### What steps do students recommend taking when a roommate situation is not working? — run 2

- Best distance: 0.2872 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_group_project.txt, thread_late_work.txt, thread_roommate_conflict.txt, thread_study_spots.txt

```
Based on the provided documents, students recommend the following steps when a roommate situation is not working:

* Talk to your RA early and frame the conversation as needing help to sort things out rather than immediately asking to move, as mediation is the required first step before room changes (thread_roommate_conflict.txt).
* Write down specific details before your meeting rather than just saying it is not working (thread_roommate_conflict.txt).
```

### What steps do students recommend taking when a roommate situation is not working? — run 3

- Best distance: 0.2872 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_group_project.txt, thread_late_work.txt, thread_roommate_conflict.txt, thread_study_spots.txt

```
Based on the provided documents, students recommend talking to your RA early and framing it as needing help to sort things out rather than asking to move immediately (*thread_roommate_conflict.txt*). Additionally, you should write down specific details before the meeting rather than just saying it is not working (*thread_roommate_conflict.txt*).
```

### What study locations do students recommend besides the library, and what are the advantages of each? — run 1

- Best distance: 0.4037 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_printing.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, students recommend the following study locations besides the library:

* **Ridgeway Café (before 10am):** It is empty, quiet, has good coffee, and the staff doesn't push you out (*thread_study_spots.txt*).
* **The science building (floors 2 through 5):** It features open lounges that are unlocked and almost always empty (*thread_study_spots.txt*).
```

### What study locations do students recommend besides the library, and what are the advantages of each? — run 2

- Best distance: 0.4037 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_printing.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, students recommend the following study locations besides the library:

* **Ridgeway Café (before 10am):** It is empty, quiet, has good coffee, and the staff doesn't push you out (*thread_study_spots.txt*).
* **The science building (floors 2 through 5):** It features open lounges that are unlocked and almost always empty (*thread_study_spots.txt*).
* **The student centre commuter lounge:** It offers lockers you can rent for $20 a year, which changes the commuting experience (*thread_commuting.txt*). Additionally, students treat the train as study time (*thread_commuting.txt*).
```

### What study locations do students recommend besides the library, and what are the advantages of each? — run 3

- Best distance: 0.4037 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_printing.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to `thread_study_spots.txt`, the recommended study locations besides the library are:

* **Ridgeway Café (before 10am):** It is empty, quiet, serves good coffee, and management does not push you out.
* **The science building:** Open lounges on floors 2 through 5 are unlocked and almost always empty.
```

### When should students email professors, and when are office hours a better option? — run 1

- Best distance: 0.3006 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_late_work.txt, thread_office_hours_etiquette.txt, thread_professor_email.txt, thread_sleep_schedule.txt

```
According to *thread_professor_email.txt*, if a syllabus does not state a response window, you should assume professors take 48 hours to answer email. Office hours are dramatically more effective than email for anything that takes more than two sentences to answer (thread_professor_email.txt).
```

### When should students email professors, and when are office hours a better option? — run 2

- Best distance: 0.3006 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_late_work.txt, thread_office_hours_etiquette.txt, thread_professor_email.txt, thread_sleep_schedule.txt

```
Office hours are dramatically more effective than email for anything that takes more than two sentences to answer. (Source: `thread_professor_email.txt`)
```

### When should students email professors, and when are office hours a better option? — run 3

- Best distance: 0.3006 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_late_work.txt, thread_office_hours_etiquette.txt, thread_professor_email.txt, thread_sleep_schedule.txt

```
According to the documents, you should assume a 48-hour response window for emails if none is stated in the syllabus (or follow the response window specified in the syllabus). Office hours are dramatically more effective for anything that takes more than two sentences to answer. 

Source: `thread_professor_email.txt`
```
