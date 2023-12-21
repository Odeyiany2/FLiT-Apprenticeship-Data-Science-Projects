-- creating a new table that contains only City hotel for each year
SELECT *
INTO H2
FROM dbo.[hotel-reviews - hotel_bookings]
WHERE hotel NOT LIKE 'Resort Hotel';
