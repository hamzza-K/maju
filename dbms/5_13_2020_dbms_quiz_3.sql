--Q1

Delimiter $$
create procedure getContinentByCountry(In otherContinent varchar(30))
begin
	select count(Name) as countries, Continent from country where Continent = otherContinent  group by Continent;
end $$
Delimiter ;

--Q2

Delimiter $$
create procedure getCityByCode(In otherCode varchar(5))
begin
	select Name from city where CountryCode = otherCode;
end $$
Delimiter ;
