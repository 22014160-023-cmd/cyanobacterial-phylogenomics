# Cyanobacterial Phylogenomics

## Analysis Overview

Phylogenomic analysis of 8 cyanobacterial genomes using single-copy core protein orthologs.

## Analysis Statistics

| Metric | Value |
|---|---:|
| Genomes analyzed | 8 |
| Total orthogroups | 3,997 |
| Single-copy core orthologs | 228 |
| Concatenated alignment | 96,612 positions |
| Phylogenetic model | Q.pfam+G4 |
| Bootstrap replicates | 1,000 |
| SH-aLRT replicates | 1,000 |

## Workflow

1. OrthoFinder
2. Single-copy core ortholog extraction
3. MAFFT multiple sequence alignment
4. Concatenation of core protein alignments
5. IQ-TREE phylogenetic reconstruction
6. Bootstrap and SH-aLRT support estimation

## Repository Structure

```text
cyanobacterial-phylogenomics/
├── results/
│   ├── trees/
│   ├── alignments/
│   │   └── Core_Orthologs/
│   ├── figures/
│   └── tables/
├── data/
│   ├── genomes/
│   └── proteins/
├── scripts/
├── docs/
├── README.md
└── .gitignore
```

## Main Tree

The main phylogenetic tree is:

`results/trees/Cyanobacterial_Core_Phylogeny.treefile`

The tree is in Newick format and can be visualized with iTOL, FigTree, MEGA, or other compatible software.

## Core Orthologs

The analysis identified 228 single-copy core orthologs shared across the 8 cyanobacterial genomes.

These orthologs were aligned and concatenated into a 96,612-position protein supermatrix.

## Phylogenetic Analysis

IQ-TREE was used for maximum-likelihood phylogenetic inference with ModelFinder, 1,000 ultrafast bootstrap replicates, and 1,000 SH-aLRT replicates.

Best-fit model: Q.pfam+G4

## Software

- OrthoFinder
- MAFFT
- IQ-TREE

## Future Work

- Expand the cyanobacterial dataset
- Comparative genomics
- Gene family expansion/contraction
- Horizontal gene transfer analysis
- Functional annotation
- Evolutionary interpretation

## Contact

Author: 22014160-023-cmd

Generated: 2026-08-20 07:55:32