from gen import *

part("A", "Recognise", "Units 1&ndash;3 · ~4 hours",
     "Inborn errors of metabolism are individually rare and collectively common, and most children who die of one die before anyone says the word &lsquo;metabolic&rsquo;. This Part teaches the three habits that change that: notice the trajectory that does not fit, run the metabolic questions alongside sepsis rather than after it, and read the first bedside results as a pattern.")

# ------------------------------------------------------------------ UNIT 1
unit(1, "A", "Could this be metabolic?",
  "Nobody diagnoses an inborn error they never considered. The skill here is not memorising hundreds of disorders; it is recognising the illness that does not behave like the diagnosis you gave it.",
  [("e", "Recognise the clinical trajectories that should prompt the question &lsquo;could this be metabolic?&rsquo;"),
   ("e", "Explain why a negative family history does not exclude an inherited disorder."),
   ("a", "Use the three mechanistic groups &mdash; intoxication, energy deficiency, complex molecules &mdash; to organise a differential."),
   ("x", "Hold two explanations open when sepsis and a metabolic disorder may coexist.")],
  [
   roles({"ug": "Recognise the pattern, describe it clearly and escalate to the supervising clinician.",
          "pg": "Keep the metabolic differential open alongside sepsis, organise first-line tests and call the metabolic team early.",
          "fac": "Assess whether learners can state the trajectory and the finding their diagnosis explains least well, not whether they can name rare enzymes."}),
   sec(1, "Begin with the trajectory", '''
  <p>Ask one question of every sick child: <b>does the course fit the working diagnosis?</b> Consider an inborn error of metabolism (IEM) when you see:</p>
  <ul>
    <li><b>A well interval, then deterioration</b> &mdash; a newborn who fed normally for days, then became sleepy and stopped feeding.</li>
    <li><b>Encephalopathy out of proportion</b> to the fever, dehydration or infection.</li>
    <li><b>Recurrent episodes</b> of vomiting, drowsiness or ataxia with illness or fasting, and a child who is well between them.</li>
    <li><b>Several organ systems</b> becoming involved without an obvious unifying cause: brain, liver, heart, muscle, kidney.</li>
    <li><b>Loss of skills</b> the child once had.</li>
  </ul>''' + pearl('''<p>Vomiting alone is common. Vomiting with altered consciousness and an unusual biochemical pattern deserves a different level of attention.</p>''')),

   sec(2, "Three groups that lead to action", table(
     ["Group", "Mechanism", "Typical story", "Examples"],
     [["<b>Intoxication</b>", "A toxic small molecule accumulates", "Symptom-free interval, then acute decompensation with feeding or illness", "Urea cycle disorders, organic acidaemias, MSUD, galactosaemia"],
      ["<b>Energy deficiency</b>", "Cells cannot make or use fuel", "Hypoglycaemia, lactic acidosis, cardiomyopathy, myopathy; acute or progressive", "Fatty-acid oxidation disorders, glycogen storage disease, mitochondrial disease"],
      ["<b>Complex molecules</b>", "Large molecules cannot be built or broken down", "Slowly progressive, multisystem; organomegaly, coarse features, regression", "Lysosomal, peroxisomal and glycosylation disorders"]]) + '''
  <p>The groups organise the differential and point to urgency: intoxication disorders are emergencies where hours matter. They are a teaching map, not a formal classification, and some disorders overlap.</p>'''),

   sec(3, "Take a family story without blame", '''
  <p>Ask about unexplained childhood deaths, siblings with similar illness, miscarriages and parental relatedness (consanguinity). Many affected children have <b>no recognised family history</b>: most IEMs are autosomal recessive, and carriers are well. Say: &ldquo;Inherited conditions can occur even when everyone else in the family is well.&rdquo;</p>''' + pitfall('''<p>&ldquo;No family history, so unlikely.&rdquo; Replace it with what you actually asked and found. A first affected child in a family with no known history is the usual situation, not the exception.</p>''')),

   sec(4, "Keep two explanations open", '''
  <p>A positive infection result may explain only part of the picture. Classic galactosaemia can present with jaundice, liver dysfunction, bleeding and <b>E. coli sepsis</b>; hyperammonaemia can be missed in a baby being treated for sepsis. Treat the infection and ask which finding your diagnosis explains <b>least well</b>.</p>''' + india('''<p>Consanguineous marriage is common in several Indian communities and raises the chance of autosomal recessive disorders. Ask about it respectfully and record it as information, never as blame. Newborn screening coverage is uneven across states (Unit 17), so many Indian children with an IEM present clinically, not through a screen.</p>'''), lvl="a"),
  ],
  [Q("An 18-month-old is admitted drowsy after two days of vomiting and poor intake. She had a similar admission at 10 months that ended without a diagnosis. There is no family history of similar illness. What is the most appropriate next approach?",
     ["Reassure the family, since inherited disorders almost always affect another relative.",
      "Wait for another episode before investigating the pattern.",
      "Assess and stabilise urgently, and investigate metabolic and endocrine causes alongside the current illness.",
      "Diagnose MCAD deficiency from the history and start a special diet."],
     2,
     "What does a recurrent, illness-triggered drowsiness pattern suggest?",
     "A negative family history is common in autosomal recessive disorders. What should happen now, during the episode?",
     "Recurrent illness-related encephalopathy is a classic metabolic trajectory. The <b>current episode</b> is the best opportunity for diagnosis: assess and stabilise urgently, check glucose and ketones, and send the first-line metabolic tests while treating the illness.",
     "<b>A</b> &mdash; most IEMs are autosomal recessive; a negative family history is usual. <b>B</b> &mdash; waiting wastes the diagnostic window and risks harm. <b>D</b> &mdash; the history raises a possibility; it does not make a diagnosis.",
     "The best time to diagnose an episodic metabolic disorder is during the episode.",
     "section 1, ‘Begin with the trajectory’"),
   Q("A 7-day-old with poor feeding, jaundice and bleeding has E. coli grown from blood culture. He is on appropriate antibiotics. Which additional consideration is most important?",
     ["None: E. coli sepsis explains all the findings.",
      "Classic galactosaemia, because it can present with liver dysfunction and E. coli sepsis together.",
      "Physiological jaundice, as it is common in the first week.",
      "Congenital hypothyroidism as the sole explanation."],
     1,
     "Which inherited disorder is classically linked with E. coli sepsis in newborns?",
     "The baby has liver dysfunction and bleeding as well as infection. Which diagnosis would explain all three?",
     "Classic galactosaemia can present with jaundice, liver dysfunction, bleeding and <b>E. coli sepsis</b>. Continue antibiotics and discuss urgent specialist-directed removal of lactose while diagnostic samples are taken.",
     "<b>A</b> &mdash; sepsis may explain only part of the picture. <b>C</b> &mdash; physiological jaundice does not cause bleeding or sepsis. <b>D</b> &mdash; hypothyroidism can prolong jaundice but does not explain E. coli sepsis and coagulopathy.",
     "A positive culture can answer only part of the question.",
     "section 4, ‘Keep two explanations open’")]
)

# ------------------------------------------------------------------ UNIT 2
unit(2, "A", "The sick neonate",
  "The newborn has only a few ways to show illness: poor feeding, sleepiness, abnormal breathing, seizures. Sepsis, heart disease, surgical problems and inborn errors all look alike at first, so they must be investigated together.",
  [("e", "Recognise the newborn who was well and then deteriorates."),
   ("e", "Start the first-line metabolic tests in parallel with the sepsis work-up."),
   ("a", "Explain why a pending or normal newborn screen does not reassure in a symptomatic baby."),
   ("x", "Recognise neonatal presentations of urea cycle disorders, organic acidaemias and MSUD.")],
  [
   roles({"ug": "Recognise the well-then-sick timeline, call for help and assist with observation and documentation.",
          "pg": "Send ammonia, glucose, gas, lactate and ketones with the sepsis screen, and escalate an abnormal result the same hour.",
          "fac": "Run the case as a simulation in which the ammonia result is the trigger; debrief on how long it took the team to ask for it."}),
   sec(1, "A well start can precede illness", '''
  <p>Fictional case: <b>Aarav</b> fed normally after an uncomplicated birth. On day 4 he has a weak suck, increasing sleepiness and fast breathing. In intoxication disorders, the placenta clears the toxic metabolite before birth; once feeds begin, it accumulates. <b>A symptom-free interval of hours to days</b> is a clue to keep, not proof.</p>''' + algo("Write the timeline", '''  Birth → normal feeds → first change → now
  day 0        days 1–3       day 4          day 4, 6 h later
  well         feeding well   weak suck      drowsy, fast breathing''')),

   sec(2, "Assess the baby before the label", '''
  <p>Airway, breathing, circulation, neurological state, temperature and <b>glucose</b> come first. A newborn who is hard to wake, feeds poorly or breathes abnormally needs prompt senior review. Fever may be absent in serious infection. Keep sepsis, congenital heart disease (duct-dependent lesions), surgical causes and endocrine emergencies (adrenal crisis) in the same differential.</p>''' + danger('''<p>Never wait for antibiotics to &ldquo;fail&rdquo; before checking ammonia. A baby with unexplained encephalopathy needs an ammonia result within the hour.</p>''')),

   sec(3, "Send the first tests in parallel", table(
     ["Test", "Why it matters now"],
     [["Glucose (bedside, confirmed in lab)", "Treat hypoglycaemia immediately; it also shapes the differential"],
      ["Blood gas with anion gap and lactate", "Acidosis versus respiratory alkalosis points to different disease groups"],
      ["<b>Ammonia</b>", "The single most important time-critical test in an encephalopathic newborn"],
      ["Ketones (blood or urine)", "Ketosis in a newborn is unusual and suggests an organic acidaemia or MSUD"],
      ["Blood count, electrolytes, liver function, clotting, culture", "Sepsis, liver failure and cytopenias guide both pathways"]]) + '''
  <p>Store extra plasma and urine for specialised tests (Unit 5). Do not delay stabilisation for a complete set.</p>'''),

   sec(4, "Do not wait for a signature sign", '''
  <p>MSUD causes feeding difficulty then encephalopathy; the maple-syrup odour is often absent or noticed late. Many classic signs &mdash; odour, cataracts, dysmorphism &mdash; are late or missing. <b>Urgency comes from the baby&rsquo;s state, not from a hallmark.</b> A newborn screening result that is pending, reported normal or never done does not exclude an IEM in a sick baby.</p>''' + tracks(
     ["Ammonia, gas, lactate and ketones available 24 hours, with results in under an hour",
      "Direct phone line to a metabolic consultant and PICU"],
     ["If ammonia is not available on site at night, send it urgently to the nearest laboratory that can run it and call the referral centre at the same time",
      "Start glucose-containing fluids and stop protein feeds while waiting (Unit 4) if a metabolic crisis is suspected",
      "Transfer early: a sick newborn with suspected hyperammonaemia is safer on the road at 250 µmol/L than at 800"]), lvl="a"),
  ],
  [Q("A term baby fed well for 3 days. On day 4 he is drowsy, feeding poorly and breathing fast. Blood culture and antibiotics have been started. Glucose is 3.8 mmol/L. What else should be sent now?",
     ["Nothing more until the culture result is back.",
      "Thyroid function tests only.",
      "Ammonia, blood gas with lactate, and ketones, alongside the sepsis work-up.",
      "A chromosome analysis."],
     2,
     "Which disorders present after a well interval of a few days?",
     "Which single blood test is most time-critical in an encephalopathic newborn?",
     "A well interval followed by encephalopathy is the classic intoxication pattern. Send <b>ammonia</b>, a gas with lactate and ketones now, in parallel with sepsis care. A high ammonia changes management within the hour.",
     "<b>A</b> &mdash; waiting for culture wastes hours in a possible hyperammonaemic crisis. <b>B</b> &mdash; thyroid disease does not cause this acute picture. <b>D</b> &mdash; chromosomes do not answer the urgent question.",
     "In an encephalopathic newborn, ammonia belongs in the first hour.",
     "section 3, ‘Send the first tests in parallel’"),
   Q("A 6-day-old with poor feeding and increasing drowsiness has a newborn screen reported as normal on day 3. What does this mean?",
     ["An IEM is excluded.",
      "Only disorders on the panel with a true-negative result are made less likely; the baby still needs full assessment.",
      "The screen should be repeated before any other test.",
      "Metabolic tests should wait until day 10."],
     1,
     "What can a normal screen not exclude?",
     "Screening panels differ, some disorders present before results, and false negatives occur. What does the baby need now?",
     "A normal screen lowers the probability only of disorders on that panel, and false negatives occur. Many disorders are not screened. A symptomatic baby needs <b>clinical assessment and first-line metabolic tests now</b>.",
     "<b>A</b> &mdash; no screen excludes every IEM. <b>C</b> &mdash; repeating the screen delays urgent tests. <b>D</b> &mdash; waiting is unsafe in a deteriorating newborn.",
     "Screening changes probability; it never replaces assessment of a sick baby.",
     "section 4, ‘Do not wait for a signature sign’")]
)

# ------------------------------------------------------------------ UNIT 3
unit(3, "A", "Read the metabolic pattern",
  "Five bedside results &mdash; glucose, ketones, pH with anion gap, lactate and ammonia &mdash; point to a disease family long before a specialised test returns. Reading them together is the most useful skill in this module.",
  [("e", "Combine acid&ndash;base state, glucose, ketones, lactate and ammonia into one physiological story."),
   ("e", "Calculate the anion gap and interpret it."),
   ("a", "Name a provisional disease family from the pattern, without declaring a diagnosis."),
   ("x", "Identify results that need urgent repetition or laboratory discussion.")],
  [
   roles({"ug": "Calculate the anion gap and describe the pattern in words.",
          "pg": "Match the pattern to a disease family and choose the next discriminating test.",
          "fac": "Give learners the five results as cards and ask for a provisional map with one explicit uncertainty."}),
   sec(1, "The anion gap", algo("Anion gap", '''  Anion gap = Na⁺ − (Cl⁻ + HCO₃⁻)
  Typical reference range about 8–16 mmol/L (check your laboratory;
  some include K⁺ and use a higher range)

  Raised gap   → unmeasured acids: lactate, ketones, organic acids,
                 toxins, renal failure
  Normal gap   → bicarbonate loss (diarrhoea) or renal tubular acidosis''') + '''
  <p>The anion gap reflects unmeasured anions, not a disease. Interpret it with the laboratory&rsquo;s method and reference interval, and with albumin (a low albumin lowers the gap).</p>'''),

   sec(2, "Five patterns worth knowing", fig("pattern", "Reading the first five results", '''  SEND TOGETHER: glucose · ketones · gas with anion gap · lactate · ammonia
  Ammonia high, no acidosis        → urea cycle disorder
  Ammonia high, acidosis, ketones  → organic acidaemia
  Raised-gap acidosis, ketones     → organic acidaemia, MSUD
  Raised lactate                   → mitochondrial, PDH, GSD I (after excluding shock)
  Low glucose, LOW ketones         → fatty-acid oxidation disorder, hyperinsulinism
  Low glucose, HIGH ketones        → ketotic hypoglycaemia, hormone deficiency, GSD 0/III/VI/IX''') + table(
     ["Pattern", "Think first of"],
     [["High ammonia, <b>respiratory alkalosis</b>, no acidosis, normal glucose", "Urea cycle disorder"],
      ["Raised-gap <b>metabolic acidosis</b>, <b>ketosis</b>, &plusmn; high ammonia, low platelets or neutrophils", "Organic acidaemia (methylmalonic, propionic, isovaleric)"],
      ["Encephalopathy, ketosis, little or no acidosis, normal ammonia", "Maple syrup urine disease (MSUD)"],
      ["<b>Hypoglycaemia</b> with <b>low or absent ketones</b>", "Fatty-acid oxidation disorder or hyperinsulinism"],
      ["Hypoglycaemia, <b>lactic acidosis</b>, large liver", "Glycogen storage disease type I or gluconeogenesis defect"],
      ["Persistent raised <b>lactate</b> with normal perfusion", "Mitochondrial or pyruvate metabolism disorder"]]) + '''
  <p>Patterns overlap, and a very sick baby can show several at once. Each pattern narrows the differential; none confirms an enzyme defect.</p>'''),

   sec(3, "Low glucose with too few ketones", '''
  <p>When glucose is low after fasting or illness, the body should be burning fat and making ketones. <b>Inappropriately low ketones</b> mean fat is not being used (fatty-acid oxidation disorder) or insulin is switching fat-burning off (hyperinsulinism). &ldquo;Hypoketotic&rdquo; does not mean zero: interpret the ketone level against how low the glucose is and for how long. Urine ketones being present does not exclude a fatty-acid oxidation disorder.</p>'''),

   sec(4, "Check context before closing the case", '''
  <p>Lactate rises with poor perfusion, seizures, a struggling child or a tourniquet. Ammonia rises falsely with a difficult sample, delayed processing or haemolysis, and truly in liver failure, some drugs (valproate) and sepsis. <b>When a result is implausible, repeat it quickly &mdash; do not dismiss it.</b> An ammonia that is high on a poor sample is still a reason to act while the repeat is done.</p>''' + pearl('''<p>Write three columns: <b>pattern</b> &rarr; <b>plausible mechanisms</b> &rarr; <b>next discriminating test</b>. Revisit it after each result instead of forcing new values to fit the first idea.</p>'''), lvl="a"),
  ],
  [Q("A 4-day-old is drowsy and breathing fast. Blood gas: pH 7.49, PCO₂ 27 mmHg, bicarbonate 20 mmol/L. Glucose is normal and ammonia is markedly raised. Which disease family is most likely?",
     ["Organic acidaemia.",
      "Fatty-acid oxidation disorder.",
      "Glycogen storage disease.",
      "Urea cycle disorder."],
     3,
     "Is this an acidosis or an alkalosis, and is it metabolic or respiratory?",
     "High ammonia stimulates breathing. Which disease family raises ammonia without causing acidosis?",
     "High pH with low PCO₂ is a <b>respiratory alkalosis</b>; ammonia drives hyperventilation. High ammonia <b>without</b> acidosis or hypoglycaemia points first to a <b>urea cycle disorder</b>. Confirmation needs plasma amino acids and urine orotic acid.",
     "<b>A</b> &mdash; organic acidaemias usually cause a raised-gap metabolic acidosis with ketosis. <b>B</b> &mdash; fatty-acid oxidation disorders usually present with hypoketotic hypoglycaemia. <b>C</b> &mdash; glycogen storage disease causes hypoglycaemia with lactic acidosis.",
     "Ammonia with alkalosis: think urea cycle. Ammonia with acidosis and ketones: think organic acid.",
     "section 2, ‘Five patterns worth knowing’"),
   Q("A 20-month-old is found drowsy after a night of vomiting. Glucose is 1.9 mmol/L and blood ketones are 0.3 mmol/L. What does this pattern most suggest?",
     ["A normal fasting response.",
      "Ketotic hypoglycaemia, which is benign.",
      "A fatty-acid oxidation disorder or hyperinsulinism, because ketones are inappropriately low for the glucose.",
      "Glycogen storage disease type I, because the ketones are high."],
     2,
     "What should happen to ketones when a child has been fasting and the glucose is low?",
     "Ketones of 0.3 mmol/L with glucose 1.9 mmol/L after a night of vomiting are far too low. Which two problems stop fat being turned into ketones?",
     "After fasting with glucose this low, ketones should be high. <b>Inappropriately low ketones</b> mean fat is not being used (fatty-acid oxidation disorder such as MCAD deficiency) or insulin is suppressing it (hyperinsulinism). Treat the hypoglycaemia first and take a critical sample if possible.",
     "<b>A</b> &mdash; a normal fasting response makes ketones. <b>B</b> &mdash; ketotic hypoglycaemia has high ketones. <b>D</b> &mdash; ketones here are low, not high.",
     "Read glucose and ketones together; neither means much alone.",
     "section 3, ‘Low glucose with too few ketones’")]
)
