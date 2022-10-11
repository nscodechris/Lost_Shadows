

import random
import time



class HangMan:
    def __init__(self):
        self.win = 0
        self.words = ['kindly', 'recite', 'repeat', 'tree', 'display', 'geeks', 'coader', 'programmer', 'python', 'premium',
                 'watch']
        self.word = random.choice(self.words)
        self.correct_word = self.word
        self.spaces = ['_'] * len(self.word)
        self.num_turns = 10
        self.count = 0

    def get_letter_position(self, guess, word, spaces):
        index = -2
        while index != -1:
            if guess in word:
                index = word.find(guess)
                # print(index)
                removed_character = '*'
                word = word[:index] + removed_character + word[index + 1:]
                # print(word)
                spaces[index] = guess
            else:
                index = -1

        return (word, spaces)


    def win_check(self):
        for i in range(0, len(hang_man_game.spaces)):
            if hang_man_game.spaces[i] == '_':
                return -1

        return 1

    def hang_man_print(self, count):
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")


    def main_game(self, num_turns, word, spaces, count):
        while num_turns > 0:
            guess = input('Guess a character:')

            if guess in word:
                word, spaces = HangMan.get_letter_position(self, guess, word, spaces)
                print(spaces)
                num_turns -= 1
            else:
                print('Sorry that letter is not in the word.')
                num_turns -= 1
                if num_turns % 2 == 0:
                    count += 1
                    HangMan.hang_man_print(self, count)

            if HangMan.win_check(self) == 1:
                print('Congratulations you won')
                self.win = 1
                break
            if num_turns == 0:
                count = 5
                HangMan.hang_man_print(self, count)
                print(f"You loose, correct word is: {self.correct_word}")
                self.win = 0
                break
            print(f'you have {num_turns} turns left.')
            print()

    def start_hang_man(self):
        HangMan.main_game(self, self.num_turns, self.word, self.spaces, self.count)


hang_man_game = HangMan()

# hang_man_game.start_hang_man()

