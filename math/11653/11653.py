N = int(input()) # 정수 N을 입력받음

i = 2 # 소인수분해를 2부터 시작

if N == 1: # N이 1인 경우 아무것도 출력 x
    print("")

while N != 1: # N이 1이 아닐때까지 반복
    if N % i == 0: # N을 i로 나눴을 때 나머지가 0이 된다면
        print(i) # i를 출력
        N /= i
    else: # 그렇지 않다면
        i+=1 # i를 1증가 시킴




