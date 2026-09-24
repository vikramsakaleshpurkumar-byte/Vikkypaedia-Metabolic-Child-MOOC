from gen import *

part("D", "From phenotype to diagnosis", "Units 14&ndash;17 · ~6 hours",
     "Genomic testing has changed metabolic diagnosis more in ten years than in the previous fifty, but a sequencing report still needs a clinician who knows what question it was meant to answer. This Part is about asking that question well, reading the answer honestly, and carrying it to the family and the next pregnancy.")

# ------------------------------------------------------------------ UNIT 14
unit(14, "D", "From phenotype to diagnosis",
  "The diagnosis is the point where the clinical story, the biochemistry and the genetic result explain one another. If one of the three does not fit, the diagnosis is not finished.",
  [("e", "Write a precise phenotype before choosing a test."),
   ("e", "Explain the difference between a biochemical marker and a diagnosis."),
   ("a", "Read a genetic report in layers: classification, gene&ndash;disease fit, inheritance, phenotype."),
   ("x", "Explain why a variant of uncertain significance cannot confirm a diagnosis.")],
  [
   roles({"ug": "Write a one-paragraph phenotype: onset, course, organs involved, triggers, family history.",
          "pg": "Choose between targeted biochemistry, a gene panel and exome sequencing, and read the report critically.",
          "fac": "Run a case conference on a VUS: what is established, what is not, and who owns the next step?"}),
   sec(1, "Write the problem before the test", '''
  <p>A phenotype is more than a label: when the child became unwell, whether development was progressing, which organs are involved, the relationship to feeding, fasting or infection, family history and results so far. &ldquo;Rule out metabolic disorder&rdquo; hides every decision the laboratory needs to make.</p>''' + pearl('''<p>Use Human Phenotype Ontology (HPO) terms in genetic test requests. Laboratories use them to filter and prioritise variants, and a good list raises the yield.</p>''')),

   sec(2, "A metabolite is evidence with a context", '''
  <p>A raised methylmalonic acid may be inherited MMA &mdash; or <b>nutritional vitamin B12 deficiency</b> in an exclusively breastfed infant of a B12-deficient mother. A low carnitine may be primary or secondary to an organic acidaemia. Ask what was measured, which processes could explain it, and what would distinguish them.</p>'''),

   sec(3, "Choosing the genetic test", table(
     ["Test", "Best when"],
     [["Single gene", "Phenotype and biochemistry point to one gene (e.g. confirmed low GALT activity)"],
      ["Gene panel", "Several genes cause the same picture (e.g. urea cycle disorders, FAODs)"],
      ["Exome sequencing", "Phenotype is broad, overlapping or unexplained; often the most efficient test now"],
      ["Genome sequencing", "Exome negative; suspected deep intronic or structural variants"],
      ["Mitochondrial DNA", "Suspected mtDNA disorder; tissue may matter (Unit 16)"]]) + '''
  <p>Trio testing (child and both parents) speeds interpretation and clarifies inheritance.</p>'''),

   sec(4, "Read a genetic result in layers", '''
  <ol>
    <li><b>Classification:</b> pathogenic, likely pathogenic, uncertain significance (VUS), likely benign, benign (ACMG/AMP framework).</li>
    <li><b>Gene&ndash;disease fit:</b> does this gene cause a disorder that matches the child?</li>
    <li><b>Inheritance:</b> for a recessive disorder, are there two variants, on different copies (in trans)?</li>
    <li><b>Phenotype and biochemistry:</b> do they agree?</li>
  </ol>''' + danger('''<p>A <b>VUS</b> must not be used to make clinical decisions or to counsel about recurrence. Manage the child on the clinical and biochemical evidence, and ask for reinterpretation as evidence grows.</p>''') + india('''<p>Exome sequencing costs have fallen sharply in India and are now often cheaper than a long list of individual biochemical tests. Indian populations are under-represented in variant databases, so VUS results are more frequent; parental testing and phenotype matching become even more important.</p>'''), lvl="a"),
  ],
  [Q("A child with developmental delay has exome sequencing. The report lists a single heterozygous variant of uncertain significance in a gene for an autosomal recessive metabolic disorder. The biochemistry is normal. What should the family be told?",
     ["Their child has the disorder and future pregnancies have a 1-in-4 risk.",
      "The finding is uncertain and does not establish a diagnosis; management continues on the clinical evidence, and the result will be reviewed as evidence grows.",
      "The result is benign and can be ignored.",
      "Start disease-specific treatment immediately."],
     1,
     "What does a VUS mean, and how many variants does a recessive disorder need?",
     "One uncertain variant in a recessive gene with normal biochemistry. Does that make a diagnosis?",
     "A <b>VUS</b> means the evidence is insufficient to classify the variant, and a recessive disorder needs two disease-causing variants. With normal biochemistry, this does <b>not</b> establish a diagnosis. Explain the uncertainty honestly and plan reinterpretation.",
     "<b>A</b> &mdash; a VUS cannot be used for diagnosis or recurrence counselling. <b>C</b> &mdash; uncertain is not benign; it may be reclassified. <b>D</b> &mdash; treatment should not be based on a VUS.",
     "A VUS is a question, not an answer.",
     "section 4, ‘Read a genetic result in layers’"),
   Q("An exclusively breastfed 5-month-old with poor feeding, hypotonia and developmental delay has raised urine methylmalonic acid. The mother is vegetarian and has been tired and pale. What should be checked first?",
     ["Genetic testing for MMA only.",
      "Infant and maternal vitamin B12 levels and homocysteine.",
      "A muscle biopsy.",
      "Nothing; start a protein-restricted diet."],
     1,
     "Which acquired condition raises methylmalonic acid in infants?",
     "The mother may be B12 deficient, and breast milk passes little B12 to the baby. What should be measured?",
     "Maternal <b>vitamin B12 deficiency</b> can cause infantile B12 deficiency with raised methylmalonic acid and homocysteine, hypotonia and developmental delay. Check infant and maternal B12 and homocysteine; treatment with B12 is simple and effective.",
     "<b>A</b> &mdash; genetics is premature before excluding a common acquired cause. <b>C</b> &mdash; muscle biopsy is not indicated. <b>D</b> &mdash; protein restriction in a B12-deficient infant is harmful.",
     "Always ask whether a metabolite has an acquired explanation.",
     "section 2, ‘A metabolite is evidence with a context’")]
)

# ------------------------------------------------------------------ UNIT 15
unit(15, "D", "Lysosomal and peroxisomal disorders",
  "These are disorders of the cell's recycling and processing plants. They progress slowly, involve many organs, and several now have treatments that work best before damage is established.",
  [("e", "Recognise the multisystem pattern of lysosomal storage disorders."),
   ("e", "Recognise the neonatal pattern of peroxisomal biogenesis disorders."),
   ("a", "Select enzyme, biomarker and genetic tests according to the phenotype."),
   ("x", "Link diagnosis to available treatments, organ surveillance and family counselling.")],
  [
   roles({"ug": "Recognise organomegaly with coarse features, bone changes or regression as a reason to refer.",
          "pg": "Choose enzyme or biomarker tests with the metabolic team and plan organ surveillance.",
          "fac": "Use serial photographs (with consent) to teach how coarse features evolve."}),
   sec(1, "Lysosomal storage patterns", table(
     ["Group", "Clues"],
     [["<b>Mucopolysaccharidoses</b> (e.g. MPS I, II)", "Coarse face, large head, hernias, joint stiffness, skeletal changes (dysostosis multiplex), corneal clouding (MPS I), hearing loss, recurrent ear and chest infections"],
      ["<b>Gaucher disease</b>", "Large spleen and liver, low platelets, anaemia, bone pain; type 2/3 with neurological involvement"],
      ["<b>Niemann&ndash;Pick disease</b>", "Hepatosplenomegaly; interstitial lung disease; vertical gaze palsy (type C)"],
      ["<b>Pompe disease</b>", "Hypotonia with cardiomyopathy in infants (Unit 9)"],
      ["<b>Neuronal ceroid lipofuscinoses, Krabbe, metachromatic leukodystrophy</b>", "Regression, seizures, vision loss, white-matter disease"]]) + pearl('''<p>A cherry-red spot at the macula suggests Tay&ndash;Sachs disease, Sandhoff disease or some other sphingolipidoses. Ask for a dilated fundus examination in any infant with regression.</p>''')),

   sec(2, "Peroxisomal disorders", '''
  <p><b>Zellweger spectrum disorders</b>: newborn with severe hypotonia, seizures, large fontanelle, high forehead, liver dysfunction, renal cysts, stippled epiphyses, and later hearing and vision loss. <b>X-linked adrenoleukodystrophy</b>: a previously well school-age boy with attention or behaviour problems, then deteriorating vision, hearing and walking, and adrenal insufficiency. Very-long-chain fatty acids (VLCFA) are the first test for both; they do not detect every peroxisomal disorder.</p>''' + danger('''<p>A boy with X-ALD can present in adrenal crisis. Check cortisol and ACTH at diagnosis and in any boy with unexplained adrenal insufficiency.</p>''')),

   sec(3, "Test the suspected pathway", '''
  <p>Dried blood spot enzyme assays screen for several disorders (Pompe, Gaucher, Fabry, MPS I); urine glycosaminoglycans for MPS; chitotriosidase and lyso-Gb1 as biomarkers; VLCFA for peroxisomal disorders; then confirmation by leukocyte enzyme activity and genetics. Pseudodeficiency alleles and carrier-range results can mislead &mdash; confirm before discussing prognosis.</p>'''),

   sec(4, "Treatment and care", '''
  <p>Treatments include enzyme replacement therapy (Gaucher, Pompe, MPS I, II, IVA, VI, Fabry), substrate reduction, and haematopoietic stem-cell transplantation (MPS I Hurler before age about 2&ndash;2.5 years; early cerebral X-ALD). Timing matters: many benefits are limited once neurological injury is established. Many disorders still need coordinated supportive care: physiotherapy, airway and anaesthetic planning, hearing, vision, orthopaedics and palliative care.</p>''' + india('''<p>Gaucher disease, MPS I, II, IVA and VI and Pompe disease are among the conditions for which the National Policy for Rare Diseases (2021) offers support for treatment through designated Centres of Excellence. Eligibility, amounts and the list of centres change; always check the current MoHFW notices and refer through a Centre of Excellence rather than promising a family funding.</p>'''), lvl="a"),
  ],
  [Q("A 2-year-old has a large head, coarse facial features, an umbilical hernia, stiff joints, noisy breathing and clouded corneas. Which first test is most appropriate?",
     ["Urine glycosaminoglycans and a dried blood spot enzyme assay for MPS I.",
      "Plasma ammonia.",
      "Blood acylcarnitines.",
      "CSF glucose."],
     0,
     "Which group of lysosomal disorders causes coarse features and skeletal changes?",
     "Corneal clouding distinguishes MPS I from MPS II. Which tests screen for MPS?",
     "Coarse features, hernia, joint stiffness, airway obstruction and <b>corneal clouding</b> suggest a mucopolysaccharidosis, particularly <b>MPS I</b>. Urine glycosaminoglycans and alpha-L-iduronidase enzyme testing come first, confirmed genetically. Early stem-cell transplantation matters for Hurler syndrome.",
     "<b>B</b> &mdash; ammonia is for acute encephalopathy. <b>C</b> &mdash; acylcarnitines are for fatty-acid oxidation disorders and organic acidaemias. <b>D</b> &mdash; CSF glucose is for GLUT1 deficiency.",
     "Coarse features plus clouded corneas: think MPS I.",
     "section 1, ‘Lysosomal storage patterns’"),
   Q("A 7-year-old boy who was doing well at school develops inattention, falling grades, then difficulty seeing and walking over 6 months. He is also tired and has darkening skin. MRI shows posterior white-matter change. What is the most important combination of tests?",
     ["Very-long-chain fatty acids, and cortisol with ACTH.",
      "Urine organic acids only.",
      "Plasma phenylalanine.",
      "CSF neurotransmitters."],
     0,
     "Which X-linked disorder combines leukodystrophy with adrenal insufficiency?",
     "Skin darkening and fatigue suggest the adrenal glands are involved. Which disorder causes that plus white-matter disease?",
     "Behavioural and school decline, then neurological loss, with <b>adrenal insufficiency</b> (fatigue, pigmentation) and posterior white-matter change, suggests <b>cerebral X-linked adrenoleukodystrophy</b>. Check VLCFA and cortisol/ACTH, and refer urgently: early transplantation can halt cerebral disease.",
     "<b>B</b>, <b>C</b> and <b>D</b> &mdash; none tests for X-ALD or the life-threatening adrenal insufficiency.",
     "A boy with leukodystrophy needs his adrenals checked.",
     "section 2, ‘Peroxisomal disorders’")]
)

# ------------------------------------------------------------------ UNIT 16
unit(16, "D", "Mitochondrial disease and glycosylation disorders",
  "Both can affect any organ at any age, and they overlap. The task is not to name one from a raised lactate or hypotonia, but to find the features that shift the probability and choose tests that can settle it.",
  [("e", "Recognise the high-energy-organ pattern of mitochondrial disease."),
   ("e", "Recognise clues that favour a congenital disorder of glycosylation (CDG)."),
   ("a", "Interpret lactate in context and use transferrin glycoform analysis appropriately."),
   ("x", "Explain mitochondrial genetics: mtDNA versus nuclear DNA, heteroplasmy.")],
  [
   roles({"ug": "List the organs involved and notice when three or more unrelated systems are affected.",
          "pg": "Build a convergence table and choose between transferrin isoforms, lactate studies and genomic testing.",
          "fac": "Reward calibrated uncertainty: 'this supports X, but Y remains possible'."}),
   sec(1, "Clues that favour mitochondrial disease", '''
  <p>High-energy tissues dominate: brain, muscle, heart, eyes, ears, kidneys, liver. Clues: developmental regression with illness, <b>Leigh syndrome</b> (symmetrical basal ganglia and brainstem lesions), ptosis and ophthalmoplegia, myopathy, cardiomyopathy, diabetes with deafness, stroke-like episodes (MELAS), liver failure after valproate (POLG), and raised lactate &mdash; though lactate can be normal.</p>''' + danger('''<p><b>Avoid valproate</b> in suspected mitochondrial disease, especially POLG-related disease: it can precipitate fatal liver failure.</p>''')),

   sec(2, "Clues that favour CDG", '''
  <p>Abnormal fat distribution (fat pads over the buttocks), inverted nipples, cerebellar hypoplasia, strabismus, <b>combined abnormalities of clotting and anticoagulant factors</b> (low antithrombin, protein C and factor XI together), liver disease, protein-losing enteropathy, hypoglycaemia and stroke-like episodes. <b>Transferrin glycoform analysis</b> screens many N-glycosylation disorders (e.g. PMM2-CDG), but a normal result does not exclude every CDG.</p>'''),

   sec(3, "Interpreting lactate", '''
  <p>Lactate rises with poor perfusion, seizures, crying, a tight tourniquet or delayed processing. A single raised value in a sick child does not mean mitochondrial disease. Useful: a free-flowing sample, repeated values, the lactate-to-pyruvate ratio, CSF lactate, and MR spectroscopy showing a lactate peak.</p>'''),

   sec(4, "Genetics is more than one pattern", '''
  <p>Most childhood mitochondrial disease is caused by <b>nuclear DNA</b> variants (usually autosomal recessive). <b>Mitochondrial DNA</b> variants are maternally inherited, and <b>heteroplasmy</b> (the proportion of altered mtDNA) varies between tissues and between siblings, so a negative blood test may not answer the question. Exome or genome sequencing with mtDNA analysis now makes the diagnosis in many children without a muscle biopsy.</p>''' + tracks(
     ["Exome/genome sequencing including mtDNA; muscle biopsy for respiratory-chain studies if needed",
      "Neuro-metabolic multidisciplinary clinic"],
     ["Start with careful phenotyping, lactate done properly, MRI where available and a genetic test chosen with a specialist",
      "Avoid valproate and prolonged fasting while the diagnosis is uncertain",
      "Support, physiotherapy and nutrition do not wait for a name"]), lvl="a"),
  ],
  [Q("A 2-year-old with developmental regression after a viral illness has ptosis, hypotonia and symmetrical basal ganglia and brainstem lesions on MRI. Lactate is repeatedly raised on free-flowing samples. His seizures are poorly controlled. Which drug should be avoided?",
     ["Levetiracetam.",
      "Sodium valproate.",
      "Clobazam.",
      "Phenobarbital."],
     1,
     "Which syndrome combines regression after illness with basal ganglia and brainstem lesions?",
     "In suspected mitochondrial disease, one antiseizure drug can cause fatal liver failure.",
     "Regression after illness, ptosis, persistently raised lactate and symmetrical basal ganglia and brainstem lesions suggest <b>Leigh syndrome</b>, a mitochondrial disorder. <b>Avoid valproate</b>, which can precipitate liver failure, particularly in POLG disease.",
     "<b>A</b>, <b>C</b> and <b>D</b> &mdash; these are generally acceptable; valproate is the drug specifically avoided.",
     "Suspected mitochondrial disease: no valproate.",
     "section 1, ‘Clues that favour mitochondrial disease’"),
   Q("An infant with developmental delay has cerebellar hypoplasia, inverted nipples, abnormal fat pads over the buttocks, and low antithrombin, protein C and factor XI. Which test is most useful first?",
     ["Transferrin glycoform (isoform) analysis.",
      "Plasma ammonia.",
      "Urine glycosaminoglycans.",
      "Very-long-chain fatty acids."],
     0,
     "Which group of disorders causes multiple coagulation factor abnormalities with abnormal fat distribution?",
     "Many clotting proteins are glycoproteins. How do you screen for defective glycosylation?",
     "Inverted nipples, abnormal fat distribution, cerebellar hypoplasia and <b>combined clotting-protein abnormalities</b> suggest a <b>congenital disorder of glycosylation</b> such as PMM2-CDG. Transferrin glycoform analysis is the first screen; genetics confirms it.",
     "<b>B</b> &mdash; ammonia is not the key abnormality. <b>C</b> &mdash; glycosaminoglycans screen for MPS. <b>D</b> &mdash; VLCFA screen for peroxisomal disorders.",
     "Many clotting factors abnormal at once, plus odd fat pads: think CDG.",
     "section 2, ‘Clues that favour CDG’")]
)

# ------------------------------------------------------------------ UNIT 17
unit(17, "D", "Newborn screening and the next pregnancy",
  "A screening result changes probability; it does not make a diagnosis. And the most useful thing a diagnosis can do for a family is often to protect the next child.",
  [("e", "Explain the difference between a screening result and a diagnosis."),
   ("e", "Act on symptoms even after a reported normal screen."),
   ("a", "Close the loop after an abnormal screening result."),
   ("x", "Tailor recurrence counselling to autosomal recessive, X-linked and mitochondrial inheritance.")],
  [
   roles({"ug": "Explain in plain words what a positive and a negative screen mean.",
          "pg": "Act on an abnormal result the same day, and plan the next baby's care with the family and genetics team.",
          "fac": "Audit how many screen-positive babies in your unit reached confirmatory testing, and how long it took."}),
   sec(1, "A screen changes probability", '''
  <p>Newborn screening identifies babies who need further assessment for a defined list of conditions. An out-of-range result is not a diagnosis; a normal result does not exclude conditions outside the panel, late-onset forms or false negatives. Ask to see the report: &ldquo;screening done&rdquo; does not tell you which conditions were tested or whether follow-up happened.</p>'''),

   sec(2, "Close the loop after an abnormal result", '''
  <p>Contact the family the same day, find out whether the baby is well, and arrange the condition-specific next step. Some disorders (e.g. MSUD, urea cycle disorders, galactosaemia) need immediate action even before confirmation. Say: &ldquo;This result means your baby needs another test; it does not yet prove the condition. Here is what happens next and when.&rdquo; Name the clinician who will review the confirmation.</p>''' + pitfall('''<p>Posting a letter and assuming the family will come. A sample sent or a referral made is not evidence that the baby reached care.</p>''')),

   sec(3, "Inheritance changes the counselling", table(
     ["Inheritance", "Example", "Recurrence (each pregnancy)"],
     [["Autosomal recessive (most IEMs)", "MSUD, PKU, MMA, galactosaemia", "1 in 4 when both parents are confirmed carriers"],
      ["X-linked", "OTC deficiency, X-ALD, MPS II", "Depends on whether the mother is a carrier; sons and daughters differ; carrier girls can be affected"],
      ["Mitochondrial DNA", "MELAS, some Leigh syndrome", "Maternal transmission; heteroplasmy makes prediction difficult"],
      ["Nuclear mitochondrial", "POLG disease, most childhood Leigh syndrome", "Usually autosomal recessive"]]) + '''
  <p>Avoid blame: inheritance describes biology, not something a parent did.</p>'''),

   sec(4, "Plan before the next pregnancy", '''
  <p>When the family&rsquo;s variants are known, <b>prenatal diagnosis</b> (chorionic villus sampling from about 11 weeks) or preimplantation genetic testing may be possible. Also plan the <b>next baby&rsquo;s first days</b>: some disorders need a specific feeding plan and tests from birth rather than waiting for routine screening. Refer to genetics before the next pregnancy, and document what the family understood and chose.</p>''' + india('''<p>India has no single national newborn screening programme for IEMs; coverage varies by state and hospital, and many panels test only congenital hypothyroidism and a few other conditions (G6PD deficiency, congenital adrenal hyperplasia, galactosaemia, biotinidase deficiency, PKU in some programmes). Expanded tandem mass spectrometry screening is available mainly in private and some state programmes. Prenatal diagnosis is regulated under the PCPNDT Act; genetic testing for a known disorder is permitted, but sex determination is prohibited.</p>'''), lvl="a"),
  ],
  [Q("A 5-day-old's newborn screen shows a raised leucine. The baby was discharged well on day 2. The family lives 3 hours away. What should happen today?",
     ["Post a letter asking the family to attend clinic next month.",
      "Phone the family today, ask how the baby is feeding and behaving, and arrange same-day assessment and confirmatory testing with the metabolic team.",
      "Wait for a repeat screen in 2 weeks.",
      "Tell the family the baby has MSUD."],
     1,
     "Which disorder raises leucine, and how quickly can it cause harm?",
     "MSUD can cause encephalopathy in the first week. What does a positive screen require, and how fast?",
     "A raised leucine suggests possible <b>MSUD</b>, which can cause encephalopathy within days. Phone the family <b>today</b>, check the baby&rsquo;s state and arrange same-day assessment and confirmation. Explain that it is a screening result, not yet a diagnosis.",
     "<b>A</b> and <b>C</b> &mdash; delay can be fatal in MSUD. <b>D</b> &mdash; a screen is not a diagnosis; confirmation is needed.",
     "A positive screen for an intoxication disorder is a same-day phone call.",
     "section 2, ‘Close the loop after an abnormal result’"),
   Q("The parents of a boy with OTC deficiency ask about the risk in their next child. The mother has had lifelong protein aversion and carrier testing confirms she carries the variant. What is accurate?",
     ["Every pregnancy has a 1-in-4 risk regardless of sex.",
      "Each son has a 1-in-2 chance of being affected; each daughter has a 1-in-2 chance of being a carrier, and carrier girls may themselves have symptoms.",
      "There is no risk, as lightning does not strike twice.",
      "Only daughters can be affected."],
     1,
     "OTC deficiency is X-linked. How does a carrier mother pass on an X-linked disorder?",
     "Sons inherit one of the mother's two X chromosomes. What about daughters?",
     "OTC deficiency is <b>X-linked</b>. With a carrier mother, each son has a <b>1 in 2</b> chance of being affected, and each daughter a 1 in 2 chance of being a carrier; carrier girls can have symptoms (as the mother&rsquo;s protein aversion suggests). Refer for genetic counselling and a birth plan for the next baby.",
     "<b>A</b> &mdash; 1 in 4 applies to autosomal recessive disorders. <b>C</b> &mdash; each pregnancy carries the same risk. <b>D</b> &mdash; boys are more often and more severely affected.",
     "Counsel from the actual inheritance pattern, not a default number.",
     "section 3, ‘Inheritance changes the counselling’")]
)
