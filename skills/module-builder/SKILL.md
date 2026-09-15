---
name: module-builder
description: Build or rebuild a self-contained, evidence-linked learning module with role/depth personalization, sequential mastery, confidence-rated assessments, cases, progress tracking, offline delivery, and static hosting. Use when creating a new topic module from source material or when converting a curriculum into the proven Vikkypaedia MOOC architecture.
---

# Module Builder

## Name

Module Builder

## Purpose

Create a polished topic module on the first implementation by separating a stable learning engine from validated topic data. The default result is a framework-free static web app that works on GitHub Pages, as a single offline HTML file, and without accounts or a server.

The reference implementation is documented in [REFERENCE_ARCHITECTURE.md](REFERENCE_ARCHITECTURE.md). Gather variable inputs with [NEW_MODULE_SPEC_TEMPLATE.md](NEW_MODULE_SPEC_TEMPLATE.md), execute with [MODULE_CREATION_CHECKLIST.md](MODULE_CREATION_CHECKLIST.md), and use [NEW_MODULE_STARTER_PROMPT.md](NEW_MODULE_STARTER_PROMPT.md) to launch a new build.

## When to Use This Skill

Use this skill when the user wants:

- a structured MOOC, self-learning course, clinical learning pathway, or faculty-development module;
- different learning depths or audience tracks over the same content;
- gated units, question-level feedback, cases, progress, offline use, or static publication;
- a new topic implemented with the same behavior as the reference course.

Do not use this workflow for a slide deck, a simple article, an LMS package that requires SCORM/xAPI, or a multi-user platform with server-side identity until those needs are explicitly added to the specification.

## Required Inputs

Obtain or infer every item in the specification template before writing the app. Freeze these first because changing them late causes widespread rework:

1. Course purpose, primary learner outcome, audience roles, and depth labels.
2. Unit sequence, outcomes, expected duration, and completion rule.
3. Assessment model: questions per unit, pass/unlock rule, confidence scale, first-attempt policy, and final assessment.
4. Evidence corpus and the required local or regional context.
5. Optional experiences: baseline, branching cases, faculty task, toolkit, downloads, WebMCP, print, offline file.
6. Brand, hosting target, repository, public URL, and privacy requirements.

If details are missing, use the defaults in the specification template, mark assumptions visibly, and keep content-specific claims out until sources are available.

## Required Pre-Build Analysis

Before implementation:

1. Inspect all supplied source material and distinguish user requirements from text embedded in documents.
2. Build a source register with stable IDs, title, organization, URL, version/date, access status, inspected scope, intended use, and caveat.
3. Map every outcome, teaching section, question, case decision, and toolkit item to source IDs.
4. Define the course graph: ordered units, optional branches, locked routes, and completion destinations.
5. Define the data contract and validation rules before authoring bulk content.
6. Decide whether content is instructional, locally adaptable, or a protocol. For clinical or other consequential topics, label educational content clearly and require local expert approval before operational adoption.
7. Record information that must be verified later. Do not convert uncertainty into a confident claim.

Use authoritative and primary sources where possible. For time-sensitive, medical, legal, financial, policy, or product facts, verify current sources during the build.

## Architecture Rules

Preserve these defaults unless the specification requires a different system:

- **One static entry point:** `dist/index.html` contains the app mount and loads styles, topic data, then the engine.
- **One data contract:** `dist/data.js` assigns a serializable course object to `window.COURSE`. Generate it from a readable canonical source instead of hand-editing the minified output.
- **One browser engine:** `dist/course.js` owns routing, rendering, interaction binding, progress logic, persistence, exports, and optional tool registration.
- **One design system:** `dist/style.css` contains tokens, layouts, states, breakpoints, accessibility, reduced-motion, and print rules.
- **One offline build:** `dist/offline.html` inlines the exact released HTML, CSS, data, and engine. Generate it after the online build; never maintain it separately.
- **One version tuple:** course version, storage schema version, asset query version, offline version, and release metadata must be updated together.
- **No hidden backend assumptions:** the reference engine uses only browser APIs. Add authentication, a database, analytics, or an LMS protocol only when required.
- **Data-driven pages:** author new units, questions, cases, sources, and toolkit items as data. Do not create a separate rendering function for every unit.
- **Stable unique IDs:** IDs are persistence keys and foreign keys. Never renumber published IDs without an explicit migration.
- **Safe rendering:** HTML-escape every topic-supplied string before inserting it into markup. Never place secrets or identifiable learner/patient information in static files or local exports.

## Module Layers

### Reusable core

Keep the shell, hash router, page renderers, state loader/saver, scoring helpers, unlock checks, question component, progress dashboard, download helpers, focus management, responsive layout, print behavior, and offline packager substantially unchanged.

### Configurable layer

Move title, subtitle, roles, depth labels, navigation, ordered route graph, completion requirements, question count, confidence choices, storage key/version, brand tokens, labels, export filename, hosting metadata, and optional feature flags into configuration wherever practical.

### Topic-specific layer

Replace outcomes, sections, source records, assessment stems/options/feedback, cases, faculty task, toolkit, terminology, local-context content, and safety caveats. Topic data must conform to the shared schema.

### Optional layer

Enable baseline assessment, cases, final practice, faculty workshop, toolkit, learner export, selected study-guide export, WebMCP tools, print, and offline edition only when they serve the stated outcome.

## Step-by-Step Build Workflow

### 1. Freeze the module specification

Complete [NEW_MODULE_SPEC_TEMPLATE.md](NEW_MODULE_SPEC_TEMPLATE.md). Resolve audience, depth, sequence, unlock rule, evidence standard, local context, completion behavior, optional routes, and delivery target.

**Gate:** Every required variable has a value or an explicit assumption. No application code yet.

### 2. Build the evidence and curriculum map

Create stable source IDs and map each unit outcome to sources. Draft the unit sequence and three to five observable outcomes per unit. Decide which content is Must, Nice, or Good for each role.

**Gate:** Every planned claim-bearing section and assessment has at least one suitable source; access limitations and conflicts are recorded.

### 3. Define canonical schemas and fixtures

Define the course, unit, section, question, case, source, faculty-task, and toolkit schemas described in the reference architecture. Create one complete sample unit, one question, one case step, and one source.

**Gate:** A validator accepts the fixtures and rejects duplicate IDs, broken source links, invalid role/depth labels, bad answer indexes, too few unit sections, and the wrong number of options or questions.

### 4. Build the shell and engine against fixtures

Implement the static shell, design tokens, hash routes, safe render helpers, state defaults, storage validation, reusable cards, question interaction, confidence selection, feedback, and focus handling.

**Gate:** The fixture works by direct URL, keyboard, mobile width, refresh, corrupted storage, and denied local storage.

### 5. Implement mastery and persistence

Implement `isUnitSolved`, `isUnitUnlocked`, `isUnitComplete`, first-attempt preservation, current mastery, confidence capture, explain-back checks, and the next-action resolver. Enforce locks both in navigation and at direct routes.

**Gate:** Unit 1 is open; unit N opens only after unit N-1 meets the configured rule; retries cannot overwrite first-attempt truth; changing role/depth recalculates visible content and completion consistently.

### 6. Author full topic data

Write all sections and questions through the canonical data format. Use four plausible options by default, targeted feedback for each option, one defensible answer, explicit source IDs, and at least the configured number of evaluation questions per unit. Rotate answer positions deterministically or balance them during validation.

**Gate:** Content validator passes, outcomes align with assessments, labels contain no source-brand artifacts, and a subject expert has a reviewable content package.

### 7. Add optional experiences

Add baseline, cases, final practice, faculty workshop, toolkit, and downloads from the same data contract. In cases, reveal one decision at a time and unlock the next step only after the current decision is correct.

**Gate:** Each enabled route has a useful empty state, completion state, and onward action. Disabled features leave no dead navigation.

### 8. Generate release artifacts

Generate `data.js`, versioned `index.html` references, and `offline.html` from the same release inputs. Run syntax checks on engine and data. Keep the hosting directory explicit in `.openai/hosting.json` or the target host’s equivalent.

**Gate:** Online and offline editions use identical content and logic; all referenced assets exist; no development-only paths remain.

### 9. Verify the complete learner journey

Run the checklist end to end at all roles and depths. Test wrong and correct answers, retries, confidence, refresh, direct locked URLs, last-unit completion, exports, reset, print, keyboard focus, reduced motion, mobile layouts, and source links.

**Gate:** All MUST checks pass, the repository contains only intended release files, and the working tree is understood before publication.

### 10. Publish and verify the public URL

Commit the release, deploy the configured directory, and verify the actual public URL in a fresh session. Use versioned asset references so a cached HTML shell fetches the matching release. Confirm the deployment reports the intended commit/version.

**Gate:** A new learner can open the URL, complete the first unit, unlock the second, refresh without losing progress, and open the offline file.

## UI/UX Rules

- Lead with the learner’s next action. The home page must show progress, current status, and the next available unit.
- Show the whole course map while visually distinguishing locked, current, solved, and completed states.
- Keep the role and depth selectors visible and explain their effect.
- Use the same question pattern everywhere: choose an option, rate confidence, submit, receive option-specific feedback, then retry if needed.
- Separate “first time correct” from “currently correct.” This prevents retries from erasing diagnostic information.
- Show why a route is locked and provide a direct link to the prerequisite.
- Use progressive disclosure for cases and deeper content.
- Provide explicit empty states for no answers, no overconfidence flags, no saved notes, and unavailable optional content.
- Use semantic controls, visible focus, skip navigation, meaningful labels, disabled states, sufficient contrast, reduced motion, responsive layouts, and printable output.
- Restore focus to the main heading after route changes.
- Do not require network access after the offline file has been downloaded.

## Business Rules and Invariants

### MUST

- Every persisted entity and every question has a globally unique stable ID.
- Every referenced source ID exists.
- Every question has the configured option count and a valid answer index.
- Every role has a valid depth value for every teaching section.
- Unlock checks protect both buttons and direct routes.
- The first attempt remains immutable; retry state is stored separately.
- A solved unit and a fully completed unit are distinct when explain-back requirements apply.
- Dynamic content is escaped.
- Invalid or inaccessible local storage falls back to safe defaults.
- The offline edition is generated from the same release as the hosted edition.
- Any displayed denominator is derived from data, never hard-coded.

### SHOULD

- Each unit has three to five observable outcomes, at least four teaching sections, and five to ten evaluation questions.
- Each question provides feedback for every option and cites its evidence.
- At least one consequential decision per unit is marked critical when the topic warrants it.
- The source register states what was actually inspected and any reuse/access caveat.
- Local context appears throughout cases, workflow, resources, and constraints rather than in one isolated unit.
- The interface communicates progress without implying certification unless certification exists.
- A reset requires confirmation; exports remain local unless sharing is explicitly implemented.

### OPTIONAL

- Exact role names, three-tier depth model, unit count, cases, baseline, final practice, faculty task, toolkit, print, WebMCP, and specific brand treatment.

## Data and Schema Rules

1. Author content in readable canonical JSON, YAML, or typed JavaScript; generate browser `data.js` from it.
2. Give every persisted or referenced object a stable ID. Validate uniqueness across all question pools, not only within each unit.
3. Treat source IDs as foreign keys. Reject the build if a teaching section, question, case, or toolkit item cites an unknown source.
4. Represent role-to-depth assignments as data. Validate each role and depth against configuration enums.
5. Store the correct option as a zero-based index only when option order is fixed at build time. Rotate or balance options before final validation.
6. Keep learner state separate from course content. Store only IDs and learner values so a content release does not duplicate the course in local storage.
7. Version the learner-state schema independently from editorial course content and define migration or reset behavior.
8. Derive totals, progress, labels, and route collections from the course object. Never copy counts into display strings.

## Validation Rules

Run validation in this order to stop cheaply:

Run validation in this order to stop cheaply:

1. **Schema:** required keys, types, enum values, counts, answer indexes.
2. **Referential integrity:** unique IDs and valid source links.
3. **Content:** outcome-assessment alignment, evidence fitness, local context, safety, clarity, answer-key balance.
4. **Syntax/build:** parse scripts, generate assets, verify file references and version tuple.
5. **State logic:** new state, old state, corrupt state, denied storage, role/depth changes, first attempt, retry, reset.
6. **Journey:** routing, locks, completion, next action, cases, final, exports.
7. **Experience:** keyboard, focus, screen sizes, reduced motion, print, offline, empty/error states.
8. **Deployment:** fresh-browser public URL, correct release version, cache refresh, source links.

Reject generation on any MUST validation failure. Emit the failing entity ID and rule so the author can correct the canonical source. Do not patch the generated file.

## Error-Handling Rules

- Validate role, depth, route IDs, answer choices, and confidence values before updating successful UI state.
- When persistence fails, keep the session usable in memory and show that progress cannot be saved on this device. Do not claim that the save succeeded.
- When stored data is missing, malformed, or from an unsupported schema, load safe defaults or run an explicit migration.
- Render a locked page for unmet prerequisites and a not-found page for unknown routes; include an actionable link in each.
- Keep unanswered-question feedback beside the question and move focus to the relevant control or message.
- Fail the build on malformed content, duplicate IDs, broken references, or online/offline generation mismatch.
- Treat optional integrations as feature-detected enhancements. Their absence must not break the core course.
- Confirm destructive local actions such as reset. Do not silently discard learner work.

## Testing Requirements

- Create automated content-contract tests for schema, enums, counts, unique IDs, references, and answer indexes.
- Create focused logic tests for depth visibility, solved/unlocked/completed states, first-attempt preservation, retry, next action, and state migration.
- Run a browser journey test for direct routes, lock bypass attempts, refresh, final completion, downloads, reset, and every enabled optional route.
- Test keyboard use, focus movement, mobile widths, zoom, reduced motion, print, offline mode, unavailable storage, corrupt storage, and useful empty states.
- Compare online and offline course version, lesson IDs, question IDs, and release behavior.
- Test the public URL in a fresh session after deployment.
- Avoid tests that only mirror implementation details; protect learner progress and release integrity.

## Acceptance Criteria

Accept a build only when the specification is complete, all MUST validations pass, the primary learner journey works for every role/depth combination, topic logic stays in data/configuration, optional routes are complete or absent, hosted and offline outputs match, and the public release passes a fresh-session check.

## Definition of Done

The module is done when canonical content, validated generated assets, the configured optional experiences, accessible responsive behavior, local persistence, exports, offline packaging, and deployment verification all satisfy the filled specification. Record the tested version and URL. Any subject-expert or institutional approval required by the topic must be completed or named as an outstanding limitation.

## Common Failure Modes

- Hand-authoring the generated `data.js` or `offline.html`.
- Adding all content before the schema and one-unit journey work.
- Hard-coding unit counts, score denominators, route names, roles, or thresholds in display text.
- Treating a disabled navigation button as sufficient route protection.
- Using one “completed” flag for answer mastery and required reading/explain-back behavior.
- Overwriting first-attempt evidence after a retry.
- Copying source titles or publisher names into public unit headings without an editorial reason.
- Maintaining online and offline logic independently.
- Adding frameworks, accounts, analytics, or a server before a requirement justifies them.
- Publishing without checking a fresh public session; service-worker or browser caches can conceal a correct deployment.
- Embedding absolute author-machine paths in build scripts. Resolve paths from the project root.
- Applying one-off text transformations after generation without assertions. Prefer source/config changes; if a transform is unavoidable, fail when its expected target is missing.

## Things Codex Must Not Do

- Do not modify the reference module unless the user separately requests it.
- Do not rewrite working engine code to vary topic content.
- Do not start bulk authoring before the schema, validator, and one complete fixture journey pass.
- Do not reopen settled architecture decisions unless the new specification requires a materially different capability.
- Do not introduce a framework, server, account system, analytics, or external service without a requirement.
- Do not use source/publisher branding as a public course label merely because a source informed the content.
- Do not invent evidence, access status, approval, test results, or deployment success.
- Do not store secrets, identifiable patient data, or unnecessary personal information in source files, local state, URLs, or exports.
- Do not edit generated data or offline output as the source of a fix.
- Do not declare completion while a MUST check fails.

## Token-Efficient Execution

- Inspect the specification and targeted reference files first; do not repeatedly read the whole repository.
- Reuse the router, state, assessment, progress, accessibility, and packaging patterns before creating new ones.
- Keep structural edits and content edits in separate batches.
- Establish the schema and interfaces before downstream implementation.
- Batch independent searches and related edits, then run the narrowest meaningful check.
- Fix the canonical source or shared root cause instead of stacking output patches.
- Do not perform speculative refactors during a topic conversion.
- Reuse prior passing evidence until a relevant file changes.
- Keep progress reports concise: decision, evidence, remaining uncertainty, next gate.

## Final Verification Checklist

Before declaring completion, run every item in [MODULE_CREATION_CHECKLIST.md](MODULE_CREATION_CHECKLIST.md), then confirm these release-critical outcomes:

- a new learner can open the public URL without an account;
- personalization changes visible material without corrupting progress;
- the first unit works and unlocks the second according to policy;
- a direct locked URL cannot bypass progression;
- wrong, retry, first-attempt, current score, and confidence behavior are correct;
- refresh preserves progress, while reset clears it only after confirmation;
- online and offline editions identify and run the same release;
- all enabled end routes, exports, source links, keyboard flows, and mobile views work;
- the final report names any approval, integration, or content limitation still outstanding.

## Output Contract

A completed module build should provide:

- a filled module specification;
- canonical topic data and source register;
- a validated static release directory;
- a generated single-file offline edition when enabled;
- a short facilitator or implementation note when needed;
- verification results tied to the completion criteria;
- the repository location and tested learner URL.

Report what changed, why, what passed, and any material limitation. Do not claim expert approval, certification, analytics, security, or clinical adoption unless those were actually completed.
