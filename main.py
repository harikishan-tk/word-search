import pandas as pd
import random
from word_search_generator import WordSearch
from word_search_generator.mask import Image
import os

DIFFICULTY_LEVEL = 3  # Example difficulty level

MASK_IMAGES_DIR = "mask_images"
PUZZLES_DIR = "puzzles"

MASK_IMAGES_FILE_NAMES = {
    'hf.png': 30,
    'git.png': 20,
    'python.png': 25
}

def main():
    df = pd.read_csv("words1.csv")
    words = df["words"].tolist()
    
    total_puzzles_created = 0  # Initialize the total counter
    
    for mask_image, limit in MASK_IMAGES_FILE_NAMES.items():
        puzzle_count = 0  # Initialize the counter for each mask image
        
        while puzzle_count < limit:
            print(f"Creating puzzle {total_puzzles_created + 1} with mask {mask_image}")
            # get current working directory
            current_dir = os.getcwd()
            mask_image_file_name = mask_image.split(".")[0]
            # get the full path of the mask image
            mask_image = os.path.join(current_dir, MASK_IMAGES_DIR, mask_image)


            # Step 2: Select 10 random words
            selected_words = random.sample(words, 10)
            
            print(selected_words)
            
            # create string of words separated by comma
            string_of_words = ", ".join(selected_words)
            puzzle = WordSearch(string_of_words, level=DIFFICULTY_LEVEL, size=35)
            puzzle.apply_mask(Image(mask_image))  # Apply the mask
            puzzle.show()
            
            # move current directory to puzzles directory
            os.path.join(current_dir, PUZZLES_DIR)

            # move the generated puzzle to the puzzles directory
            puzzle.save(f"{mask_image_file_name}_{total_puzzles_created + 1}_lvl_{DIFFICULTY_LEVEL}.pdf")
            
            puzzle_count += 1  # Increment the counter for the current mask image
            total_puzzles_created += 1  # Increment the total counter

    print("Total puzzles created:", total_puzzles_created)

if __name__ == "__main__":
    main()