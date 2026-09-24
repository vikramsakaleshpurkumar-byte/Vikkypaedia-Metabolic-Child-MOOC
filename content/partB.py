from gen import *

part("B", "The first hour", "Units 4&ndash;8 · ~7 hours",
     "In a metabolic crisis the diagnosis usually arrives days later; the outcome is often decided in the first hour. This Part is about what to do before you know: stop the toxic load, give glucose, capture the sample that will make the diagnosis, and get the ammonia down.")

# ------------------------------------------------------------------ UNIT 4
unit(4, "B", "The first hour",
  "When a metabolic crisis is suspected, four things happen together: resuscitate, stop the fuel for the toxin, give enough glucose to stop the body breaking itself down, and call for expert help.",
  [("e", "Name the concurrent first-hour priorities in a suspected metabolic crisis."),
   ("e", "Start glucose-containing fluid at a rate that reverses catabolism."),
   ("a", "Explain why protein is stopped for a short time only, and why lipid is not given until a fatty-acid oxidation disorder is excluded."),
   ("x", "Give a complete, closed-loop referral to the metabolic and intensive-care team.")],
  [
   roles({"ug": "Call for help, check glucose, and help with monitoring and documentation as directed.",
          "pg": "Lead the first hour: resuscitation, glucose infusion, stopping feeds, sampling, and the call to the metabolic team.",
          "fac": "Time the scenario: when did glucose start, when was ammonia sent, when was the metabolic team called?"}),
   sec(1, "Four things at once", algo("Suspected metabolic crisis: the first hour", '''  RESUSCITATE     airway, breathing, circulation; treat seizures and shock
  STOP            protein and milk feeds (and lactose/fructose if suspected)
  GLUCOSE         10% glucose IV at a rate that stops catabolism
                  (e.g. 5 mL/kg/h ≈ 8 mg/kg/min in a baby — BIMDG example)
  SAMPLE          ammonia, gas, lactate, ketones, glucose + stored plasma
                  and urine (Unit 5) — do not delay treatment for them
  CALL            metabolic team and PICU/NICU early; plan transfer
  REASSESS        glucose, ammonia, gas and neurology every 1–4 hours''')),

   sec(2, "Why glucose, and how much", '''
  <p>In illness and fasting the body breaks down its own muscle protein and fat for fuel. In an intoxication disorder that <b>catabolism</b> produces more of the toxin; in a fat-oxidation disorder the fat cannot be used. Enough glucose switches catabolism off. A maintenance-strength drip is often not enough.</p>
  <ul>
    <li>Treat hypoglycaemia first: <b>10% glucose 2 mL/kg</b> (200 mg/kg) IV.</li>
    <li>Then 10% glucose with appropriate electrolytes; the BIMDG undiagnosed-hyperammonaemia guideline uses <b>5 mL/kg/h</b> in a baby (about 8 mg/kg/min). Watch fluid balance and cerebral oedema risk, and adjust to the child and the protocol.</li>
    <li>If glucose rises above the target range, the specialist team may add insulin rather than reduce glucose.</li>
  </ul>''' + pitfall('''<p>Running 0.9% saline or a maintenance-strength drip &ldquo;until we know&rdquo;. It rehydrates without stopping catabolism, and in intoxication disorders the toxin keeps rising.</p>''')),

   sec(3, "Protein, lipid and the emergency letter", '''
  <ul>
    <li><b>Stop protein</b> when an intoxication disorder is suspected, but for a short time: prolonged protein restriction (more than 24&ndash;48 hours) causes the body to break down its own protein. The metabolic team reintroduces it.</li>
    <li><b>Do not give IV lipid</b> until a fatty-acid oxidation disorder has been excluded; in other disorders the team may add it for calories.</li>
    <li><b>Known diagnosis?</b> Find the child&rsquo;s emergency letter or regimen, confirm it is current, and follow it. Families often carry it; ask.</li>
  </ul>'''),

   sec(4, "Close the communication loop", '''
  <p>A useful call says: who the child is; current airway, breathing, circulation and neurological state; timed results with units; what has been given and when; and <b>what you need</b> (advice, drugs, transfer, dialysis). Read back the plan and name who owns each task. A referral is incomplete until somebody accepts responsibility.</p>''' + tracks(
     ["On-site metabolic team, PICU, dialysis and specialist drugs",
      "Ammonia, gas and lactate repeated every 2&ndash;4 hours"],
     ["Start glucose and stop feeds before transfer; do not wait for confirmation",
      "Phone the referral centre early; ask which specialist drugs they want started and whether you hold them",
      "Send stored plasma and urine with the child, labelled with collection times and what treatment preceded them"]), lvl="a"),
  ],
  [Q("A 5-day-old with suspected hyperammonaemia is on 0.9% saline at maintenance rate while the team waits for the ammonia result. Glucose is 4.2 mmol/L. What should change first?",
     ["Nothing until the ammonia result returns.",
      "Change to 10% glucose at a rate that reverses catabolism, stop protein feeds and call the metabolic team.",
      "Start full-strength milk feeds to provide calories.",
      "Start IV lipid for calories before anything else."],
     1,
     "What drives toxin production in an intoxication disorder during illness?",
     "Saline does not stop catabolism. What does, and what else should stop?",
     "Catabolism produces more toxin. Switch to <b>10% glucose</b> at a rate that stops it (for example 5 mL/kg/h in a baby, per BIMDG), <b>stop protein</b> for a short period, and call the metabolic team without waiting for the result.",
     "<b>A</b> &mdash; waiting loses hours while ammonia rises. <b>C</b> &mdash; milk feeds provide the protein load that drives the toxin. <b>D</b> &mdash; IV lipid is not given until a fatty-acid oxidation disorder is excluded, and it does not replace glucose.",
     "In a suspected metabolic crisis, glucose is treatment, not just fluid.",
     "section 2, ‘Why glucose, and how much’"),
   Q("A 3-year-old with known MSUD is vomiting and drowsy in the emergency room. His mother has a letter from the metabolic centre. What is the best first step after assessing ABC?",
     ["Ignore the letter and follow the general paediatric fluid protocol.",
      "Read the letter, confirm it is current, follow its emergency regimen and call the named metabolic team.",
      "Give oral fluids and observe for 6 hours.",
      "Stop all nutrition for 72 hours."],
     1,
     "Who knows this child's disorder best?",
     "The emergency letter is written for exactly this moment. What should you do with it?",
     "The emergency letter is the child&rsquo;s individual first-hour plan. Confirm it is current, start the regimen (usually IV glucose and a stop to protein), and call the named team.",
     "<b>A</b> &mdash; general protocols do not account for the disorder. <b>C</b> &mdash; a vomiting, drowsy child needs IV treatment now. <b>D</b> &mdash; prolonged withdrawal of protein and calories worsens catabolism.",
     "When a family brings an emergency letter, read it first.",
     "section 3, ‘Protein, lipid and the emergency letter’")]
)

# ------------------------------------------------------------------ UNIT 5
unit(5, "B", "Send the right sample",
  "The biochemistry during a crisis is often the only chance to make a diagnosis; hours later, after glucose, it may look normal. A critical sample taken in the first minutes can save a child years of uncertainty.",
  [("e", "Explain what a critical sample is and why it is time-sensitive."),
   ("e", "Collect ammonia correctly and recognise sources of false results."),
   ("a", "Match specialised tests (amino acids, acylcarnitines, urine organic acids) to the question."),
   ("x", "Document timing and treatment so that results can be interpreted.")],
  [
   roles({"ug": "Know the critical-sample list and label every sample with the time and what treatment preceded it.",
          "pg": "Assign sampling to one team member, agree tests with the laboratory, and own the results.",
          "fac": "Audit rejected and unlabelled metabolic samples in your unit and teach from them."}),
   sec(1, "The critical sample", table(
     ["Blood (during the episode)", "Urine (first passed after the episode starts)"],
     [["Glucose, blood gas, lactate, <b>ammonia</b>", "Ketones (dipstick)"],
      ["Beta-hydroxybutyrate (ketones) and free fatty acids", "Organic acids"],
      ["Insulin, C-peptide, cortisol, growth hormone (if hypoglycaemic)", "Amino acids, orotic acid (if ammonia high)"],
      ["Plasma amino acids; dried blood spot acylcarnitine profile", "Reducing substances (if galactosaemia suspected)"],
      ["<b>Extra plasma or serum stored</b> (separated, frozen per laboratory instruction)", "<b>Extra urine stored</b> frozen"]]) + danger('''<p>Never delay treatment of hypoglycaemia, seizures or shock to collect a sample. Take what you can in the first minutes; a partial, well-labelled set is still valuable.</p>''')),

   sec(2, "Ammonia: a sample that lies easily", '''
  <ul>
    <li>Free-flowing sample, <b>no prolonged tourniquet</b>; arterial or venous per local practice.</li>
    <li>Tube type per your laboratory; <b>on ice, to the laboratory within about 15&ndash;30 minutes</b>, processed promptly.</li>
    <li>Haemolysis, delay, a warm sample and a squeezed heel-prick all raise the value falsely.</li>
    <li>Call ahead so the laboratory knows it is urgent, and name who receives the result.</li>
  </ul>''' + pitfall('''<p>&ldquo;It was probably a bad sample.&rdquo; Repeat it immediately &mdash; but act on a high value in a sick child while you wait for the repeat.</p>''')),

   sec(3, "Match the test to the question", table(
     ["Test", "Main question it answers"],
     [["Plasma amino acids", "Urea cycle disorders (citrulline, arginine), MSUD (leucine, alloisoleucine), glycine and other amino acid disorders"],
      ["Acylcarnitine profile (blood spot)", "Fatty-acid oxidation disorders, organic acidaemias"],
      ["Urine organic acids", "Organic acidaemias, some FAODs; many other disorders"],
      ["Urine orotic acid", "Separates OTC deficiency (high) from CPS1/NAGS deficiency (low or normal)"],
      ["Succinylacetone (blood or urine)", "Tyrosinaemia type I"]]) + '''
  <p>Ask for named tests. &ldquo;Metabolic screen&rdquo; means different things in different laboratories.</p>'''),

   sec(4, "Label, document, track", '''
  <p>Each sample needs the time taken, the child&rsquo;s state (well, fasting, in crisis) and what treatment came before it (glucose, carnitine, blood transfusion, feeds). Profiles can normalise after treatment; a normal report taken after 24 hours of glucose does not erase a compelling episode.</p>''' + india('''<p>Specialised tests are often sent to a referral laboratory by courier. Agree in advance the container, volume, freezing and transport, and whether the laboratory accepts dried blood spots (which travel well and are cheap). Many state and private laboratories accept filter-paper spots for acylcarnitines and amino acids. Keep a laminated sample card in the emergency room and NICU.</p>'''), lvl="a"),
  ],
  [Q("A 2-year-old arrives drowsy with glucose 1.8 mmol/L. The team wants a critical sample. What is the correct sequence?",
     ["Collect the full critical sample, wait for it to go to the laboratory, then give glucose.",
      "Draw the blood for the critical sample while the IV line is placed, give 10% glucose 2 mL/kg immediately, and save the first urine.",
      "Give glucose and take the critical sample 4 hours later when she is stable.",
      "Skip the sample, as the diagnosis can be made later."],
     1,
     "What does a critical sample capture, and what must never be delayed?",
     "The blood can come from the same cannulation. What happens to the biochemistry after glucose?",
     "Take blood for the critical sample from the cannula as it is placed, then give <b>10% glucose 2 mL/kg</b> immediately. Save the first urine. The sample captures the biochemistry of the episode; treatment is never delayed for it.",
     "<b>A</b> &mdash; delaying glucose risks brain injury. <b>C</b> &mdash; four hours of glucose may normalise the diagnostic findings. <b>D</b> &mdash; the episode may be the only chance to make the diagnosis.",
     "Sample during the crisis, not after it &mdash; but never instead of treating it.",
     "section 1, ‘The critical sample’"),
   Q("An ammonia sample from a drowsy newborn was taken by heel-prick, squeezed, and reached the laboratory 2 hours later. It reads 190 µmol/L. What should happen?",
     ["Dismiss it as artefact.",
      "Repeat it immediately as a free-flowing sample on ice, processed promptly, and keep treating the baby's condition in the meantime.",
      "Wait 24 hours and repeat.",
      "Start dialysis immediately on this value."],
     1,
     "What raises ammonia falsely?",
     "The sample was squeezed and delayed, so it may be falsely high &mdash; or it may be true. What is safe?",
     "Squeezing and delay raise ammonia falsely, but a sick baby may also truly have hyperammonaemia. <b>Repeat immediately</b> with a correct sample and continue assessment and supportive treatment while waiting.",
     "<b>A</b> &mdash; dismissing it risks missing a urea cycle disorder. <b>C</b> &mdash; 24 hours is far too long. <b>D</b> &mdash; dialysis is decided on a reliable value and the trend, not a doubtful sample.",
     "An implausible ammonia gets repeated now, not ignored.",
     "section 2, ‘Ammonia: a sample that lies easily’")]
)

# ------------------------------------------------------------------ UNIT 6
unit(6, "B", "Hyperammonaemia",
  "Ammonia is directly toxic to the brain, and the damage depends on how high it goes and for how long. Every hour at a high level matters, which is why the response has to be organised before the diagnosis is known.",
  [("e", "Recognise the symptoms of hyperammonaemia and when to measure ammonia."),
   ("e", "Know the ammonia levels that demand urgent action and transfer."),
   ("a", "Describe the emergency treatment: stop protein, glucose, nitrogen scavengers, arginine, carglumic acid."),
   ("x", "Recognise when extracorporeal removal (haemofiltration or dialysis) is needed.")],
  [
   roles({"ug": "Recognise encephalopathy, vomiting and fast breathing as reasons to check ammonia.",
          "pg": "Start the emergency protocol with the metabolic team and organise transfer for dialysis early.",
          "fac": "Check that the unit has the scavenger drugs, a protocol and a dialysis referral route before the first case arrives."}),
   sec(1, "Think ammonia early", '''
  <p>Symptoms: poor feeding, vomiting, lethargy, irritability, <b>fast breathing</b> (central hyperventilation), seizures, abnormal posturing, coma. In a newborn the picture often looks like sepsis. In older children: episodic vomiting, ataxia, confusion or behavioural change after a protein load or illness, sometimes labelled as psychiatric or &ldquo;cyclical vomiting&rdquo;.</p>''' + table(
     ["Ammonia (µmol/L)", "Action (BIMDG undiagnosed hyperammonaemia, 2016)"],
     [["Above 150 in a child, or above 200 in a neonate", "Repeat immediately; start the emergency plan while waiting"],
      ["Above 200", "Urgent treatment and discussion with a metabolic centre"],
      ["Above 250", "Arrange transfer to a specialist centre as soon as possible"]]) + '''
  <p>Normal reference ranges are usually below about 50 µmol/L in older children and higher in newborns; check your laboratory.</p>'''),

   sec(2, "Emergency treatment", table(
     ["Step", "Detail (BIMDG 2016 examples; follow your centre&rsquo;s protocol)"],
     [["Stop protein", "For 24&ndash;48 hours at most, then the metabolic team reintroduces it"],
      ["Glucose", "10% glucose 2 mL/kg, then 10% glucose infusion (e.g. 5 mL/kg/h in a baby); insulin if hyperglycaemic"],
      ["Sodium benzoate IV", "Loading 250 mg/kg over 90 minutes, then 250 mg/kg/day (max 500 mg/kg/day)"],
      ["Sodium phenylbutyrate (or phenylacetate)", "Loading 250 mg/kg, then 250 mg/kg/day (max 600 mg/kg/day)"],
      ["Arginine IV", "Loading 150 mg/kg, then 300 mg/kg/day (max 500 mg/kg/day); not in arginase deficiency"],
      ["Carglumic acid (oral/NG)", "Consider a single dose of 250 mg/kg (BIMDG); used in NAGS deficiency and some organic acidaemias"]]) + evidence('''<p>Doses and thresholds differ slightly between protocols (GeneReviews 2025 gives arginine 200&ndash;250 mg/kg as the loading dose). Use one protocol consistently, agreed with your metabolic centre, and prepare the drugs in advance: they are rarely stocked in district hospitals.</p>''')),

   sec(3, "When drugs are not enough", '''
  <p>If ammonia remains high or rises despite treatment &mdash; for example, above about 250 µmol/L and not falling within about 3 hours &mdash; or the child is deeply encephalopathic, <b>extracorporeal removal</b> is needed. High-dose continuous kidney replacement therapy is now preferred; peritoneal dialysis is much slower and used only when nothing else is available.</p>''' + danger('''<p>Exchange transfusion does not clear ammonia effectively. Do not waste hours on it. Organise transfer to a centre that can do haemofiltration or haemodialysis, with scavenger drugs and glucose running on the way.</p>''')),

   sec(4, "Use the pattern, then confirm", '''
  <p>High ammonia with respiratory alkalosis suggests a urea cycle disorder; with acidosis and ketosis, an organic acidaemia; with liver failure, a primary liver problem. Plasma amino acids (citrulline, arginine), urine orotic acid, acylcarnitines and urine organic acids separate them. OTC deficiency is X-linked: girls can be affected, and mothers may have been symptomatic without a diagnosis.</p>''' + india('''<p>Few district hospitals stock sodium benzoate, phenylbutyrate or carglumic acid, and ammonia assays may not run overnight. Know where your nearest stock and dialysis-capable PICU are before you need them. Oral sodium benzoate is cheaper and more often available than IV forms; the metabolic team can advise on using it by nasogastric tube while transfer is arranged.</p>'''), lvl="a"),
  ],
  [Q("A 4-day-old has an ammonia of 480 µmol/L on a correctly taken sample. He is encephalopathic. The district hospital has no dialysis. What is the best plan?",
     ["Give an exchange transfusion and observe.",
      "Stop protein, start 10% glucose, give available scavenger drugs as advised, and transfer urgently to a centre that can do haemofiltration or dialysis.",
      "Start a low-protein formula and repeat ammonia tomorrow.",
      "Give IV lipid and wait for plasma amino acid results."],
     1,
     "What level of ammonia needs transfer, and what clears ammonia fastest?",
     "At 480 µmol/L with encephalopathy, drugs alone are unlikely to be enough. Where must this baby be?",
     "Ammonia of 480 µmol/L with encephalopathy is an emergency. Start glucose, stop protein, give scavenger drugs (sodium benzoate, arginine) as the metabolic team advises, and <b>transfer urgently</b> to a centre that can do haemofiltration or dialysis.",
     "<b>A</b> &mdash; exchange transfusion does not clear ammonia effectively. <b>C</b> &mdash; feeding protein and waiting a day risks severe brain injury. <b>D</b> &mdash; waiting for amino acids delays life-saving treatment.",
     "High ammonia is a transfer decision, not an overnight observation.",
     "section 3, ‘When drugs are not enough’"),
   Q("A 7-year-old girl has recurrent episodes of vomiting, confusion and ataxia after protein-rich meals. Between episodes she is well. Her ammonia during an episode is 210 µmol/L with a normal pH. Which diagnosis should be considered, and why?",
     ["Cyclical vomiting syndrome, because she is well between episodes.",
      "OTC deficiency, because this X-linked urea cycle disorder can present later and in girls.",
      "Migraine, because the episodes are recurrent.",
      "Classic PKU, because it causes acute encephalopathy."],
     1,
     "Can urea cycle disorders present in older children and in girls?",
     "Protein triggers, high ammonia and a normal pH. Which X-linked disorder fits?",
     "Recurrent protein-triggered encephalopathy with hyperammonaemia and a normal pH suggests a partial <b>urea cycle disorder</b>. OTC deficiency is X-linked, but heterozygous girls can be affected. Check urine orotic acid and plasma amino acids, and ask about the mother&rsquo;s protein aversion or symptoms.",
     "<b>A</b> &mdash; cyclical vomiting is a diagnosis of exclusion; ammonia must be checked. <b>C</b> &mdash; migraine does not raise ammonia. <b>D</b> &mdash; PKU does not cause acute hyperammonaemic crises.",
     "In an older child with episodic encephalopathy, check ammonia during the episode.",
     "section 4, ‘Use the pattern, then confirm’")]
)

# ------------------------------------------------------------------ UNIT 7
unit(7, "B", "Acidosis and the organic acidaemias",
  "A raised-gap metabolic acidosis in a sick newborn with ketones is an organic acidaemia until proved otherwise. The acidosis is only part of it: the same crisis can bring high ammonia, low platelets and a failing heart.",
  [("e", "Confirm and characterise metabolic acidosis with the anion gap."),
   ("e", "Recognise the organic acidaemia pattern: raised-gap acidosis, ketosis, &plusmn; high ammonia and cytopenias."),
   ("a", "Describe emergency treatment, including carnitine and a hydroxocobalamin trial."),
   ("x", "Recognise MSUD and pyruvate disorders as different acidosis stories.")],
  [
   roles({"ug": "Calculate the anion gap and name the pattern that suggests an organic acidaemia.",
          "pg": "Start emergency treatment, send the discriminating tests, and watch for cardiac, pancreatic and haematological complications.",
          "fac": "Use a case with a normal glucose and high ketones to show that ketosis in a newborn is abnormal."}),
   sec(1, "The organic acidaemia pattern", '''
  <p>Methylmalonic (MMA), propionic (PA) and isovaleric acidaemia (IVA) are the commonest. The typical neonate: well interval, then vomiting, poor feeding, lethargy, fast breathing and coma.</p>
  <ul>
    <li>Raised-gap <b>metabolic acidosis</b> with <b>ketosis</b> (ketones in a newborn are always worth noticing).</li>
    <li>Often <b>hyperammonaemia</b>, sometimes very high.</li>
    <li><b>Neutropenia, thrombocytopenia</b>, hypocalcaemia, hypo- or hyperglycaemia.</li>
    <li>Isovaleric acidaemia: &ldquo;sweaty feet&rdquo; odour (often absent).</li>
  </ul>'''),

   sec(2, "Emergency treatment", table(
     ["Step", "Detail"],
     [["Glucose and stop protein", "As in Unit 4; high-energy glucose infusion, insulin if needed"],
      ["L-carnitine IV", "Commonly 100 mg/kg/day (specialist protocol); binds toxic organic acids"],
      ["Hydroxocobalamin", "In suspected MMA, 1 mg IM daily to test for vitamin B12 responsiveness (per metabolic team)"],
      ["Biotin", "If multiple carboxylase deficiency is possible (e.g. 10 mg/day), per metabolic team"],
      ["Carglumic acid", "Can reduce hyperammonaemia in MMA and PA"],
      ["Extracorporeal removal", "For severe hyperammonaemia or refractory acidosis"]]) + pitfall('''<p>Repeated large bicarbonate boluses to &ldquo;correct the gas&rdquo;. The acid keeps coming until catabolism is switched off; glucose, and removal of the toxin, fix the acidosis. Bicarbonate has a limited role under specialist guidance.</p>''')),

   sec(3, "Not every acidosis is the same", table(
     ["Disorder", "Distinguishing features"],
     [["<b>MSUD</b>", "Encephalopathy with ketosis, often little acidosis, normal ammonia; maple-syrup odour; raised leucine and alloisoleucine"],
      ["<b>Pyruvate dehydrogenase / carboxylase deficiency</b>", "Persistent lactic acidosis; brain malformations; ketones depend on the defect"],
      ["<b>Ketone utilisation defects</b>", "Severe recurrent ketoacidosis with normal glucose"],
      ["<b>Acquired causes</b>", "Sepsis, shock, poisoning, renal failure, diarrhoea (normal gap)"]])),

   sec(4, "Complications to watch for", '''
  <p>Children with MMA and PA can develop <b>cardiomyopathy</b>, arrhythmia (prolonged QT in PA), <b>pancreatitis</b>, basal ganglia stroke during crises, and chronic kidney disease (MMA). A child with a known organic acidaemia and abdominal pain needs lipase; a child with breathlessness needs an echo.</p>''' + india('''<p>In Indian series, MMA and PA are among the more frequently diagnosed organic acidaemias, and many are diagnosed late after repeated &ldquo;sepsis&rdquo; admissions. Vitamin B12-responsive forms exist, and maternal B12 deficiency can cause raised methylmalonic acid in infants: check maternal and infant B12 before accepting an inherited diagnosis.</p>'''), lvl="a"),
  ],
  [Q("A 6-day-old is lethargic and breathing fast. Blood gas: pH 7.12, bicarbonate 8 mmol/L, anion gap 28 mmol/L. Blood ketones are high, ammonia is 320 µmol/L and platelets are 60 × 10⁹/L. Which disease group is most likely?",
     ["Urea cycle disorder.",
      "Organic acidaemia.",
      "Fatty-acid oxidation disorder.",
      "Glycogen storage disease."],
     1,
     "Is there a metabolic acidosis, and are ketones present?",
     "Raised-gap acidosis, ketosis, high ammonia and low platelets together. Which group causes all four?",
     "Raised-gap acidosis with <b>ketosis</b>, hyperammonaemia and thrombocytopenia is the classic <b>organic acidaemia</b> pattern (MMA, PA, IVA). Confirm with urine organic acids and acylcarnitines.",
     "<b>A</b> &mdash; urea cycle disorders usually cause respiratory alkalosis, not ketoacidosis. <b>C</b> &mdash; FAODs cause hypoketotic hypoglycaemia. <b>D</b> &mdash; GSD causes hypoglycaemia with lactic acidosis, not this picture.",
     "Ketoacidosis plus high ammonia in a newborn: think organic acidaemia.",
     "section 1, ‘The organic acidaemia pattern’"),
   Q("A 2-year-old with propionic acidaemia on regular follow-up presents with severe epigastric pain and vomiting. His ammonia and gas are only mildly abnormal. What must be checked?",
     ["Nothing further; this is a mild decompensation.",
      "Serum lipase or amylase, for acute pancreatitis.",
      "Urine for reducing substances.",
      "Thyroid function."],
     1,
     "Which complications occur in organic acidaemias?",
     "Epigastric pain and vomiting in a child with PA. Which organ is often involved?",
     "Acute <b>pancreatitis</b> is a recognised complication of organic acidaemias and can occur without a severe metabolic crisis. Check lipase or amylase.",
     "<b>A</b> &mdash; missing pancreatitis can be fatal. <b>C</b> &mdash; reducing substances relate to galactosaemia. <b>D</b> &mdash; thyroid disease does not explain acute abdominal pain.",
     "Know the complications of the disorders you manage.",
     "section 4, ‘Complications to watch for’")]
)

# ------------------------------------------------------------------ UNIT 8
unit(8, "B", "Hypoglycaemia",
  "Low glucose is a symptom, not a diagnosis. The body's response to it &mdash; whether it makes ketones, lactate or insulin &mdash; tells you which fuel pathway has failed.",
  [("e", "Treat hypoglycaemia immediately and take a critical sample when possible."),
   ("e", "Interpret glucose with ketones, lactate and liver size."),
   ("a", "Distinguish fatty-acid oxidation disorders, glycogen storage disease, gluconeogenesis defects and hyperinsulinism."),
   ("x", "Plan fasting avoidance and a sick-day regimen without provoking a fast.")],
  [
   roles({"ug": "Treat hypoglycaemia at once and know the critical-sample list.",
          "pg": "Interpret the critical sample and plan fasting safety with the metabolic team and dietitian.",
          "fac": "Teach the fuel map: glycogen first, then gluconeogenesis, then fat and ketones."}),
   sec(1, "Treat first", '''
  <p>IV: <b>10% glucose 2 mL/kg</b> (200 mg/kg), then a glucose infusion; recheck in 15&ndash;30 minutes. If no IV access and the child is conscious, oral glucose. Take the critical sample (Unit 5) as the line goes in, and save the first urine.</p>''' + pearl('''<p>Glucagon raises glucose only if liver glycogen is present and releasable &mdash; a good response suggests hyperinsulinism; no response is expected in glycogen storage disease type I and in prolonged fasting.</p>''')),

   sec(2, "The fuel map", algo("How the body keeps glucose up", '''  0–4 h after a meal     absorbed glucose
  up to ~12–24 h         liver GLYCOGEN broken down        (fails in GSD)
  hours onward           GLUCONEOGENESIS from lactate,
                         amino acids, glycerol             (fails in FBPase deficiency, GSD I)
  longer fasts/illness   FAT → fatty-acid oxidation → KETONES   (fails in FAODs)
  insulin switches off glycogen breakdown, gluconeogenesis and ketone production
  (younger children reach each stage sooner)''')),

   sec(3, "Read the critical sample", table(
     ["Ketones", "Lactate", "Liver", "Think of"],
     [["<b>Low</b>", "Normal", "Normal or large", "Fatty-acid oxidation disorder (e.g. MCAD); hyperinsulinism if insulin detectable and glucose need high"],
      ["<b>Low</b>", "Normal", "Normal", "Hyperinsulinism (glucose requirement often above 8 mg/kg/min)"],
      ["Low or normal", "<b>High</b>", "<b>Large</b>", "Glycogen storage disease type I; gluconeogenesis defect"],
      ["<b>High</b>", "Normal", "Normal", "Ketotic hypoglycaemia, cortisol or growth hormone deficiency, GSD types 0, III, VI, IX"]]) + '''
  <p>Interpret &ldquo;low&rdquo; ketones against how low the glucose was and how long the fast was.</p>'''),

   sec(4, "Prevention is the treatment", '''
  <p>Most fuel disorders are managed by <b>avoiding fasting</b>: age-appropriate maximum fasting times, regular feeds, and a <b>sick-day regimen</b> of glucose-polymer drinks when the child is unwell (the BIMDG regimens use concentrations rising with age, from 10% in infants to 25% from 10 years). If the drinks are vomited or refused, or the child becomes drowsy, the child needs IV glucose in hospital immediately.</p>''' + danger('''<p>Never do a diagnostic fast outside a specialist unit with a protocol. Children with fatty-acid oxidation disorders have died during unsupervised fasting tests.</p>''') + india('''<p>Glucose-polymer powder may be unavailable or costly. The metabolic dietitian can convert the regimen to locally available glucose powder with measured scoops, and families need a written recipe and a clear rule for when to come to hospital. Long travel times mean the threshold for coming in should be lower, not higher.</p>'''), lvl="a"),
  ],
  [Q("A 14-month-old with a 2-day history of vomiting is found unresponsive. Glucose is 1.5 mmol/L. The IV cannula has just been placed. What should be done?",
     ["Wait for the critical sample results before giving glucose.",
      "Draw the critical sample from the cannula, give 10% glucose 2 mL/kg IV at once, then start a glucose infusion and recheck.",
      "Give 50% glucose 5 mL/kg IV.",
      "Give oral glucose gel to the unresponsive child."],
     1,
     "What is the IV dose of glucose for hypoglycaemia in a child?",
     "The sample can be taken from the new cannula without delay. Which concentration is safe for a peripheral vein?",
     "Take the critical sample from the new cannula and immediately give <b>10% glucose 2 mL/kg</b> (200 mg/kg), then an infusion. Recheck glucose in 15&ndash;30 minutes.",
     "<b>A</b> &mdash; treatment is never delayed for results. <b>C</b> &mdash; 50% glucose is hyperosmolar, damages veins and overshoots. <b>D</b> &mdash; oral gel is unsafe in an unresponsive child.",
     "Sample and treat in the same minute.",
     "section 1, ‘Treat first’"),
   Q("A 10-month-old has fasting hypoglycaemia, a large liver, a doll-like face and a raised lactate and triglycerides. Glucagon given during an episode does not raise the glucose. What is the most likely diagnosis?",
     ["MCAD deficiency.",
      "Hyperinsulinism.",
      "Glycogen storage disease type I.",
      "Ketotic hypoglycaemia."],
     2,
     "Which disorder combines hypoglycaemia with lactic acidosis and a large liver?",
     "No response to glucagon means glycogen cannot be released as glucose. Which enzyme defect causes that?",
     "Hepatomegaly, hypoglycaemia, <b>lactic acidosis</b>, raised triglycerides and no response to glucagon fit <b>glycogen storage disease type I</b> (glucose-6-phosphatase deficiency).",
     "<b>A</b> &mdash; MCAD deficiency causes hypoketotic hypoglycaemia without a large liver or high lactate. <b>B</b> &mdash; hyperinsulinism usually responds to glucagon. <b>D</b> &mdash; ketotic hypoglycaemia has high ketones and a normal liver.",
     "Large liver plus high lactate plus low glucose: think GSD type I.",
     "section 3, ‘Read the critical sample’")]
)
