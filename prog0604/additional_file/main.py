def count_pos_neg(arr: list[int]) -> list[int]
    pass

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    res = count_pos_neg(arr)
    print(f"{res[0]} {res[1]}")
