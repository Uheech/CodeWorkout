# Lv2. 우유와 요거트가 담긴 장바구니
SELECT
    cart_id
FROM
    CART_PRODUCTS
WHERE
    NAME IN ('Milk', 'Yogurt') # 조건을 걸어주고
GROUP BY
    cart_id # ID 별로 묶어줘야 함 
HAVING
    COUNT(DISTINCT NAME) = 2; # 그리고 중복 피하기
