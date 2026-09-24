"""Appendices A–G for The Metabolic Child. Reuses the Standard's generic
faculty material (C3–C6, PEARLS, G) and adds topic-specific content."""
import os, re
from gen import table, box
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "build", "80_appendices.html")
STD = os.path.join(HERE, "_standard_appendix_source.html")   # NRP-2025 v1.5 appendices — source of the shared faculty and design blocks
std = open(STD, encoding="utf-8").read().split("\n")
pearls = "\n".join(std[242:266]).replace("where the blender was", "where the 10% glucose and the ammonia tubes were").replace("I noticed compressions started while the chest wasn't moving. I was concerned because that circulates deoxygenated blood.", "I noticed the saline was continued after the ammonia came back high. I was concerned because saline does not stop catabolism.")
appC_generic = "\n".join(std[271 - 1 + 32:271 - 1 + 111 - 4])   # C3 … C6, without closing divs
appG = "\n".join(std[597:666])

def app(letter, title, body):
    return '''
<!-- ===================================================== APPENDIX %s -->
<div class="appendix" id="app%s">
  <h3><span class="caret">▸</span>%s · %s</h3>
  <div class="app-body">
%s
  </div>
</div>
''' % (letter, letter, letter, title, body)

# ------------------------------------------------------------------ A
A = """    <h4>A1 · Blueprint against Miller's pyramid</h4>
    <p>No single instrument samples all four levels. This is what each part of the programme can honestly claim.</p>
""" + table(["Miller level", "What it means", "Instrument here", "Weight"],
  [["<b>Knows</b>", "Recalls patterns, thresholds, doses", "Unit checkpoints; final assessment", "~25%"],
   ["<b>Knows how</b>", "Applies knowledge to a clinical problem", "Case-vignette checkpoints; integrative items; key-feature problems", "~45%"],
   ["<b>Shows how</b>", "Demonstrates in simulation", "OSCE stations (A3); scenarios (Appendix B)", "~20%"],
   ["<b>Does</b>", "Performs in real practice", "Mini-CEX, CBD, MSF, entrustment (A4)", "~10%"]]) + box("pitfall", "What the written assessment cannot do", "<p>The certificate covers only the top two rows. Recognising a metabolic crisis at 2 a.m., running the first hour and making the call are team behaviours: add simulation and workplace assessment before any consequential decision.</p>") + """
    <h4>A2 · Key-feature problems</h4>
    <p>Short answers, no options. They test only the decisions on which the case turns.</p>
    <h5 class="sub">KF1 — The sleepy newborn</h5>
    <p><i>Day 4, fed well for 3 days, now drowsy and tachypnoeic. Glucose normal. Sepsis screen sent.</i></p>
    <ol>
      <li><b>Which test must be sent in the next 15 minutes?</b><br><small>Model: plasma ammonia (with gas, lactate and ketones).</small></li>
      <li><b>Ammonia 420 µmol/L. Name four first-hour actions.</b><br><small>Model: stop protein; 10% glucose; scavengers and arginine per protocol; call metabolic team and dialysis-capable PICU; critical sample.</small></li>
    </ol>
    <h5 class="sub">KF2 — The toddler after gastroenteritis</h5>
    <p><i>20 months, vomiting overnight, now drowsy. Glucose 1.7 mmol/L, ketones 0.2 mmol/L.</i></p>
    <ol>
      <li><b>What do you give, and how much?</b><br><small>Model: 10% glucose 2 mL/kg IV, then a glucose infusion.</small></li>
      <li><b>What does the ketone result suggest?</b><br><small>Model: inappropriately low ketones — fatty-acid oxidation disorder (e.g. MCAD) or hyperinsulinism.</small></li>
    </ol>
    <h5 class="sub">KF3 — The jaundiced newborn with sepsis</h5>
    <p><i>Day 8, breastfed, jaundice, INR 3.2, E. coli bacteraemia.</i></p>
    <ol>
      <li><b>Which disorder must be considered?</b><br><small>Model: classic galactosaemia.</small></li>
      <li><b>What changes today?</b><br><small>Model: stop lactose (lactose-free formula) under specialist advice; GALT sample before any transfusion; continue antibiotics.</small></li>
    </ol>
    <h5 class="sub">KF4 — The screen-positive baby</h5>
    <p><i>Day 5 newborn screen: raised leucine. Baby at home 3 hours away.</i></p>
    <ol>
      <li><b>What do you do today?</b><br><small>Model: phone the family today; check feeding and alertness; same-day assessment and confirmation with the metabolic team.</small></li>
      <li><b>What do you tell the family?</b><br><small>Model: it is a screening result, not a diagnosis; the next test is urgent because this condition can make babies unwell quickly.</small></li>
    </ol>

    <h4>A3 · OSCE stations</h4>
    <p>Twelve stations, 6&ndash;8 minutes each, with printed results cards and an actor parent where needed. Score with the six-domain rubric in Appendix C.</p>
""" + table(["#", "Station", "Tests", "Critical failure"],
  [["1", "History from a parent of a child with recurrent encephalopathy", "Trajectory, triggers, family history without blame", "Does not ask about fasting or illness triggers"],
   ["2", "Read five results cards (glucose, ketones, gas, lactate, ammonia)", "Pattern and provisional disease family", "Misses a raised ammonia"],
   ["3", "Calculate the anion gap and interpret it", "Arithmetic and meaning", "Wrong calculation"],
   ["4", "First-hour prescription for suspected hyperammonaemia", "Glucose rate, stop protein, scavengers, call", "Continues milk feeds"],
   ["5", "Collect and label a critical sample", "Timing, labelling, storage, ammonia handling", "Delays glucose for sampling"],
   ["6", "Phone referral to a metabolic centre", "Structured, timed results, clear request", "No specific request; no read-back"],
   ["7", "Hypoglycaemia with low ketones", "Treatment dose, sample, interpretation", "Wrong glucose concentration or dose"],
   ["8", "Refractory neonatal seizures", "Monitored pyridoxine trial, pre-trial samples", "Unmonitored IV pyridoxine"],
   ["9", "Explain a positive newborn screen to a parent", "Screen versus diagnosis, urgency, next step", "Says the baby has the disease"],
   ["10", "Explain a VUS", "Uncertainty, no clinical decisions on it", "Treats the VUS as a diagnosis"],
   ["11", "Recurrence counselling: recessive versus X-linked", "Correct risk for the actual inheritance", "Gives 1 in 4 for an X-linked disorder"],
   ["12", "Teach-back of a sick-day plan", "When to start, when to come in", "No clear threshold for hospital"]]) + """
    <h4>A4 · Workplace-based assessment</h4>
""" + table(["Tool", "Use it for", "Frequency", "Note"],
  [["<b>Mini-CEX</b>", "Assessment of a sick neonate or child with an unexplained course", "2&ndash;4 per learner per year", "The feedback is the intervention"],
   ["<b>CBD</b>", "Reasoning behind a metabolic work-up or referral", "2&ndash;3 per year", "Ask &ldquo;what finding did your diagnosis explain least well?&rdquo;"],
   ["<b>MSF</b>", "Teamwork and communication with families, laboratory and referral centres", "Annual", "Detects the behaviours that cause harm"]]) + """
    <h5 class="sub">Entrustment scale for the core EPA</h5>
    <p><b>EPA:</b> <i>Recognise a possible metabolic crisis in a child, start first-hour treatment, collect the critical sample and escalate to a metabolic team.</i></p>
""" + table(["Level", "Descriptor"],
  [["1", "Observes only"], ["2", "Performs with direct supervision"], ["3", "Performs with indirect supervision, supervisor reachable within minutes"],
   ["4", "Performs unsupervised; supervisor available for the unexpected"], ["5", "Supervises and teaches others"]]) + """
    <p><b>Suggested minimum for a doctor covering a NICU or paediatric emergency room alone:</b> level 4 for recognition, glucose treatment, ammonia testing and the critical sample; level 3 for starting scavenger drugs, which remain agreed with a metabolic team.</p>"""

# ------------------------------------------------------------------ B
def scenario(n, title, setup, stages, points):
    rows = "".join("<tr><td class='num'>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % s for s in stages)
    return """    <h4>Scenario %d — %s</h4>
    <p>%s</p>
    <div class="tw"><table class="reflow"><thead><tr><th class="num">Stage</th><th>Results card</th><th>Expected actions</th><th>Facilitator trigger</th></tr></thead><tbody>%s</tbody></table></div>
    <p><b>Debrief points:</b> %s</p>
""" % (n, title, setup, rows, points)

B = """    <p>Four branching scenarios that run on a doll and printed results cards &mdash; no simulator needed. Show the next card only when the team has done, or clearly failed to do, the expected actions.</p>
""" + scenario(1, "The sleepy newborn at night",
  "District hospital, 1 a.m. Day 4, 3.2 kg, fed well until yesterday. One doctor, two nurses. Ammonia assay available only in the city laboratory.",
  [("1", "Drowsy, RR 70, T 36.8, glucose 4.1", "ABC, sepsis care, send ammonia, gas, lactate, ketones", "If ammonia not requested in 10 min: &ldquo;The baby is now posturing.&rdquo;"),
   ("2", "pH 7.51, PCO₂ 25, ammonia 420 (phoned from city lab)", "Stop feeds, 10% glucose, critical sample, call metabolic centre and PICU", "If saline only: next card ammonia 560 and apnoea"),
   ("3", "Awaiting transfer", "Scavengers per phone advice if available; transfer checklist; handover", "Receiving team asks: &ldquo;What has he had, and when?&rdquo;")],
  "ammonia in the first hour; glucose as treatment; transfer as treatment.") + scenario(2, "The drowsy toddler after vomiting",
  "Emergency room. 20 months, 11 kg, vomiting overnight. Previous similar admission.",
  [("1", "Drowsy, glucose 1.6, ketones 0.2", "Critical sample from cannula, 10% glucose 2 mL/kg, infusion", "If glucose is delayed for sampling: seizure card"),
   ("2", "Glucose 6.5 after 15 min", "Continue glucose infusion; do not give lipid; send acylcarnitines", "Parent asks: &ldquo;Can we go home after this drip?&rdquo;"),
   ("3", "Acylcarnitines suggest MCAD deficiency", "Explain; emergency letter; sick-day plan; screen siblings", "&mdash;")],
  "hypoketotic hypoglycaemia; sample and treat together; sibling screening.") + scenario(3, "The ketoacidotic newborn",
  "NICU. Day 6, 2.9 kg, poor feeding then fast breathing.",
  [("1", "pH 7.10, HCO₃ 7, AG 30, ketones high, ammonia 290, platelets 55", "Recognise organic acidaemia; stop protein; glucose; call metabolic team", "If large bicarbonate boluses only: next card unchanged"),
   ("2", "Metabolic team advises carnitine and B12 trial", "Carnitine, hydroxocobalamin, carglumic acid if advised; plan dialysis if ammonia rises", "Ammonia 480 at 3 h: does the team escalate?"),
   ("3", "Stabilising", "Urine organic acids, acylcarnitines, maternal B12", "&mdash;")],
  "ketones in a newborn; the toxin not the gas; escalation on trajectory.") + scenario(4, "Jaundice, bleeding and sepsis",
  "Postnatal ward. Day 8, breastfed, jaundiced, vomiting.",
  [("1", "Bilirubin 290, INR 3.4, glucose 2.6", "Glucose, vitamin K, sepsis screen, antibiotics", "Blood culture later: E. coli"),
   ("2", "E. coli bacteraemia", "Consider galactosaemia; stop lactose under advice; GALT before transfusion", "If transfusion planned first: facilitator asks what test will now fail"),
   ("3", "Improving on lactose-free formula", "Confirm diagnosis; counsel; plan for next pregnancy", "&mdash;")],
  "two diagnoses at once; pre-transfusion samples; diet as treatment.") + pearls

C = '''    <h4>C1 · Three delivery models</h4>
''' + table(["Model", "Shape", "Best for", "Watch out for"],
  [["<b>Fully self-paced</b>", "Learners work through alone; one skills session at the end", "Large cohorts, interns, CME", "The skills session becoming a demonstration. Cap at 6 learners per doll."],
   ["<b>Flipped, Part by Part</b>", "Learners master a Part before each session; sessions are simulation and discussion", "PG residents, nursing cohorts", "Verify mastery first, or you end up teaching content"],
   ["<b>Intensive, 2 days</b>", "Parts A&ndash;C day one with simulation; D&ndash;E day two", "District outreach, visiting faculty", "Retention: schedule the review checks and a 6-week follow-up"]]) + '''
    <h4>C2 · A worked flipped-classroom session &mdash; Part B, the first hour</h4>
    <p>90 minutes, 8&ndash;12 learners, 2 dolls, printed results cards, 2 facilitators. Prerequisite: Units 4&ndash;8 mastered.</p>
''' + table(["Time", "Activity", "Purpose"],
  [["0&ndash;5", "Learning contract: &ldquo;Nobody here is being examined.&rdquo;", "Psychological safety"],
   ["5&ndash;15", "Rapid retrieval: the five bedside results; the BIMDG ammonia thresholds; the critical-sample list", "Retrieval practice; shows where the cohort is"],
   ["15&ndash;35", "Deliberate practice: write a first-hour prescription (glucose rate, scavenger doses) for three weights and check each other", "The highest-yield calculation in Part B"],
   ["35&ndash;55", "Scenarios 1 and 2 (Appendix B)", "The first hour under time pressure"],
   ["55&ndash;75", "Debrief both runs, PEARLS, two points maximum", "Consolidation"],
   ["75&ndash;85", "Role-play the phone referral with read-back", "Makes the call a habit"],
   ["85&ndash;90", "&ldquo;One thing to keep, one thing to change.&rdquo;", "Commitment to change"]]) + "\n" + appC_generic

C = C.replace("A cut score chosen by preference — including the 90%", "A cut score chosen by preference — including the 80%")
C = C.replace("&ldquo;a labour-room nurse who would reliably ventilate a flat baby within 60 seconds and recognise when it was not working, but would hesitate over an unfamiliar drug dose.&rdquo;",
              "&ldquo;a first-year resident who would reliably send ammonia in a sleepy newborn, start 10% glucose, take the critical sample and call the metabolic team, but would hesitate over scavenger doses or dialysis thresholds.&rdquo;")
C = re.sub(r"Delivery-room audit: time to PPV, DCC rate, routine suction rate, admission temperature", "Metabolic audit: time to ammonia result, glucose rate in suspected crises, critical samples labelled, time to metabolic team call", C)
C = C.replace("with a labour-room audit", "with a metabolic audit")
C = re.sub(r"Admission hypothermia, early neonatal mortality, HIE referrals within window", "Time to diagnosis, repeat admissions before diagnosis, neurological outcome after hyperammonaemia, screen-positive babies lost to follow-up", C)

# ------------------------------------------------------------------ D
D = """    <p>Map each unit to the <b>competency descriptors</b> of the NMC CBME curriculum (UG) and the MD Paediatrics curriculum (PG). The code column is deliberately blank: codes were revised in the September 2024 guidelines, and Volume II is the only authority. <b>Do not invent codes</b>; fill them in from the current document.</p>
""" + table(["Unit", "Competency descriptor (paraphrased)", "NMC code (verify)", "Domain", "Teaching method", "Assessment"],
  [["1&ndash;3", "Recognise clinical features suggesting an inborn error of metabolism; interpret first-line investigations", "", "K, S", "Self-paced module; case discussion", "Checkpoints; OSCE 1&ndash;3"],
   ["4&ndash;8", "Initiate emergency management of metabolic crises (hyperammonaemia, acidosis, hypoglycaemia) and refer", "", "K, S", "Flipped session (C2); simulation", "OSCE 4&ndash;7; KF1&ndash;2"],
   ["9&ndash;13", "Recognise metabolic causes of myopathy, liver disease, seizures, movement disorder and developmental delay", "", "K", "Case-based", "OSCE 8; CBD"],
   ["14&ndash;16", "Plan and interpret biochemical and genetic investigations", "", "K, S", "Case conference", "OSCE 10; CBD"],
   ["17", "Explain newborn screening results and inheritance to families", "", "S, A, C", "Role play", "OSCE 9, 11"],
   ["18&ndash;19", "Plan long-term care, emergency plans and referral in the Indian health system", "", "S, A, C", "Role play; pathway design", "OSCE 12; MSF"],
   ["20", "Integrate recognition, treatment, diagnosis and counselling", "", "K, S, A", "Capstone case", "CBD"]]) + box("pitfall", "Why the code column is empty", "<p>Invented or outdated competency codes are worse than none. Fill the column from NMC CBME Volume II (2024) and the MD Paediatrics curriculum at your institution.</p>")

# ------------------------------------------------------------------ E
E = box("danger", "Verify before every use", "<p>Doses here are drawn from the cited guidelines for learning. Metabolic emergency drugs are prescribed with a metabolic team; check every dose against your centre's protocol, a current formulary and the child in front of you. This annex is never locked.</p>") + """
    <h4>E1 · First hour</h4>
""" + table(["Item", "Guide", "Source / notes"],
  [["Hypoglycaemia", "10% glucose 2 mL/kg (200 mg/kg) IV, then infusion", "BIMDG"],
   ["Glucose infusion in suspected crisis (baby)", "10% glucose 5 mL/kg/h (&asymp;8 mg/kg/min)", "BIMDG undiagnosed hyperammonaemia (2016); adjust fluids and electrolytes"],
   ["Protein", "Stop; no longer than 24&ndash;48 h", "GeneReviews UCD overview (2025)"],
   ["IV lipid", "Avoid until FAOD excluded", ""]]) + """
    <h4>E2 · Hyperammonaemia (BIMDG undiagnosed hyperammonaemia, 2016)</h4>
""" + table(["Drug / action", "Loading", "Maintenance (max/day)", "Notes"],
  [["Repeat ammonia", "&gt;150 µmol/L (child), &gt;200 (neonate)", "", "&gt;200 urgent treatment; &gt;250 arrange transfer"],
   ["Sodium benzoate IV", "250 mg/kg over 90 min", "250 mg/kg/day (max 500)", ""],
   ["Sodium phenylbutyrate", "250 mg/kg", "250 mg/kg/day (max 600)", ""],
   ["Arginine IV", "150 mg/kg", "300 mg/kg/day (max 500)", "Not in arginase deficiency; GeneReviews gives 200&ndash;250 mg/kg loading"],
   ["Carglumic acid (oral/NG)", "Consider 250 mg/kg single dose", "Per metabolic team", "GeneReviews: 100&ndash;250 mg/kg/day in 2&ndash;4 doses for NAGS deficiency"],
   ["Extracorporeal removal", "&mdash;", "&mdash;", "If ammonia not falling (e.g. &gt;250 after ~3 h) or severe encephalopathy; high-dose CKRT preferred"]]) + """
    <h4>E3 · Other emergency and cofactor treatments</h4>
""" + table(["Drug", "Indication", "Dose", "Source / notes"],
  [["L-carnitine IV", "Organic acidaemias", "Commonly 100 mg/kg/day", "Per metabolic team"],
   ["Hydroxocobalamin IM", "Suspected MMA (B12 responsiveness)", "1 mg daily", "Per metabolic team; exclude maternal B12 deficiency"],
   ["Biotin oral", "Biotinidase deficiency", "5&ndash;10 mg/day (profound); 2.5&ndash;10 mg/day (partial)", "GeneReviews (Feb 2026)"],
   ["Pyridoxine IV (diagnostic)", "Refractory neonatal/infant seizures", "100 mg with EEG and cardiorespiratory monitoring; repeat to max 500 mg", "GeneReviews PDE-ALDH7A1; apnoea risk"],
   ["Pyridoxine oral", "Non-acute trial / maintenance", "30 mg/kg/day (max 500 mg/day)", "GeneReviews PDE-ALDH7A1"]]) + """
    <h4>E4 · Home emergency regimen (glucose polymer drinks)</h4>
""" + table(["Age", "Concentration (BIMDG regimens)"],
  [["0&ndash;1 year", "10%"], ["1&ndash;2 years", "15%"], ["2&ndash;9 years", "20%"], ["10 years and over", "25%"]]) + """
    <p>Volumes and frequency are individual and set by the metabolic dietitian. Vomiting or refusing the regimen, or drowsiness, means hospital now.</p>
    <h4>E5 · Targets and ranges</h4>
""" + table(["", "Value"],
  [["Anion gap", "Na&#8314; − (Cl&#8315; + HCO&#8323;&#8315;); about 8&ndash;16 mmol/L (laboratory-specific)"],
   ["Phenylalanine target in children with PKU", "120&ndash;360 µmol/L (European 2017 and ACMG guidelines)"],
   ["GLUT1 deficiency", "CSF:blood glucose ratio usually below about 0.45 (paired sample)"]])

# ------------------------------------------------------------------ F
F = """    <h4>Emergency and disease guidelines</h4>
    <ul>
      <li>British Inherited Metabolic Diseases Group. <b>Emergency guidelines</b>: undiagnosed hyperammonaemia (2016), recurrent hypoglycaemia (2016), and disease-specific paediatric protocols. <a href="https://bimdg.org.uk/emergency/">bimdg.org.uk</a></li>
      <li>H&auml;berle J, Burlina A, Chakrapani A, et&nbsp;al. <b>Suggested guidelines for the diagnosis and management of urea cycle disorders: first revision.</b> J Inherit Metab Dis 2019. <a href="https://pubmed.ncbi.nlm.nih.gov/30982989/">PubMed</a></li>
      <li>Forny P, H&ouml;rster F, Ballhausen D, et&nbsp;al. <b>Guidelines for the diagnosis and management of methylmalonic acidaemia and propionic acidaemia: first revision.</b> J Inherit Metab Dis 2021.</li>
      <li>van Wegberg AMJ, MacDonald A, Ahring K, et&nbsp;al. <b>The complete European guidelines on phenylketonuria: diagnosis and treatment.</b> Orphanet J Rare Dis 2017.</li>
      <li>Coughlin CR, Tseng LA, Abdenur JE, et&nbsp;al. <b>Consensus guidelines for the diagnosis and management of pyridoxine-dependent epilepsy due to &alpha;-aminoadipic semialdehyde dehydrogenase deficiency.</b> J Inherit Metab Dis 2021.</li>
      <li>Raina R, et&nbsp;al. <b>Consensus guidelines for management of hyperammonaemia in paediatric patients receiving continuous kidney replacement therapy.</b> Nat Rev Nephrol 2020.</li>
      <li><b>GeneReviews</b> (University of Washington; NCBI Bookshelf): Urea Cycle Disorders Overview (updated July 2025); MCAD Deficiency; Isolated Methylmalonic Acidemia; Biotinidase Deficiency (revised February 2026); Pyridoxine-Dependent Epilepsy &ndash; ALDH7A1; Classic Galactosemia; Maple Syrup Urine Disease; Wilson Disease; Pompe Disease; Phenylalanine Hydroxylase Deficiency (revised November 2025); Primary Mitochondrial Disorders Overview.</li>
      <li>Richards S, et&nbsp;al. <b>Standards and guidelines for the interpretation of sequence variants</b> (ACMG/AMP). Genet Med 2015.</li>
    </ul>
    <h4>Reference texts</h4>
    <ul>
      <li>Saudubray JM, Baumgartner MR, Garc&iacute;a-Cazorla &Aacute;, Walter J (eds). <b>Inborn Metabolic Diseases: Diagnosis and Treatment</b>, 7th edition. Springer.</li>
      <li>Blau N, et&nbsp;al. (eds). <b>Physician&rsquo;s Guide to the Diagnosis, Treatment, and Follow-Up of Inherited Metabolic Diseases</b>, 2nd edition. Springer.</li>
      <li><b>Inborn errors of metabolism</b> (issue). Pediatr Clin North Am 2018;65(2) &mdash; eleven review articles by presentation.</li>
      <li>International Classification of Inherited Metabolic Disorders (ICIMD) and the Online Inherited Metabolic Disease WebApp. <a href="https://oimd.org/">oimd.org</a></li>
    </ul>
    <h4>Indian sources</h4>
    <ul>
      <li>IAP&ndash;NNF. <b>Approach and Management of Inborn Errors of Metabolism in the Neonate</b>, QRG 51, IAP Action Plan 2026.</li>
      <li>Indian Journal of Practical Pediatrics 2025;27(3&ndash;4): red flags, laboratory work-up, genetic testing, treatable IEMs in developmental disorders, and newborn screening in India (Gupta, Gupta, Kabra, Kapoor).</li>
      <li>Ministry of Health and Family Welfare. <b>National Policy for Rare Diseases, 2021</b>, with later amendments and Centre of Excellence notifications (including March and July 2026). <a href="https://www.mohfw-dohfw.gov.in/documents/acts-and-policies">MoHFW</a></li>
      <li>Press Information Bureau, 13 March 2026: statement on rare-disease treatment support of up to &#8377;50 lakh per patient through Centres of Excellence.</li>
      <li>Department of Biotechnology. <b>UMMID initiative and NIDAN Kendras</b> (2020 programme document).</li>
      <li>Indian Society for Inborn Errors of Metabolism (ISIEM) &ndash; NNF Foundation Course on IEM.</li>
      <li>National Medical Commission. <b>CBME curriculum</b> (2024) and MD Paediatrics curriculum.</li>
    </ul>
    <h4>Educational evidence base</h4>
    <ul>
      <li>Larsen DP, Butler AC, Roediger HL (2009) &mdash; test-enhanced learning in medical education. Cepeda NJ, et&nbsp;al. (2006) &mdash; distributed practice. Butterfield B, Metcalfe J (2001) &mdash; the hypercorrection effect.</li>
      <li>Raupach T, et&nbsp;al. (2016) &mdash; test-enhanced learning of clinical reasoning (crossover randomised trial).</li>
      <li>Stojan J, et&nbsp;al. <b>BEME Guide No. 69</b> &mdash; technology-enhanced learning in health professions education.</li>
      <li><b>Ottawa 2020 Consensus Statements</b> on programmatic assessment. McKinley RK, Norcini JJ. <b>AMEE Guide No. 85</b> &mdash; standard setting.</li>
    </ul>
""" + box("danger", "Check the edition before you teach from anything", "<p>GeneReviews chapters are revised continually, emergency protocols differ between centres, and India&rsquo;s rare-disease policy is amended every few months. Confirm any dose, threshold or policy figure against the current source before teaching or treating. If you are reading this more than three years after the build date in the footer, assume something here is out of date.</p>")

# ------------------------------------------------------------------ G (generic, adapted)
G = appG
G = G.replace("sample 50 items from a pool of 78", "sample 50 items from a pool of 70")
G = G.replace("This module has no evidence that it changes delivery-room behaviour or neonatal outcomes.", "This module has no evidence yet that it changes time to diagnosis or child outcomes.")
G = G.replace("WHO guidance on newborn care", "BIMDG, GeneReviews and IAP–NNF guidance on inborn errors of metabolism")
G = G.replace("Part D is unintelligible without Part C", "Part B's first-hour decisions make no sense without Part A's pattern reading")
# strip wrapper lines from the NRP block so we can re-wrap consistently
G = G[G.index('<div class="app-body">') + len('<div class="app-body">'):]
G = G[:G.rindex("</div>\n</div>")] if "</div>\n</div>" in G else G

head = '''<section class="part" id="appendices">
  <div class="part-head">
    <div>
      <span class="pk">Appendices</span>
      <h2>Appendices A&ndash;G</h2>
    </div>
    <span class="part-meta"><span class="app-open-note">Never locked</span></span>
  </div>
  <p class="part-lede">Open from the first minute, whatever your progress. Appendix E (emergency drugs and doses) and Appendix F (references) are clinical safety material, and clinical safety material behind a quiz is a patient-safety problem. Every appendix can be printed on its own.</p>
'''
html = head + app("A", "Assessment bank", A) + app("B", "Simulation library", B) + app("C", "Faculty guide", C) + \
       app("D", "Curriculum mapping", D) + app("E", "Emergency drug and dose annex", E) + app("F", "References", F) + \
       app("G", "Evidence-governed design", G) + "\n</section>\n"
open(OUT, "w", encoding="utf-8").write(html)
print("wrote", OUT, len(html) // 1024, "KB")
for bad in ["NRP", "PPV", "labour", "oxygen", "ventilat", "CPAP"]:
    n = len(re.findall(bad, html, re.I))
    if n: print("  check:", bad, n)
