import random


def pick_a_word(word_list):
    w = random.choice(word_list)
    return w


def make_anagram(word):
    shuffled_word = ""
    while len(word) > 0:
        position = random.randrange(len(word))
        shuffled_word += word[position]
        word = word[:position] + word[(position + 1):]
    return shuffled_word


def get_user_input(shuffled_word):
    ask = "Colored word anagram: %s" % shuffled_word
    return ask


def user_guessing(user_input, w):
    if user_input == w:
        print("Correct")


def main():
    colors = ["yellow", "brown", "blue", "green", "red", "black", "brown", "orange"]
    chosen_word = pick_a_word(colors)
    shuffled_word = make_anagram(chosen_word)
    ask = get_user_input(shuffled_word)
    print(ask)
    answer = ""
    while answer != chosen_word:
        print(str("Guess the color word!"))
        answer = input()
        user_guess = user_guessing(answer, chosen_word)


if __name__ == '__main__':
    main()
