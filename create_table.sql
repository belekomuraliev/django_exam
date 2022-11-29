create table payments
(
	id serial primary key,
	courseid integer not null references user_course(id) on delete set default,
	amount integer,
	pay_date date not null
);



insert into payments(courseid, amount, pay_date)
values(2, 15000, '2022-08-15' )

insert into payments(courseid, amount, pay_date)
values(2, 55000, '2022-08-15' )

insert into payments(courseid, amount, pay_date)
values(1, 5000, '2022-08-15' )
