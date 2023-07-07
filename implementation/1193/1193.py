X = int(input()) # X를 입력 값으로 받는다.

line = 1 # 대각선의 line을 정의, 시작은 1로 한다.

while X > line: # 입력받은 X가 line보다 크면 계속 반복
    X -= line # X = X-line
    line += 1 # line = line + 1

if line % 2 == 0: # 만약 line이 짝수면,
    denominator = X # 분모가 X
    numerator = line - X + 1 # 분자가 line - X + 1

else: # line이 홀수면,
    numerator = X # 분자가 X
    denominator = line - X + 1 # 분모가 line - X + 1

print(denominator, "/",numerator, sep="")


