import sys

A, B, C = map(int, input().split()) # 3개의 숫자 입력 받음

def cal(a, b, c): # a, b, c 3개의 파라미터
    if b == 1: # A^B가 될 때의 b, 즉 몇번을 곱할지 정하는 수가 1이라면,
        return a % c # A % C를 return한다. (어떤 수에 1을 몇 번을 곱하더라도 그 자신)
    
    if b % 2 == 0: # 몇번을 곱할지 정하는 수가 짝수라면,
        return (cal(a, b//2, c)**2)%c # 예를들어, 2^8 => 2^4 * 2^4 => 2^2 * 2^2 * 2^2 * 2^2
    else:
        return (cal(a, (b-1)//2, c)**2*a)%c
    
print(cal(A,B,C))