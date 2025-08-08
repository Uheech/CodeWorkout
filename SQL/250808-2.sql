# Lv2.재구매가 일어난 상품과 회원 리스트 구하기
SELECT USER_ID, PRODUCT_ID 
FROM ONLINE_SALE
# 동일한 회원이, 동일한 상품을 구매했는지 보려면 순차적으로 묶어주기
GROUP BY USER_ID,PRODUCT_ID 
# 그리고 그 값이 1이 넘어야 함, 그러니까 2번이상 산거임
HAVING count(*)>1
ORDER BY USER_ID ASC, PRODUCT_ID DESC;
