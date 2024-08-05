-- 코드를 입력하세요
# SELECT MONTH, CAR_ID, COUNT(*) RECORDS
# FROM (
#     SELECT CAR_ID, MONTH(START_DATE) AS MONTH
#     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     WHERE YEAR(START_DATE) = '2022' AND MONTH(START_DATE) IN ('08', '09', '10')
#     GROUP BY MONTH(START_DATE)
# ) AS RH
# GROUP BY CAR_ID
# ORDER BY MONTH, CAR_ID DESC

SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE YEAR(START_DATE) = '2022' AND MONTH(START_DATE) IN ('08', '09', '10') AND CAR_ID IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE YEAR(START_DATE) = '2022' AND MONTH(START_DATE) IN ('08', '09', '10')
    GROUP BY CAR_ID
    HAVING COUNT(*) >= 5
)
GROUP BY CAR_ID, MONTH
HAVING RECORDS > 0
ORDER BY MONTH, CAR_ID DESC