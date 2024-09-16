# MGI_manuscript_code
The scripts to estimate misdemultiplexing rate in MGI runs 

The Jupyterlab notebooks:
* `Notebook_Test_IndividualBarcode.ipynb` - an example of misdemultiplexing rate estimation starting from fastq.gz files. 
Only one barcode 46 is considered
* `Notebook_Test_full_PE300.ipynb` - an estimation of misdemultiplexing rate in all barcodes in the PE300 run. Precalculated 
barcode_stat files are used.
* `Notebook_Plot_IDdiff_histograms.ipynb` - the code to plot distribution of differences in read ID between duplicated reads.


### Duplicates analysis
The `test_duplicates` folder contains demo data for the duplicates identification. It includes the fastq-file for one field of view (C001R001).
The full processing pipeline could be run using `run.sh` script.

The dependencies for `run.sh`: pandas, numpy, matplotlib, seaborn, biopython, blastn, makeblastdb