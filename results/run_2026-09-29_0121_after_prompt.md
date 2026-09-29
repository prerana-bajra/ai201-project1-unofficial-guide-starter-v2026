# Run log — after_prompt

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `advice_threads` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-09-29 01:21

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| When should students start looking for a summer internship, and how does timing differ between large and local employers? | pass | pass | pass |
| What laptop specification do students say matters most for CS courses, and what alternatives are available for demanding assignments? | pass | pass | pass |
| What steps do students recommend taking when a roommate situation is not working? | pass | pass | pass |
| What study locations do students recommend besides the library, and what are the advantages of each? | pass | pass | pass |
| When should students email professors, and when are office hours a better option? | pass | pass | pass |

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
Students should start looking for a summer internship earlier than feels reasonable (*thread_internship_timing.txt*). Large employers close their applications in October and November, whereas smaller and local places hire later, in February and March (*thread_internship_timing.txt*).
```

### When should students start looking for a summer internship, and how does timing differ between large and local employers? — run 2

- Best distance: 0.2790 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_internship_timing.txt, thread_professor_email.txt, thread_roommate_conflict.txt

```
Students should start looking for a summer internship earlier than feels reasonable (*thread_internship_timing.txt*). Large employers close their applications in October and November, whereas smaller and local places hire later in February and March (*thread_internship_timing.txt*).
```

### When should students start looking for a summer internship, and how does timing differ between large and local employers? — run 3

- Best distance: 0.2790 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_internship_timing.txt, thread_professor_email.txt, thread_roommate_conflict.txt

```
Students should start looking for a summer internship earlier than feels reasonable (*thread_internship_timing.txt*). Large employers close their applications in October and November for the following summer, whereas smaller and local places hire later, in February and March (*thread_internship_timing.txt*).
```

### What laptop specification do students say matters most for CS courses, and what alternatives are available for demanding assignments? — run 1

- Best distance: 0.2918 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_laptop_specs.txt, thread_pass_fail.txt, thread_printing.txt, thread_textbook_editions.txt

```
According to *thread_laptop_specs.txt*, 16GB of RAM is the specification worth paying for, as everything else is barely noticeable. Additionally, the document notes that lab machines are available and are better than anything you can buy, allowing students to use them for heavy assignments.
```

### What laptop specification do students say matters most for CS courses, and what alternatives are available for demanding assignments? — run 2

- Best distance: 0.2918 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_laptop_specs.txt, thread_pass_fail.txt, thread_printing.txt, thread_textbook_editions.txt

```
According to `thread_laptop_specs.txt`, 16GB of RAM is the specification worth paying for because anything less can struggle with heavy projects. As an alternative for heavy assignments, students note that campus lab machines exist, which are better than personal laptops and what people use for those heavy assignments.
```

### What laptop specification do students say matters most for CS courses, and what alternatives are available for demanding assignments? — run 3

- Best distance: 0.2918 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_laptop_specs.txt, thread_pass_fail.txt, thread_printing.txt, thread_textbook_editions.txt

```
Based on the documents, students state that 16GB of RAM is the specification worth paying for in computer science courses (*thread_laptop_specs.txt*). As an alternative for heavy assignments, students can use the lab machines, which are described as being better than anything you can buy (*thread_laptop_specs.txt*).
```

### What steps do students recommend taking when a roommate situation is not working? — run 1

- Best distance: 0.2872 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_group_project.txt, thread_late_work.txt, thread_roommate_conflict.txt, thread_study_spots.txt

```
Based on *thread_roommate_conflict.txt*, students recommend taking the following steps when a roommate situation is not working:
- Talk to your RA early, framing it as needing help to sort things out rather than immediately asking to move, as room changes usually require going through a mediation process first.
- Write down specific details before the meeting (such as guests four nights a week past 2 am) rather than just stating that things are not working.
```

### What steps do students recommend taking when a roommate situation is not working? — run 2

- Best distance: 0.2872 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_group_project.txt, thread_late_work.txt, thread_roommate_conflict.txt, thread_study_spots.txt

```
Based on `thread_roommate_conflict.txt`, students recommend the following steps when a roommate situation is not working:
- Talk to your RA early, framing it as needing help to sort things out rather than immediately asking to move, since room changes usually start with mediation.
- Write down specific details before your meeting (such as guests four nights a week past 2am) instead of just saying "it's not working."
```

### What steps do students recommend taking when a roommate situation is not working? — run 3

- Best distance: 0.2872 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_group_project.txt, thread_late_work.txt, thread_roommate_conflict.txt, thread_study_spots.txt

```
Based on `thread_roommate_conflict.txt`, students recommend the following steps when a roommate situation is not working:
- Talk to your RA early, framing it as needing help to sort things out rather than immediately asking to move, as room changes usually require going through mediation first.
- Write down specific details before your meeting (such as "guests four nights a week past 2am") rather than just saying "it's not working."
```

### What study locations do students recommend besides the library, and what are the advantages of each? — run 1

- Best distance: 0.4037 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_printing.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on *thread_study_spots.txt*, students recommend the following study locations besides the library:
- **Ridgeway Café before 10am**: It is empty, quiet, has good coffee, and the staff doesn't push you out.
- **The science building**: Floors 2 through 5 have open lounges that are unlocked and almost always empty.
```

### What study locations do students recommend besides the library, and what are the advantages of each? — run 2

- Best distance: 0.4037 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_printing.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the documents provided:

* **Ridgeway Café:** Recommended because it is empty and quiet before 10am, offers good coffee, and the staff doesn't push you out (*thread_study_spots.txt*).
* **The science building:** Recommended because floors 2 through 5 have open lounges that are unlocked and almost always empty (*thread_study_spots.txt*).
```

### What study locations do students recommend besides the library, and what are the advantages of each? — run 3

- Best distance: 0.4037 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_printing.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on *thread_study_spots.txt*, students recommend the following study locations besides the library:
- **Ridgeway Café before 10am**: It is empty, quiet, has good coffee, and staff do not push you out.
- **The science building**: Floors 2 through 5 have open lounges that are unlocked and almost always empty.
```

### When should students email professors, and when are office hours a better option? — run 1

- Best distance: 0.3006 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_late_work.txt, thread_office_hours_etiquette.txt, thread_professor_email.txt, thread_sleep_schedule.txt

```
According to `thread_professor_email.txt`, you should assume a 48-hour response window for emails if one is not stated in the syllabus. Office hours are a better option for anything that takes more than two sentences to answer, and they are usually empty (`thread_professor_email.txt`).
```

### When should students email professors, and when are office hours a better option? — run 2

- Best distance: 0.3006 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_late_work.txt, thread_office_hours_etiquette.txt, thread_professor_email.txt, thread_sleep_schedule.txt

```
According to `thread_professor_email.txt`, you should assume a 48-hour response window for emails if one is not stated in the syllabus. Office hours are a better option for anything that takes more than two sentences to answer, and they are usually empty (`thread_professor_email.txt`).
```

### When should students email professors, and when are office hours a better option? — run 3

- Best distance: 0.3006 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_late_work.txt, thread_office_hours_etiquette.txt, thread_professor_email.txt, thread_sleep_schedule.txt

```
Based on the provided documents, you should check the syllabus for a professor's response window, or otherwise assume a 48-hour wait before panicking about an email (`thread_professor_email.txt`). Office hours are a better option for anything that takes more than two sentences to answer, and they are typically empty (`thread_professor_email.txt`).
```
