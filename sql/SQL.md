
## Entity Relationship Diagram: 


https://github.com/sksingh56/qvc/blob/bd33e7e9a63e4e54d93a2a5c81c889b6bfd219f3/sql/qvc_entity_relation_ship.drawio.png

### Note : SQL Queries have been tested on GCP BigQuery.

## Query 1 : All orders and their SUM, between 02.01.2019 and 04.01.2019.

The query calculates sales at order for orders between 02.01.2019 and 04.01.2019
 
 ```
SELECT
  PID_ORDER
 ,SUM(Unitprice * UNTS) total_sales
FROM
 `test.ORDERS` ord
JOIN
 `test.ORDER_ITEM` oritm
ON
 (ord.PID_ORDER = FID_ORDERS)
WHERE
 order_time >= '2019-01-02'
 and order_Time< '2019-01-05'
Group by PID_ORDER
order by PID_ORDER
 
PID_ORDER	total_sales
BB-83219	18.24
BB-83220	66.84
BB-83221	13.26
BB-83222	5.55
 ```

## Query 2: How many red, green and blue blocks have been sold in total including the ones that are part of the Starter Set? Hint: Article may have multiple levels of Child articles.

 ```

WITH
  article_hier AS (
  SELECT
    DISTINCT PID_ARTICLE,
    NAME,
    FID_PARENT_ARTICLE
  FROM
    test.ARTICLE art
  WHERE
    art.name IN ('RED',
      'BLUE',
      'GREEN',
      'BLOCKSET STARTER KIT')
    OR EXISTS (
    SELECT
      chld.FID_parent_ARTICLE
    FROM
      test.ARTICLE chld
    WHERE
      art.pid_article = chld.fid_parent_Article ) )
SELECT
  arh.PID_ARTICLE,
  arh.name Name,
  SUM(UNTS) Number_Sold
FROM
  article_hier arh
JOIN
  `test.ORDER_ITEM` ori
ON
  arh.PID_ARTICLE = ori.FID_ARTICLE
GROUP BY
  arh.PID_ARTICLE,
  arh.name
ORDER BY
  1


PID_ARTICLE	       Name	                     number_Sold
BB-10001	         BLOCKSET STARTER KIT	       13
BB-10002	         SQUARE BLOCK	               19
BB-10003	         RED	                       8
BB-10004	         BLUE	                       13
BB-10005	         GREEN	                     3

 ```
## Query 3: Top 3 Products of 2019 in comparison to 2018 by SUM OF PRICE

## option 1:
This query uses a CASE statement to sum the price of each product separately for 2019 and 2018. The results are then grouped by product name and ordered by 2019 sales in descending order. The LIMIT clause is used to only retrieve the top 3 products by sales in 2019.

 ```
 SELECT
  art.name,
  SUM(CASE
      WHEN EXTRACT(year FROM ord.order_time) = 2019 THEN (orit.unitprice * orit.unts)
    ELSE
    0
  END
    ) sale_2019,
  SUM(CASE
      WHEN EXTRACT(year FROM ord.order_time) = 2018 THEN (orit.unitprice * orit.unts)
    ELSE
    0
  END
    ) sale_2018
FROM
  `test.ORDERS` ord
INNER JOIN
  `test.ORDER_ITEM` orit
ON
  ord.pid_order = orit.FID_ORDERS
INNER JOIN
  test.ARTICLE art
ON
  art.pid_article = orit.fid_article
WHERE
  EXTRACT(year
  FROM
    ord.order_time) IN (2019,
    2018)
GROUP BY
  art.name
ORDER BY
  sale_2019 DESC
LIMIT
  3

name	                sale_2019	 sale_2018
BLOCKSET STARTER KIT	66.84	     367.62
SQUARE BLOCK	        18.24	     25.08
RED                   13.26	     22.1

 ```

## option 2: using window function rank
This query first calculates the total sales for each product and year  Then, it uses the RANK() windowing function to rank the products by total sales within each year, and stores the results in a CTE called ranked_products.

```
WITH product_sales AS (
SELECT
  art.name product,
  extract(year FROM ord.order_time) year,
  sum(orit.unitprice * orit.unts) total_sales,
  FROM
  `test.ORDERS` ord
INNER JOIN
  `test.ORDER_ITEM` orit
ON
  ord.pid_order = FID_ORDERS
INNER JOIN
  `test.ARTICLE` art
ON
  art.pid_article = orit.fid_article
WHERE ord.order_time >= '2018-01-01' 
AND ord.order_time < '2020-01-01'
GROUP BY
  art.name, year

), ranked_products AS (
  SELECT
    product,
    year,
    total_sales,
    RANK() OVER (PARTITION BY year ORDER BY total_sales DESC) AS rank
  FROM product_sales
)
SELECT 
  p2019.product AS product_2019,
  p2019.total_sales AS sales_2019,
  p2018.product AS product_2018,
  p2018.total_sales AS sales_2018
FROM 
  ranked_products p2019
  INNER JOIN ranked_products p2018 ON p2019.rank = p2018.rank
WHERE
  p2019.year = 2019
  AND p2018.year = 2018
ORDER BY
  p2019.total_sales DESC
LIMIT 3;

product_2019	        sales_2019	       product_2018	            sales_2018
BLOCKSET STARTER KIT	66.84              BLOCKSET STARTER KIT	     367.62
SQUARE BLOCK          18.24	             SQUARE BLOCK              25.08
RED                   13.26              RED                       22.1


 ```
