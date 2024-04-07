def is_solvable(board):
    inversions = 0
    for i in range(9):
        if board[i] == 'x':
            continue
        for j in range(i+1, 9):
            if board[j] != 'x' and int(board[i]) > int(board[j]):
                inversions += 1

    # 判断逆序数是否为偶数
    return inversions % 2 == 0

def dfs(board):
    stack = [(board, 0)]
    visited = set()

    while stack:
        current_board, depth = stack.pop()
        if current_board == '12345678x':
            return 1
        if current_board in visited:
            continue
        visited.add(current_board)

        # 获取空格位置
        index = current_board.index('x')
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in moves:
            x, y = index // 3 + dx, index % 3 + dy
            if 0 <= x < 3 and 0 <= y < 3:
                new_index = x * 3 + y
                new_board = list(current_board)
                new_board[index], new_board[new_index] = new_board[new_index], new_board[index]
                new_board_str = ''.join(new_board)
                stack.append((new_board_str, depth + 1))

    return 0

# 读取输入
initial_board = input().replace(' ', '')

# 判断是否可解
if is_solvable(initial_board):
    # 使用DFS判断是否有解
    print(dfs(initial_board))
else:
    print(0)