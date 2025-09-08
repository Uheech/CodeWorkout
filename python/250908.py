# Lv.0 한번만 등장한 문자 
def solution(s):
# 문자열을 하나의 원소로 할당한 뒤 dictionary의 key로 배분하고 거기에 따라 등장 횟수를 추가한다.
    one_dic={}
    one_list=[]
# 문자열을 원소로 할당 
    for i in s:
# 만약 key값이 dictionary에 없다면
        if i not in one_dic:
# 키값 만들어주고 1 추가해줌 
            one_dic[i]=1
# 있으면 거기에 1 증가시켜줌 
        else:
            one_dic[i]+=1
# return key를 하려고 햇으나 for의 특성상 하나의 값만을 반환함.
# 따라서 for 문을 돌면서 list에 추가해줘야함. 
    for key in one_dic:
# one_dic[key]에 해당하는 value값이 1인 경우
        if one_dic[key]==1:
# list값에 추가한다.
            one_list.append(key)
# 사전 순으로 정렬한 뒤
    one_list=sorted(one_list)
# 다시 합치고(문자열로 다시 만들어주고)
    one_list=''.join(one_list)
# 해당 문자열을 반환
    return(one_list)
