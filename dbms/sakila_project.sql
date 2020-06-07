--Q1
Select first_name, last_name from actor where last_name="SON" order by first_name; --The result is an empty set, hence I used a different query to show the results
Select first_name, last_name from actor where last_name="DEPP" order by first_name;
--Q2
Select concat(s.first_name, " ", s.last_name) as staff_member, sum(p.amount) as total_amount from staff as s left join payment as p on s.staff_id = p.staff_id where month(p.payment_date) = 7 and year(payment_date) = 2005 group by s.staff_id limit 10;
--Q3
Select count(film_id) as Huncback_Impossible_copies from inventory where film_id = (select film_id from film where title="Hunchback Impossible");
--Q4
Select count(FA.actor_id) as Number_of_Actors, F.title from film as F, film_actor as FA where film_id=FA.film_id group by title;
--Q5
Select concat(first_name, " ", last_name) as Actor_Name from actor where actor_id in (select actor_id from film_actor where film_id in (select film_id from film where title="Alone Trip"));
--Q6
Select email from customer where customer_id in (select ID from customer_list where country="Canada");
--Q7
Select title, description as Description from film_list where category="Family";
--Q8
Select r.rental_date, f.title from rental as r, film as f, inventory as i where f.film_id = i.inventory_id and i.inventory_id = r.rental_id order by r.rental_date desc limit 10;
--Q9
Select s.store_id, a.address, c.city, co.country from store as s, address as a, city as c, country as co where s.address_id = a.address_id and a.city_id = c.city_id and c.country_id = co.country_id;
--Q10
Select title, description from film where description like "%Crocodile%" or title like "%Shark%" limit 10;
--Q11
Select f.title, f.release_year, l.name from film as f left join language as l on f.language_id = l.language_id limit 10;
--Q12
Select title, rental_duration from film where rental_duration in (select max(rental_duration) from film) limit 10;
--Q13
Select f.title, c.name from film as f, category as c, film_category as fi where f.film_id = fi.film_id and fi.category_id = c.category_id limit 10;
--Q14
Select c.customer_id, p.amount from customer as c left join payment as p on c.customer_id = p.customer_id order by p.amount asc limit 10;
--Q15
select concat(a.first_name, " ", a.last_name) as name, count(fa.film_id) as number_of_movies from actor as a, film_actor as fa, film as f where a.actor_id = fa.actor_id and fa.film_id = f.film_id group by name limit 10;
--Q16
Select film_id, title from film where film_id not in (select film_id from inventory) limit 10;
--Q17
Select customer_id from customer where customer_id not in (select customer_id from rental);
--Q18
Select count(f.film_id) as number_of_films, l.name from film as f, language as l, film_category as fc, category as c where f.language_id = l.language_id and f.film_id = fc.film_id and c.category_id = fc.category_id and c.name="Documentary" and l.name="English" group by l.name;
--Q19
Select name from language where name like "%n";
--Q20
Select country, count(ID) as total_Clients from customer_list group by country order by total_Clients desc limit 5;


--Question#2
create or replace view vw_Film_details as select FID as film_id, title, description, category, price, length, rating, actors from film_list;
--b
create or replace view vw_store_sales as select ss.store, ss.manager, ss.total_sales, c.city, co.country  from staff as s inner join sales_by_store as ss on concat(s.first_name, " ", s.last_name) = ss.manager left join address as a on s.address_id = a.address_id left join city as c on a.city_id = c.city_id left join country as co on c.country_id = co.country_id;

--Question#3
create trigger customer_date before insert on customer for each row begin if new.current_date > curdate() then signal sqlstate '45000' set message_text = "future date not allowed";
--Question#4
delimiter $$
create procedure counter() begin declare fws integer default 1;
declare sws integer default 1;
declare fwc integer default 1;
declare swc integer default 6;
set fwc = 101;
while fws < fwc
       	do while sws < swc do
	       	select concat(fws, " - ", sws) as counter;
	       	set sws = sws + 1; end while;
	       	set fws = fws + 1;
	       	set sws = 1;
 end while;
end$$

--Question#5
delimiter $$
create procedure sp_cust_info(In othercountry varchar(30))
begin
	select c.customer_id, c.first_name, c.last_name from customer where address_id in (select address_id from address where city_id in (select city_id from city where country_id in (select country_id from country where country = othercountry)));
end $$

