## Automated Peptide Filtration for Immunoinformatics.

A reproducible Python-based workflow for automated peptide processing and filtration in immunoinformatics-based vaccine prediction studies.
<img width="1536" height="1024" alt="Automated Peptide Filtration" src="https://github.com/user-attachments/assets/fb48394c-4fd8-471c-831e-c6e972347fbc" />


 ## Overview
This repository provides a **post-publication computational workflow** developed to automate a peptide-processing and filtration step associated with the methodology described in the **published study:** [Epitope-Based Peptide Vaccine Against Glycoprotein GPC Precursor of *Lujo Virus* Using Immunoinformatics Approaches]([url](https://journalspress.com/epitope-based-peptide-vaccine-against-glycoprotein-gpc-precursor-of-lujo-virus-using-immunoinformatics-approaches/)

## Published article:
**Arwa A. Mohammed, Mayada E. Elkhalifa, Khadija E. Elamin, Rawan A. Mohammed, Musab E. Ibrahim, Amina I. Dirar, Sara H. Migdar, Maha A. H. Musa, Emeirii H. Elawad, Salam O. Abdelsalam & Mohamed A. Hassan. (2023).** Epitope-based Peptide Vaccine against Glycoprotein GPC Precursor of *Lujo Virus* using Immunoinformatics Approaches. Great Britain Journal Press, 23(2).

The published study investigated an epitope-based vaccine candidate against the Lujo virus glycoprotein GPC precursor using immunoinformatics approaches, including B-cell and T-cell epitope prediction, population coverage analysis, and molecular docking.

This repository focuses specifically on **automating peptide processing and filtration** associated with that computational methodology. The workflow transforms peptide data into **structured and standardized datasets** suitable for subsequent peptide selection and downstream immunoinformatics analysis.

Additionally, provides Python scripts, example input and output datasets, and supplementary workflow documentation to facilitate reproducibility and demonstrate how the computational steps can be applied.

## Workflow
The computational workflow consists of sequential peptide-processing steps:

1- Peptide–HLA association data
            │
            ▼
     group_peptides.py
            │
            ▼
Peptide_grouping and unique allele counting
            │
            ▼
   Grouped peptide dataset

   2- 
            │
            ▼
     truncate_peptides.py
            │
            ▼
Fixed-length peptide processing
            │
            ▼
     Processed peptides
            │
            ▼
Subsequent peptide filtration

[peptide_filtration_workflow.pdf](https://github.com/user-attachments/files/31126524/peptide_filtration_workflow.pdf)

and immunoinformatics analysis

The individual scripts are designed as modular components so that each processing step can be reproduced independently or incorporated into a larger computational workflow.
