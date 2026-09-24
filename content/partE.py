from gen import *

part("E", "Living with a metabolic disorder", "Units 18&ndash;20 · ~4 hours",
     "A diagnosis is the start of decades of care, most of it delivered by families at home, in schools and in the nearest hospital at 2 a.m. This Part is about making that care work in India, and it ends by following one child from the first crisis to follow-up.")

# ------------------------------------------------------------------ UNIT 18
unit(18, "E", "Living with a diagnosis",
  "Long-term care protects the brain and the body by controlling the metabolic problem, and protects the child by keeping growth, school and family life going. Success is measured in both.",
  [("e", "Explain why treatments differ by mechanism: diet, cofactor, scavenger, enzyme replacement, transplant."),
   ("e", "Describe the parts of a sick-day plan and an emergency letter."),
   ("a", "Review growth, development and daily function alongside biochemical results."),
   ("x", "Plan school, anaesthesia and transition to adult care.")],
  [
   roles({"ug": "Explain an emergency letter and a sick-day plan in plain language.",
          "pg": "Review growth, intake, biochemistry and development at each visit, and update the emergency plan.",
          "fac": "Use a teach-back role play: the caregiver explains the sick-day plan in their own words."}),
   sec(1, "Treatment follows mechanism", table(
     ["Approach", "Examples"],
     [["Reduce the substrate (diet)", "Phenylalanine-restricted diet in PKU; protein restriction with amino acid supplements in urea cycle disorders and MSUD"],
      ["Replace the missing product or cofactor", "Biotin in biotinidase deficiency; hydroxocobalamin in B12-responsive MMA; arginine in urea cycle disorders"],
      ["Remove the toxin", "Sodium benzoate and phenylbutyrate in urea cycle disorders; carnitine in organic acidaemias"],
      ["Block an upstream step", "Nitisinone in tyrosinaemia type I"],
      ["Replace the enzyme", "Enzyme replacement therapy in Pompe, Gaucher and MPS"],
      ["Replace the organ", "Liver transplantation in urea cycle disorders and MMA; stem-cell transplantation in MPS I and cerebral X-ALD"]])),

   sec(2, "Prepare for illness before it happens", '''
  <p>Every child at risk of decompensation needs:</p>
  <ul>
    <li>A <b>written sick-day plan</b>: when to start the emergency regimen at home, how often to give it, and when to come to hospital (vomiting, refusing the regimen, drowsiness, or no improvement after a set time).</li>
    <li>An <b>emergency letter</b> for the hospital: diagnosis, first-hour treatment, drug doses, what to avoid, and a 24-hour contact.</li>
    <li>A copy with the family, on their phone, and at the local hospital.</li>
  </ul>''' + pitfall('''<p>A child with a known disorder waits four hours in triage because nobody read the letter. Flag known metabolic patients in your hospital record so they are seen immediately.</p>''')),

   sec(3, "Look beyond the laboratory value", '''
  <p>Each review: growth (weight, length, head circumference), dietary intake and supplies, biochemistry, development and school, bone health, and the family&rsquo;s burden. A child can have perfect phenylalanine levels and be failing to thrive because the protein substitute is not being taken, or can be struggling at school with good biochemistry.</p>'''),

   sec(4, "School, surgery and adulthood", '''
  <ul>
    <li><b>School:</b> a short letter on meals, snacks, sick days and emergency contacts.</li>
    <li><b>Surgery and anaesthesia:</b> fasting is dangerous; plan with the metabolic team for IV glucose from the start of the fast, and avoid drugs that are contraindicated (e.g. propofol-containing lipid in long-chain FAOD, per specialist advice).</li>
    <li><b>Transition:</b> teenagers need to learn their own diagnosis, diet and emergency plan; plan transfer to adult metabolic care and discuss pregnancy planning (maternal PKU).</li>
  </ul>''' + india('''<p>Special medical foods and protein substitutes are often imported, expensive and hard to obtain outside major cities. Families may ration them or stop. Ask directly about supply at each visit, involve the Centre of Excellence and patient support groups, and help the family with the paperwork for any government support.</p>'''), lvl="a"),
  ],
  [Q("A 6-year-old with MSUD has been vomiting since morning and has refused two doses of her home emergency drink. She is alert. What does her sick-day plan most likely say?",
     ["Continue the drink at home and review tomorrow.",
      "Come to hospital now for IV glucose, because she cannot take the emergency regimen.",
      "Stop all fluids until the vomiting settles.",
      "Give her usual protein-containing meals."],
     1,
     "What is the usual trigger to move from home to hospital in a sick-day plan?",
     "She is vomiting and refusing the regimen, so it is not working. Where does she need to be?",
     "When a child is vomiting or cannot take the emergency regimen, the plan is to <b>come to hospital now</b> for IV glucose, before drowsiness develops. MSUD crises can progress to cerebral oedema quickly.",
     "<b>A</b> &mdash; waiting until tomorrow risks encephalopathy. <b>C</b> &mdash; stopping fluids worsens catabolism. <b>D</b> &mdash; protein increases leucine during a crisis.",
     "Vomiting or refusing the regimen means hospital, not waiting.",
     "section 2, ‘Prepare for illness before it happens’"),
   Q("A 9-year-old with PKU has phenylalanine levels within target at every visit, but her weight has fallen from the 50th to the 9th centile over a year. What is the most important next step?",
     ["Congratulate the family on good control and continue.",
      "Review her full dietary intake, protein substitute use and supply with the metabolic dietitian.",
      "Tighten the phenylalanine target further.",
      "Stop the protein substitute."],
     1,
     "What does good biochemistry fail to show?",
     "Falling weight centiles with good phenylalanine levels suggest the total diet is not meeting her needs. Who can find out why?",
     "Good phenylalanine control with <b>falling growth</b> suggests inadequate energy or protein intake, often from missed protein substitute or supply problems. Review the whole diet with the metabolic dietitian.",
     "<b>A</b> &mdash; growth failure is a problem even with good biochemistry. <b>C</b> &mdash; tighter restriction would worsen growth. <b>D</b> &mdash; the protein substitute provides essential protein.",
     "Measure the child, not only the metabolite.",
     "section 3, ‘Look beyond the laboratory value’")]
)

# ------------------------------------------------------------------ UNIT 19
unit(19, "E", "IEM care in India",
  "In India, the gap is rarely knowledge about the disease. It is the distance between the child who is sick tonight and the laboratory, the drug, the dialysis machine and the specialist who can help. This unit is about closing it.",
  [("e", "Match referral urgency to the child's clinical needs."),
   ("e", "Build a tiered investigation plan that fits local laboratories."),
   ("a", "Describe the National Policy for Rare Diseases (2021) and Centres of Excellence as dated, checkable information."),
   ("x", "Design and test an institutional pathway for suspected metabolic emergencies.")],
  [
   roles({"ug": "Know where the nearest metabolic referral centre is and how to reach it.",
          "pg": "Stabilise, call, and send a usable handover; help families navigate the rare-disease policy through a Centre of Excellence.",
          "fac": "Write, test and audit your unit's metabolic emergency pathway with a fictional night-time case."}),
   sec(1, "Choose the destination the child needs now", '''
  <p>First decide: does the child need <b>emergency stabilisation and transfer</b>, <b>urgent specialist discussion</b>, or <b>planned outpatient evaluation</b>? A child with hyperammonaemia needs a centre that can do dialysis and has a PICU &mdash; a genetics clinic listing is not enough. Phone before transfer and agree what the receiving centre needs.</p>'''),

   sec(2, "Spend the next test on the next decision", '''
  <p>For every test, complete: &ldquo;This result could change&hellip;&rdquo; &mdash; today&rsquo;s treatment, the next diagnostic step, or family counselling. Start with glucose, gas, lactate, ammonia and ketones (usually available), store samples, and send dried blood spots and urine for specialised tests to a laboratory agreed with the metabolic team. Ask for real local prices when cost matters.</p>''' + tracks(
     ["Tertiary centre with a metabolic laboratory, dietitian and PICU",
      "Same-day amino acids and acylcarnitines"],
     ["District hospital: glucose, gas, ammonia (sometimes), lactate; dried blood spots by courier",
      "A laminated pathway: who to call, what to send, how to transport, which drugs to start",
      "A tele-consultation with the metabolic centre before transfer"])),

   sec(3, "The National Policy for Rare Diseases", '''
  <p>The <b>National Policy for Rare Diseases (NPRD) 2021</b> groups rare diseases by treatment need and funds treatment through designated <b>Centres of Excellence</b>. A Government of India statement of March 2026 reported financial support of <b>up to ₹50 lakh per patient</b> for identified rare diseases through these centres. The list of centres and the rules are amended from time to time (for example, a new centre notified in July 2026).</p>''' + danger('''<p>Describe policy as dated information. Do not promise a family eligibility or a specific amount. Confirm the current rules, the eligible condition and the application process with a Centre of Excellence, and refer through them.</p>''')),

   sec(4, "Build and test an institutional pathway", '''
  <p>Agree a written pathway with paediatrics, emergency medicine, the laboratory, a metabolic or genetics contact, dietetics and administration: who gives urgent advice, how samples are sent, who reviews results, which drugs are stocked or where they can be obtained at night, and how children are transferred. Test it with a fictional night-time referral; audit time to ammonia result, rejected samples and unreviewed results.</p>''' + india('''<p>The DBT UMMID initiative (NIDAN Kendras) and several ICMR and state programmes have built genetic diagnosis, counselling and screening capacity, and patient organisations (e.g. for lysosomal and urea cycle disorders) help families with access. Keep a current, verified contact list rather than relying on an old directory.</p>'''), lvl="a"),
  ],
  [Q("A district hospital paediatrician has a 3-day-old with ammonia 390 µmol/L. The nearest centre with a PICU and dialysis is 4 hours away. What is the best plan?",
     ["Transfer to the nearest genetics clinic listed online.",
      "Start glucose, stop protein, call the metabolic centre and a dialysis-capable PICU, agree drugs and transfer, and send a structured handover with stored samples.",
      "Keep the baby locally and repeat ammonia tomorrow.",
      "Wait for plasma amino acids before calling anyone."],
     1,
     "What capability does this baby need?",
     "At 390 µmol/L the baby may need dialysis. Which centre can provide it, and what should happen before and during transfer?",
     "This baby needs a centre with <b>dialysis and a PICU</b>. Start emergency treatment, call the metabolic team and PICU, agree drugs and transport, and send a structured handover with timed results and stored samples.",
     "<b>A</b> &mdash; a genetics clinic cannot manage acute hyperammonaemia. <b>C</b> &mdash; waiting risks brain injury. <b>D</b> &mdash; the diagnosis is not needed to start treatment and transfer.",
     "Send the child to the capability they need, not to the nearest name.",
     "section 1, ‘Choose the destination the child needs now’"),
   Q("The parents of a child newly diagnosed with Gaucher disease ask whether the government will pay for enzyme replacement therapy. What is the most accurate response?",
     ["Yes, every child receives ₹50 lakh automatically.",
      "No, there is no government support for rare diseases.",
      "The National Policy for Rare Diseases supports treatment for some conditions through Centres of Excellence; we will refer you to one to confirm current eligibility and the process.",
      "Only adults are eligible."],
     2,
     "How is rare-disease treatment funded under the national policy?",
     "Support exists, but it is given through designated centres and the rules change. What can you honestly promise?",
     "The NPRD 2021 supports treatment of listed rare diseases (including Gaucher disease) through designated <b>Centres of Excellence</b>, with support of up to ₹50 lakh per patient reported in 2026. Eligibility and process must be confirmed with a centre; do not promise an amount.",
     "<b>A</b> &mdash; support is not automatic and amounts are limits, not guarantees. <b>B</b> &mdash; the policy exists. <b>D</b> &mdash; the policy is not restricted to adults.",
     "Describe policy honestly: support exists, and it runs through Centres of Excellence.",
     "section 3, ‘The National Policy for Rare Diseases’")]
)

# ------------------------------------------------------------------ UNIT 20
unit(20, "E", "Capstone: follow the child",
  "One fictional baby, Aarav, from the first sign on day 4 to the family's questions about their next pregnancy. At each stage, name what is threatened, what you will do, and how you will know it is working. Then look at where the field is going.",
  [("e", "Apply recognition, the first hour and the critical sample to an evolving case."),
   ("e", "Escalate on the trajectory of ammonia and neurology."),
   ("a", "Interpret the confirmatory results and explain them to the family."),
   ("x", "Discuss current developments: genomic newborn screening, gene and mRNA therapies.")],
  [
   roles({"ug": "At each stage, say what you would observe, report and document.",
          "pg": "Lead the decisions: tests, emergency drugs, transfer, dialysis and counselling.",
          "fac": "Run the capstone as a table-top simulation and debrief on timing: when did each decision happen, and could it have been earlier?"}),
   sec(1, "Stage 1: day 4, the first sign", '''
  <p><b>Aarav, 3.2 kg</b>, fed well for 3 days. Now sleepy, feeding poorly, breathing fast. Temperature normal. Glucose 4.0 mmol/L.</p>
  <p><b>Action:</b> assess ABC, start sepsis care, and send ammonia, gas, lactate and ketones now (Unit 2). <b>Result:</b> pH 7.50, PCO₂ 26 mmHg, ammonia 420 µmol/L. <b>Pattern:</b> respiratory alkalosis with high ammonia &mdash; a urea cycle disorder is likely (Unit 3).</p>'''),

   sec(2, "Stage 2: the first hour", fig("firsthour", "The first hour in suspected hyperammonaemia", '''  RECOGNISE  sleepy newborn after a well interval → check AMMONIA
  STOP       protein and milk feeds
  GLUCOSE    10% glucose 2 mL/kg, then infusion (e.g. 5 mL/kg/h)
  SAMPLE     critical sample + stored plasma and urine (label times)
  SCAVENGE   sodium benzoate ± phenylbutyrate + arginine (per protocol)
  CALL       metabolic team + dialysis-capable PICU; transfer early
  REASSESS   ammonia and neurology every 2–4 h; dialysis if not falling''') + '''
  <p><b>Action:</b> stop feeds, 10% glucose, critical sample, call the metabolic centre, start sodium benzoate and arginine as advised, organise transfer (Units 4&ndash;6).</p>'''),

   sec(3, "Stage 3: not falling", '''
  <p>Three hours later ammonia is 510 µmol/L and Aarav is less responsive. <b>Decision:</b> drugs alone are not enough &mdash; he needs <b>extracorporeal removal</b> now. He is transferred to a PICU for high-dose continuous kidney replacement therapy with scavengers and glucose running. Ammonia falls below 200 µmol/L within 12 hours.</p>''' + danger('''<p>Do not wait for the next result if the child is deteriorating. Escalate on the trajectory.</p>''')),

   sec(4, "Stage 4: the diagnosis and the family", '''
  <p>Plasma citrulline is very low and urine orotic acid is very high: <b>OTC deficiency</b>. Genetic testing finds a pathogenic variant on the X chromosome; the mother is a carrier. She mentions she has always disliked meat and eggs. Long-term plan: protein-restricted diet with essential amino acids, sodium benzoate or phenylbutyrate, citrulline or arginine, a sick-day plan, emergency letter, and discussion of liver transplantation (Units 17&ndash;19).</p>
  <p><b>Debrief:</b> what was the earliest warning, and when was ammonia sent? Name one decision you would make earlier next time.</p>'''),

   sec(5, "Future directions", '''
  <ul>
    <li><b>Genomic newborn screening.</b> Several large research programmes are testing whether sequencing newborns finds treatable disorders that biochemical screening misses. Questions of interpretation, cost and consent remain open.</li>
    <li><b>Gene and mRNA therapies.</b> AAV gene therapy for OTC deficiency and mRNA therapies for propionic and methylmalonic acidaemia are in clinical trials; none is yet routine care.</li>
    <li><b>Expanded screening in India.</b> Tandem mass spectrometry screening is expanding through state and private programmes; equitable coverage and follow-up are the main challenges.</li>
    <li><b>Rare-disease policy.</b> India&rsquo;s NPRD continues to be amended; indigenous and lower-cost therapies are a stated priority.</li>
  </ul>''', tier="nice"),
  ],
  [Q("In Stage 3, Aarav's ammonia has risen from 420 to 510 µmol/L after 3 hours of glucose, sodium benzoate and arginine, and he is less responsive. What is the correct decision?",
     ["Continue the same drugs and recheck in 6 hours.",
      "Arrange extracorporeal ammonia removal (haemofiltration or dialysis) now, continuing drugs and glucose.",
      "Start protein feeds to reverse catabolism.",
      "Give an exchange transfusion."],
     1,
     "What should happen when ammonia is rising despite drug treatment?",
     "The ammonia is above 500 and rising, and the baby is worse. Which treatment removes ammonia fastest?",
     "Rising ammonia with worsening neurology despite 3 hours of drugs means <b>extracorporeal removal now</b>: high-dose continuous kidney replacement therapy or haemodialysis, with drugs and glucose continuing.",
     "<b>A</b> &mdash; waiting 6 hours at this level risks severe brain injury. <b>C</b> &mdash; protein now adds to the nitrogen load; it is reintroduced later by the metabolic team. <b>D</b> &mdash; exchange transfusion does not clear ammonia effectively.",
     "Escalate on the trajectory, not on the timetable.",
     "section 3, ‘Stage 3: not falling’"),
   Q("Aarav's results show very low citrulline and very high urine orotic acid. His mother has lifelong protein aversion. What is the diagnosis, and who else may need testing?",
     ["Carbamoyl phosphate synthetase 1 deficiency; no family testing needed.",
      "OTC deficiency; the mother (a possible carrier) and any sisters or future children should be offered testing and counselling.",
      "Argininosuccinic aciduria; only the father needs testing.",
      "Transient hyperammonaemia of the newborn; no testing needed."],
     1,
     "Which urea cycle defect gives low citrulline with high orotic acid?",
     "High orotic acid separates OTC deficiency from CPS1 and NAGS deficiency. OTC is X-linked. Who is at risk?",
     "Low citrulline with <b>high orotic acid</b> indicates <b>OTC deficiency</b>, which is X-linked. The mother&rsquo;s protein aversion suggests she is a symptomatic carrier. Offer testing and counselling to her, to female relatives, and for future pregnancies.",
     "<b>A</b> &mdash; CPS1 deficiency has low or normal orotic acid. <b>C</b> &mdash; argininosuccinic aciduria has raised citrulline and argininosuccinic acid. <b>D</b> &mdash; transient hyperammonaemia does not produce this amino acid pattern.",
     "Orotic acid splits the proximal urea cycle defects.",
     "section 4, ‘Stage 4: the diagnosis and the family’")]
)
