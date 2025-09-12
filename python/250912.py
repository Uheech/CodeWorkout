#Lv.0 다항식 더하기
def solution(polynomial):
    x_list=[]
    num_list=[]
    polynomial=polynomial.split()
    polynomial=''.join(polynomial)
    polynomial=polynomial.split('+')
    for i in polynomial:
        if 'x' in i:
            if len(i) == 1:
                x_list.append(1)
            else:
            # 처음엔 i[0]으로 앞에 있는 숫자만 더하려고 했는데 그러면 숫자의 길이가 긴 경우에는 처리할 수 없음.
            # x를 제거하고 남은 숫자를 list에 추가하는게 나을 듯 
                i=i.replace('x','')
                x_list.append(int(i))
        else:
            num_list.append(int(i))
    
    x=sum(x_list)
    num=sum(num_list)
    
        # x항과 상수항이 모두 0일 때
    if x==0 and num==0:
        return '0'
    # x항만 0일 때
    elif x==0:
        return str(num)
    # 상수항만 0일 때
    elif num==0:
        if x==1:
            return 'x'
        else:
            return str(x)+'x'
    # 모든 항이 0이 아닐 때
    else:
        if x==1:
            return 'x' + ' + ' + str(num)
        else:
            return str(x)+'x' + ' + ' + str(num)
    
