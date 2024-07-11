import random

total_stories = 2_120_000
needed_stories = total_stories // 2
selected_stories = set(random.sample([i for i in range(total_stories)], needed_stories))
story_id = 0
is_story_selected = story_id in selected_stories

with open("train.txt", "r") as input, \
     open("fifty-percent-train.txt", "w") as output:
    for line in input:
        if line.startswith("---"):
            story_id += 1
            is_story_selected = story_id in selected_stories 

        if is_story_selected:
            output.write(line)