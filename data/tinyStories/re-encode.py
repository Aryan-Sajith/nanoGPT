import os
import tiktoken
import numpy as np

training_file_to_encode = 'data/tinyStories/sizes/100-percent-size/dup-100-percent/size100-dup100.txt' 

# create a generator that yields lines from the file
def read_in_chunks(file_path):
    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break  # EOF
            yield line

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")

# create a generator that yields encoded tokens
def encode_generator(data_generator):
    for data in data_generator:
        yield from enc.encode_ordinary(data)

train_data_gen = read_in_chunks(training_file_to_encode)
train_ids_gen = encode_generator(train_data_gen)

# export to bin file
with open(os.path.join(os.path.dirname(__file__), 'train.bin'), 'wb') as f:
    for token in train_ids_gen:
        f.write(np.array(token, dtype=np.uint16).tobytes())

print("Encoding and writing to file completed.")
