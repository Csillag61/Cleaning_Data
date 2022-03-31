%%capture
%load_ext sql
%sql sqlite:///factbook.db

%%sql
SELECT *
  FROM sqlite_master
 WHERE type='table';

# type	name	tbl_name	rootpage	sql
# table	facts	facts	2	CREATE TABLE "facts" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "code" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "area" integer, "area_land" integer, "area_water" integer, "population" integer, "population_growth" float, "birth_rate" float, "death_rate" float, "migration_rate" float, "created_at" datetime, "updated_at" datetime)
# table	sqlite_sequence	sqlite_sequence	3	CREATE TABLE sqlite_sequence(name,seq)

%%sql
SELECT *
  FROM facts
 LIMIT 5;
 
# id	code	name	area	area_land	area_water	population	population_growth	birth_rate	death_rate	migration_rate	created_at	updated_at
# 1	af	Afghanistan	652230	652230	0	32564342	2.32	38.57	13.89	1.51	2015-11-01 13:19:49.461734	2015-11-01 13:19:49.461734
# 2	al	Albania	28748	27398	1350	3029278	0.3	12.92	6.58	3.3	2015-11-01 13:19:54.431082	2015-11-01 13:19:54.431082
# 3	ag	Algeria	2381741	2381741	0	39542166	1.84	23.67	4.31	0.92	2015-11-01 13:19:59.961286	2015-11-01 13:19:59.961286
# 4	an	Andorra	468	468	0	85580	0.12	8.13	6.96	0.0	2015-11-01 13:20:03.659945	2015-11-01 13:20:03.659945
# 5	ao	Angola	1246700	1246700	0	19625353	2.78	38.78	11.49	0.46	2015-11-01 13:20:08.625072	2015-11-01 13:20:08.625072

%%sql
SELECT MIN(population), MAX(population), MIN(population_growth), MAX(population_growth)
  FROM facts;

# MIN(population)	MAX(population)	MIN(population_growth)	MAX(population_growth)
# 0	7256490011	0.0	4.02

# There's a country with a population of 0
# There's a country with a population of 7256490011 (or more than 7.2 billion people)
# Let's use subqueries to zoom in on just these countries without using the specific values.

%%sql
SELECT *
  FROM facts
 WHERE population = (SELECT MIN(population)
                       FROM facts
                      WHERE name !='World'
                       );
# id	code	name	area	area_land	area_water	population	population_growth	birth_rate	death_rate	migration_rate	created_at	updated_at
# 250	ay	Antarctica	None	280000	None	0	None	None	None	None	2015-11-01 13:38:44.885746	2015-11-01 13:38:44.885746

%%sql
SELECT *
  FROM facts
 WHERE population = (SELECT MAX(population)
                       FROM facts
                      WHERE name !='World'
                       );  
 
# id	code	name	area	area_land	area_water	population	population_growth	birth_rate	death_rate	migration_rate	created_at	updated_at
# 37	ch	China	9596960	9326410	270550	1367485388	0.45	12.49	7.53	0.44	2015-11-01 13:22:53.813142	2015-11-01 13:22:53.813142

%%sql
SELECT *
  FROM facts
 WHERE population = (SELECT MIN(population_growth)
                       FROM facts
                      WHERE name !='World'
                       );  
 
%%sql
SELECT *
  FROM facts
 WHERE population = (SELECT MAX(population_growth)
                       FROM facts

%%sql
SELECT name, MIN(population), MAX(population), 
             MIN(population_growth), MAX(population_growth)
  FROM facts
 WHERE name != 'World'
 GROUP BY name;
 
%%sql
SELECT name, AVG(population), AVG(area)
  FROM facts
 WHERE name != 'World'
 GROUP BY name;
 
%%sql
SELECT COUNT(*)
  FROM facts;

%%sql
SELECT AVG(population), AVG(area)
  FROM facts
 WHERE population > 0
   AND name != 'World';
   
%%sql
SELECT name AS 'COUNTRY NAME', population AS 'POPULATION', area AS 'AREA'
  FROM facts
 WHERE population > 0
   AND name !='World'
   AND population > (SELECT AVG(population) 
                       FROM facts
                      WHERE population > 0
                        AND name !='World')
   AND area < (SELECT AVG(area)
           FROM facts
           WHERE name != 'World'
           AND population > 0)
 GROUP BY name;
   
# Which country has the most people? Which country has the highest growth rate?
%%sql
SELECT *
  FROM facts
 WHERE population_growth = (SELECT MAX(population_growth)
                            FROM facts
                            WHERE name != 'World');
 
%%sql
SELECT *
  FROM facts
 WHERE population = (SELECT MAX(population)
                       FROM facts
                    WHERE name !='World');
 
%%sql 
SELECT name AS 'Countries with more Water than Land', area_land, area_water
  FROM facts
 WHERE name != 'World'
   AND area_water > area_land
 ORDER BY area_water;
 
%%sql
SELECT name, area_land, area_water, 
        CAST(area_water as FLOAT)/area_land AS water_to_land
  FROM facts
 ORDER BY water_to_land DESC
 LIMIT 20;
 
%%sql
SELECT name, MAX(population*population_growth)
  FROM facts
 WHERE name !='World';
 
%%sql
SELECT name AS 'Country', birth_rate, death_rate
  FROM facts
 WHERE death_rate > birth_rate;

# Which countries have the highest population/area ratio, and how does it compare to list we found in the previous screen?

%%sql
SELECT *
  FROM facts
 WHERE population > (SELECT AVG(population)
                       FROM facts
                      WHERE name <> 'World'
                    )
   AND area < (SELECT AVG(area)
                 FROM facts
                WHERE name <> 'World'
);