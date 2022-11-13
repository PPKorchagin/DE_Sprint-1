;#a
select first_name||' '||case when middle_name is not null then (middle_name||' ') end || last_name,salary from employees where salary=(select max(salary) from employees);

;#b
select last_name from employees order by last_name asc;

;#c
select grade,avg(NOW()-start_date) from employees group by grade;

;#d
select e.last_name,d.name from employees e left join departments as d on d.id=e.dept_id;

;#e
with ms as (select e.dept_id,max(e.salary) sal from employees e group by e.dept_id) 
select d.name,ms.sal,e.last_name from departments d left join ms on ms.dept_id=d.id left join employees e on e.dept_id=d.id and ms.sal=e.salary;

;#f

with sc_int as (select emp_id,case 
  when score='A' then 0.2
  when score='B' then 0.1
  when score='C' then 0
  when score='D' then -0.1
  when score='E' then -0.2
  else 0
end sc from scores where year=2022),
coeffs as (select e.id,e.dept_id,e.salary*(1+(case when sum(s.sc) is not null then sum(s.sc) else 0 end)) ssum from employees e left join sc_int s on (e.id=s.emp_id) group by e.id,e.dept_id,e.salary order by ssum desc)
select d.name,sum(c.ssum) s from coeffs c left join departments d on c.dept_id=d.id group by c.dept_id,d.name order by s desc limit 1;

;#g 
with sc_int as (select emp_id,case 
  when score='A' then 0.2
  when score='B' then 0.1
  when score='C' then 0
  when score='D' then -0.1
  when score='E' then -0.2
  else 0
end sc from scores where year=2022) 
select emp_id,e.first_name,e.last_name,salary old_sal,salary*(case when sc>0.2 then 1.2 when sc>0 then 1.1 else 1 end) new_sal  from sc_int si left join employees e on e.id=si.emp_id;

;#f
create or replace view employees_indexed  as
with sc_int as (select emp_id,sum(case 
  when score='A' then 0.2
  when score='B' then 0.1
  when score='C' then 0
  when score='D' then -0.1
  when score='E' then -0.2
  else 0
end) sc from scores where year=2022 group by emp_id) 
select e.id,e.first_name,e.middle_name,e.last_name,e.start_date,e.job_title,e.grade,salary*(case when sc>0.2 then 1.2 when sc>0 then 1.1 else 1 end) salary,e.dept_id,e.driver_license  from sc_int si left join employees e on e.id=si.emp_id;

create or replace view employees_coeffs  as
with sc_int as (select emp_id,case 
  when score='A' then 0.2
  when score='B' then 0.1
  when score='C' then 0
  when score='D' then -0.1
  when score='E' then -0.2
  else 0
end sc from scores where year=2022) 
select e.dept_id,avg(case when sc>0.2 then 1.2 when sc>0 then 1.1 else 1 end) c_avg from sc_int si left join employees e on e.id=si.emp_id group by e.dept_id;


create or replace view stat_p1 as
with emp_cnt as (select e.dept_id,count(e.id) e_cnt from employees e group by e.dept_id),
emp_age as (select e.dept_id,avg(NOW()-e.start_date) e_exp from employees e group by e.dept_id),
emp_gr_j as (select e.dept_id,count(grade) g from employees e where grade='jun' group by e.dept_id),
emp_gr_m as (select e.dept_id,count(grade) g from employees e where grade='middle' group by e.dept_id),
emp_gr_s as (select e.dept_id,count(grade) g from employees e where grade='senior' group by e.dept_id),
emp_gr_l as (select e.dept_id,count(grade) g from employees e where grade='lead' group by e.dept_id),
emp_sal as (select e.dept_id,sum(salary) sal from employees e group by e.dept_id),
emp_sali as (select e.dept_id,sum(salary) sal from employees_indexed e group by e.dept_id),
score_a as (select e.dept_id,count(score) sc from employees e left join scores sc on e.id=sc.emp_id where score='A' group by e.dept_id ),
score_b as (select e.dept_id,count(score) sc from employees e left join scores sc on e.id=sc.emp_id where score='B' group by e.dept_id ),
score_c as (select e.dept_id,count(score) sc from employees e left join scores sc on e.id=sc.emp_id where score='C' group by e.dept_id ),
score_d as (select e.dept_id,count(score) sc from employees e left join scores sc on e.id=sc.emp_id where score='D' group by e.dept_id ),
score_e as (select e.dept_id,count(score) sc from employees e left join scores sc on e.id=sc.emp_id where score='E' group by e.dept_id )
select d.id,d.name,
e.last_name,
ec.e_cnt count_of_employees,
ea.e_exp experience,
ej.g juniors,
em.g middles,
es.g seniors,
el.g leads,
s.sal old_salary,
si.sal new_salary,
score_a.sc score_a,
score_b.sc score_b,
score_c.sc score_c,
score_d.sc score_d,
score_e.sc score_e
from departments d 
left join employees e on e.id=d.head 
left join emp_cnt ec on ec.dept_id=d.id 
left join emp_age ea on ea.dept_id=d.id
left join emp_gr_j ej on ej.dept_id=d.id
left join emp_gr_m em on em.dept_id=d.id
left join emp_gr_s es on es.dept_id=d.id
left join emp_gr_l el on el.dept_id=d.id
left join emp_sal s on s.dept_id=d.id
left join emp_sali si on si.dept_id=d.id
left join score_a  on score_a.dept_id=d.id
left join score_b  on score_b.dept_id=d.id
left join score_c  on score_c.dept_id=d.id
left join score_d  on score_d.dept_id=d.id
left join score_e  on score_e.dept_id=d.id
;

select p1.*,cf.c_avg,new_salary-old_salary prem_s,100*(new_salary-old_salary)/old_salary index_percent from stat_p1 p1 left join employees_coeffs cf on cf.dept_id=p1.id;

;Непонятно, чем отличается 10 и 11 от 19 и 20
