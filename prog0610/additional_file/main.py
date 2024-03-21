def step(board: List[List[int]], n: int) -> None:
    # your code here
    pass

def print_board(board: List[List[int]], n: int) -> None:
    # your code here
    pass

if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for i in range(n)]

    m = int(input())
    for _ in range(m):
        step(board, n)
    print_board(board, n)
