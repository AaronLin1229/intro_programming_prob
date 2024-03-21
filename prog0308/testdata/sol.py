def calculate_score(N):
    score = 0
    if N > 40:
        return 100
    else:
        for i in range(1, N + 1):
            if i <= 10:
                score += 6
            elif i <= 20:
                score += 2
            else:
                score += 1
    return score

# Read the number of correct answers from input
N = int(input())
print(calculate_score(N))
