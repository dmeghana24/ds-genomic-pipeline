# Methods

This pipeline includes:
- WGS alignment with BWA-MEM
- Variant calling with GATK HaplotypeCaller
- RNA-seq alignment with STAR
- Quantification with featureCounts
- Differential analysis with DESeq2
- Methylation processing with simulated Bismark output
- Integration via pandas, visualization in R/Python

References:
- Li, H. & Durbin, R. (2009). Fast and accurate short read alignment with Burrows–Wheeler transform. Bioinformatics.
- McKenna, A. et al. (2010). The Genome Analysis Toolkit. Genome Res.
- Love, M.I. et al. (2014). DESeq2. Genome Biol.

