N, K = map(int, input().split()) # N과 K를 입력받음

list = [] # 빈 리스트 생성
X = 0 # X = 0으로 초기화

for i in range(N): # N번 반복하여 list에 0부터 N까지의 숫자 추가
    list.append(i+1)

print("<", end="")

while len(list) != 0: # list의 길이가 0이 아닐때까지 반복
    X = (X + K - 1) % len(list) # 반복을하면서 K번째 사람을 계산한다. (index는 0부터 시작이므로 1을 뺌)
    if len(list) == 1: # 마지막 사람
        print(list.pop(X), end="")
    else: # 나머지 사람
        print(list.pop(X), end=", ")

print(">")