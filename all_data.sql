

select cor.name as Название_курса,  cor.date_started as Дата_начала, st.name as ФИО_студента ,
		men.name as ФИО_Ментора, cor.language as Язык_название  
from user_course as cor
inner join user_student as st
on cor.student_id = st.id
inner join user_mentor as men
on cor.mentor_id = men.id