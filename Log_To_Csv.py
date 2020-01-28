import csv
import itertools 
import pandas as pd
def log_to_df(log_path):
    with open(log_path, 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line for line in stripped if line)
    grouped = zip(*[lines] * 1)
    with open('logfile.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(grouped)
    with open('logfile.csv', encoding='utf-8', errors='ignore') as infile:
        df=pd.read_csv(infile)    
        return df
