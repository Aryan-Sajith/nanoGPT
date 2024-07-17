import os
import tiktoken
import numpy as np


training_file_to_encode = '25percentdup-25percentsize.txt' 

# load the data
with open(training_file_to_encode, 'r') as f:
    train_data = f.read()

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
print(f"train has {len(train_ids):,} tokens")

# export to bin file
train_ids = np.array(train_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))

print(f"train.bin has {len(train_ids):,} tokens")
