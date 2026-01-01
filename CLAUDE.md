# Instructions for Claude Code

## Generating the Comprehensive Genome Analysis Report

When regenerating `GENOME_ANALYSIS.html`, create a **comprehensive, detailed, dense report** with the following requirements:

### ✅ CRITICAL REQUIREMENTS

#### 0. **NEVER TRUNCATE - Process Every Variant Completely**
**MANDATORY: You MUST process ALL variants found in the genome, not just a subset.**

- If there are 26 variants, process all 26 with full details
- If there are 50 variants, process all 50 with full details
- **DO NOT** stop early or summarize remaining variants
- **DO NOT** say "and X more variants..." or similar truncations
- Each variant gets full treatment: inline explanations, quantitative comparisons, citations
- If the file gets large (100KB+), that's expected and correct
- Use efficient formatting but never skip content for brevity

### ✅ CRITICAL REQUIREMENTS

#### 1. Use the Verified Database
- **ALWAYS** use `rsid_genome_analyzer_verified.py` as the source database
- This database has all variants verified against peer-reviewed research
- All allele assignments are correct (rs3918290, rs776746, rs12913832 all fixed)
- Contains extensive research citations in comments

#### 2. Inline Explanations (NOT Hover Tooltips)
**Every technical term must be explained inline in parentheses or immediately following**

Examples:
- "Stevens-Johnson Syndrome (SJS): a rare but life-threatening skin reaction causing blistering and peeling of skin and mucous membranes"
- "Half-life (time for half the drug to be eliminated from your body): 6-8 hours"
- "Acetylation (adding an acetyl chemical tag to drugs for breakdown): slow acetylators break down drugs slower"
- "OCA2 gene: produces melanin in the iris; more melanin = darker eyes; HERC2 is a genetic switch that controls OCA2"

**Format:**
```html
<span class="explained">Technical Term: clear explanation of what it means</span>
```

#### 3. Quantitative Comparisons in Real Units
**Every relative term (slow/fast, high/low, increased/decreased) MUST include specific numbers**

Examples for different variant types:

**Caffeine Metabolism (CYP1A2 rs762551):**
```
Caffeine Half-Life (half-life: time for half the drug to be eliminated from your body):
• Fast metabolizers (A/A): 2.5-3.5 hours
• Intermediate (A/C): 4-5 hours
• Slow metabolizers (C/C - YOU): 6-8 hours (or longer)
```

**Warfarin Dosing (VKORC1 rs9923231):**
```
Warfarin Dose Requirements:
• Normal (C/C): 6-7 mg/day
• Moderate sensitivity (C/T - YOU): 4-5 mg/day (25-30% lower)
• High sensitivity (T/T): 2.5-3.5 mg/day (40-60% lower)
```

**Athletic Performance (ACTN3 rs1815739):**
```
Performance Differences:
• Vertical jump: 2-3 cm difference between R/R and X/X
• 100m sprint: 0.1-0.2 second difference
• Muscle fiber composition: R/R has 5-10% more fast-twitch fibers
```

**MTHFR Enzyme Activity (rs1801133):**
```
Enzyme Activity Levels:
• C/C (wild-type): 100% activity
• C/T (YOU): 65% activity (30-35% reduced)
• T/T: 30-40% activity (60-70% reduced)

Impact on Homocysteine:
• C/C: Normal levels (5-15 μmol/L)
• C/T: Slight elevation (10-20 μmol/L)
• T/T: May be elevated (15-30+ μmol/L)

Impact on Folate:
• T/T genotype: 16% lower red blood cell folate vs C/C
```

**Factor V Leiden (rs6025):**
```
Blood Clot Risk:
• C/C (normal): 1x baseline risk
• C/T (YOU): 4-8x increased risk
• T/T: 50-80x increased risk
```

#### 4. Comprehensive Research Citations

**EVERY variant must have citations with clickable links to peer-reviewed papers**

**Citation Format in Variant Sections:**
Use inline reference numbers like `<a href="#ref8" class="ref">[8]</a>`

**References Section at Bottom:**
Create a comprehensive references section organized by category:

```html
<h2 id="references">📄 Scientific References</h2>
<p style="margin-bottom: 10px;">All claims in this report are backed by peer-reviewed research. Click links to read full papers.</p>

<h3>Pharmacogenomics References</h3>
<ol>
    <li id="ref1"><strong>HLA-B*15:02 and Carbamazepine:</strong> NEJM (2011). "Carbamazepine-Induced Toxic Effects and HLA-B*1502 Screening in Taiwan." <a href="https://www.nejm.org/doi/full/10.1056/NEJMoa1009717" target="_blank">Read paper</a></li>

    <li id="ref2"><strong>VKORC1 Warfarin Dosing:</strong> NCBI Bookshelf. "Warfarin Therapy and VKORC1 and CYP Genotype." <a href="https://www.ncbi.nlm.nih.gov/books/NBK84174/" target="_blank">Read paper</a></li>
</ol>

<h3>Clinical References</h3>
<ol start="9">
    <li id="ref9"><strong>MTHFR C677T:</strong> CDC. "MTHFR Gene Variant and Folic Acid Facts." <a href="https://www.cdc.gov/folic-acid/data-research/mthfr/index.html" target="_blank">Read article</a></li>
</ol>

<h3>Trait References</h3>
<ol start="17">
    <li id="ref17"><strong>HERC2 rs12913832 Eye Color:</strong> PMC (2023). "Association between Variants in the OCA2-HERC2 Region and Blue Eye Colour." <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10048254/" target="_blank">Read paper</a></li>
</ol>
```

**Citation Sources to Use:**
- PharmGKB (https://www.pharmgkb.org/)
- CPIC Guidelines (https://cpicpgx.org/)
- NCBI Bookshelf Medical Genetics Summaries
- PMC (PubMed Central)
- NEJM (New England Journal of Medicine)
- Nature journals
- JAMA journals
- CDC resources
- FDA guidelines

#### 5. Dense UI with Minimal Whitespace

**CSS Guidelines:**
```css
.variant {
    padding: 20px;  /* Not 40px */
    margin: 20px 0; /* Not 40px */
}

.comparison {
    background: #f8f9fa;
    border-left: 4px solid #3498db;
    padding: 15px;
    margin: 10px 0;
    font-size: 16px;
    line-height: 1.6;
}

.meaning-box {
    background: #fff9e6;
    border: 2px solid #ffd700;
    padding: 15px;
    margin: 10px 0;
    border-radius: 8px;
}
```

**Layout:**
- Reduce padding and margins throughout
- Use compact spacing between sections
- Make better use of horizontal space
- Use columns where appropriate

#### 6. Comprehensive Content Structure

**For Each Variant, Include:**

```html
<div class="variant [importance-class]">
    <div class="variant-header">
        <div><span class="gene">GENE NAME (Function)</span></div>
        <span class="rsid">rsID | chr:position</span>
        <span class="genotype [het|hom]">YOU HAVE: 0/1</span>
    </div>

    <div class="variant-body">
        <div class="variant-info">
            <div><span class="info-label">Condition/Drug/Trait:</span> Name</div>
            <div><span class="info-label">Your Genotype:</span> A/G (heterozygous)</div>
            <div><span class="info-label">Effect Allele:</span> G allele increases risk</div>
        </div>

        <div>
            <div class="meaning-box">
                <div class="meaning-title">🎯 What This Means For YOU:</div>
                [Detailed explanation with inline term definitions]
                <a href="#ref1" class="ref">[1]</a>
            </div>

            <div class="comparison">
                <strong>Quantitative Comparison Title:</strong><br>
                • Genotype 1: Specific numbers and units<br>
                • Genotype 2 (YOU): Specific numbers and units<br>
                • Genotype 3: Specific numbers and units<br>
                <a href="#ref2" class="ref">[2]</a>
            </div>

            <div class="comparison">
                <strong>Mechanism:</strong> Detailed explanation of how this variant works biologically
                <a href="#ref3" class="ref">[3]</a>
            </div>

            <div class="comparison">
                <strong>Population Frequency:</strong> X% of Europeans, Y% of East Asians, etc.
                <a href="#ref4" class="ref">[4]</a>
            </div>

            <div class="action" *if applicable*>
                <strong>📋 Action:</strong> Specific actionable recommendations
            </div>
        </div>
    </div>
</div>
```

#### 7. Glossary Section

Include a comprehensive glossary of terms:

```html
<h2 id="glossary">📖 Glossary</h2>
<table style="width: 100%; border-collapse: collapse;">
    <tr>
        <td style="width: 200px;"><strong>Term</strong></td>
        <td><strong>Definition</strong></td>
    </tr>
    <tr>
        <td><strong>Heterozygous</strong></td>
        <td>Having two different alleles (versions) of a gene. Denoted as 0/1 or A/G. You inherited one version from each parent.</td>
    </tr>
    <tr>
        <td><strong>Half-life</strong></td>
        <td>The time it takes for half of a drug to be eliminated from your body. Longer half-life = drug stays in system longer.</td>
    </tr>
</table>
```

### 📋 Complete Example for One Variant

Condensed example showing all requirements (VKORC1 warfarin variant):

```html
<div class="variant high">
    <div class="variant-header">
        <div><span class="gene">VKORC1 (Vitamin K Epoxide Reductase)</span></div>
        <span class="rsid">rs9923231 | chr16:31096368</span>
        <span class="genotype het">YOU HAVE: 0/1</span>
    </div>

    <div class="variant-body">
        <div class="variant-info">
            <div><span class="info-label">Drug:</span> Warfarin (Coumadin)</div>
            <div><span class="info-label">Your Genotype:</span> C/T (heterozygous)</div>
        </div>

        <div class="meaning-box">
            <div class="meaning-title">🎯 What This Means For YOU:</div>
            You have one T allele in <span class="explained">VKORC1: enzyme that recycles vitamin K for blood clotting; warfarin blocks this enzyme</span>. Your T allele increases sensitivity, requiring <strong>25-30% lower warfarin dose</strong> vs C/C to avoid <span class="explained">bleeding complications: bruising, nosebleeds, internal bleeding</span>.<a href="#ref2" class="ref">[2]</a>
        </div>

        <div class="comparison">
            <strong>Warfarin Dose Requirements:</strong><br>
            • C/C: 6-7 mg/day | <strong>C/T (YOU): 4-5 mg/day (25-30% lower)</strong> | T/T: 2.5-3.5 mg/day (40-60% lower)<br>
            Time to target INR: C/C 5-7 days, <strong>C/T 3-5 days</strong>, T/T 2-4 days<a href="#ref2" class="ref">[2]</a>
        </div>

        <div class="comparison">
            <strong>Mechanism:</strong> T allele at -1639 <span class="explained">promoter: DNA "on/off switch"</span> reduces VKORC1 expression → less enzyme → more sensitive to warfarin blockage. Explains ~25-30% of dose variation.<a href="#ref47" class="ref">[47]</a>
        </div>

        <div class="comparison">
            <strong>Population Frequencies:</strong> T allele: Europeans 40%, East Asians 80-90%, Africans 10-15%. Explains why East Asians need lower doses.<a href="#ref47" class="ref">[47]</a>
        </div>

        <div class="action">
            <strong>📋 Actions:</strong> 1) Tell doctor about C/T genotype 2) Request pharmacogenetic dosing 3) Start ~4-5 mg/day (not 7.5-10) 4) Frequent INR monitoring initially 5) Watch for bleeding 6) Consistent vitamin K intake 7) Consider DOACs (apixaban, rivaroxaban)
        </div>
    </div>
</div>
```

### 🎨 UI/UX Requirements

**Colors:**
- Critical variants: Red border (#e74c3c), light red background (#fef5f5)
- High importance: Orange border (#f39c12), light orange background (#fffbf0)
- Protective variants: Green border (#27ae60), light green background (#eafaf1)
- Standard variants: Blue border (#3498db), white background

**Typography:**
- Gene names: 24-28px, bold
- Body text: 16-18px
- Comparisons: 15-17px
- Use clear hierarchy with appropriate sizing

**Spacing:**
- Reduce all padding/margins by ~30% compared to default
- Use compact line-height (1.6-1.8)
- Minimize empty space while maintaining readability

### ✅ Verification Checklist

Before finalizing GENOME_ANALYSIS.html, verify:

- [ ] Using `rsid_genome_analyzer_verified.py` database (NOT the old one)
- [ ] Every technical term explained inline (NO hover tooltips)
- [ ] Every comparison has specific numbers with units (hours, mg/day, %, fold-change)
- [ ] Every variant has at least 1-2 research citations
- [ ] Comprehensive references section with clickable links
- [ ] Dense UI with reduced whitespace
- [ ] Glossary section with all technical terms
- [ ] Mechanism explanations for key variants
- [ ] Population frequency data where relevant
- [ ] Specific actionable recommendations
- [ ] Examples in multiple measurement types (time, dose, risk ratios, percentages)

### 📚 Citation Template

When adding new variants, use this citation gathering process:

1. Search PharmGKB: `[variant rsID] [gene] [drug/condition] PharmGKB`
2. Search CPIC: `[gene] CPIC guideline [drug]`
3. Search PubMed: `[variant rsID] [phenotype] [year]`
4. Search PMC: `[gene name] [condition] [year]`
5. Always prefer peer-reviewed journal articles over websites
6. Include DOI or direct PMC/PMID link
7. Format: `<strong>Topic:</strong> Journal/Source (Year). "Title." <a href="URL">Read paper</a>`

### 🔄 Regeneration Command

To regenerate the comprehensive report:

```bash
# Use the verified database
uv run python rsid_genome_analyzer_verified.py

# Then manually enhance GENOME_ANALYSIS.html with:
# 1. Add inline explanations for every technical term
# 2. Add quantitative comparisons with real units
# 3. Add research citations for every variant
# 4. Add comprehensive references section
# 5. Optimize for dense UI
```

### ⚠️ Common Mistakes to Avoid

❌ **DON'T:**
- Use hover tooltips (`title=""` attributes)
- Say "increased risk" without specifying how much (need fold-change, percentage, or odds ratio)
- Say "slow metabolizer" without comparing times (need hours, half-lives)
- Leave terms unexplained (e.g., "acetylation" without defining it)
- Generate citations without actual web research
- Use the old `rsid_genome_analyzer.py` (has errors!)
- Create sparse layouts with lots of whitespace
- Forget the references section

✅ **DO:**
- Explain every term inline in parentheses
- Provide specific numbers: "6-8 hours vs 2.5-3.5 hours"
- Include multiple quantitative comparisons per variant
- Research and cite actual peer-reviewed papers
- Use the verified database (`rsid_genome_analyzer_verified.py`)
- Create dense, information-rich layouts
- Include comprehensive references section at bottom

---

## Database Maintenance

The verified database is in `rsid_genome_analyzer_verified.py` and contains:
- 25 pharmacogenomic variants (all verified with PharmGKB/CPIC)
- 20 clinical disease risk variants (all verified with ClinVar/journals)
- 30+ trait variants (all verified with genetics research)

**Critical fixes applied:**
- rs3918290 (DPYD): Changed from C>T to G>A ✓
- rs776746 (CYP3A5): Changed from G/A to T/C, fixed interpretation ✓
- rs12913832 (HERC2): Fixed eye color interpretation (G=blue, A=brown) ✓

**DO NOT** modify allele assignments without verifying against:
1. The actual VCF file (to see what ref/alt alleles are present)
2. PharmGKB or dbSNP (to verify allele orientation)
3. Multiple peer-reviewed publications

### Adding New Variants to the Database

**MANDATORY: All new variants MUST include research citations in comments**

When adding new variants to `rsid_genome_analyzer_verified.py`, follow this process:

#### 1. Research and Verification
For each variant, conduct thorough research:
- **Pharmacogenomic variants**: PharmGKB, CPIC guidelines, FDA labels
- **Disease risk variants**: ClinVar, GWAS catalog, journal articles
- **Trait variants**: Peer-reviewed genetics papers, population studies

#### 2. Citation Format in Database Comments
Add a comment block above each variant entry with citations:

```python
# rs1065852 (CYP2D6*4) - VERIFIED
# Major CYP2D6 loss-of-function allele affecting ~25% of drugs
# Sources:
# - PharmGKB: "CYP2D6 Frequency Tables" https://www.pharmgkb.org/
# - CPIC (2019): "Clinical Pharmacogenetics Implementation Consortium Guideline for CYP2D6 and CYP2C19 Genotypes and Dosing of Tricyclic Antidepressants"
#   PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC6977318/
# - Affects: Codeine (no pain relief), Tamoxifen (reduced efficacy), SSRIs, TCAs
# - Allele frequency: Europeans 12-21%, East Asians 0.5-1%, Africans 2-5%
'rs1065852': {
    'gene': 'CYP2D6', 'star': '*4',
    'drugs': 'Codeine, Tamoxifen, Antidepressants',
    'ref_allele': 'G', 'alt_allele': 'A',
    'if_het': 'Intermediate metabolizer - 50% reduced activity',
    'if_hom_alt': 'Poor metabolizer - No CYP2D6 activity',
    'importance': 'HIGH'},
```

#### 3. Required Information for Each Citation
Include in the comment block:
- **Verification status**: Mark as "VERIFIED" after research
- **Brief description**: 1-2 sentences explaining the variant
- **Sources section**: List all references with:
  - Database name or journal
  - Year (if applicable)
  - Title or description
  - Direct URL (PharmGKB, PMC, DOI, etc.)
- **Clinical relevance**: Drugs affected, phenotype, risk levels
- **Population frequencies**: By major ancestry groups

#### 4. Citation Sources (in priority order)
**Pharmacogenomics:**
1. CPIC guidelines (https://cpicpgx.org/)
2. PharmGKB (https://www.pharmgkb.org/)
3. FDA pharmacogenomic labels
4. NCBI Bookshelf Medical Genetics Summaries
5. Peer-reviewed pharmacogenomics journals

**Disease Risk:**
1. ClinVar (https://www.ncbi.nlm.nih.gov/clinvar/)
2. GWAS Catalog (https://www.ebi.ac.uk/gwas/)
3. NEJM, Nature, Science journals
4. Disease-specific databases (e.g., Alzforum for APOE)
5. Large population studies (UK Biobank, 23andMe research)

**Traits:**
1. Peer-reviewed genetics papers (PMC, Nature Genetics)
2. GWAS studies for specific traits
3. Population genetics papers
4. dbSNP annotations
5. Functional validation studies

#### 5. Verification Checklist
Before adding a variant, verify:
- [ ] At least 2 independent sources confirm the association
- [ ] Allele orientation matches the VCF reference genome (GRCh38/hg38)
- [ ] Effect sizes/risk estimates are quantified (not just "associated with")
- [ ] Population frequencies are documented
- [ ] Clinical or practical relevance is clear
- [ ] Sources are cited with direct URLs
- [ ] No conflicting evidence in recent literature

#### 6. Example: Complete Variant Entry with Citations

```python
# ============================================================================
# rs429358 + rs7412 (APOE ε4 allele) - VERIFIED
# ============================================================================
# Strongest genetic risk factor for late-onset Alzheimer's disease
#
# Sources:
# - Alzforum: "APOE Genetics" https://www.alzforum.org/mutations/apoe
# - Nature (2019): "APOE and Alzheimer disease: a major gene with semi-dominant inheritance"
#   https://www.nature.com/articles/s41593-019-0473-9
# - PMC (2020): "Dose-dependent effect of APOE ε4 on Alzheimer risk"
#   https://pmc.ncbi.nlm.nih.gov/articles/PMC7341278/
# - GWAS Catalog: https://www.ebi.ac.uk/gwas/variants/rs429358
#
# Allele determination (2 SNPs required):
# - rs429358 (C=ε4, T=ε3/ε2) + rs7412 (C=ε2, T=ε3/ε4)
# - ε2/ε2: Protective (0.6x risk)
# - ε3/ε3: Baseline risk (most common, 60% of population)
# - ε3/ε4: 3-4x increased risk (25% of population)
# - ε4/ε4: 8-15x increased risk (2-3% of population)
#
# Population frequencies (ε4 allele):
# - Europeans: 14-16%
# - East Asians: 8-10%
# - Africans: 19-25% (but lower penetrance)
# - Native Americans: 2-5%
#
# Note: Effect is age-dependent; risk increases with age
# Also affects: Cardiovascular disease risk, response to head injury
# ============================================================================
'rs429358': {
    'gene': 'APOE', 'variant': 'ε4 allele component',
    'condition': 'Alzheimer\'s Disease Risk', 'category': 'Disease Risk',
    'ref_allele': 'T', 'alt_allele': 'C',
    'requires_additional_snp': 'rs7412',  # Need both to determine allele
    'if_het': 'One ε4 allele: 3-4x increased AD risk (ε3/ε4)',
    'if_hom_alt': 'Two ε4 alleles: 8-15x increased AD risk (ε4/ε4)',
    'note': 'Risk is age-dependent; ε4/ε4 lifetime risk ~60% by age 85',
    'importance': 'HIGH'},
```

#### 7. Web Search Strategy for Citations
For each new variant, use this search sequence:

**Step 1 - Database Search:**
```
[rsID] [gene name] PharmGKB
[rsID] [gene name] ClinVar
[rsID] [gene name] dbSNP
```

**Step 2 - Guidelines Search:**
```
[gene name] CPIC guideline
[drug name] pharmacogenomics FDA label
[condition] genetic risk factors
```

**Step 3 - Literature Search:**
```
[rsID] [phenotype] 2020-2025
[gene name] [condition] meta-analysis
[gene name] GWAS [ancestry]
```

**Step 4 - Validation:**
```
[rsID] allele frequency
[rsID] functional validation
[gene name] [variant] mechanism
```

#### 8. Common Pitfalls to Avoid
❌ **Don't add variants without citations** - Every entry needs sources
❌ **Don't trust single sources** - Require 2+ independent confirmations
❌ **Don't confuse strands** - Verify ref/alt alleles against actual VCF
❌ **Don't use weak associations** - Require effect sizes/odds ratios
❌ **Don't cite websites without papers** - Link to actual research
❌ **Don't ignore ancestry differences** - Document population frequencies
❌ **Don't skip mechanism** - Understand WHY the variant matters

✅ **Do cite primary research** - Peer-reviewed journals preferred
✅ **Do verify alleles** - Check against VCF and dbSNP
✅ **Do quantify effects** - Include OR, RR, fold-change, percentages
✅ **Do include population data** - Allele frequencies by ancestry
✅ **Do document clinical utility** - Actionable information only
✅ **Do update regularly** - Re-verify with new publications
✅ **Do mark verification status** - "VERIFIED" tag in comments

---

## Incremental Report Update Pipeline

### 🔄 Overview

The genome analysis uses a **two-stage pipeline** to avoid regenerating the entire comprehensive report when adding new variants:

```
┌──────────────────────┐
│  Python Analyzer     │
│  (Basic Report)      │
└──────────┬───────────┘
           │
           │ Generates
           ▼
┌──────────────────────────────────┐
│  GENOME_ANALYSIS.html            │  ← Basic HTML (Python output)
│  GENOME_ANALYSIS_MANIFEST.json   │  ← Tracking file
└──────────┬───────────────────────┘
           │
           │ Claude processes
           ▼
┌──────────────────────────────────┐
│  GENOME_ANALYSIS_COMPREHENSIVE   │  ← Detailed HTML (Claude output)
│  .html                            │
└──────────────────────────────────┘
```

### 📋 File Descriptions

1. **GENOME_ANALYSIS.html** (from Python)
   - Basic report with all variants found in genome
   - Simple formatting, minimal detail
   - Generated by `rsid_genome_analyzer_verified.py`
   - **Intermediate file** - foundation for comprehensive report

2. **GENOME_ANALYSIS_MANIFEST.json** (from Python)
   - Lists all variants currently analyzed
   - Includes rsID, category, gene, position, genotype
   - Used to detect NEW variants when database is updated
   - Enables incremental updates
   - **Also embedded** in GENOME_ANALYSIS.html for self-contained tracking

3. **GENOME_ANALYSIS_COMPREHENSIVE.html** (from Claude)
   - Fully detailed report with all variants
   - Inline explanations, quantitative comparisons, citations
   - Created/updated by Claude Code based on basic HTML

### 🚀 Pipeline Workflows

#### **Workflow 1: Initial Comprehensive Report (First Time)**

```bash
# Step 1: Run Python analyzer
python rsid_genome_analyzer_verified.py

# Output:
# - GENOME_ANALYSIS.html (26 variants, basic)
# - GENOME_ANALYSIS_MANIFEST.json (tracking)

# Step 2: Ask Claude to create comprehensive report
# "Create comprehensive report from GENOME_ANALYSIS.html"
```

**Claude's task:**
- Read GENOME_ANALYSIS.html to see all variants
- Process ALL 26 variants with full comprehensive detail
- Generate GENOME_ANALYSIS_COMPREHENSIVE.html
- Follow all requirements from sections above (inline explanations, quantitative data, citations)

#### **Workflow 2: Incremental Update (After Adding New Variants)**

```bash
# Step 1: Update database (add new variants to rsid_genome_analyzer_verified.py)
# Step 2: Run Python analyzer again
python rsid_genome_analyzer_verified.py

# Output:
# - GENOME_ANALYSIS.html (now has 30 variants instead of 26)
# - GENOME_ANALYSIS_MANIFEST.json (updated with 30 variants)
# - Backups: GENOME_ANALYSIS.2025-12-31_14-30-00.html (old version)

# Step 3: Ask Claude to incrementally update
# "Incrementally update comprehensive report with new variants"
```

**Claude's task for incremental update:**
1. Read OLD manifest (GENOME_ANALYSIS_MANIFEST.2025-12-31_14-30-00.json) to see what was previously analyzed
2. Read NEW manifest (GENOME_ANALYSIS_MANIFEST.json) to see current variants
3. **Identify NEW variants** = variants in new manifest but NOT in old manifest
4. Read existing GENOME_ANALYSIS_COMPREHENSIVE.html
5. Process ONLY the NEW variants with full comprehensive detail
6. Insert new variants into existing comprehensive HTML in appropriate sections
7. Update file metadata (total count, generation date)
8. **DO NOT regenerate** existing variants - keep them as-is

### 📝 Instructions for Incremental Updates

**When user says "incrementally update" or "add new variants to comprehensive report":**

#### Step 1: Identify New Variants

**Manifests are embedded in HTML files** as `<script type="application/json" id="genome-manifest">`.

```python
# Extract manifest from HTML files
import re
import json

def extract_manifest_from_html(html_path):
    """Extract embedded manifest from HTML file"""
    with open(html_path) as f:
        html = f.read()

    # Find manifest in <script type="application/json" id="genome-manifest">
    pattern = r'<script type="application/json" id="genome-manifest">\s*\n(.*?)</script>'
    match = re.search(pattern, html, re.DOTALL)

    if match:
        manifest_json = match.group(1)
        return json.loads(manifest_json)
    return None

# Find old HTML backup (has manifest embedded)
old_html = "GENOME_ANALYSIS.2025-12-31_14-30-00.html"  # Latest backup
new_html = "GENOME_ANALYSIS.html"  # Current

# Extract manifests from HTML
old_manifest = extract_manifest_from_html(old_html)
new_manifest = extract_manifest_from_html(new_html)

# Compare variant lists
old_variants = set(old_manifest['variant_details'].keys())
new_variants = set(new_manifest['variant_details'].keys())
added_variants = new_variants - old_variants

# Example output:
# Added: rs1142345, rs8175347, rs671, rs1801282
# (4 new variants to process)
```

**Note**: Manifests are also written as separate JSON files for convenience with external tools.

#### Step 2: Get Variant Details

For each NEW variant:
- Read from GENOME_ANALYSIS.html to get user's genotype
- Read from rsid_genome_analyzer_verified.py database to get citations and details
- Determine category (pharmacogenomic/clinical/traits)

#### Step 3: Process New Variants

For each NEW variant, create comprehensive section following standard format:
- Inline explanations for all technical terms
- 3-5 quantitative comparison boxes with real units
- Research citations with links
- Mechanism explanations
- Population frequencies
- Practical recommendations

#### Step 4: Insert into Existing HTML

**Critical: INSERT, don't replace**

Find the appropriate section in GENOME_ANALYSIS_COMPREHENSIVE.html:
- Pharmacogenomic variants → Insert in `<h2>💊 Pharmacogenomics</h2>` section
- Clinical variants → Insert in `<h2>🏥 Clinical Health</h2>` section
- Trait variants → Insert in appropriate trait category

**Insertion strategy:**
- Maintain alphabetical or importance-based ordering within category
- Insert complete `<div class="variant">...</div>` block
- Update section headers if needed (e.g., "(5 variants)" → "(6 variants)")
- Add new references to the References section at bottom

#### Step 5: Update Metadata

Update the footer section:
```html
<strong>Report Generated:</strong> 2025-12-31 (Updated)<br>
<strong>Total Variants in Report:</strong> 30 (5 pharmacogenomic, 4 clinical, 21 traits)<br>
```

### ⚙️ Helper Script for Detecting New Variants

Created: `detect_new_variants.py`

```python
#!/usr/bin/env python3
"""
Detect new variants by comparing manifest files.
Usage: python detect_new_variants.py
"""
import json
import glob
import os

def find_latest_backup_manifest():
    """Find most recent backup manifest"""
    backups = glob.glob("GENOME_ANALYSIS_MANIFEST.*.json")
    if not backups:
        return None
    # Sort by modification time
    backups.sort(key=os.path.getmtime, reverse=True)
    return backups[0]

def main():
    # Find files
    current_manifest = "GENOME_ANALYSIS_MANIFEST.json"
    old_manifest_file = find_latest_backup_manifest()

    if not os.path.exists(current_manifest):
        print("❌ No current manifest found. Run analyzer first.")
        return

    if not old_manifest_file:
        print("📝 No previous manifest found. This is the first run.")
        print("   All variants will need comprehensive processing.")
        with open(current_manifest) as f:
            data = json.load(f)
        print(f"\n   Total variants: {data['total_variants']}")
        return

    # Load manifests
    with open(current_manifest) as f:
        current = json.load(f)
    with open(old_manifest_file) as f:
        old = json.load(f)

    # Compare
    old_variants = set(old['variant_details'].keys())
    new_variants = set(current['variant_details'].keys())
    added = new_variants - old_variants
    removed = old_variants - new_variants

    print(f"📊 Comparing manifests:")
    print(f"   Old: {old_manifest_file} ({len(old_variants)} variants)")
    print(f"   New: {current_manifest} ({len(new_variants)} variants)")
    print(f"\n{'='*60}")

    if added:
        print(f"\n✅ NEW variants to process ({len(added)}):")
        for rsid in sorted(added):
            details = current['variant_details'][rsid]
            print(f"   • {rsid} ({details['gene']}) - {details['category']}")
        print(f"\n💡 To update comprehensive report:")
        print(f"   Tell Claude: 'Incrementally update comprehensive report'")
        print(f"   Claude will process only these {len(added)} new variants.")
    else:
        print("\n✓ No new variants detected.")

    if removed:
        print(f"\n⚠️  Removed variants ({len(removed)}):")
        for rsid in sorted(removed):
            details = old['variant_details'][rsid]
            print(f"   • {rsid} ({details['gene']})")
        print(f"\n   These should be removed from comprehensive report.")

    print(f"\n{'='*60}")

if __name__ == "__main__":
    main()
```

### 🎯 Example Session

```bash
# Initial setup
$ python rsid_genome_analyzer_verified.py
✅ VERIFIED REPORT GENERATED!
📄 GENOME_ANALYSIS.html
📋 GENOME_ANALYSIS_MANIFEST.json (for incremental updates)

💡 To create comprehensive report:
   Run: Claude, create comprehensive report from GENOME_ANALYSIS.html

# User to Claude: "Create comprehensive report from GENOME_ANALYSIS.html"
# Claude processes all 26 variants → GENOME_ANALYSIS_COMPREHENSIVE.html

# Later: Add 4 new variants to database
# Edit rsid_genome_analyzer_verified.py (add rs1142345, rs8175347, rs671, rs1801282)

$ python rsid_genome_analyzer_verified.py
📦 Backed up existing file to: GENOME_ANALYSIS.2025-12-31_14-30-00.html
📦 Backed up existing file to: GENOME_ANALYSIS_MANIFEST.2025-12-31_14-30-00.json
✅ VERIFIED REPORT GENERATED!
📄 GENOME_ANALYSIS.html (now 30 variants)

$ python detect_new_variants.py
📊 Comparing manifests:
   Old: GENOME_ANALYSIS_MANIFEST.2025-12-31_14-30-00.json (26 variants)
   New: GENOME_ANALYSIS_MANIFEST.json (30 variants)

✅ NEW variants to process (4):
   • rs1142345 (TPMT) - pharmacogenomic
   • rs8175347 (UGT1A1) - pharmacogenomic
   • rs671 (ALDH2) - traits
   • rs1801282 (PPARG) - clinical

💡 To update comprehensive report:
   Tell Claude: 'Incrementally update comprehensive report'
   Claude will process only these 4 new variants.

# User to Claude: "Incrementally update comprehensive report"
# Claude:
#  1. Detects 4 new variants by comparing manifests
#  2. Processes only those 4 with full comprehensive detail
#  3. Inserts them into existing GENOME_ANALYSIS_COMPREHENSIVE.html
#  4. Updates metadata (26 → 30 variants)
#  5. DOES NOT regenerate the 26 existing variants
```

### 🔍 Detection Algorithm

Claude should use this algorithm for incremental updates:

```python
def detect_new_variants():
    # 1. Find backup manifest
    backups = glob.glob("GENOME_ANALYSIS_MANIFEST.*.json")
    if not backups:
        return "FULL_GENERATION_NEEDED"
    latest_backup = max(backups, key=os.path.getmtime)

    # 2. Load manifests
    with open(latest_backup) as f:
        old_manifest = json.load(f)
    with open("GENOME_ANALYSIS_MANIFEST.json") as f:
        new_manifest = json.load(f)

    # 3. Compare
    old_rsids = set(old_manifest['variant_details'].keys())
    new_rsids = set(new_manifest['variant_details'].keys())
    added_rsids = new_rsids - old_rsids

    # 4. Get details for new variants
    new_variants = []
    for rsid in added_rsids:
        details = new_manifest['variant_details'][rsid]
        new_variants.append({
            'rsid': rsid,
            'category': details['category'],
            'gene': details['gene'],
            'genotype': details['genotype']
        })

    return new_variants
```

### ✅ Benefits of Incremental Updates

1. **Speed**: Process 4 new variants in 2 minutes instead of regenerating all 30 in 15 minutes
2. **Consistency**: Existing variants stay exactly as reviewed/approved
3. **Version control**: Old versions are backed up with timestamps
4. **Tracking**: Manifest makes it explicit what's been processed
5. **Scalability**: Works efficiently as database grows to 100+ variants

---

Last updated: 2025-12-31
Database version: verified v1.0
Pipeline version: incremental v1.0
