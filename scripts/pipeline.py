#!/usr/bin/env python3

"""
Cyanobacterial Phylogenomics Pipeline

OrthoFinder -> Core Genes -> MAFFT -> IQ-TREE
"""

import subprocess


def run_pipeline(genome_dir, output_dir):
    print('Running cyanobacterial phylogenomics pipeline...')

    print('Step 1: Running OrthoFinder...')
    subprocess.run(
        ['orthofinder', '-f', genome_dir, '-t', '4', '-a', '4'],
        check=True
    )

    print('Step 2: Extracting core genes...')
    # Core-gene extraction code goes here.

    print('Step 3: Running MAFFT...')
    # MAFFT alignment code goes here.

    print('Step 4: Running IQ-TREE...')
    # IQ-TREE code goes here.

    print('Pipeline complete!')


if __name__ == '__main__':
    run_pipeline('data/genomes', 'results')