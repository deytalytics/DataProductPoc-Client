# continents_and_countries 0.1
select cn.ContinentName,cn.ContinentCode, c.CountryName, c.TwoLetterCountryCode, c.ThreeLetterCountryCode,c.CountryNumber
from continents cn, countries c
where c.ContinentCode = cn.ContinentCode;