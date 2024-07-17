import os
import tiktoken
import numpy as np
from datasets import load_dataset

# load the datasets
train_dataset = load_dataset("roneneldan/TinyStories", split="train")
val_dataset = load_dataset("roneneldan/TinyStories", split="validation")

# convert the datasets to strings
train_data = '\n---\n'.join([str(item) for item in train_dataset['text']])
val_data = '\n---\n'.join([str(item) for item in val_dataset['text']])

# save the datasets to .txt files
baseline_training_txt = 'train.txt'
validation_txt = 'val.txt'

with open(baseline_training_txt, 'w') as f:
    f.write(train_data)
with open(validation_txt, 'w') as f:
    f.write(val_data)


# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

# train.bin has 301,966 tokens
# val.bin has 36,059 tokens
