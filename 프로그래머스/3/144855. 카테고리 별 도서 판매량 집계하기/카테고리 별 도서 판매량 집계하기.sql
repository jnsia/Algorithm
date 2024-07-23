-- 코드를 입력하세요
SELECT CATEGORY, SUM(BS.SALES) AS TOTAL_SALES
FROM BOOK AS B
JOIN (
    SELECT BOOK_ID, SALES
    FROM BOOK_SALES
    WHERE SALES_DATE LIKE '2022-01%'
) AS BS
ON B.BOOK_ID = BS.BOOK_ID
GROUP BY CATEGORY
ORDER BY CATEGORY