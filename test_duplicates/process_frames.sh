#!/bin/bash

# Go through all the frame_i.fa files in the all_frames folder
for fa_file in all_frames/frame_*.fa; do
    # Extracting the i number from the file name
    i=$(echo "$fa_file" | sed 's/.*frame_\([0-9]*\)\.fa/\1/')

    # Forming paths to the frame_i.fa and frame_i.txt files
    fa_path="./all_frames/frame_$i.fa"
    txt_path="./all_frames/frame_$i.txt"

    makeblastdb -in "$fa_path" -out "./all_frames/db_frame_$i" -parse_seqids -dbtype nucl

    # Execute blastn with the specified parameters
    blastn -query "$fa_path" -db "./all_frames/db_frame_$i" -outfmt 6 > "./all_aligns/align_$i.txt"
done

