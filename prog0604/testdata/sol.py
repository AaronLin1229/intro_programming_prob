def count_pos_neg(arr: list[int]) -> list[int]:
    pos_count = sum(1 for x in arr if x > 0)
    neg_count = sum(1 for x in arr if x < 0)
    return [pos_count, neg_count]

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    res = count_pos_neg(arr)
    print(f"{res[0]} {res[1]}")
