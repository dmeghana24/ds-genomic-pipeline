#!/bin/bash
bwa mem ref.fa ../data/mock_wgs_R1.fastq ../data/mock_wgs_R2.fastq | samtools sort -o ../results/mock_wgs.bam

