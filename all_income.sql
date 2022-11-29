select*t from payments

select  co.language, pay.amount 
from payments as pay
inner join user_course as co
on pay.courseid = co.id
