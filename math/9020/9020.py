def isPrime(x): # 소수 판별 함수
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1): # 제곱근까지만 나누어 보면 소수판별 가능
        if x % i == 0:
            return False
    return True

N = int(input()) # 몇번의 입력을 받을지 결정하는 N

for _ in range(N): # N번 반복
    num = int(input()) # 숫자를 입력받는다
    a = b = num // 2 # 입력받은 숫자를 2로 나눈 값을 각각 a, b에 대입
    while not (isPrime(a) and isPrime(b)): # a와 b가 둘다 소수일때 까지 a는 1씩 감소, b는 1씩 증가시킨다.
        a -= 1
        b += 1
    print(a, b)