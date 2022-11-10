create TYPE if not exists grade AS ENUM('jun','middle','senior','lead');


create TABLE if not exists departments (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  head INTEGER NULL
);

drop table if exists employees;
create table if not exists employees (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(64) NOT NULL,
  middle_name VARCHAR(64) NULL,
  last_name VARCHAR(64) NOT NULL,
  start_date date NOT NULL,
  job_title VARCHAR(32) NOT NULL,
  grade grade NOT NULL,
  salary numeric NOT NULL,
  dept_id integer NOT NULL,
  driver_license BOOLEAN NOT NULL,
  CONSTRAINT dept_fk FOREIGN KEY (dept_id) REFERENCES departments(id)
);
;dept_id integer references departments(id) ON DELETE CASCADE NOT NULL,

CREATE TYPE score AS ENUM('A','B','C','D','E');

create table if not exists scores(
  emp_id INTEGER references employees(id) ON DELETE CASCADE NOT NULL,
  year SMALLINT NOT NULL,
  quarter SMALLINT NOT NULL,
  score score NOT NULL,
  CONSTRAINT scores_pk PRIMARY KEY (emp_id,year,quarter)
);
;UNIQUE (emp_id,year,quarter),

INSERT INTO departments VALUES 
(DEFAULT,'Accounting',NULL),
(DEFAULT,'IT Dept',NULL),
(DEFAULT,'HR',NULL),
(DEFAULT,'MD',NULL);

INSERT INTO employees VALUES 
(DEFAULT, 'Ivanov','Ivan','Ivanovich','2020-01-14','Head of Accounting','lead',100000,1,False);

;ALTER SEQUENCE employees_id_seq RESTART WITH 1;
INSERT INTO employees VALUES 
(DEFAULT, 'Petrov','Petr','Petrovich','2019-02-15','Head of IT Dept','lead',200000,2,True),
(DEFAULT, 'Sidorov','Sidor','Sidorovich','2018-03-16','Head of HR','lead',150000,3,True),
(DEFAULT, 'Dmitriev','Dmitry','Dmitrievich','2017-04-17','Head of MD','lead',400000,4,False),
(DEFAULT, 'Sergeev','Sergey','Sergeevich','2016-05-18','Accounting Assistant', 'middle',80000,1,False),
(DEFAULT, 'Alexandrov','Alexandr','Alexandrovich','2015-06-19','System Administrator', 'middle',150000,2,False),
(DEFAULT, 'Artemev','Artemy','Artemevich','2014-07-20','Network engineer', 'middle',100000,2,True),
(DEFAULT, 'Viktorov','Viktor','Viktorovich','2013-08-21','L1 support engineer', 'jun',50000,2,False),
(DEFAULT, 'Denisov','Denis','Denisovich','2012-09-22','MD developer', 'jun',150000,4,False),
(DEFAULT, 'Mikhailov','Mikhail','Mikhailovich','2011-10-23','MD developer', 'middle',200000,4,True),
(DEFAULT, 'Kirillov','Kirill','Kirillovich','2010-11-24','MD developer', 'senior',300000,4,True);

;;ar=(A B C D E); echo "INSERT INTO scores VALUES"; for i in `seq 1 10`; do for y in `seq 2018 2022`; do for q in 1 2 3 4; do echo "($i,$y,$q,'${ar[$(( $RANDOM % ${#ar[@]} + 1 ))]}')"; done; done; done | sed -e '$!s/$/,/g;$s/$/;/g'

UPDATE departments SET head=1 where id=1;
UPDATE departments SET head=2 where id=2;
UPDATE departments SET head=3 where id=3;
UPDATE departments SET head=4 where id=4;

INSERT INTO departments VALUES (DEFAULT,'Data Analytics',NULL);

WITH dept as (select id from departments where name='Data Analytics')
INSERT INTO employees VALUES
(DEFAULT, 'Pavlov','Paul','Pavlovich','2009-12-16','Head of DA','lead',400000,(select id from dept),False);

WITH dept as (select id from departments where name='Data Analytics')
INSERT INTO employees VALUES
(DEFAULT, 'Igorev','Igor','Igorevich','2009-12-16','DA','jun',100000,(select id from dept),False),
(DEFAULT, 'Pavlov','Paul','Pavlovich','2009-12-16','DA','middle',200000,(select id from dept),False);

;#6.1
SELECT id,first_name||' '|| case when middle_name is null then ' ' else (middle_name || ' ') end || last_name as name, DATE_PART('year',NOW())-DATE_PART('year',start_date) as exp_years from employees;

;#6.2
SELECT id,first_name||' '|| case when middle_name is null then ' ' else (middle_name || ' ') end || last_name as name, DATE_PART('year',NOW())-DATE_PART('year',start_date) as exp_years from employees limit 3;

;#6.3
SELECT id from employees where driver_license ;

;#6.4
SELECT distinct e.id from employees e join scores s on (e.id=s.emp_id) where s.score in ('D','E');

;#6.5
SELECT max(salary) from employees;

;#6.6
SELECT d.name,count(e.id) from departments d left join employees e on (d.id=e.dept_id) group by (d.name) order by count(e.id) desc limit 1;

WITH c as (select d.name name,count(e.id) cnt from departments d left join employees e on (d.id=e.dept_id) group by (d.name))
SELECT name from c where cnt=(select max(cnt) from c);

;Крутая штука, взял с https://database.guide/3-ways-to-select-the-row-with-the-maximum-value-in-sql/ - opt 3
WITH c as (select d.name name,count(e.id) cnt from departments d left join employees e on (d.id=e.dept_id) group by (d.name))
SELECT c1.name from c c1 left join c c2 on c1.cnt<c2.cnt where c2.name is null; 

;#6.7
SELECT id from employees order by start_date;

;#6.8
SELECT e.grade,avg(e.salary) from employees e group by e.grade order by avg(e.salary);

;#6.9
select e.id,
first_name||' '|| case when middle_name is null then ' ' else (middle_name || ' ') end || last_name as name,
sum(
case 
  when s.score='A' then 0.2
  when s.score='B' then 0.1
  when s.score='C' then 0
  when s.score='D' then -0.1
  when s.score='E' then -0.2
  else 0
end) as s
  from employees e left join scores s on s.emp_id=e.id where year=2022 group by e.id order by s desc;

;second variant
with sc_int as (select emp_id,case 
  when score='A' then 0.2
  when score='B' then 0.1
  when score='C' then 0
  when score='D' then -0.1
  when score='E' then -0.2
  else 0
end sc from scores where year=2022)
select e,sum(s.sc) ssum from employees e left join sc_int s on (e.id=s.emp_id) group by e order by ssum desc;
