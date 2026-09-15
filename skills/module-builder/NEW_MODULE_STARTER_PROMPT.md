# New Module Starter Prompt

Copy this prompt, replace the bracketed values, and attach the source materials.

```text
Read skills/module-builder/SKILL.md, my completed skills/module-builder/NEW_MODULE_SPEC_TEMPLATE.md, and skills/module-builder/REFERENCE_ARCHITECTURE.md. Use them to create a complete, evidence-linked learning module on [TOPIC] for [AUDIENCES], following the proven architecture of the reference module. Inspect the reference implementation only where needed to confirm a component or behavior; do not modify it.

First produce a brief dependency-ordered implementation plan and identify any material assumptions. Reuse the existing architecture and components wherever appropriate, keep topic-specific logic isolated in data/configuration, and avoid speculative refactors.

The main outcome is: “By the end, learners can [OBSERVABLE OUTCOME].” Use [DEPTH LEVELS; default Must Know, Nice to Know, Good to Know], with [DEFAULT ROLE] and [DEFAULT DEPTH] selected initially.

Build [NUMBER] ordered units from [CURRICULUM/SOURCE MATERIALS]. Each unit must have 3–5 observable outcomes, at least 4 teaching sections, role-specific depth assignments, a takeaway, source links, and [5–10] substantive questions with four options, option-specific feedback, confidence selection, retry, and immutable first-attempt tracking. Unit N unlocks only when [UNLOCK RULE; default all evaluation questions in unit N−1 are currently correct]. Completion means [COMPLETION RULE].

Integrate [COUNTRY/REGION/SERVICE CONTEXT] throughout cases, resources, logistics, examples, access, policy, and communication. Create a source register with stable IDs, provenance, date/version, inspected scope, access, use, and caveats. Do not turn uncertain or inaccessible source material into confident claims. For consequential content, state the educational boundary and what requires local expert approval.

Enable these optional features: [BASELINE / CASES / FINAL PRACTICE / FACULTY WORKSHOP / TOOLKIT / EXPORTS / PRINT / OFFLINE / WEBMCP]. Use the proven static architecture: one HTML shell, one CSS design system, generated topic data, one reusable browser engine, local progress storage, hash routes, sequential lock enforcement in navigation and direct routes, responsive/accessibility behavior, and a generated single-file offline edition. Keep engine, configuration, topic data, and optional features separate.

Implement in gated dependency order: evidence map → schema and validator → one complete fixture journey → mastery/persistence → full content → optional routes → design/accessibility → online/offline packaging → end-to-end verification. Run the relevant tests after each meaningful stage and fix failures before proceeding. Derive all counts from data, keep IDs stable and unique, validate every source link, escape dynamic content, and synchronize release/cache/offline versions.

Before declaring completion, execute every gate in MODULE_CREATION_CHECKLIST.md. Deliver the completed module in [WORKSPACE/REPOSITORY], publish to [HOST/PUBLIC URL] if authorized, and report the files, validations, tested learner journey, URL, and material limitations. Do not modify [REFERENCE PROJECT, IF ANY].
```

Minimum input block:

```text
TOPIC:
AUDIENCES:
MAIN OUTCOME:
COUNTRY/REGION/SERVICE CONTEXT:
SOURCE MATERIALS:
NUMBER OF UNITS:
QUESTIONS PER UNIT:
OPTIONAL FEATURES:
BRAND/TONE:
REPOSITORY/HOST:
REFERENCE PROJECT TO PRESERVE:
```
