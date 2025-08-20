# Lv.4 주문량이 많은 아이스크림들 조회하기
# 쿼리가 지저분하다.. 더 깔끔하게 쓰는 법도 있었을텐데 
SELECT flavor 
FROM (SELECT flavor, 
SUM(total_order) AS total_sale_by_flavor 
FROM (SELECT f.shipment_id, f.flavor, f.total_order FROM FIRST_HALF f
LEFT JOIN JULY j
ON f.shipment_id=j.shipment_id
UNION
SELECT j.shipment_id, j.flavor, j.total_order FROM FIRST_HALF f
RIGHT JOIN JULY j
ON f.shipment_id=j.shipment_id) as new
GROUP BY flavor
ORDER BY total_sale_by_flavor DESC) as real_new
LIMIT 3;