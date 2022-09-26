import os
import random
from os import system, name

class TickTack:
    def __init__(self, board):
        self.board = board
        self.win = 0

    def print_board(self, board):
        row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
        row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
        row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])
        print()
        print(row1)
        print(row2)
        print(row3)
        print()


    def player_move(self, icon, board):
        if icon == "X":
            number = 1
            print(f"Your turn player {icon}")
            choice = int(input("Enter your move (1-9)").strip())
            if board[choice - 1] == " ":
                board[choice - 1] = icon
            else:
                print("That space is taken!")
                TickTack.player_move(self, icon, self.board)
        elif icon == "O":
            number = 2
            print(f"Your turn player {icon}")
            if board[0] == icon and board[1] == icon or board[0] == "X" and board[1] == "X":
                choice = 3
                TickTack.if_taken(self, choice, self.board)
            elif board[1] == icon and board[2] == icon or board[1] == "X" and board[2] == "X":
                choice = 1
                TickTack.if_taken(self, choice, self.board)
            elif board[0] == icon and board[2] == icon or board[0] == "X" and board[2] == "X":
                choice = 4
                TickTack.if_taken(self, choice, self.board)
            elif board[3] == icon and board[4] == icon or board[3] == "X" and board[4] == "X":
                choice = 6
                TickTack.if_taken(self, choice, self.board)
            elif board[3] == icon and board[5] == icon or board[3] == "X" and board[5] == "X":
                choice = 5
                TickTack.if_taken(self, choice, self.board)
            elif board[4] == icon and board[5] == icon or board[4] == "X" and board[5] == "X":
                choice = 4
                TickTack.if_taken(self, choice, self.board)
            elif board[6] == icon and board[7] == icon or board[6] == "X" and board[7] == "X":
                choice = 9
                TickTack.if_taken(self, choice, self.board)
            elif board[6] == icon and board[8] == icon or board[6] == "X" and board[8] == "X":
                choice = 8
                TickTack.if_taken(self, choice, self.board)
            elif board[7] == icon and board[8] == icon or board[7] == "X" and board[8] == "X":
                choice = 7
                TickTack.if_taken(self, choice, self.board)
            elif board[0] == icon and board[3] == icon or board[0] == "X" and board[3] == "X":
                choice = 7
                TickTack.if_taken(self, choice, self.board)
            elif board[0] == icon and board[6] == icon or board[0] == "X" and board[6] == "X":
                choice = 4
                TickTack.if_taken(self, choice, self.board)
            elif board[3] == icon and board[6] == icon or board[4] == "X" and board[6] == "X":
                choice = 1
                TickTack.if_taken(self, choice, self.board)
            elif board[0] == icon and board[3] == icon or board[0] == "X" and board[3] == "X":
                choice = 7
                TickTack.if_taken(self, choice, self.board)
            elif board[1] == icon and board[4] == icon or board[1] == "X" and board[4] == "X":
                choice = 8
                TickTack.if_taken(self, choice, self.board)
            elif board[1] == icon and board[7] == icon or board[1] == "X" and board[7] == "X":
                choice = 5
                TickTack.if_taken(self, choice, self.board)
            elif board[4] == icon and board[7] == icon or board[4] == "X" and board[7] == "X":
                choice = 2
                TickTack.if_taken(self, choice, self.board)
            elif board[2] == icon and board[5] == icon or board[2] == "X" and board[5] == "X":
                choice = 9
                TickTack.if_taken(self, choice, self.board)
            elif board[2] == icon and board[8] == icon or board[2] == "X" and board[8] == "X":
                choice = 6
                TickTack.if_taken(self, choice, self.board)
            elif board[5] == icon and board[8] == icon or board[5] == "X" and board[8] == "X":
                choice = 3
                TickTack.if_taken(self, choice, self.board)
            elif board[0] == icon and board[4] == icon or board[0] == "X" and board[4] == "X":
                choice = 9
                TickTack.if_taken(self, choice, self.board)
            elif board[0] == icon and board[8] == icon or board[0] == "X" and board[8] == "X":
                choice = 5
                TickTack.if_taken(self, choice, self.board)
            elif board[4] == icon and board[8] == icon or board[4] == "X" and board[8] == "X":
                choice = 1
                TickTack.if_taken(self, choice, self.board)
            elif board[2] == icon and board[6] == icon or board[2] == "X" and board[6] == "X":
                choice = 5
                TickTack.if_taken(self, choice, self.board)
            elif board[2] == icon and board[4] == icon or board[2] == "X" and board[4] == "X":
                choice = 7
                TickTack.if_taken(self, choice, self.board)
            elif board[4] == icon and board[6] == icon or board[4] == "X" and board[6] == "X":
                choice = 3
                TickTack.if_taken(self, choice, self.board)
            elif board[4] == " ":
                choice = 5
            else:
                choice = random.randint(1, 9)
                TickTack.if_taken(self, choice, self.board)
            if board[choice - 1] == " ":
                board[choice - 1] = icon
            else:
                print("That space is taken!")
                board[TickTack.if_taken(self, choice, self.board) - 1] = icon
                # if_taken(choice)
                # player_move(icon)


    def if_taken(self, choice, board):
        if board[choice - 1] == "X" or board[choice - 1] == "O":
            empty_space = []
            for i in range(1, 10):
                if board[i - 1] == " ":
                    empty_space.append(i)
            choice = random.choice(empty_space)
        return choice



    def clear_board(self, player_win_count, computer_win_count, turn, player_name, board):
        score_board = {}
        print(f"Player points = {player_win_count}\nComputer points = {computer_win_count}")
        if player_win_count >= 3:
            self.win = 1
            print(f"Congratulations {player_name}, you won!!")
            score_board[player_name] = player_win_count
            score_board["Computer"] = computer_win_count
            with open('score_board.txt', 'a') as file:
                file.write(str(score_board))
            # exit()
        elif computer_win_count >= 3:
            self.win = 0
            print(f"Sorry {player_name}, you loose, the Computer wins!!")
            score_board[player_name] = player_win_count
            score_board["Computer"] = computer_win_count
            with open('score_board.txt', 'a') as file:
                file.write(str(score_board))
            # exit()
        else:
            input(f"Press enter for round {turn}!!")
            print("-"*25)
            for x in range(1, 10):
                if board[x - 1] != " ":
                    board[x - 1] = " "


    def is_victory(self, icon, board):
        if (board[0] == icon and board[1] == icon and board[2] == icon) or \
            (board[3] == icon and board[4] == icon and board[5] == icon) or \
            (board[6] == icon and board[7] == icon and board[8] == icon) or \
            (board[0] == icon and board[3] == icon and board[6] == icon) or \
            (board[1] == icon and board[4] == icon and board[7] == icon) or \
            (board[2] == icon and board[5] == icon and board[8] == icon) or \
            (board[0] == icon and board[4] == icon and board[8] == icon) or \
            (board[2] == icon and board[4] == icon and board[6] == icon):
            return True
        else:
            return False

    def is_draw(self, board):
        if " " not in board:
            return True
        else:
            return False


    def start_game(self):
        turn = 1
        player_win_count = 0
        computer_win_count = 0
        player_name = input("What is your name").lower()
        who_starts = input("Who start?").lower()
        TickTack.clear_board(self, player_win_count, computer_win_count, turn, player_name, self.board)
        if "i" in who_starts:
            print("Ok, you will start")
            player_start = "X"
            second_player = "O"
        else:
            print("Ok, I will start")
            player_start = "O"
            second_player = "X"
        while player_win_count < 3 and computer_win_count < 3:
            if player_win_count < 3 and computer_win_count < 3:
                TickTack.print_board(self, self.board)
                TickTack.player_move(self, player_start, self.board)
                TickTack.print_board(self, self.board)
                if TickTack.is_victory(self, player_start, self.board):
                    if player_start == "X":
                        player_win_count += 1
                    else:
                        computer_win_count += 1
                    turn += 1
                    print(f"{player_start} Wins! Congratulations!")
                    TickTack.clear_board(self, player_win_count, computer_win_count, turn, player_name, self.board)
                elif TickTack.is_draw(self, self.board):
                    print("Its a draw!")
                    turn += 1
                    TickTack.clear_board(self, player_win_count, computer_win_count, turn, player_name, self.board)
                TickTack.player_move(self, second_player, self.board)
                TickTack.print_board(self, self.board)
                if TickTack.is_victory(self, second_player, self.board):
                    if second_player == "X":
                        player_win_count += 1
                    else:
                        computer_win_count += 1
                    turn += 1
                    print(f"{second_player} Wins! Congratulations!")
                    TickTack.clear_board(self, player_win_count, computer_win_count, turn, player_name, self.board)
                elif TickTack.is_draw(self, self.board):
                    turn += 1
                    print("Its a draw!")
                    TickTack.clear_board(self, player_win_count, computer_win_count, turn, player_name, self.board)
            elif player_win_count > 3:
                break
            elif computer_win_count > 3:
                break

# game_tick_tack = TickTack([" " for i in range(9)])
# game_tick_tack.start_game()
# print("now")

