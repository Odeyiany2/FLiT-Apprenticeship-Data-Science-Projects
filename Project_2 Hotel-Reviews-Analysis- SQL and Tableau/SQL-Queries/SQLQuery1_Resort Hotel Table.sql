/*select *
from dbo.[hotel-reviews - hotel_bookings]
*/

-- creating a new table that contains only Resort hotel for each year
SELECT *
INTO H1
FROM dbo.[hotel-reviews - hotel_bookings]
WHERE hotel NOT LIKE 'City Hotel';

