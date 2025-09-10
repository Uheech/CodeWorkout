#Lv.O OX퀴즈
def solution(quiz):
    ans_list=[]
# 문자열 안의 등호를 python에 맞게 변경해서 그대로 조건문을 씌워서 True, False를 가려내면 된다고 생각했다. 
    for i in quiz:
        i= i.replace('=','==')
# 그런데, 문자열 자체는 항상 True라서 문자열 안에 있는 내용을 그대로 읽어줄 함수가 필요햇음!
# eval(): 근데 얘는 좀 위험할 수 있는 함수라고 해서 다른 방법도 찾아보자 
        if eval(i):
            ans_list.append('O')
        else:
            ans_list.append('X')
    return ans_list

# 다른 풀이방법
'''
def solution(quiz):
  ans_list=[]
  for q in quiz:
  # 공백을 기준으로 문자열을 분리
  parts=q.split('')

  # 각 부분을 변수에 할당
  x_str,op,y_str,eq,z_str=parts

  #문자열을 정수형으로 반환
  x=int(x_str)
  y=int(y_str)
  z=int(z_str)

  # 연산자에 따라서 직접 계산
  if op == '+':
    if x+y==z:
      ans_list.append('O')
    else:
      ans_list.append('X')
  elif op == '-':
    if x-y==z:
      ans_list.append('O')
    else:
      ans_list.append('X')
      
  retun ans_list
'''
