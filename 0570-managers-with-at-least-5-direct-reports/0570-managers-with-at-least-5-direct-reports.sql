# Write your MySQL query statement below
-- select name from Employee where id in (select DISTINCT B.managerId  from Employee as A left join Employee as B on A.id = B.managerId having managerId <> '');

select name from Employee where id in (select managerId from Employee group by managerId having count(managerId) >=5 ) ;
