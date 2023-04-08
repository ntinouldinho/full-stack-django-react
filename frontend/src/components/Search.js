import React, { useState, useEffect } from 'react';
import Autocomplete from './Autocomplete';
import Weather from './Weather';

const Search = () => {
  const [city, setCity] = useState('');
  const [weatherData, setWeatherData] = useState(null);

  const handleSelectedCity = (event, { suggestion }) => {
    setCity(suggestion.name);
  };

  useEffect(() => {
    if (city) {
      const fetchWeatherData = async () => {
        const response = await fetch(
          `http://api.openweathermap.org/data/2.5/weather?q=${city}&APPID=a6a511a552d838f54f37472a395f846e`
        );
        const data = await response.json();
        setWeatherData(data);
      };
      fetchWeatherData();
      const interval = setInterval(() => {
        fetchWeatherData();
      }, 5000);
      return () => clearInterval(interval);
    }
  }, [city]);

  return (
    <div>
      <Autocomplete onSelectedCity={handleSelectedCity} />
      {weatherData && <Weather data={weatherData} />}
    </div>
  );
};

export default Search;
