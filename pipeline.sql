# continents_and_countries 0.1
select cn."ContinentName",cn."ContinentCode", c."CountryName", c."TwoLetterCountryCode", c."ThreeLetterCountryCode",c."CountryNumber"
from src_data.continents cn, src_data.countries c
where c."ContinentCode" = cn."ContinentCode"    ;

# continents_and_countries 0.2
select cn."ContinentName" as Continent_Name,cn."ContinentCode" as Continent_Code, c."CountryName" as Country_Name,
c."TwoLetterCountryCode" as Two_Letter_Country_Code, c."ThreeLetterCountryCode" as Three_Letter_Country_Code,
c."CountryNumber" as Country_Number
from src_data.continents cn, src_data.countries c
where c."ContinentCode" = cn."ContinentCode";

# countries 0.1
select c."CountryName", c."TwoLetterCountryCode", c."ThreeLetterCountryCode",c."CountryNumber"
from src_data.countries c;

# continents 0.1
select cn."ContinentName" as Continent_Name,cn."ContinentCode" as Continent_Code
from src_data.continents cn;