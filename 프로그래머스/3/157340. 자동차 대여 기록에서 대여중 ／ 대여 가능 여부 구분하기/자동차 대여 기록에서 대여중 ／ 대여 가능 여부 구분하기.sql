-- 코드를 입력하세요
SELECT A.CAR_ID, CASE WHEN B.CAR_ID IS NULL THEN '대여 가능' ELSE '대여중' END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS A
LEFT JOIN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE '2022-10-16' BETWEEN START_DATE AND END_DATE
) AS B
ON A.CAR_ID = B.CAR_ID
GROUP BY A.CAR_ID
ORDER BY A.CAR_ID DESC