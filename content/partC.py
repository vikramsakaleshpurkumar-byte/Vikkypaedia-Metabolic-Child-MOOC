from gen import *

part("C", "Presentations by system", "Units 9&ndash;13 · ~7 hours",
     "Outside the neonatal crisis, inborn errors usually arrive through one organ: weak muscles, a large liver, seizures that will not stop, abnormal movements, or a child who is losing skills. This Part starts with that organ and asks which metabolic questions it should raise &mdash; especially the ones with treatments.")

# ------------------------------------------------------------------ UNIT 9
unit(9, "C", "Muscle, heart and fatty-acid oxidation",
  "Fasting, fever and exercise are stress tests of the body's fuel supply. A child who collapses, gets rhabdomyolysis or develops cardiomyopathy under that stress may have a fatty-acid oxidation disorder.",
  [("e", "Recognise presentations of fatty-acid oxidation disorders (FAODs) at different ages."),
   ("e", "Link fasting, fever and exercise triggers to fuel failure."),
   ("a", "Assess heart, muscle and kidneys together in an acute episode."),
   ("x", "Recognise infantile Pompe disease as a weak baby with a large heart.")],
  [
   roles({"ug": "Ask about the last meal, fever, exercise and dark urine in any child with weakness or collapse.",
          "pg": "Send the acute sample, check CK, renal function and echo, and avoid IV lipid until FAOD is excluded.",
          "fac": "Teach through a sudden unexpected death case: what questions would have changed the outcome for the next sibling?"}),
   sec(1, "Triggers reveal the fuel problem", '''
  <ul>
    <li><b>Infancy:</b> hypoketotic hypoglycaemia, encephalopathy, liver dysfunction, cardiomyopathy, arrhythmia, sudden death, often after a fast or intercurrent illness.</li>
    <li><b>MCAD deficiency</b> (the commonest FAOD in many populations): previously well child, becomes drowsy with vomiting after poor intake; hypoketotic hypoglycaemia; can be fatal in the first episode.</li>
    <li><b>Long-chain disorders</b> (VLCAD, LCHAD, CPT2): cardiomyopathy and liver disease in infants; exercise- or illness-induced muscle pain and <b>rhabdomyolysis</b> in older children.</li>
  </ul>''' + pearl('''<p>LCHAD deficiency in the fetus is associated with maternal acute fatty liver of pregnancy or HELLP syndrome. Ask the mother.</p>''')),

   sec(2, "The acute episode", table(
     ["Check", "Why"],
     [["Glucose and ketones", "Hypoketotic hypoglycaemia"],
      ["CK, urine myoglobin, potassium, creatinine", "Rhabdomyolysis threatens the kidneys and heart"],
      ["ECG and echocardiogram", "Cardiomyopathy and arrhythmia"],
      ["Liver function, ammonia", "Liver involvement"],
      ["Acylcarnitine profile, urine organic acids", "Diagnostic during the episode; can normalise afterwards"]]) + danger('''<p>Treat with IV glucose at a rate that stops fat breakdown. <b>Do not give IV lipid</b> to a child with a suspected long-chain FAOD. Give generous fluids for rhabdomyolysis and watch potassium.</p>''')),

   sec(3, "A weak baby with a large heart", '''
  <p><b>Infantile-onset Pompe disease</b> (a lysosomal glycogen storage disorder): hypotonia, weakness, feeding and breathing difficulty, large tongue, and <b>hypertrophic cardiomyopathy</b>, often with a short PR interval and huge QRS complexes on ECG. CK is often raised. Enzyme assay (dried blood spot) and genetic testing confirm it. Enzyme replacement therapy works best when started early, so a delay of months matters.</p>'''),

   sec(4, "Prevention is individual", '''
  <p>Long-term care avoids fasting, provides a sick-day plan, and for some long-chain disorders uses special fat formulas; the plan depends on the exact disorder, age and heart. Families need a written emergency letter.</p>''' + india('''<p>Sudden unexplained infant deaths are rarely investigated in India. If a sibling died suddenly after a brief illness, ask about it, and consider acylcarnitine testing of the living child. Pompe disease is one of the rare diseases for which enzyme replacement may be supported under the National Policy for Rare Diseases through Centres of Excellence (Unit 19); refer early.</p>'''), lvl="a"),
  ],
  [Q("A 12-year-old has dark brown urine and severe muscle pain after a long football match on a day he skipped lunch. CK is 85,000 U/L. He had a similar episode after a fever last year. What is the most likely underlying problem?",
     ["Muscle strain from overexertion only.",
      "A long-chain fatty-acid oxidation disorder such as CPT2 deficiency.",
      "MCAD deficiency presenting with hypoglycaemia.",
      "Duchenne muscular dystrophy."],
     1,
     "Which disorders cause recurrent rhabdomyolysis triggered by exercise, fasting or fever?",
     "Recurrent episodes with fasting plus exercise, and normal between them. Which fuel pathway fails?",
     "Recurrent <b>rhabdomyolysis</b> triggered by prolonged exercise, fasting or fever suggests a long-chain FAOD, commonly <b>CPT2 deficiency</b> or VLCAD deficiency. Treat the rhabdomyolysis (fluids, potassium, renal function) and send acylcarnitines.",
     "<b>A</b> &mdash; recurrent rhabdomyolysis with fever is not simple strain. <b>C</b> &mdash; MCAD deficiency typically causes hypoketotic hypoglycaemia, not rhabdomyolysis. <b>D</b> &mdash; Duchenne causes progressive weakness and constantly high CK, not episodic triggered attacks.",
     "Recurrent rhabdomyolysis is a metabolic question.",
     "section 1, ‘Triggers reveal the fuel problem’"),
   Q("A 3-month-old is floppy, feeds slowly and breathes fast. He has a large tongue. The chest X-ray shows a large heart and the ECG shows a short PR interval with very large QRS complexes. What should be arranged?",
     ["Repeat review in 3 months.",
      "An acid-alpha glucosidase enzyme assay for Pompe disease, with urgent cardiology and metabolic referral.",
      "A sweat test.",
      "A muscle biopsy before any other test."],
     1,
     "Which disorder combines hypotonia with hypertrophic cardiomyopathy in infancy?",
     "Large tongue, short PR and huge QRS complexes point to one lysosomal disorder. How is it confirmed quickly?",
     "Hypotonia with <b>hypertrophic cardiomyopathy</b>, macroglossia and a short PR interval suggests <b>infantile Pompe disease</b>. A dried blood spot enzyme assay and genetic testing confirm it; early enzyme replacement changes outcomes.",
     "<b>A</b> &mdash; delay worsens outcomes in infantile Pompe disease. <b>C</b> &mdash; a sweat test is for cystic fibrosis. <b>D</b> &mdash; muscle biopsy is rarely needed now; the blood enzyme test is faster and non-invasive.",
     "A floppy baby with a big heart needs a Pompe test.",
     "section 3, ‘A weak baby with a large heart’")]
)

# ------------------------------------------------------------------ UNIT 10
unit(10, "C", "The liver",
  "Galactosaemia, hereditary fructose intolerance and tyrosinaemia type I all injure the liver, and all have treatments. The history of what the child has eaten, and when, is often the diagnosis.",
  [("e", "Recognise metabolic red flags in neonatal and infant liver disease."),
   ("e", "Link the timing of lactose, fructose or sucrose exposure to symptoms."),
   ("a", "Know the urgent first steps for suspected galactosaemia and tyrosinaemia type I."),
   ("x", "Recognise Wilson disease in the older child with liver and neurological signs.")],
  [
   roles({"ug": "Take a precise feeding history: breast milk, formula, first fruit, sugar and sweet medicines.",
          "pg": "Stop the suspected sugar under specialist advice, treat sepsis and coagulopathy, and send the confirmatory tests.",
          "fac": "Assess whether learners ask what the child ate before they order a liver panel."}),
   sec(1, "Read the liver phenotype", '''
  <p>IEMs cause neonatal cholestasis, acute liver failure, hepatomegaly, coagulopathy out of proportion to jaundice, and renal tubular dysfunction. Ask about feed type, when fruit, juice or sugar started, sweet medicines (sucrose or sorbitol syrups), vomiting after feeds, hypoglycaemia, and aversion to sweets.</p>'''),

   sec(2, "Three diet-linked disorders", table(
     ["Disorder", "When", "Clues", "First steps"],
     [["<b>Classic galactosaemia</b>", "Days after milk feeds begin (breast or formula)", "Vomiting, jaundice, liver failure, bleeding, <b>E. coli sepsis</b>, cataracts", "Stop lactose (lactose-free formula) under specialist advice; treat sepsis; GALT enzyme assay (before any transfusion)"],
      ["<b>Hereditary fructose intolerance</b>", "When fruit, sucrose or sorbitol enters the diet", "Vomiting, hypoglycaemia, liver and kidney dysfunction, aversion to sweets", "Remove fructose, sucrose and sorbitol; genetic testing. <b>Never</b> do a fructose challenge"],
      ["<b>Tyrosinaemia type I</b>", "Infancy (acute liver failure) or later (rickets, liver disease)", "Coagulopathy with modest jaundice, renal Fanconi syndrome, rickets, neurological crises; cancer risk", "<b>Succinylacetone</b> in blood or urine; nitisinone and diet via the metabolic team"]]) + pitfall('''<p>Sending the GALT enzyme after a blood transfusion. Donor red cells give a falsely normal result for weeks; store a pre-transfusion sample or use genetic testing.</p>''')),

   sec(3, "The older child: Wilson disease", '''
  <p>Wilson disease can present from about 3&ndash;5 years with unexplained raised transaminases, hepatitis, acute liver failure with haemolysis, or later with deteriorating handwriting, tremor, dystonia, behavioural change or falling school performance. Kayser&ndash;Fleischer rings are often absent in children with liver presentation. Diagnosis combines ceruloplasmin, 24-hour urine copper, liver copper and genetics; no single test is enough. Treatment works, and siblings must be screened.</p>''' + danger('''<p>Acute liver failure with Coombs-negative haemolysis in a child or teenager: think Wilson disease and contact a liver transplant centre at once.</p>''')),

   sec(4, "Act within a shared pathway", '''
  <p>Urgent liver care (vitamin K, glucose, infection treatment, liver unit referral) and diagnostic confirmation proceed together. Give the family a precise interim feeding plan from the treating team; broad unguided eliminations can cause malnutrition.</p>''' + india('''<p>Soy-based or lactose-free formulas are widely available in Indian cities but may be costly or absent in rural areas. Nitisinone for tyrosinaemia type I is expensive; check support through the National Policy for Rare Diseases and Centres of Excellence (Unit 19). Wilson disease is relatively frequently diagnosed in Indian liver and neurology clinics &mdash; include it early in any unexplained liver disease after infancy.</p>'''), lvl="a"),
  ],
  [Q("A 9-day-old breastfed baby has vomiting, jaundice, a large liver, prolonged INR and E. coli bacteraemia. What is the most appropriate additional step?",
     ["Continue breastfeeding and treat sepsis only.",
      "Stop breast milk and start a lactose-free formula under specialist advice, send a pre-transfusion GALT assay, and continue sepsis treatment.",
      "Start a fructose-free diet.",
      "Give phototherapy and discharge when bilirubin falls."],
     1,
     "Which disorder presents with liver failure and E. coli sepsis in the first weeks of milk feeding?",
     "Breast milk contains lactose. What must stop, and which test must be taken before any blood transfusion?",
     "Liver dysfunction, coagulopathy and <b>E. coli sepsis</b> after milk feeds suggest <b>classic galactosaemia</b>. Stop lactose (breast milk and standard formula) under specialist advice, take a GALT sample before any transfusion, and continue sepsis care.",
     "<b>A</b> &mdash; continuing lactose worsens the liver failure. <b>C</b> &mdash; a newborn on milk has not yet been exposed to fructose. <b>D</b> &mdash; this is not simple jaundice.",
     "In a newborn with liver failure and E. coli sepsis, think galactosaemia before the next feed.",
     "section 2, ‘Three diet-linked disorders’"),
   Q("A 7-month-old has had vomiting, poor growth and a large liver since starting fruit purée and sweetened cereal at 6 months. She now refuses sweet foods. What is the most likely diagnosis, and what should be avoided?",
     ["Galactosaemia; avoid milk.",
      "Hereditary fructose intolerance; remove fructose, sucrose and sorbitol, and never perform a fructose challenge.",
      "Cow's milk protein allergy; avoid dairy.",
      "Coeliac disease; start a gluten-free diet."],
     1,
     "What changed in the diet at 6 months?",
     "Symptoms began with fruit and sugar, and she now avoids sweets. Which enzyme defect fits, and why is a challenge dangerous?",
     "Symptoms that start when <b>fructose and sucrose</b> enter the diet, with aversion to sweets, suggest <b>hereditary fructose intolerance</b>. Remove fructose, sucrose and sorbitol (including sweet medicines) and confirm genetically. A fructose challenge can cause severe hypoglycaemia and liver failure.",
     "<b>A</b> &mdash; galactosaemia presents in the first weeks of milk feeding. <b>C</b> &mdash; milk allergy does not explain a link with fruit. <b>D</b> &mdash; coeliac disease does not cause aversion to sweets or this timing with fruit.",
     "Ask when symptoms began relative to each new food.",
     "section 2, ‘Three diet-linked disorders’")]
)

# ------------------------------------------------------------------ UNIT 11
unit(11, "C", "Seizures",
  "Most seizures are not metabolic. A few metabolic epilepsies have specific treatments, and missing them leaves a child on a growing list of antiseizure drugs that do not work.",
  [("e", "Recognise seizure patterns that should prompt a metabolic question."),
   ("e", "Check glucose, calcium, magnesium and sodium in every seizing child."),
   ("a", "Know the monitored pyridoxine trial and the other vitamin-responsive epilepsies."),
   ("x", "Plan paired CSF and blood sampling before a lumbar puncture.")],
  [
   roles({"ug": "Check glucose and electrolytes in every seizing child and describe the seizure pattern.",
          "pg": "Consider pyridoxine, pyridoxal phosphate, biotin and GLUT1 deficiency in early refractory seizures, and store samples before treatment trials.",
          "fac": "Use a refractory neonatal seizure case to teach that treatment trials need monitoring and pre-trial samples."}),
   sec(1, "When seizures become a metabolic question", '''
  <ul>
    <li>Neonatal or early infantile seizures that do not respond to first- and second-line drugs.</li>
    <li>Seizures with encephalopathy, acidosis, hypoglycaemia or hyperammonaemia.</li>
    <li>Seizures related to fasting, with developmental regression, or with a movement disorder.</li>
    <li>A family history of neonatal seizures or death.</li>
  </ul>
  <p>First exclude the common: hypoglycaemia, hypocalcaemia, hypomagnesaemia, hyponatraemia, infection, hypoxic&ndash;ischaemic injury and structural lesions.</p>'''),

   sec(2, "Vitamin-responsive epilepsies", table(
     ["Disorder", "Treatment trial (under monitoring, per protocol)"],
     [["<b>Pyridoxine-dependent epilepsy</b> (ALDH7A1)", "Pyridoxine 100 mg IV with EEG and cardiorespiratory monitoring; repeat up to 500 mg if no response. Non-acute: 30 mg/kg/day orally for 3&ndash;5 days (GeneReviews)"],
      ["<b>Pyridoxal-phosphate-responsive epilepsy</b> (PNPO)", "Pyridoxal 5&prime;-phosphate orally, per specialist protocol"],
      ["<b>Biotinidase deficiency</b>", "Biotin 5&ndash;10 mg/day orally (profound deficiency, GeneReviews 2026)"],
      ["<b>Cerebral folate deficiency</b>", "Folinic acid, per specialist protocol"]]) + danger('''<p>Give the first IV pyridoxine dose with resuscitation ready: some infants with pyridoxine-dependent epilepsy develop apnoea and cardiorespiratory depression after it. Take plasma and urine for biomarkers (alpha-AASA, pipecolic acid) <b>before</b> the trial when possible, but do not delay treatment of status epilepticus to do so.</p>''')),

   sec(3, "Other metabolic epilepsies", table(
     ["Disorder", "Clue", "Test"],
     [["<b>GLUT1 deficiency</b>", "Seizures before meals, paroxysmal movements, acquired microcephaly", "Low CSF glucose with a paired blood glucose (CSF:blood ratio usually below about 0.45); treated with ketogenic diet"],
      ["<b>Glycine encephalopathy</b> (non-ketotic hyperglycinaemia)", "Neonatal encephalopathy, hiccups, apnoea, burst-suppression EEG", "Paired CSF and plasma glycine"],
      ["<b>Serine deficiency</b>", "Congenital microcephaly, seizures", "Low CSF and plasma serine (fasting)"],
      ["<b>Creatine deficiency</b>", "Speech delay, intellectual disability, seizures", "Urine and plasma creatine metabolites; brain MR spectroscopy"]])),

   sec(4, "Plan samples before the lumbar puncture", '''
  <p>CSF glucose, lactate, glycine and neurotransmitters need a <b>paired blood sample</b> taken just before the LP, specific tubes and fraction order, and often immediate freezing. Contact the laboratory first; a CSF sample for neurotransmitters cannot be repeated easily.</p>''' + india('''<p>Specialised CSF studies usually go to a handful of referral laboratories. If they are not available, a monitored pyridoxine trial and genetic testing (epilepsy gene panels are increasingly affordable in India) may give the answer. Biotin is cheap and widely available; a child with seizures, alopecia and rash deserves a biotinidase assay.</p>'''), lvl="a"),
  ],
  [Q("A 10-day-old has frequent seizures despite phenobarbital and levetiracetam. Glucose, calcium, magnesium, sodium, CSF and MRI are normal. What is the most appropriate next step?",
     ["Add a third and fourth antiseizure drug and wait.",
      "Store plasma and urine for biomarkers, then give pyridoxine 100 mg IV with EEG and cardiorespiratory monitoring and resuscitation ready.",
      "Give pyridoxine orally at home.",
      "Stop all antiseizure drugs."],
     1,
     "Which treatable metabolic epilepsy presents with refractory neonatal seizures?",
     "The trial needs monitoring because of a known risk. What is that risk, and what should be saved first?",
     "Refractory neonatal seizures with normal first-line tests call for a <b>monitored pyridoxine trial</b> for pyridoxine-dependent epilepsy: 100 mg IV with EEG and cardiorespiratory monitoring, as apnoea can follow. Save biomarker samples first if it causes no delay.",
     "<b>A</b> &mdash; more drugs will not treat a vitamin-dependent epilepsy. <b>C</b> &mdash; an unmonitored first dose is unsafe. <b>D</b> &mdash; stopping all drugs is dangerous.",
     "Refractory neonatal seizures: think pyridoxine, under monitoring.",
     "section 2, ‘Vitamin-responsive epilepsies’"),
   Q("A 4-year-old has seizures that tend to occur before breakfast, episodes of unsteadiness, and a head circumference that has fallen across centiles. Which test is most likely to make the diagnosis?",
     ["Serum ammonia.",
      "Lumbar puncture for CSF glucose with a paired blood glucose taken just before.",
      "Urine reducing substances.",
      "Sweat chloride."],
     1,
     "Which disorder causes seizures linked to fasting, movement problems and acquired microcephaly?",
     "The brain cannot take up glucose. How do you show that?",
     "Seizures before meals, paroxysmal ataxia and falling head growth suggest <b>GLUT1 deficiency</b>. A <b>low CSF glucose with a normal paired blood glucose</b> (ratio usually below about 0.45) supports it; genetics confirms it. The ketogenic diet is the treatment.",
     "<b>A</b> &mdash; ammonia does not diagnose GLUT1 deficiency. <b>C</b> &mdash; reducing substances relate to galactosaemia. <b>D</b> &mdash; sweat chloride is for cystic fibrosis.",
     "CSF glucose means nothing without a paired blood glucose.",
     "section 3, ‘Other metabolic epilepsies’")]
)

# ------------------------------------------------------------------ UNIT 12
unit(12, "C", "Movement disorders",
  "Describe the movement before naming the disease. Dystonia, chorea, ataxia and parkinsonism in a child point to different metabolic pathways &mdash; and several of them have treatments.",
  [("e", "Describe paediatric movement disorders accurately."),
   ("e", "Recognise Wilson disease and glutaric aciduria type 1 as treatable causes."),
   ("a", "Recognise fluctuating dystonia and oculogyric crises as clues to neurotransmitter disorders."),
   ("x", "Plan CSF neurotransmitter sampling correctly.")],
  [
   roles({"ug": "Describe the movement in words and, with consent, record a video.",
          "pg": "Link the movement to associated liver, eye, skin or imaging clues and choose the pathway to test.",
          "fac": "Use short consented videos for learners to name the movement before discussing causes."}),
   sec(1, "Name the movement", table(
     ["Movement", "What it looks like"],
     [["Dystonia", "Sustained or intermittent muscle contractions causing twisting postures"],
      ["Chorea", "Brief, irregular, flowing movements moving from one body part to another"],
      ["Ataxia", "Unsteady, poorly coordinated movement and gait"],
      ["Parkinsonism", "Slowness, rigidity, reduced facial expression, tremor"],
      ["Oculogyric crisis", "Episodes of sustained upward eye deviation"]]) + '''
  <p>Ask whether it is constant or episodic, worse later in the day, triggered by illness, and whether skills have been lost.</p>'''),

   sec(2, "Treatable causes not to miss", table(
     ["Disorder", "Clues", "Why it matters"],
     [["<b>Wilson disease</b>", "Older child or teenager; dystonia, tremor, dysarthria, behaviour change; liver disease; Kayser&ndash;Fleischer rings (usual in neurological presentation)", "Chelation or zinc treatment works; untreated it is fatal"],
      ["<b>Glutaric aciduria type 1</b>", "Large head (macrocephaly) in infancy, then sudden dystonia after an illness; wide Sylvian fissures on imaging", "Brain injury can be prevented by diet and an emergency regimen if diagnosed before the first crisis"],
      ["<b>Dopa-responsive dystonia</b>", "Dystonia worse in the evening, improving after sleep", "Dramatic response to low-dose levodopa"],
      ["<b>Biotin&ndash;thiamine-responsive basal ganglia disease</b>", "Subacute encephalopathy, dystonia, basal ganglia changes after a fever", "Responds to biotin and thiamine if given early"]]) + pitfall('''<p>Labelling a child with dystonia after a febrile illness as &ldquo;encephalitis&rdquo; or &ldquo;cerebral palsy&rdquo; without checking urine organic acids (GA1) or trying biotin and thiamine.</p>''')),

   sec(3, "Neurotransmitter disorders", '''
  <p>Disorders of dopamine and serotonin production (e.g. AADC deficiency, tyrosine hydroxylase deficiency) cause hypotonia, oculogyric crises, dystonia, autonomic symptoms (sweating, nasal congestion, temperature instability) and developmental delay, often with daily fluctuation. Diagnosis needs CSF neurotransmitter metabolites and genetics.</p>'''),

   sec(4, "CSF has a strict protocol", '''
  <p>CSF neurotransmitters need specific fractions in order, no blood contamination, immediate freezing and dry-ice transport. Interpretation uses age-specific reference ranges and medication history. Never improvise the collection; plan it with the laboratory.</p>''' + india('''<p>Many children with metabolic movement disorders in India carry a label of cerebral palsy. Reassess when there was no clear perinatal injury, the course is progressive or fluctuating, or the imaging does not fit. A levodopa trial for suspected dopa-responsive dystonia is cheap, safe under supervision and can be transformative.</p>'''), lvl="a"),
  ],
  [Q("A 13-year-old has 6 months of declining handwriting, slurred speech and a fixed smile. His transaminases are mildly raised. Which test is most useful first?",
     ["Serum ceruloplasmin and 24-hour urine copper, with a slit-lamp examination for Kayser–Fleischer rings.",
      "Plasma ammonia.",
      "CSF neurotransmitters.",
      "Urine organic acids."],
     0,
     "Which metabolic disease combines a movement disorder with liver involvement in a teenager?",
     "Copper accumulates in liver and brain. Which three tests begin the assessment?",
     "Dysarthria, dystonic facial expression, worsening handwriting and raised transaminases suggest <b>Wilson disease</b>. Start with ceruloplasmin, 24-hour urine copper and a slit-lamp examination; genetics and liver copper may follow.",
     "<b>B</b> &mdash; ammonia is not the key test here. <b>C</b> &mdash; CSF neurotransmitters are for early-onset disorders with a different picture. <b>D</b> &mdash; organic acids do not diagnose Wilson disease.",
     "Liver plus movement disorder in a teenager: check copper.",
     "section 2, ‘Treatable causes not to miss’"),
   Q("A 10-month-old with a head circumference above the 98th centile develops sudden severe dystonia after a febrile gastroenteritis. MRI shows wide Sylvian fissures and basal ganglia injury. Which disorder is most likely?",
     ["Cerebral palsy.",
      "Glutaric aciduria type 1.",
      "Classic PKU.",
      "Galactosaemia."],
     1,
     "Which organic aciduria causes macrocephaly and acute dystonia after illness?",
     "Large head, wide Sylvian fissures and a crisis after fever. What should the urine organic acids show?",
     "Macrocephaly, an acute encephalopathic crisis with dystonia after illness, and wide Sylvian fissures are characteristic of <b>glutaric aciduria type 1</b>. Urine organic acids and acylcarnitines confirm it. Siblings need testing, as diagnosis before a crisis prevents injury.",
     "<b>A</b> &mdash; cerebral palsy is non-progressive and does not start after a febrile illness. <b>C</b> &mdash; PKU does not cause acute dystonic crises. <b>D</b> &mdash; galactosaemia presents with liver disease in newborns.",
     "Macrocephaly plus dystonia after fever: think GA1.",
     "section 2, ‘Treatable causes not to miss’")]
)

# ------------------------------------------------------------------ UNIT 13
unit(13, "C", "Developmental delay and regression",
  "Most developmental delay is not metabolic. Regression &mdash; losing skills once gained &mdash; changes that, as do associated clues in the eyes, skin, bones, liver or behaviour.",
  [("e", "Distinguish developmental delay from regression."),
   ("e", "Recognise red flags that raise the yield of metabolic testing."),
   ("a", "Know the treatable metabolic causes of intellectual disability: PKU, homocystinuria, creatine and biotin disorders, others."),
   ("x", "Build a tiered, affordable evaluation with neurology and genetics.")],
  [
   roles({"ug": "Establish whether skills were never gained or were lost, with examples and dates.",
          "pg": "Look for red flags and send a targeted first-tier panel for treatable causes.",
          "fac": "Teach that developmental support and diagnostic work run together; neither waits for the other."}),
   sec(1, "Delay or regression?", '''
  <p><b>Delay</b> is slow acquisition of skills. <b>Regression</b> is loss of skills the child had reliably: walking, words, feeding, school work. Confirm with caregivers using specific examples and videos. Regression, episodic worsening, a movement disorder, seizures, eye or skeletal changes, organomegaly or thrombosis raise the chance of an IEM.</p>''' + pitfall('''<p>An old label such as &ldquo;cerebral palsy&rdquo; or &ldquo;autism&rdquo; stops people looking again. When the course changes, reassess.</p>''')),

   sec(2, "Treatable causes", table(
     ["Disorder", "Clues", "First test"],
     [["<b>Phenylketonuria</b> (untreated)", "Fair hair and skin, eczema, musty odour, intellectual disability, seizures", "Plasma phenylalanine"],
      ["<b>Classic homocystinuria</b>", "Lens dislocation, tall thin build, thrombosis, intellectual disability", "Plasma total homocysteine"],
      ["<b>Creatine deficiency syndromes</b>", "Severe speech delay, behaviour problems, seizures", "Urine creatine and guanidinoacetate; MR spectroscopy"],
      ["<b>Biotinidase deficiency</b>", "Seizures, hypotonia, alopecia, rash, hearing loss", "Biotinidase enzyme"],
      ["<b>Congenital hypothyroidism</b> (not an IEM, but a must)", "Prolonged jaundice, constipation, poor growth", "TSH and free T4"]]) + '''
  <p>Other clues: self-injury with high uric acid (Lesch&ndash;Nyhan syndrome); regression with organomegaly or coarse features (lysosomal disorders, Unit 15).</p>'''),

   sec(3, "Phenylketonuria", '''
  <p>Untreated classic PKU causes severe intellectual disability; early dietary treatment prevents it, which is why PKU was the first disorder screened in newborns. Current European and American guidelines aim to keep blood phenylalanine at <b>120&ndash;360 µmol/L</b> in children, with a phenylalanine-restricted diet and protein substitute, lifelong. Some children respond to sapropterin (BH4). Women with PKU need tight control before and during pregnancy to prevent maternal PKU syndrome in the baby.</p>'''),

   sec(4, "A tiered evaluation", '''
  <p>Start with history, examination, growth, hearing and vision, thyroid function, and a first-tier panel for treatable causes chosen with neurology and genetics: plasma amino acids, total homocysteine, urine organic acids, acylcarnitines, and creatine metabolites where indicated. Genomic testing (exome) now has a high yield in unexplained delay and may be the most efficient next step. Early intervention and rehabilitation start now, not when the diagnosis arrives.</p>''' + india('''<p>Newborn screening for PKU is not universal in India, so untreated PKU still presents with intellectual disability and seizures. Phenylalanine-free protein substitutes are expensive and not always available; ask the Centre of Excellence and patient support groups about access.</p>'''), lvl="a"),
  ],
  [Q("A 3-year-old walked at 13 months and spoke in phrases at 2 years, but over the last 6 months has stopped using words, walks unsteadily and has new seizures. What does this history indicate?",
     ["Global developmental delay; routine review in a year.",
      "Developmental regression, which needs a prompt structured evaluation that includes treatable metabolic and neurodegenerative causes.",
      "Autism only; refer to speech therapy.",
      "Normal variation."],
     1,
     "Did this child fail to gain skills, or lose skills he had?",
     "He lost speech and walking and developed seizures. Why does regression change the plan?",
     "The child has <b>lost</b> skills he had reliably: this is regression, and with new seizures it needs a prompt evaluation that includes metabolic, neurodegenerative and genetic causes, alongside developmental support.",
     "<b>A</b> &mdash; regression is not delay; waiting a year is unsafe. <b>C</b> &mdash; autism alone does not explain loss of walking and new seizures. <b>D</b> &mdash; loss of skills is never normal.",
     "Loss of skills is a red flag at any age.",
     "section 1, ‘Delay or regression?’"),
   Q("A 10-year-old with learning difficulty, a tall thin build and a dislocated lens has a deep vein thrombosis. What is the most useful test?",
     ["Plasma total homocysteine.",
      "Plasma phenylalanine.",
      "Urine organic acids.",
      "Serum ammonia."],
     0,
     "Which metabolic disorder causes lens dislocation, a marfanoid build and thrombosis?",
     "The combination of eye, skeleton, brain and blood clots points to one amino acid pathway.",
     "Lens dislocation, a tall thin build, learning difficulty and <b>thrombosis</b> suggest <b>classic homocystinuria</b>. Plasma total homocysteine is the key test. Some patients respond to pyridoxine.",
     "<b>B</b> &mdash; phenylalanine is for PKU, which does not cause lens dislocation or thrombosis. <b>C</b> &mdash; organic acids are not the first test here. <b>D</b> &mdash; ammonia is not raised in homocystinuria.",
     "Thrombosis plus lens dislocation in a child: check homocysteine.",
     "section 2, ‘Treatable causes’")]
)
