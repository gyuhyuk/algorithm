from collections import deque

N, K = map(int, input().split()) # N, K를 입력받음

q = deque() # deque선언
answer = [] # 답을 입력받을 리스트 선언

for i in range(N): # 1부터 N명의 사람 추가
    q.append(i+1)

while q: # q에 수가 있을때 까지
    for i in range(K-1): 
        q.append(q.popleft())
    answer.append(q.popleft())

print("<", end="")
print(*answer, sep=", ", end="") # *을 붙이면 리스트에서 대괄호를 없애고 출력할 수 있음
print(">")