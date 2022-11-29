select * from user_language
select * from user_student
select * from user_course

create or replace function get_course_id_by_email(email varchar(50)) 
returns table (user_cours_id bigint)as'
select co.id
from user_course as co
inner join user_student as st
on co.student_id=st.id
where st.email = email;
'language sql

select * from get_course_id_by_email('spencer@microsoft.com') 



