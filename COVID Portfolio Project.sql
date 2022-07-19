SELECT * FROM coviddeaths
WHERE location = 'World'
group by location;

-- SELECT Data that we are going to be using

select location, date, total_cases, new_cases, total_deaths, population 
FROM coviddeaths
ORDER BY 1,2;

-- Looking at Total Cases vs Total Deaths
-- Shows the likelihood of dying if you contract covid in the United States
select location, date, total_cases, total_deaths, (total_deaths / total_cases)*100 as death_percentage
FROM coviddeaths
where location = 'United states'
ORDER BY 1,2;

-- Looking at Total Cases vs Population in the United States
-- Shows what percentage of population got Covid
select location, date, population, total_cases, (total_cases / population)*100 as percent_population_infected
FROM coviddeaths
where location = 'United states'
ORDER BY 1,2;

-- Looking at countries with highest infection rate compared to population
select location, population, MAX(total_cases) as highest_infection_count, (MAX(total_cases / population))*100 as percent_population_infected
FROM coviddeaths
Group by location, population
ORDER BY percent_population_infected desc;

-- Showing countries with highest death count per population and excluding continents
select location, MAX(total_deaths) as total_death_count
FROM coviddeaths
WHERE continent is not null
Group by location
ORDER BY total_death_count desc;

-- LET'S BREAK THINGS DOWN BY CONTINENT
-- Showing the continents with the highest death count per population
select location, MAX(total_deaths) as total_death_count
FROM coviddeaths
WHERE continent is null AND location NOT IN ('High income','Upper middle income', 'Lower middle income', 'Low income', 'International') 
Group by location
ORDER BY total_death_count desc;


-- GLOBAL NUMBERS
-- Looking at the death percentage per day
select date, SUM(new_cases) as total_cases, SUM(new_deaths) as total_deaths, SUM(new_deaths)/SUM(new_cases)*100 as death_percentage
FROM coviddeaths
-- where location = 'United states' 
Where continent is not null
GROUP BY date
ORDER BY 1,2;


-- JOIN COVIDDEATHS AND COVIDVACCINATINOS TOGETHER
-- Looking at Total Population vs Vaccinations

select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
SUM(vac.new_vaccinations) OVER (Partition by dea.location order by dea.location, dea.date) as rolling_people_vaccinated
FROM coviddeaths dea
join covidvaccinations vac on dea.location = vac.location AND dea.date = vac.date
WHERE dea.continent is not null
order by 2,3;

-- USE CTE

With PopvsVac (continent, location, date, population, new_vaccinations, rolling_people_vaccinated)
as
(
select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
SUM(vac.new_vaccinations) OVER (Partition by dea.location order by dea.location, dea.date) as rolling_people_vaccinated
FROM coviddeaths dea
join covidvaccinations vac on dea.location = vac.location AND dea.date = vac.date
WHERE dea.continent is not null
)
Select *, (rolling_people_vaccinated / population)*100 FROM PopvsVac;



-- Creating view to store data for later visualizations

Create VIEW percent_population_vaccinated as 
select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
SUM(vac.new_vaccinations) OVER (Partition by dea.location order by dea.location, dea.date) as rolling_people_vaccinated
FROM coviddeaths dea
join covidvaccinations vac on dea.location = vac.location AND dea.date = vac.date
WHERE dea.continent is not null;


