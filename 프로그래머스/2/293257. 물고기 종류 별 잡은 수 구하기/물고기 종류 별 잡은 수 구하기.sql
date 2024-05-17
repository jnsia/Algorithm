SELECT COUNT(FI.ID) AS FISH_COUNT ,FN.FISH_NAME
FROM FISH_INFO AS FI
JOIN FISH_NAME_INFO AS FN
ON FI.FISH_TYPE = FN.FISH_TYPE
GROUP BY FISH_NAME
ORDER BY FISH_COUNT DESC