import sys

input = sys.stdin.readline

N = int(input())

list = [] # 사람을 담을 리스트

for _ in range(N): # N번 반복
    weight, height = map(int, input().split()) # 몸무게와 키를 입력받음
    list.append((weight, height)) #list에 append
    
for i in list: # 리스트의 튜플 값들을 i에 저장
    rank = 1 # rank는 1로 초기화
    for j in list: # 리스트의 튜플 값들을 j에 저장
        if i[0] < j[0] and i[1] < j[1]: # 키와 몸무게가 둘다 작다면,
            rank += 1 # rank + 1
    print(rank, end=" ")