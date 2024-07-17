"""
1) Store the current index of the story to duplicate as 399_485
2) Determine how many stories are to duplicated.
3) Randomly pick (2 -- the number of stories specified by step 2) stories from 1 - 530_000 excluding 399_485 as it's already the original
4) Open the twenty_five-percent-train.txt file and read to the Xpercentdup-25percentsize.txt file whereby the selected indexes of stories to be
dupped are swapped for the duplicate story.

Additional Information:
1) Stories separated by "\n---\n"
2) The duplicate story can be found from random_story.txt where you first first Story: (the actual story) then \n
"""
import random


duplicate_story_index = 399_485
total_stories = 530_000
duplicable_total = total_stories - 1 # Calculate the total number of stories that can be duplicated
percent_duplicates = 0.25
num_duplicates = int(percent_duplicates * duplicable_total)

# Randomly pick (num_duplicates) stories from 1 - 530_000 excluding duplicate_story_index as it's the original
story_indices = list(range(1, total_stories + 1))
story_indices.remove(duplicate_story_index)
selected_indices = set(random.sample(story_indices, num_duplicates)) # Set used to optimize member inclusion check later

# Read the duplicate story
with open('random_story.txt', 'r') as f:
    duplicate_story = f.read().split('Story number')[0].strip()

story_separator = "\n---\n"
# Open the twenty_five-percent-train.txt file and read to the 10percentdup-25percentsize.txt file whereby the selected indexes of stories to be dupped are swapped for the duplicate story.
with open('twenty_five-percent-train.txt', 'r') as f_in, open('25percentdup-25percentsize.txt', 'w') as f_out:
    stories = f_in.read().split(story_separator)
    for i, story in enumerate(stories):
        if i in selected_indices:
            f_out.write(duplicate_story + story_separator)
        else:
            f_out.write(story + story_separator)
