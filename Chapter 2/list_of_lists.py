boards = [['_'] * 3 for i in range(3)]
print(boards)
boards[1][2] = 'X'

print('\n')
for board in boards:
    print(board)

#incorrect way (list of three references to the same board)
print('\n')
weird_boards = [['_'] * 3] * 3
print(weird_boards)
weird_boards[1][2] = 'O'
print('\n')
for board in weird_boards:
    print(board)