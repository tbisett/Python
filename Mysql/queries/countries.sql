-- Number 1
SELECT countries.name, languages.language, languages.percentage 
FROM countries 
JOIN languages 
ON countries.id = languages.country_id 
WHERE languages.language = "Slovene"
ORDER BY languages.percentage DESC;

-- Number 2
SELECT countries.name, COUNT(cities.country_id) AS number_cities
FROM countries
JOIN cities 
ON cities.country_id = countries.id
GROUP BY cities.country_id
ORDER BY number_cities DESC;

-- Number 3
SELECT countries.name,  cities.name, cities.population, countries.id
FROM countries 
JOIN cities
ON cities.country_id = countries.id
WHERE countries.name = "Mexico" AND cities.population > 500000
ORDER BY cities.population DESC;

-- number 4
SELECT countries.name, languages.language, languages.percentage 
FROM countries
JOIN languages
ON languages.country_id = countries.id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;


-- number 5
SELECT countries.name, countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000;

-- number 6
SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE countries.government_form = "Constitutional Monarchy" AND countries.capital > 200 AND countries.life_expectancy > 75;


-- number 7
SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities
ON cities.country_id = countries.id
WHERE cities.district = "Buenos Aires" AND cities.population > 500000;


-- number 8
SELECT countries.region, COUNT(countries.id) AS countries
FROM countries
GROUP BY countries.region
ORDER BY countries DESC;








