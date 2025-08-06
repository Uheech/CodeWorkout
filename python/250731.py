''' 
최빈값: 제일 많이 나온 애
각 요소들의 등장횟수를 비교해서 제일 많이 나온 애를
return 하면 되겠구나
'''
# 정수 배열의 요소를 딕셔너리의 키로 추가하고 그 개수를 count
def solution(array):
    array_dict={}
    for a in array:
        if a in array_dict:
            array_dict[a]+=1
        else:
            array_dict[a]=1
            
# 딕셔너리의 아이템 중 value값이 max인 value값을 찾아서같은 value값을 가지는 key값이 잇는지 찾아서 빈 배열에 넣기
    same_value=[]
    max_item=max(array_dict.items(), key=lambda item: item[1])
    for key, value in array_dict.items():
        if value==max_item[1]:
            same_value.append(max_item[0])
            
# 만약 해당 배열안에 숫자가 1개를 초과한다면 최빈값이 여러개이므로 -1을 return, 아니면 최빈값 하나만 return~
    if len(same_value)>1:
        return -1
    else:
        return max_item[0]
