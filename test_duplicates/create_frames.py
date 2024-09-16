import sys
from Bio import SeqIO
from os import mkdir

# division into cells of 1000 IDs with an overlap of 500
file_dir, file_name = sys.argv[1], sys.argv[2]

with open(f'{file_dir}/{file_name}.fq', 'r') as fastq_file, open(f'{file_dir}/{file_name}.fa', 'w') as fasta_file:

    fastq_records = SeqIO.parse(fastq_file, 'fastq')
    SeqIO.write(fastq_records, fasta_file, 'fasta-2line')

try:
    mkdir(f'{file_dir}/all_frames/')
except FileExistsError:
    pass

try:
    mkdir(f'{file_dir}/all_aligns/')
except FileExistsError:
    pass




with open(f"{file_dir}/{file_name}.fa", "r") as file:

    lines = file.readlines()

    for i in range(0, len(lines), 1000):
        
        file = open(f"{file_dir}/all_frames/frame_{int(i/1000)}.fa", "w") 

        if i < len(lines) - 2000:
            for i in range(i, i + 2000):
                file.write(lines[i])
        else:
            for i in range(i, len(lines)):
                file.write(lines[i])

