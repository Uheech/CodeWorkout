# Lv4. 년, 월, 성별 별 상품 구매 회원 수 구하기
# SUBSTRING(해당 컬럼, 시작 위치, 글자 수): 문자열을 쪼갤 때
SELECT SUBSTRING(SALES_DATE, 1, 4) as YEAR,
SUBSTRING(SALES_DATE, 6, 2) as MONTH, GENDER, count(DISTINCT u.USER_ID) as USERS 
# DISTINCT: 회원 수에 대한 집계시 중복을 주의할 것
FROM USER_INFO as u
RIGHT JOIN ONLINE_SALE o
ON u.USER_ID = o.USER_ID
# TRIM: SQL이 멋대로 데이터를 바꾸는 걸 막을 수 있음
/*
원래는 공백을 제거하는 역할이 맞음.
1. TRIM이 없을 때
- SQL은 컬럼값의 숫자와 문자열을 비교하려고 함.
- 이때 SQL 자동번역기가 작동, ' '을 0이라는 숫자로 바꿈
- 그래서 컬럼의 값 !=0이 되니까 0을 제외하는 것.
2. TRIM이 있을 때 
- TRIM() 함수가 먼저 실행, 숫자 0을 '0' 문자열로 바꿈
- 문자열'0'이랑 문자열 ' '이 비교 대상임
- 두 데이터 타입이 같으니까 번역기가 작동할 필요가 없음.
*/
WHERE u.GENDER IS NOT NULL AND TRIM(u.GENDER) != ' '
GROUP BY SUBSTRING(SALES_DATE, 1, 4),
SUBSTRING(SALES_DATE, 6, 2), u.GENDER
ORDER BY YEAR, MONTH, GENDER ASC;

/* 
SQL가 자동으로 번역하는 경우
1. 숫자와 문자열을 비교할 때: 문자열을 숫자로 바꿔줌
2. 숫자와 날짜를 비교할 때: 숫자<->날짜(양방향)
3. 수학 연산에 다른 타입이 섞일 때: 숫자에 문자열을 더하면 문자열을 숫자로 바꿔서 계산함. 
*/