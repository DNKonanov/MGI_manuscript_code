from pathlib import Path
import sys
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
import seaborn as sns

file_dir = sys.argv[1]

directory = Path(f'{file_dir}/all_aligns/')
files = [f for f in directory.iterdir() if f.is_file()]
n = len(files)

id_1_num = []
id_2_num = []

for i in range(0, n):

    file_path = f"{file_dir}/all_aligns/align_{i}.txt"

    if os.path.exists(file_path):
        df = pd.read_csv(f"{file_dir}/all_aligns/align_{i}.txt", delimiter='\t', 
                     names = ['id_1', 'id_2', 'identity', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'start', 'send', 'evalue', 'bitscore'])
    
        df = df[df['identity'].astype(float) > 95]
        df = df[df['length'].astype(int) == 300]
        df = df[df['id_1'] != df['id_2']]
        id_1 = list(df['id_1'])
        id_2 = list(df['id_2'])
    
        for i in range(len(id_1)):
            id_1_num.append(int(id_1[i][-8:-2]))
            id_2_num.append(int(id_2[i][-8:-2]))

diff = np.array(id_1_num) - np.array(id_2_num)

diff = diff[np.abs(diff) < 1000]

sns.kdeplot(diff, bw_adjust=0.1, linewidth=1, color='black')
plt.ylabel('density')
plt.xlabel('Difference between read IDs')
plt.xlim(-50, 500)

save_path = os.path.join(file_dir, 'plot_image.png')

plt.savefig(save_path)
plt.close()

