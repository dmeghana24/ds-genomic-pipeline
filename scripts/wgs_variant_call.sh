#!/bin/bash
gatk HaplotypeCaller -R ref.fa -I ../results/mock_wgs.bam -O ../results/mock_variants.vcf

