# Lv.0 인덱스바꾸기 
def solution(my_string, num1, num2):
    # 먼저 문자열을 리스트로 변환해준다.
    list_string=list(my_string)
    # 각 index에 새로운 문자를 할당해준다
    list_string[num1]=my_string[num2]
    list_string[num2]=my_string[num1]
    # 그리고 문자열로 다시 합친다.
    new_string="".join(list_string)
    return new_string
