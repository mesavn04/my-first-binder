import os
import glob
import pandas as pd
os.chdir("C:/Users/nhungtth/Downloads/test_N2")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv