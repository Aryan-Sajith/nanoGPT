# Character level RNN small language model on tinyStories dataset 

[Original Dataset](https://huggingface.co/datasets/roneneldan/TinyStories) License: [CDLA-Sharing-1.0](https://spdx.org/licenses/CDLA-Sharing-1.0.html) shared by Ronen Eldan.
- Dataset variations obtained via the prepare-*.py scripts are also licensed under [CDLA-Sharing-1.0](https://spdx.org/licenses/CDLA-Sharing-1.0.html). Specific stochastic variations used for my work are shared [here](https://drive.google.com/drive/folders/1gJi6v5nH314OkCwN8xj4oaCpGfy95GvS?usp=drive_link) and licensed under [CDLA-Sharing-1.0](https://spdx.org/licenses/CDLA-Sharing-1.0.html).

Prepared the baseline dataset used to train a character-level rnn language model.

After running `prepare.py`:
- train.txt/train.bin & val.txt/val.bin have been created from the tinyStories dataset
- train.bin has 471,650,941 tokens
- val.bin has 4,741,881 tokens

General Steps to Train:
1. Use the base data/tinyStories/sizes/100-percent-size/prepare.py program to obtain the primary tinyStories train.txt file if you don't already have it.
2. Run a prepare-*.py program to obtain the variation of the tinyStories dataset you desire from the sizes/
3. Update re-encode.py's training_file_to_encode to encode the new train file into the train.bin file
4. Update config/train_tinyStories.py based for new train file:
    - Change write_output in config/train_tinyStories.py for model checkpoint
    - Change output_file in train.py for output file on eval stats
5. Finally, to train run:
```sh
python train.py config/train_tinyStories.py
```
