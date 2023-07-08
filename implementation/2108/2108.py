from collections import Counter
import sys
input = sys.stdin.readline # input으로 입력을 받으면 runtime 에러가 뜸

N = int(input()) # N개를 입력받음
list = [] # 입력받은 정수들을 담을 리스트 생성

for i in range(N): # N번 반복
    list.append(int(input())) # list에 추가

list.sort() # 리스트를 오름차순으로 정렬

Mean = round(sum(list) / len(list)) # 산술평균 (첫째자리에서 반올림을 해야 하므로 round사용)
print(Mean)

MedIndex = len(list) // 2 # 중앙값 (이 문제에서는 N이 홀수이므로, 2로 나눈 몫을 index로 사용한다)
print(list[MedIndex])

count_list = Counter(list).most_common() # 최빈값 (Counter 모듈 사용하여 최빈값을 구함)

if len(count_list) > 1 and count_list[0][1] == count_list[1][1]: # 첫번째로 작은 수와 두번째로 작은수의 최빈 값이 같다면
    print(count_list[1][0]) # 두번째로 작은 수의 최빈 값 출력
else:
    print(count_list[0][0])


print(max(list) - min(list)) # 범위를 구하기 위해 최대값에서 최소값의 차를 이용
