import string
from word_search_generator import WordSearch
import pandas as pd

DIFFICULTY_LEVEL = 3

def main():
    df = pd.read_csv("words.csv")
    words = df["words"].tolist()
    # for each 10 words, create a new puzzle
    for i in range(0, len(words), 10):
        print(words[i:i+10])
        # create string of words separated by comma
        string_of_words = ", ".join(words[i:i+10])
        puzzle = WordSearch(string_of_words, level=DIFFICULTY_LEVEL)
        puzzle.show()
        puzzle.save(f"puzzle_from_{i}_to_{i+10}_lvl_{DIFFICULTY_LEVEL}.pdf")

if __name__ == "__main__":
    main()