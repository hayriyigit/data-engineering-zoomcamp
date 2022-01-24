
## Week 1 Homework


## Question 3. Count records 

How many taxi trips were there on January 15?
= **53024**
```sql
SELECT COUNT(*)
FROM YELLOW_TAXI_DATA
WHERE EXTRACT(DAY FROM TPEP_PICKUP_DATETIME) = 15
	AND EXTRACT(MONTH FROM TPEP_PICKUP_DATETIME) = 1
```


## Question 4. Largest tip for each day

Find the largest tip for each day. 
On which day it was the largest tip in January?
= **2021-01-20 / 1140.44**
```sql
SELECT DATE(TPEP_PICKUP_DATETIME) AS _DATE,
	MAX(TIP_AMOUNT) AS MAX_TIP
FROM YELLOW_TAXI_DATA
WHERE EXTRACT(MONTH FROM TPEP_PICKUP_DATETIME) = 1
GROUP BY _DATE
ORDER BY MAX_TIP DESC
```


## Question 5. Most popular destination

What was the most popular destination for passengers picked up 
in central park on January 14?
= **97 Upper East Side South**
```sql
SELECT COUNT(*) AS _COUNT,
	TZD."Zone"
FROM YELLOW_TAXI_DATA AS YTD
LEFT JOIN TAXI_ZONE_DATA AS TZD ON YTD."DOLocationID" = TZD."LocationID"
WHERE YTD."PULocationID" = 43
	AND EXTRACT(DAY FROM YTD.TPEP_PICKUP_DATETIME) = 14
	AND EXTRACT(MONTH FROM YTD.TPEP_PICKUP_DATETIME) = 1
GROUP BY TZD."Zone"
ORDER BY _COUNT DESC
```

## Question 6. Most expensive locations

What's the pickup-dropoff pair with the largest 
average price for a ride (calculated based on `total_amount`)?
= **Alphabet City/Unknown**
```sql
SELECT AVG(TOTAL_AMOUNT) AS _AVG,
	YTD."PULocationID" AS PICKUP,
	YTD."DOLocationID" AS DROPOFF
FROM YELLOW_TAXI_DATA AS YTD
GROUP BY YTD."PULocationID",
	YTD."DOLocationID"
ORDER BY _AVG DESC
```

