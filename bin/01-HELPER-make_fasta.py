import csv
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='the name of the input file')
parser.add_argument('output_file', help='the name of the output file')
args = parser.parse_args()

df = pd.read_csv(args.input_file, delimiter = '\t')
with open(args.output_file, 'w') as fout:
    for index, row in df.iterrows():
        # Append row index

        fout.write(f'>{index}\n{row[0]}\n')
