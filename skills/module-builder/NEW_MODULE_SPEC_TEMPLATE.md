# New Module Specification Template

Complete this before implementation. Replace bracketed text; delete guidance that does not apply. Keep the specification short enough to review in one sitting.

## 1. Identity and outcome

| Variable | Decision |
|---|---|
| Working title | [Title] |
| Public title | [Title learners will see] |
| Topic | [Topic boundary] |
| Problem solved | [Learner or service problem] |
| Main learner outcome | By the end, learners can [observable performance]. |
| Exclusions | [What the course does not teach or authorize] |
| Version / evidence checked date | [Version] / [YYYY-MM-DD] |

## 2. Learners and personalization

| Variable | Decision |
|---|---|
| Roles | [Default: UG, PG, Faculty] |
| Default role | [Role] |
| Depth levels, shallow to deep | [Default: Must Know, Nice to Know, Good to Know] |
| Default depth | [Depth] |
| Role-specific expectations | [What changes by role] |
| Accessibility/language needs | [Needs] |

Depth rule: a learner sees a section when its role-specific depth rank is less than or equal to the selected depth rank.

## 3. Course graph

| Unit ID | Unit title | Minutes | 3–5 observable outcomes | Prerequisite | Required for completion? |
|---|---|---:|---|---|---|
| 1 | [Title] | [N] | [Outcomes] | None | Yes |
| 2 | [Title] | [N] | [Outcomes] | Unit 1 | Yes |

Part/group labels: [Optional groupings]

Completion definition: [Default: all unit evaluation questions currently correct plus every visible Must-level explain-back check marked complete].

Unlock definition: [Default: unit N unlocks when all evaluation questions in N−1 are currently correct].

End destination: [Final practice / toolkit / completion page / external action].

## 4. Unit content contract

For every unit provide:

- stable ID, title, subtitle, duration, and three to five outcomes;
- at least four teaching sections;
- for each section: stable ID, title, paragraphs, key points, role-to-depth mapping, and source IDs;
- one memorable takeaway;
- [5–10] evaluation questions;
- at least one explain-back or reflection prompt if required.

Configured questions per unit: [N]

Configured options per question: [Default: 4]

Critical-decision policy: [Which questions/decisions receive `critical: true`]

## 5. Assessment behavior

| Variable | Decision |
|---|---|
| Confidence choices | [Default: Low, Medium, High] |
| Submit requirement | [Default: option + confidence] |
| Feedback | [Default: feedback for every option] |
| Retry policy | [Default: unlimited; first attempt preserved] |
| Unit unlock threshold | [Default: all current answers correct] |
| Baseline | [Enabled/disabled; purpose; count] |
| Final practice | [Enabled/disabled; count by role; pass behavior] |
| Certification | [None unless explicitly implemented] |

## 6. Cases and applied learning

Enabled: [Yes/No]

For each case: fictional identity, setting, opening information, stable ID, source IDs, three or more sequential decisions, option-specific feedback/consequence, reveal, debrief, and eligible roles.

Safety and privacy constraints: [No real patient identifiers by default].

## 7. Evidence and local context

Evidence standard: [Primary/official/current sources preferred; subject-expert review requirement].

Required geography or service context: [Country/region/system].

Local-context dimensions to integrate:

- care setting and workforce;
- available investigations/resources;
- referral and transport;
- language and family communication;
- affordability/access;
- policy/curriculum alignment;
- culturally relevant examples.

Source register fields: `id`, `title`, `organization`, `url`, `date_version`, `verified_scope`, `access`, `use_in_module`, `caveat`.

Known evidence conflicts or pending verification: [List].

Required disclaimers/approval boundary: [List].

## 8. Optional routes

| Feature | Enabled? | Purpose / acceptance condition |
|---|---|---|
| Baseline | [ ] | [ ] |
| Cases | [ ] | [ ] |
| Final practice | [ ] | [ ] |
| Faculty workshop | [ ] | [ ] |
| Toolkit | [ ] | [ ] |
| Progress dashboard | [ ] | [ ] |
| Learner-record export | [ ] | [ ] |
| Selected study-guide export | [ ] | [ ] |
| Print layout | [ ] | [ ] |
| Single-file offline edition | [ ] | [ ] |
| WebMCP tools | [ ] | [ ] |

## 9. Interface and brand

| Variable | Decision |
|---|---|
| Brand/product name | [Name] |
| Visual tone | [Tone] |
| Primary/accent colors | [Tokens] |
| Logo/favicon/hero assets | [Files or none] |
| Navigation labels | [Labels] |
| Home-page promise | [One sentence] |
| Progress labels | [Solved/completed wording] |
| Locked-state wording | [Text] |
| Completion wording | [Text] |

## 10. State, privacy, and lifecycle

| Variable | Decision |
|---|---|
| Storage key | `[module-slug]-v[STATE_SCHEMA_VERSION]` |
| State schema version | [Integer] |
| Stored fields | [Answers, confidence, read checks, notes, case steps, faculty work] |
| Migration policy | [Reset or migrate earlier versions] |
| Reset behavior | [Confirm, then clear local state] |
| Data location | [Default: current browser only] |
| Sensitive-data rule | [Do not enter personal/sensitive data] |
| Analytics | [None / explicitly specified] |

## 11. Delivery and release

| Variable | Decision |
|---|---|
| Repository | [URL/path] |
| Static output directory | `dist` |
| Host | [GitHub Pages / Sites / other] |
| Public URL | [URL] |
| Offline filename | `[module-slug]-offline.html` |
| Export filename | `[module-slug]-learning-record.txt` |
| Asset version | [Must match release version] |
| Browser support | [Targets] |

## 12. Acceptance criteria

- [ ] All content and source validations pass.
- [ ] A new learner can start without an account.
- [ ] Personalization changes visible depth correctly.
- [ ] Each unit has the configured number of questions.
- [ ] Sequential locks work in navigation and direct URLs.
- [ ] First attempts survive retries and refresh.
- [ ] Online and offline editions match.
- [ ] Keyboard, focus, mobile, reduced-motion, and print checks pass.
- [ ] A fresh browser loads the intended public release.
- [ ] [Topic-specific expert/safety criterion].
