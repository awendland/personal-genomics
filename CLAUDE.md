# Genome Analysis Report Instructions

## Update Command

**User says:** `Update comprehensive genome report`

**Claude will:**
1. Check if `analyses/GENOME_ANALYSIS_COMPREHENSIVE.html` exists
2. If not → Full generation (process ALL variants)
3. If yes → Compare manifests to find new variants:
   - 0 new → "Report is up to date"
   - 1-5 new → Incremental update (add only new variants)
   - >5 new → Suggest full regeneration
4. Show what will happen before proceeding

---

## Critical Rules

### 1. NEVER TRUNCATE
- Process ALL variants with FULL detail
- If there are 30 variants, process all 30 completely
- Large files (100KB+) are expected and correct
- DO NOT summarize, skip, or use "and X more..."

### 2. ONE FORMAT FOR ALL VARIANTS
**Every variant (pharmacogenomics, clinical, AND traits) uses the SAME full format.**
There is NO simplified format. NO exceptions.

### 3. Use Verified Database
Always use `rsid_genome_analyzer_verified.py` (not the old unverified one).

---

## Variant Format (ALL variants use this)

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
            <div><span class="info-label">Effect Allele:</span> G allele description</div>
        </div>

        <div class="key-paper">
            <strong>📄 Key Research Paper:</strong> Author, Journal Year. "Title"
            <a href="URL" target="_blank">[Read Full Paper]</a>
        </div>

        <div class="verify-box">
            <strong>🔬 Verify This Variant:</strong><br>
            <code>gzip -dc data/MDNRTM4FA.hard-filtered.vcf.gz | awk '$1=="chrX" && $2==POSITION {print $1":"$2, $3, $4">"$5, "Genotype:", substr($10,1,3)}'</code>
        </div>

        <div class="meaning-box">
            <div class="meaning-title">🎯 What This Means For YOU:</div>
            Detailed explanation with <span class="explained">term: definition</span> inline.
            <a href="#refN" class="ref">[N]</a>
        </div>

        <div class="comparison">
            <strong>Quantitative Comparison:</strong><br>
            • Genotype 1: X units<br>
            • Genotype 2 (YOU): Y units<br>
            • Genotype 3: Z units<a href="#refN" class="ref">[N]</a>
        </div>

        <div class="comparison">
            <strong>Mechanism:</strong> How this variant works biologically.
            <a href="#refN" class="ref">[N]</a>
        </div>

        <div class="comparison">
            <strong>Population Frequency:</strong> X% Europeans, Y% East Asians, Z% Africans.
            <a href="#refN" class="ref">[N]</a>
        </div>

        <div class="action">
            <strong>📋 Action:</strong> Specific recommendations (if applicable)
        </div>
    </div>
</div>
```

---

## Content Requirements

### Inline Explanations
Every technical term explained inline:
```html
<span class="explained">acetylation: adding acetyl group to drugs for breakdown</span>
```

### Quantitative Data (REQUIRED)
Never say "increased" or "slow" without numbers:
- Times: "6-8 hours vs 2.5-3.5 hours"
- Doses: "4-5 mg/day (25-30% lower)"
- Risks: "3-4x increased risk" or "OR 1.5 (50% higher)"
- Activity: "65% enzyme activity (35% reduced)"

### Citations
- Use inline refs: `<a href="#ref1" class="ref">[1]</a>`
- Every variant needs 1-2 citations minimum
- Include References section at bottom with clickable links

### Each Variant Must Have
- [ ] Key research paper box
- [ ] Verification command box
- [ ] Meaning box with inline term explanations
- [ ] 2-3 comparison boxes with quantitative data
- [ ] At least one citation reference

---

## Complete Example: HERC2 Eye Color (Trait)

```html
<div class="variant">
    <div class="variant-header">
        <div><span class="gene">HERC2 (OCA2 Regulatory Region)</span></div>
        <span class="rsid">rs12913832 | chr15:28120472</span>
        <span class="genotype hom">YOU HAVE: 1/1</span>
    </div>

    <div class="variant-body">
        <div class="variant-info">
            <div><span class="info-label">Trait:</span> Eye Color</div>
            <div><span class="info-label">Your Genotype:</span> G/G (homozygous)</div>
            <div><span class="info-label">Effect:</span> G allele reduces OCA2 expression → blue eyes</div>
        </div>

        <div class="key-paper">
            <strong>📄 Key Research Paper:</strong> PMC 2023. "Association between OCA2-HERC2 Variants and Blue Eye Colour"
            <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10048254/" target="_blank">[Read Full Paper]</a>
        </div>

        <div class="verify-box">
            <strong>🔬 Verify This Variant:</strong><br>
            <code>gzip -dc data/MDNRTM4FA.hard-filtered.vcf.gz | awk '$1=="chr15" && $2==28120472 {print $1":"$2, $3, $4">"$5, "Genotype:", substr($10,1,3)}'</code>
        </div>

        <div class="meaning-box">
            <div class="meaning-title">🎯 What This Means For YOU:</div>
            You have two G alleles at rs12913832, the <span class="explained">strongest genetic predictor of eye color: explains 74% of European eye color variation</span>. G/G reduces expression of <span class="explained">OCA2: gene producing melanin pigment in iris</span>, resulting in <strong>blue eyes with 99% prediction accuracy</strong>.<a href="#ref27" class="ref">[27]</a>
        </div>

        <div class="comparison">
            <strong>Eye Color Prediction by Genotype:</strong><br>
            • A/A: Brown eyes (85-95% accuracy)<br>
            • A/G: Green/hazel eyes (intermediate melanin)<br>
            • <strong>G/G (YOU): Blue eyes (99% accuracy)</strong><a href="#ref27" class="ref">[27]</a>
        </div>

        <div class="comparison">
            <strong>Mechanism:</strong> rs12913832 is in the <span class="explained">intron: non-coding DNA region</span> of HERC2, acting as an <span class="explained">enhancer: regulatory switch controlling nearby genes</span>. G allele creates weaker enhancer → less OCA2 transcription → less melanin in iris → blue eyes.<a href="#ref28" class="ref">[28]</a>
        </div>

        <div class="comparison">
            <strong>Population Frequency:</strong> G allele: 80% Northern Europeans, 50% Southern Europeans, 5% East Asians, <1% sub-Saharan Africans. Blue eyes originated ~10,000 years ago near Black Sea.<a href="#ref27" class="ref">[27]</a>
        </div>
    </div>
</div>
```

---

## CSS (include in report)

```css
.variant { background: white; border: 2px solid #e0e0e0; border-left: 5px solid #3498db; padding: 20px; margin: 20px 0; border-radius: 8px; }
.critical { border-left-color: #e74c3c; background: #fef5f5; }
.high { border-left-color: #f39c12; background: #fffbf0; }
.positive { border-left-color: #27ae60; background: #eafaf1; }
.gene { font-size: 24px; font-weight: bold; color: #2c3e50; }
.rsid { color: #7f8c8d; font-family: monospace; font-size: 15px; }
.genotype { background: #34495e; color: white; padding: 6px 14px; border-radius: 5px; font-family: monospace; font-size: 18px; font-weight: bold; display: inline-block; margin: 12px 0; }
.het { background: #f39c12; }
.hom { background: #e74c3c; }
.meaning-box { background: #fff9e6; border: 2px solid #ffd700; padding: 16px; margin: 12px 0; border-radius: 6px; }
.comparison { background: #e8f4f8; border-left: 4px solid #3498db; padding: 14px; margin: 10px 0; border-radius: 5px; }
.explained { background: #ffe5b4; padding: 2px 5px; border-radius: 3px; font-style: italic; }
.ref { color: #3498db; text-decoration: none; font-weight: 600; font-size: 14px; }
.action { background: #fff3cd; border: 2px solid #ffc107; padding: 14px; margin: 10px 0; border-radius: 5px; }
.verify-box { background: #f0f4f8; border: 2px solid #4a90e2; padding: 12px; margin: 10px 0; border-radius: 5px; font-family: monospace; font-size: 13px; }
.key-paper { background: #e8f5e9; border-left: 4px solid #4caf50; padding: 12px; margin: 10px 0; border-radius: 5px; }
.key-paper a { color: #2e7d32; font-weight: 600; }
```

---

## Key Research Paper Sources

**Pharmacogenomics:** PharmGKB, CPIC guidelines, NCBI Bookshelf
**Disease Risk:** ClinVar, GWAS Catalog, NEJM, Nature
**Traits:** PMC, Nature Genetics, population studies

Example URLs:
- HLA-B*15:02: https://www.nejm.org/doi/full/10.1056/NEJMoa1009717
- CYP3A5: https://www.pharmgkb.org/gene/PA131
- HERC2: https://pmc.ncbi.nlm.nih.gov/articles/PMC10048254/
- ACTN3: https://pubmed.ncbi.nlm.nih.gov/12879365/
- COMT: https://www.pnas.org/doi/10.1073/pnas.0601443103

---

## Database Maintenance

**Adding new variants to `rsid_genome_analyzer_verified.py`:**

1. Research: PharmGKB/CPIC (pharma), ClinVar/GWAS (clinical), PMC (traits)
2. Verify alleles match VCF reference genome (GRCh38)
3. Require 2+ independent sources
4. Include citations in database comments:

```python
# rs12913832 (HERC2) - VERIFIED
# Strongest predictor of eye color (74% of variation)
# Sources:
# - PMC 10048254: "OCA2-HERC2 and Blue Eye Colour"
# - dbSNP: https://www.ncbi.nlm.nih.gov/snp/rs12913832
# G=blue (reduces OCA2), A=brown
'rs12913832': {...}
```

---

## Incremental Update Process

When doing incremental updates:
1. Compare manifests (embedded in HTML or .json files)
2. Identify NEW variants only
3. Process each new variant with FULL format (same as above)
4. Insert into existing comprehensive HTML in appropriate section
5. Add new references to References section
6. Update metadata (variant counts, date)

**Never regenerate existing variants** - keep approved content as-is.

---

## Common Mistakes

❌ Using simplified format for traits (NO - use full format)
❌ Missing key-paper or verify-box
❌ "Increased risk" without numbers
❌ Terms without inline explanations
❌ Missing citations

✅ Every variant has same full format
✅ Quantitative data in every comparison
✅ Inline explanations for technical terms
✅ Research citations with links
