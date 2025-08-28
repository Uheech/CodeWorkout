# Lv.1 x만큼 간격이 있는 n개의 숫자
# 최초에 range로 문제를 해결하려했으나 음수일 때의 보완방법을 모르겠어서 while로 진행함.
def solution(x, n):
    num_list=[]
    new_x=0
    while len(num_list)<n:
        new_x+=x
        num_list.append(new_x)
    return num_list

'''
<range() 함수를 사용한 코드 예시
1. return list(range(x,x*n+(1 if x>0 else -1),x))
: 조건 자체에도 함수를 걸어줄 수 있음
2. return [x*i for i in range(1, n+1)]
: 이게 출제자가 의도한 풀이방법이었을 듯.. 
'''
  
