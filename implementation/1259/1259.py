def reverse(Number):
    return int(str(Number)[::-1]) # Number를 입력하면, 그 Number의 역으로 읽은 것을 return한다.


while True: # True이면 계속 실행
    X = int(input()) # 정수를 입력받는다.
    Y = reverse(X) # Y를 X의 역으로 읽은 수로 정의한다.

    if str(X).startswith('0'):  # X가 0으로 시작하는 경우
        break  # 반복문을 종료한다.
    
    if(X == Y): # 만약 입력받은 수 X와 X의 역으로 정의된 Y가 같다면,
        print("yes") # Yes를 출력한다.
    elif(X!=Y): # 그렇지 않다면,
        print("no") #No를 출력한다.