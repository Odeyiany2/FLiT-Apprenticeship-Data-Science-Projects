/*select *
from dbo.[hotel-reviews - hotel_bookings]
*/

-- Creating a table that shows the total revenue for each year in each hotel
SELECT
    SUM(([hotel-reviews - hotel_bookings].stays_in_week_nights + [hotel-reviews - hotel_bookings].stays_in_weekend_nights) * [hotel-reviews - hotel_bookings].adr) AS Revenue, 
    arrival_date_year, hotel
FROM [hotel-reviews - hotel_bookings]
WHERE [hotel-reviews - hotel_bookings].reservation_status NOT LIKE 'Canceled'
GROUP BY arrival_date_year, hotel
ORDER BY arrival_date_year;


----getting the total yearly revenue
SELECT
    SUM(([hotel-reviews - hotel_bookings].stays_in_week_nights + [hotel-reviews - hotel_bookings].stays_in_weekend_nights) * [hotel-reviews - hotel_bookings].adr) AS Revenue, 
    arrival_date_year
FROM [hotel-reviews - hotel_bookings]
WHERE [hotel-reviews - hotel_bookings].reservation_status NOT LIKE 'Canceled'
GROUP BY arrival_date_year
ORDER BY arrival_date_year;


-- getting the total revenue cotributed by each segment yearly 
SELECT
    SUM(([hotel-reviews - hotel_bookings].stays_in_week_nights + [hotel-reviews - hotel_bookings].stays_in_weekend_nights) * [hotel-reviews - hotel_bookings].adr) AS Revenue, 
    arrival_date_year,hotel, market_segment
FROM [hotel-reviews - hotel_bookings]
WHERE [hotel-reviews - hotel_bookings].reservation_status NOT LIKE 'Canceled'
GROUP BY arrival_date_year,hotel, market_segment
ORDER BY arrival_date_year;


-- getting the total number of people that visits the Hotel
select sum([hotel-reviews - hotel_bookings].adults+[hotel-reviews - hotel_bookings].children+[hotel-reviews - hotel_bookings].babies) as Visitors, arrival_date_year, arrival_date_month, hotel
from [hotel-reviews - hotel_bookings]
where [hotel-reviews - hotel_bookings].reservation_status not like 'Canceled'
group by arrival_date_year, arrival_date_month, hotel

--calculation to check if there is an increase in the demand for parking spaces over the years
select sum([hotel-reviews - hotel_bookings].required_car_parking_spaces) as parking_spaces, [hotel-reviews - hotel_bookings].arrival_date_year, hotel
from [hotel-reviews - hotel_bookings]
where [hotel-reviews - hotel_bookings].reservation_status not like 'Canceled'
group by arrival_date_year, hotel
order by arrival_date_year


--calculation to check if there is an increase in the demand for special requests over the years
select sum([hotel-reviews - hotel_bookings].total_of_special_requests) as special_requests, [hotel-reviews - hotel_bookings].arrival_date_year, hotel, customer_type
from [hotel-reviews - hotel_bookings]
where [hotel-reviews - hotel_bookings].reservation_status not like 'Canceled'
group by arrival_date_year, hotel, customer_type
order by arrival_date_year
