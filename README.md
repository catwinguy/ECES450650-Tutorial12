# Tutorial 12: MetaPhlAn (and Humann)

## About Us

Team Members: Zoe Sucato, Catherine Nguyen, and Tobenna Oduah

Organization: Drexel University

Course: ECES 450/650 - Statistical Analysis of Metagenomics

Last Updated: May 26, 2022

## Description

In the [presentation](https://docs.google.com/presentation/d/1OATd0aiiLBT8dHkw8y5ogU3HX3HEDCAFWVoMfOvPLKo/edit?usp=sharing) included within this respository, we discussed MetaPhlAn and Humann, specifically their brief descriptions and how they work.

## Step-by-Step Instructions for Running MetaPhlAn

1. First, git clone this repository onto your local machine.

2. The dataset (```evol1.sorted.unmapped.R1.fastq.gz```) we used can be found in the ```dataset``` folder.
    
    2a. This file has the ```.fastq.gz``` extension, but you can also use any files with the ```.fastq``` extension.

3. Navigate to [Galaxy Hutlab](https://huttenhower.sph.harvard.edu/galaxy/).

4. Run MetaPhlAn2 (step-by-step instructions are included in the presentation).

5. Visualize MetaPhlAn2's output (TBD).

Our resulting MetaPhlAn file is lcoated in the ```output``` folder.

### Getting visualization for one sample output file
1. With your metaphlan output in the same directory, run map.py.
2. This outputs an excel sheet with the top 5 reads.
3. Highlight both rows of data and click Insert.
4. Select any type of chart style desired.
