import random


def get_story(file_name, story_number):
    with open(file_name, 'r') as f:
        stories = f.read().split('\n---\n')
    return stories[story_number]

# Function to create a dictionary where the keys are the stories and the values are their indices.
# This function is used to create an efficient lookup table for the stories in the 50% and 100% datasets.
def create_indexed_set(file_name):
    story_dict = {}
    with open(file_name, 'r') as f:
        stories = f.read().split('\n---\n')
        for i, story in enumerate(stories):
            story_dict[story] = i
    return story_dict

# Function to find a story that is present in all datasets.
# This function repeatedly chooses a random story from the 25% dataset until it finds one that is also in the 50% dataset.
# It then returns the chosen story and its indices in all three datasets.
def find_story():
    story_dict_50 = create_indexed_set('fifty-percent-train.txt')
    story_dict_100 = create_indexed_set('train.txt')
    while True:
        story_number = random.randint(0, 530000)
        story = get_story('twenty_five-percent-train.txt', story_number)
        if story in story_dict_50:
            return story, story_number, story_dict_50[story], story_dict_100[story]

story, story_number_25, story_number_50, story_number_100 = find_story()

# Stores randomly chosen story and positions in all datasets to output file for further use.
with open('random_story.txt', 'w') as f:
    f.write(f'Story: {story}\n')
    f.write(f'Story number in 25% dataset: {story_number_25}\n')
    f.write(f'Story number in 50% dataset: {story_number_50}\n')
    f.write(f'Story number in 100% dataset: {story_number_100}\n')
