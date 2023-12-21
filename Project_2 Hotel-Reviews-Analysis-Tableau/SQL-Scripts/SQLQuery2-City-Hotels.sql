-- creating a new table that contains only Resort hotel for each year
with H2 as (
select *
from dbo.[hotel-reviews - hotel_bookings]
where hotel not like 'Resort Hotel'
)

select *
from H2