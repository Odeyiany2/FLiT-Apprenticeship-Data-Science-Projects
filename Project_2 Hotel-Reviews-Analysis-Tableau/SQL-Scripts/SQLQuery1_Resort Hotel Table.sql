/*select *
from dbo.[hotel-reviews - hotel_bookings]
*/

-- creating a new table that contains only Resort hotel for each year
with H1 as (
select *
from dbo.[hotel-reviews - hotel_bookings]
where hotel not like 'City Hotel'
)

select *
from H1
