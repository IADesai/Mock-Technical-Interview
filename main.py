import random


def calculate_word_score(word: str) -> int:
    """Function that calculates the score of a word based on its letters"""
    word = word.upper()
    word_score = 0
    for letter in word:
        letter_score = check_letter(letter)
        word_score += letter_score
    return word_score


def check_letter(letter):
    """Function that checks the letter for its score"""
    scores = {"EAIONRTLSU": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}
    for values in scores.items():
        if letter in values[0]:
            score = values[1]
    return score


def choose_letters() -> str:
    """Function that chooses seven random letters from the english alphabet"""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chosen_letters = []
    for i in range(7):
        chosen_letters.append(alphabet[random.randint(0, len(alphabet)-1)])
    return "".join(chosen_letters)


def choose_letters_from_bag(bag: dict) -> str:
    """Function that chooses letters from the bag"""
    chosen_letters = []
    for i in range(7):
        chosen_letters.append(list(bag.keys())[random.randint(0, len(bag.keys())-1)])
    chosen_letters = "".join(chosen_letters)
    check_letters(chosen_letters, bag)
    return chosen_letters


def check_letters(chosen_letters: str, bag: dict) -> bool:
    """Function that checks if this letter string is possible"""
    for letter in chosen_letters:
        for index in range(len(list(bag.keys()))):
            if list(bag.keys())[index] == letter:
                if list(bag.values())[index] == 0:
                    return False
                else:
                    list(bag.values())[index] -= 1
    return True                  


def create_bag() -> dict:
    """Function that creates a bag as a dictionary with number of available letters"""
    bag = {"E": 12, "A": 9, "I": 9, "O": 8, "N": 6, "R": 6, "T": 6, "L": 4, "S": 4, "U": 4,
        "D": 4, "G": 3, "B": 2, "C": 2, "M": 2, "P": 2, "F": 2, "H": 2, "V": 2, "W": 2, "Y": 2,
        "K": 1, "J": 1, "X": 1, "Q": 1, "Z": 1}
    return bag


if __name__ == "__main__":
    print(calculate_word_score("GUARDIAN"))
    print(choose_letters_from_bag(create_bag()))