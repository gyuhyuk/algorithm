def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

N = int(input())
for _ in range(N):
    num = int(input())
    a = b = num // 2
    while not (isPrime(a) and isPrime(b)):
        a -= 1
        b += 1
    print(a, b)