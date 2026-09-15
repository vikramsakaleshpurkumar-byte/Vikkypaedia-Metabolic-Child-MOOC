# Module Creation Checklist

Use this as a gated build sheet. Stop at a failed MUST item and fix it before moving on.

## Required status snapshot

- [ ] Specification complete
- [ ] Topic variables identified
- [ ] Core architecture reused
- [ ] Data schema defined
- [ ] Primary flow working
- [ ] Validation implemented
- [ ] Error states implemented
- [ ] UI states complete
- [ ] Edge cases tested
- [ ] No unnecessary duplicated code
- [ ] Topic-specific logic isolated
- [ ] Existing shared functionality reused
- [ ] Automated tests passing
- [ ] Build passes
- [ ] Final operational-flow test passes

## A. Specification gate

- [ ] Course problem, main outcome, exclusions, roles, and depth levels are frozen.
- [ ] Ordered unit graph and completion destination are approved.
- [ ] Unlock, solved, completed, retry, confidence, and first-attempt rules are explicit.
- [ ] Optional routes and hosting target are selected.
- [ ] Local-context and privacy requirements are explicit.
- [ ] Every missing input is marked as an assumption or open verification item.

## B. Evidence and curriculum gate

- [ ] Each source has a unique stable ID and full provenance fields.
- [ ] `verified_scope` says what was actually inspected.
- [ ] Access/reuse caveats are recorded.
- [ ] Every unit has three to five observable outcomes.
- [ ] Every section, question, case decision, and toolkit card has source IDs where claims require evidence.
- [ ] Local context is integrated across content and cases.
- [ ] Consequential guidance has a clear educational/approval boundary.

## C. Schema gate

- [ ] One canonical, readable topic-data source exists.
- [ ] Course, unit, section, question, case, source, faculty-task, and toolkit shapes are defined.
- [ ] All entity IDs and question IDs are globally unique.
- [ ] Every source reference resolves.
- [ ] All role/depth values use configured enums.
- [ ] Every question has the configured option count and a valid answer index.
- [ ] Unit section and question minimums pass.
- [ ] One complete fixture passes before bulk authoring begins.

## D. Engine gate

- [ ] Static shell loads CSS, data, and engine in that order.
- [ ] Hash routes work from a direct URL and browser back/forward.
- [ ] Topic strings are HTML-escaped.
- [ ] New, old, corrupt, and unavailable local storage fail safely.
- [ ] State schema version and migration/reset behavior are implemented.
- [ ] Role/depth filter follows rank order consistently.
- [ ] Progress denominators are derived from data.
- [ ] Reset requires confirmation.

## E. Mastery gate

- [ ] Unit 1 is open initially.
- [ ] Unit N unlocks only from the configured status of unit N−1.
- [ ] Locked cards and locked direct routes agree.
- [ ] Submit requires an option and confidence when configured.
- [ ] Every option produces targeted feedback.
- [ ] Retry can change current mastery without changing first-attempt truth.
- [ ] Solved and completed are separate when explain-back checks are required.
- [ ] The next-action resolver always points to an actionable destination.
- [ ] The final unit leads to the specified completion experience.

## F. Content gate

- [ ] Unit titles are editorial titles, free of accidental publisher/source branding.
- [ ] Each unit has at least four coherent sections.
- [ ] Each unit has five to ten substantive questions, or the configured count.
- [ ] Questions sample recognition, interpretation, and action where relevant.
- [ ] Correct-answer positions are balanced and do not form a visible pattern.
- [ ] Distractors are plausible, unambiguous, and educational.
- [ ] Outcomes, teaching, and evaluation align.
- [ ] Terminology, units, labels, and caveats are consistent.
- [ ] A subject expert can review content without reading application code.

## G. Optional experience gate

- [ ] Enabled baseline has a stated purpose and does not block starting unless specified.
- [ ] Cases reveal one step at a time and handle wrong answers safely.
- [ ] Final practice filters questions correctly by role.
- [ ] Faculty work remains local and clearly identifies approval responsibility.
- [ ] Toolkit content links back to sources.
- [ ] Exports use configured names and derived counts.
- [ ] Disabled features leave no dead routes or navigation.
- [ ] Empty and completion states provide a next action.

## H. Accessibility and responsive gate

- [ ] Skip link works.
- [ ] Route changes move focus to the main heading.
- [ ] All controls are reachable and operable by keyboard.
- [ ] Visible focus, labels, selected, correct, incorrect, disabled, and locked states are distinguishable.
- [ ] Color is not the only status cue.
- [ ] Motion respects `prefers-reduced-motion`.
- [ ] Phone, tablet, desktop, and zoomed layouts remain usable.
- [ ] Tables scroll or reflow without hiding content.
- [ ] Print output is readable and omits irrelevant navigation.

## I. Build and offline gate

- [ ] Generated files are rebuilt from canonical inputs.
- [ ] Engine and generated data pass syntax checks.
- [ ] Release version, asset query version, state version, and offline version are intentional.
- [ ] The offline file inlines the exact released CSS, data, and engine.
- [ ] Online/offline route, score, lock, and export behavior match.
- [ ] No machine-specific path or secret appears in release files.
- [ ] The static output contains every referenced file and no obsolete runtime file.

## J. Journey test

- [ ] Start as each role at each depth.
- [ ] Change role/depth before and after progress exists.
- [ ] Submit without a choice; submit without confidence.
- [ ] Answer incorrectly, inspect feedback, retry correctly.
- [ ] Confirm first-attempt and current scores differ correctly.
- [ ] Refresh and reopen; progress remains intact.
- [ ] Attempt a locked unit from its card and direct URL.
- [ ] Complete all units and optional cases/final.
- [ ] Test notes, faculty fields, downloads, print, and reset.
- [ ] Test corrupt storage and blocked storage.

## K. Release gate

- [ ] Repository status is understood and only intended files will be committed.
- [ ] Release commit/version is recorded.
- [ ] Correct static directory is deployed.
- [ ] Public URL is tested in a fresh browser session.
- [ ] Asset caching returns the intended release.
- [ ] Offline file opens with the network unavailable.
- [ ] Source links and downloads work.
- [ ] Final report states changes, validation, URL, and limitations without unsupported claims.
