import sys

input = sys.stdin.readline


# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Function to perform permutation
def permutation(depth):
    global perm_count
    global answer

    if depth == length:
        if N == perm_count:
            answer = result[:]
        perm_count += 1
        return

    for i in range(length):
        if not collected[i]:
            collected[i] = 1
            result[depth] = str[i]
            permutation(depth + 1)
            collected[i] = 0


# Initialize variables
dp = [0] * 11
dp[1] = 1

for i in range(2, 11):
    dp[i] = dp[i - 1] * i

# Main loop
while True:
    # Input
    try:
        line = input()

        if not line:
            break

        str, N = line.split()
        N = int(N)

        perm_count = 1

        length = len(str)
        str = list(str)
        result = [0] * length
        collected = [0] * length

        if dp[length] < N:
            print(''.join(str), N, "= No permutation")
        else:
            permutation(0)
            print(''.join(str), N, '=', ''.join(answer))
    except:
        break