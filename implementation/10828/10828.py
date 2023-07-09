import sys

stack = [] # 파이썬에는 stack 라이브러리가 없음
order = int(input())

for _ in range(order):
    command = sys.stdin.readline().split()

    if(command[0] == "push"): # 명령이 push라면, stack에 append
        stack.append(command[1])

    elif(command[0] == "pop"): # 명령이 pop이면,
        if len(stack)==0: # 만약 stack이 비어있다면 -1 출력
            print("-1")
        else: # 그렇지 않다면,
            x=stack[-1]
            stack.pop(-1)
            print(x) # pop하면서 x출력

    elif(command[0] == "size"): # stack의 길이 출력
        print(len(stack))

    elif(command[0] == "empty"): # stack이 비어있으면 1, 아니면 0출력
        if(len(stack)) == 0:
            print("1")
        else:
            print("0")

    elif(command[0] == "top"): # 명령이 top이면,
        if len(stack)==0: # 만약 stack이 비어있으면
            print("-1") # -1 출력
        else: # 그렇지 않다면
            print(stack[-1]) # stack의 맨 위 값 출력