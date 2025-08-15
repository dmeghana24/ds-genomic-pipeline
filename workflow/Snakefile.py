rule all:
    input:
        "results/mock_wgs.bam",
        "results/mock_variants.vcf",
        "results/mock_counts.txt",
        "results/mock_methyl_results.txt"

rule wgs_align:
    input: r1="data/mock_wgs_R1.fastq", r2="data/mock_wgs_R2.fastq"
    output: "results/mock_wgs.bam"
    shell: "bwa mem ref.fa {input.r1} {input.r2} | samtools sort -o {output}"

rule wgs_variant:
    input: "results/mock_wgs.bam"
    output: "results/mock_variants.vcf"
    shell: "gatk HaplotypeCaller -R ref.fa -I {input} -O {output}"

rule rna_align:
    input: fq="data/mock_rnaseq.fastq"
    output: "results/mock_rnaseq_Aligned.out.sam"
    shell: "STAR --runThreadN 2 --genomeDir ref_genome --readFilesIn {input.fq} --outFileNamePrefix results/mock_rnaseq_"

rule rna_counts:
    input: "results/mock_rnaseq_Aligned.out.sam"
    output: "results/mock_counts.txt"
    shell: "featureCounts -a annotation.gtf -o {output} {input}"

rule meth_align:
    input: "data/mock_methyl.bam"
    output: "results/mock_methyl_results.txt"
    shell: "echo 'Simulated Bismark methylation alignment step' > {output}"

