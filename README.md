# The Metabolic Child

**Live:** https://vikramsakaleshpurkumar-byte.github.io/Vikkypaedia-Metabolic-Child-MOOC/
**All Vikkypaedia modules:** https://vikramsakaleshpurkumar-byte.github.io/

The Metabolic Child is a mastery-based, self-paced module on inborn errors of metabolism (IEMs). It runs from recognising the sick newborn, through the first hour of a metabolic crisis, to diagnosis, long-term care and the family's next pregnancy. It is aligned to:

- the **BIMDG emergency guidelines**
- the **international urea cycle disorder guidelines (first revision, 2019)**
- current **GeneReviews** chapters
- **IAP–NNF guidance** on IEMs in the neonate
- India's **National Policy for Rare Diseases (2021, as amended)**

Every unit reads the content across the resource gradient, from a tertiary centre to a district hospital.

**Version 3.0.0** (built 2026-09-24) is a complete rebuild on the Vikkypaedia Standard engine (v2.1). The earlier edition 2.2 had 21 lessons; this version reorganises them into 20 units in 5 Parts. It also adds verified emergency doses, a critical-sample protocol, two diagrams and a certificate. Progress from the earlier edition is not carried over, because the units and questions have changed. Learners who used it see a one-time notice.

## What it is

- **One self-contained HTML file.** No CDN, no framework and no network request. It works offline on a phone.
- **Scale:** 20 units in 5 Parts, about 28 notional hours.
- **Questions:** 40 checkpoint questions with two-tier hints and rationales that explain why the wrong options are wrong, plus 30 fresh integrative items for the final assessment.
- **Parts:**
  - **A Recognise:** could this be metabolic?; the sick neonate; reading the first five results.
  - **B The first hour:** glucose, stop, sample, call; the critical sample; hyperammonaemia; organic acidaemias; hypoglycaemia.
  - **C Presentations by system:** muscle and fatty-acid oxidation; liver; seizures; movement disorders; developmental delay and regression.
  - **D From phenotype to diagnosis:** genomics and VUS; lysosomal and peroxisomal disorders; mitochondrial disease and CDG; newborn screening and the next pregnancy.
  - **E Living with a metabolic disorder:** long-term care; IEM care in India; a capstone following one baby, plus future directions.
- **A "Your role" box opens every unit**, for Student, PG resident and Faculty. It says what each should take from the unit, and the Faculty line suggests how to teach or assess it.
- **An India lens** in every clinical unit, and **ideal and resource-constrained panels** where management differs.
- **Two diagrams:** reading the first five results, and the first hour in suspected hyperammonaemia. Each has a text version.

## Who it is for

| Learner | Default depth |
|---|---|
| MBBS students, interns, nurses | Essentials: Parts A–B |
| MBBS doctors, PG residents (MD/DNB) | Advanced: Parts A–D |
| Paediatricians, neonatologists, faculty | Expert: all 20 units and appendices |

## What changed from edition 2.2

The earlier edition deliberately gave no doses or thresholds. This edition adds them for the first hour and labels each with its source:

- BIMDG ammonia action levels (repeat above 150 µmol/L in a child or 200 in a neonate; urgent treatment above 200; transfer above 250).
- The glucose regimen (10% glucose 2 mL/kg, then 5 mL/kg/h in a baby).
- Scavenger and arginine loading doses.
- Pyridoxine and biotin trials (GeneReviews).
- Home emergency-regimen concentrations.

Every figure is to be verified against the local protocol and the metabolic centre. The four patient journeys, the source library and the careful language on policy and uncertainty are kept.

## Certification

The certificate requires all three criteria:

1. **Coverage:** all 40 checkpoints currently correct.
2. **Retention:** at least 15 of the 20 units evidenced by an item answered correctly 24 hours or more after first passing it.
3. **Applied performance:** a closed-book assessment of 50 items (from a pool of 70) in 75 minutes. Learners get 2 attempts, with a 24-hour lock between them. The 80% cut score is **provisional**.

The certificate carries the default signature of Dr Vikram Sakaleshpur Kumar and states its own limits. It does not attest competence to manage IEMs independently.

## Enrolment and completion records

A four-step first run collects the learner's details and plan, stored in the browser only. `verify.html` checks a downloaded completion record offline. **Records are self-attested.** A matching checksum shows the record was not casually altered. It does not prove the learner sat the assessment.

## Faculty adoption

- Final assessment → Faculty settings → **Export a configured copy**.
- Appendix A has key-feature problems, 12 OSCE stations, WPBA tools and an entrustment scale.
- Appendix B has four branching scenarios on a doll with printed results cards.
- Appendix C has a worked flipped session on Part B and standard-setting worksheets.

## Rebuilding and testing it

```bash
python content/build_content.py   # units 1–20 from content/*.py → build/20_…60_*.html
python content/appendices.py      # Appendices A–G → build/80_appendices.html
python build.py                   # assemble index.html with structural assertions
python tests/test_full.py; python tests/test_ui.py; python tests/test_enrol.py
python tests/test_search.py; python tests/test_sig.py; python tests/test_loops.py
python tests/contrast.py; python tests/offline_test.py; python tests/print_test.py
```

## Privacy

Everything is stored in the learner's browser. There is no account, no server, no analytics and no telemetry.

## Known limitations

- The module teaches recognition, first-hour treatment and escalation. It does not qualify anyone to manage IEMs without a metabolic team.
- Emergency protocols differ between centres; the module quotes BIMDG and GeneReviews and flags differences.
- The India policy information (NPRD, Centres of Excellence, funding) is dated to 2026 and changes often.
- Fixed Leitner intervals, thin item sampling (two checkpoints per unit), rule-based placement, an unproctored assessment, self-attested records and a provisional cut score.
- The clinical content has not been externally peer reviewed. NMC codes are deliberately left blank in Appendix D.

## Contributing, licence and citation

See `CONTRIBUTING.md`. Licensed CC BY-NC-SA 4.0, **excluding** the Vikkypaedia name, the name and likeness of Dr Vikram Sakaleshpur Kumar, and the certificate signature block (see `LICENSE.md`).

> Sakaleshpur Kumar V. *The Metabolic Child: an evidence-governed, competency-based digital module for resource-constrained settings.* Vikkypaedia; 2026. Available from: https://vikramsakaleshpurkumar-byte.github.io/Vikkypaedia-Metabolic-Child-MOOC/

## Disclaimer

This module is education, not a clinical protocol, and not certification to practise. Manage suspected metabolic emergencies with a metabolic team, and verify every dose against your institution's protocol.
