import sys

input = sys.stdin.readline

N, K = map(int, input().split()) # N = 동전의 총 종류, K = 가치의 합
coin_list = [] # coin을 입력받을 리스트 생성
count = 0 # count = 0으로 초기화

for i in range(N): # 동전의 종류 만큼 반복하여 입력 받음
    X = int(input()) # 입력받는 변수
    coin_list.append(X) # 입력받은 변수를 coin_list에 append시킴

coin_list.reverse() # coin_list를 내림차순으로 정렬하기 위해 reverse를 시킨다

for i in range(N): # N번 반복
    count += K // coin_list[i] # 가치의 합인 K를 list에 있는 가장 큰 수 부터 나누기 시작하여, 그 몫을 count에 더함
    K = K % coin_list[i] # K는 list의 나머지로 다시 초기화 시킨다

print(count) # count값 출력


