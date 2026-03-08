#!/usr/bin/env python3

import pandas as pd
import torch
from transformers import AutoTokenizer
import sys

csv_file = sys.argv[1]
output_file = sys.argv[2]

model_name = "facebook/esm2_t6_8M_UR50D"

tokenizer = AutoTokenizer.from_pretrained(model_name)

df = pd.read_csv(csv_file)

sequences = df["v_sequence_alignment_aa"].tolist()

tokens = tokenizer(
    sequences,
    padding=True,
    truncation=True,
    return_tensors="pt"
)

torch.save(tokens, output_file)

print("Saved tokens to:", output_file)