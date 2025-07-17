# Hi there, I'm Ugochi Ndubuisi 👋

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=2E97F7&center=true&vCenter=true&width=435&lines=DHSc,+MT(AMT),+MB(ASCP);Bioinformatics+Developer;NGS+Data+Analyst;Johns+Hopkins+University" alt="Typing SVG" />
</div>

## 🧬 About Me

Healthcare professional and bioinformatics developer at Kaiser Permanente, transforming clinical insights through computational genomics. Currently pursuing MS in Biotechnology at Johns Hopkins University (2024-2026), I specialize in NGS data analysis, gene prediction, and developing Python tools for genomic research.

🏥 **Current Role**: Kaiser Permanente - Integrating bioinformatics into clinical workflows 
🎓 **Education**: DHSc, MS Biotechnology (JHU, in progress) 
💻 **Focus**: NGS variant analysis, gene prediction, disease-gene networks 
🧬 **Achievement**: Identified 20 mitochondrial genes linked to neurological disorders 

## 🛠️ Technical Stack

### Bioinformatics & Genomics
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![BioPython](https://img.shields.io/badge/BioPython-4B8BBE?style=for-the-badge&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)
![biomaRt](https://img.shields.io/badge/biomaRt-276DC3?style=for-the-badge&logo=r&logoColor=white)

### NGS & Analysis Tools
![VEP](https://img.shields.io/badge/Ensembl_VEP-86B817?style=for-the-badge)
![BLAST](https://img.shields.io/badge/BLAST-336791?style=for-the-badge)
![Glimmer](https://img.shields.io/badge/Glimmer3-FF6900?style=for-the-badge)
![gnomAD](https://img.shields.io/badge/gnomAD-4169E1?style=for-the-badge)

### Clinical & Laboratory
![Medical Technology](https://img.shields.io/badge/MT(AMT)-FF4500?style=for-the-badge)
![Molecular Biology](https://img.shields.io/badge/MB(ASCP)-4B0082?style=for-the-badge)
![Lean Six Sigma](https://img.shields.io/badge/Lean_Six_Sigma-FFC000?style=for-the-badge)

## 📊 GitHub Stats & Activity

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=ugochi141&show_icons=true&theme=tokyonight" alt="GitHub Stats" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=ugochi141&theme=tokyonight" alt="GitHub Streak" />
</div>

## 🔬 Featured Bioinformatics Projects

### 🧬 [NGS Variant Analysis Pipeline](https://github.com/ugochi141/ngs-variant-analysis)
Comprehensive pipeline for analyzing patient variants using VEP, gnomAD, and ClinVar
- **Tech**: Python, Ensembl VEP, matplotlib
- **Impact**: Automated variant classification for clinical interpretation
- **Key Finding**: Novel variant chr6:15241774 A>G characterized as VUS

### 🧪 [Mitochondrial-Neurological Gene Discovery](https://github.com/ugochi141/mito-neuro-genes)
Database mining project identifying disease associations in 2,847 mitochondrial genes
- **Results**: 20 high-confidence genes linked to neurological disorders
- **Conditions**: Leber Optic Atrophy, MELAS, Charcot-Marie-Tooth
- **Clinical Impact**: 60% are current drug targets

### 🔍 [Bacterial Gene Prediction Suite](https://github.com/ugochi141/gene-prediction-tools)
Glimmer3-based pipeline for prokaryotic gene prediction and functional annotation
- **Organism**: Halanaerobium sp. MDAL1
- **Findings**: 4 genes predicted, 86.3% coding density
- **Validation**: BLAST revealed truncated predictions, improving accuracy

### 💊 [HTT Gene Analysis Tool](https://github.com/ugochi141/huntington-analysis)
biomaRt-based tool for analyzing Huntington's disease CAG repeats
- **Features**: Automated repeat counting, penetrance classification
- **Database**: Integration with Ensembl and OMIM
- **Application**: Clinical genetic counseling support

# 🤖 Bioinformatics Python Toolkit

A collection of Python scripts for sequence analysis and data visualization in bioinformatics.

## Features

- DNA sequence analysis
- RNA transcription
- GC content calculation
- Motif finding
- And more...

## Example Usage

```python
from dna_tools import analyze_sequence

dna = "ATGGGCCGCAGTAATTGA"
result = analyze_sequence(dna)
print(result)
