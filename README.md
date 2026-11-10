## Automated Peptide Processing and Filtration for Immunoinformatics.

A reproducible Python-based workflow for automated peptide processing and filtration in immunoinformatics-based vaccine prediction studies.
<img width="1536" height="1024" alt="Automated Peptide Filtration" src="https://github.com/user-attachments/assets/fb48394c-4fd8-471c-831e-c6e972347fbc" />


 ## Overview
This repository presents an open-source Python workflow developed after the publication of the study, Epitope-Based Peptide Vaccine Against Glycoprotein GPC Precursor of Lujo Virus Using Immunoinformatics Approaches.

Building on the peptide-processing and filtration steps used in the published study, this workflow automates repetitive data-processing tasks applied to IEDB prediction outputs, including peptide truncation and peptide–HLA association grouping with unique HLA allele counting (NOI). The resulting datasets are organized to facilitate the subsequent manual selection of candidate peptides and downstream immunoinformatics analyses.

The workflow was developed to improve processing efficiency, reproducibility, and scalability while reducing the time required for repetitive manual operations.

## Published article:
**Arwa A. Mohammed, Mayada E. Elkhalifa, Khadija E. Elamin, Rawan A. Mohammed, Musab E. Ibrahim, Amina I. Dirar, Sara H. Migdar, Maha A. H. Musa, Emeirii H. Elawad, Salam O. Abdelsalam & Mohamed A. Hassan. (2023).** Epitope-based Peptide Vaccine against Glycoprotein GPC Precursor of *Lujo Virus* using Immunoinformatics Approaches. Great Britain Journal Press, 23(2).
([url](https://journalspress.com/epitope-based-peptide-vaccine-against-glycoprotein-gpc-precursor-of-lujo-virus-using-immunoinformatics-approaches/)


The published study investigated an epitope-based vaccine candidate against the Lujo virus glycoprotein GPC precursor using immunoinformatics approaches, including B-cell and T-cell epitope prediction, population coverage analysis, and molecular docking.

This repository focuses specifically on **automating peptide processing and filtration** associated with that computational methodology. The workflow transforms peptide data into **structured and standardized datasets** suitable for subsequent peptide selection and downstream immunoinformatics analysis.

Additionally, provides Python scripts, example input and output datasets, and supplementary workflow documentation to facilitate reproducibility and demonstrate how the computational steps can be applied.

## Workflow
The computational workflow consists of sequential peptide-processing steps:

<img width="1024" height="1536" alt="Workflow" src="https://github.com/user-attachments/assets/e35224d9-6392-4c3e-9e60-0dacfc44b82f" />

The individual scripts are designed as modular components, allowing each processing step to be reproduced independently or incorporated into a larger computational workflow.

## Example Data

**Important:** The datasets included in this repository are **example datasets created to demonstrate and reproduce the computational workflow.** They are not the original peptide datasets used in the published study.

The example data are designed to represent the type of input and output encountered in the workflow while allowing users to understand how the scripts operate without requiring access to the original study data.

**For example:**
raw_peptide_truncate_input.csv → example input for peptide truncation
conical_peptides_output.csv → example processed peptide output
raw_peptides_input.csv → example peptide–HLA association input
peptide_allele_aggregator_output.csv → example peptide–HLA aggregation output

These datasets are provided for demonstration, testing, and reproducibility of the computational concept only.

## Repository Structure
<img width="1024" height="1536" alt="Repository Structure" src="https://github.com/user-attachments/assets/e6ee39bd-b6d3-42fd-8074-46174e108915" />

## Workflow PDF documentation

[peptide_filtration_workflow.pdf](https://github.com/user-attachments/files/31701064/peptide_filtration_workflow.pdf)
