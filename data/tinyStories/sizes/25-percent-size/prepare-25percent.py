import random

"""
Key Idea:
Randomly sample from 0 till the total_stories by the number of needed stories. Then when iterating through each story,
assign an id to each story and check if said id is to be included in the random sample. If the story_is_selected then
write it to the output file.
"""
total_stories = 2_120_000
needed_stories = total_stories // 4  # Divide by 4 to obtain 25%
selected_stories = set(random.sample([i for i in range(total_stories)], needed_stories)) # Convert to set to optimize story_id inclusion check
story_id = -1
story_is_selected = story_id in selected_stories
baseline_training_txt = "data/tinyStories/sizes/100-percent-size/train.txt"
output_training_txt = "data/tinyStories/twenty-five-percent-train.txt"

with open(baseline_training_txt, "r") as input, \
     open(output_training_txt, "w") as output:
    for line in input:
        if line.startswith("---"): # Stories are separated using ---
            story_id += 1
            story_is_selected = story_id in selected_stories 

        if story_is_selected:
            output.write(line)