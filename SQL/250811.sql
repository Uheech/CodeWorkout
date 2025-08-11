-- 코드를 입력하세요
# Lv2. 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기
'''
1. 조회수가 가장 높은 중고거래 게시물
- USED_GOODS_BOARD 에서 가장 조회수가 높은 BOARD_ID추출
- MAX랑 GROUPBY로 하자니 직관적이지 않아서 내 스스로도 이해가 어려워서 ORDER BY , LIMIT으로 해결함
2. 파일경로는 칵 컬럼 값을 CONCAT으로 합침
'''
SELECT CONCAT('/home/grep/src/',u2.BOARD_ID,'/',u2.FILE_ID,u2.FILE_NAME,u2.FILE_EXT) as FILE_PATH FROM (SELECT BOARD_ID FROM USED_GOODS_BOARD ORDER BY VIEWS DESC LIMIT 1) as u1
LEFT JOIN USED_GOODS_FILE u2
ON u1.BOARD_ID=u2.BOARD_ID
ORDER BY FILE_ID DESC;