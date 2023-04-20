-- Select total sales per product category
Select PRODUCT_CATEGORY, ROUND(SUM(ORDER_SALES),0) as Sales FROM sales
group by PRODUCT_CATEGORY
order by Sales DESC;

-- Select the average price per product category and year
Select YEAR_ID, PRODUCT_CATEGORY, round(AVG(PRICE_PER_PRODUCT),2) AS AVG_PRICE FROM sales
GROUP BY PRODUCT_CATEGORY, YEAR_ID
ORDER BY PRODUCT_CATEGORY, YEAR_ID, AVG_PRICE DESC;

-- Join sales & customer table to get avg & total sales per customer ordered by total sales
SELECT c.CUSTOMER_NAME, ROUND(SUM(s.ORDER_SALES),0)  as total_sales, ROUND(AVG(S.PRICE_PER_PRODUCT),2) as avg_price FROM sales s
LEFT JOIN customer c
on s.Customer_ID = c.CUSTOMER_ID
GROUP BY c.CUSTOMER_NAME
ORDER BY total_sales DESC;

-- Calculate the percentage of Large Deals compared to Total_Sales
SELECT c.CUSTOMER_NAME, COUNT(CASE WHEN s.DEAL_SIZE = 'Large' THEN 1 END) as Large_Deals, COUNT(s.DEAL_SIZE) as Total_Sales,
ROUND(COUNT(CASE WHEN s.DEAL_SIZE = 'Large' THEN 1 END) / COUNT(s.DEAL_SIZE)*100,2) as perc_of_Large_Deals
FROM customer c
LEFT JOIN sales s ON s.Customer_ID = c.CUSTOMER_ID
GROUP BY c.CUSTOMER_NAME
ORDER BY perc_of_Large_Deals DESC, Total_Sales DESC;

-- Select the total sales per customer & total sales from the company and calculate the percentage of total sales per customer
SELECT c.CUSTOMER_NAME, ROUND(SUM(s.ORDER_SALES),0) as Total_Sales_Per_Customer,
ROUND((SELECT SUM(s.ORDER_SALES) FROM sales s),0) as Total_Sales, 
ROUND(ROUND(SUM(s.ORDER_SALES),0) / ROUND((SELECT SUM(s.ORDER_SALES) FROM sales s),0)*100,2) as Sales_Percentage
FROM customer c
LEFT JOIN sales s ON s.Customer_ID = c.CUSTOMER_ID
GROUP BY c.CUSTOMER_NAME
ORDER BY Sales_Percentage DESC;


SELECT * FROM customer c
LEFT JOIN sales s ON s.Customer_ID = c.CUSTOMER_ID;

-- Compare the average sales price to the msrp for each category per year
SELECT YEAR_ID, PRODUCT_CATEGORY, ROUND(AVG(PRICE_PER_PRODUCT),2) as average_price_per_product, ROUND(AVG(MSRP),2) AS average_MSRP,
ROUND(ROUND(AVG(PRICE_PER_PRODUCT),2) / ROUND(AVG(MSRP),2)*100,2) as price_compared_to_msrp 
FROM sales
GROUP BY YEAR_ID, PRODUCT_CATEGORY
ORDER BY price_compared_to_msrp DESC;

-- Most profitable month converting MONTH_ID to actual month names
SELECT 
    CASE 
        WHEN MONTH_ID = 1 THEN 'January'
        WHEN MONTH_ID = 2 THEN 'February'
        WHEN MONTH_ID = 3 THEN 'March'
        WHEN MONTH_ID = 4 THEN 'April'
        WHEN MONTH_ID = 5 THEN 'May'
        WHEN MONTH_ID = 6 THEN 'June'
        WHEN MONTH_ID = 7 THEN 'July'
        WHEN MONTH_ID = 8 THEN 'August'
        WHEN MONTH_ID = 9 THEN 'September'
        WHEN MONTH_ID = 10 THEN 'October'
        WHEN MONTH_ID = 11 THEN 'November'
        WHEN MONTH_ID = 12 THEN 'December'
    END AS Month_Name,
    ROUND(SUM(ORDER_SALES),0) AS Sales_per_Month 
FROM sales
GROUP BY MONTH_ID
ORDER BY MONTH_ID;

select PRODUCT_CATEGORY, MAX(ORDER_SALES) from sales
GROUP BY PRODUCT_CATEGORY;
