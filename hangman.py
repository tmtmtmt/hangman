'''
1.wrong
2.stages
3.rletters
4.boad
5.win
6.print
'''

import random

def hangman(words):
    wrong = 0
    stages = [
        "",
        "____________      ",
        "|                 ",
        "|          |      ",
        "|          0      ",
        "|         /|\     ",
        "|         / \     ",
        "|                 "
    ]
    rletters = list(words)
    board = ["_"] * len(words)
    win = False
    print('ハングマンへようこそ！')

    while wrong < len(stages) - 1:
        print('\n')
        msg = "1文字を入力してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print("\n".join(stages[:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break

    if not win:
        print('\n'.join(stages[:wrong+1]))
        print('あなたの負け！正解は {}.'.format(words))

wordslists = [
    "cat",
    "dog",
    "spider",
    "bhuman",
    "byson",
    "aigjpoagj"
]

num = random.randint(1,len(wordslists)-1)
wordlist = wordslists[num]

hangman(wordlist)

'''
a = ["a", "b", "c"]
print(a[:2])
'''

