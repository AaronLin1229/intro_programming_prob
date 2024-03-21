def bubble_sort(arr, n):
    # your code here

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    bubble_sort(arr, n)
    print(*arr, sep = ' ', end = '\n')
