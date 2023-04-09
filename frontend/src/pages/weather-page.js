import React, { useState, useEffect } from 'react';
import Autocomplete from '../components/Autocomplete';
import Weather from '../components/Weather';
import axios from 'axios';
import { useAuth0 } from "@auth0/auth0-react";
import { PageLayout } from "../components/page-layout";
import {getSearch,postSearch,deleteSearch,addNotification,fetchWeatherDataAPI, rememberCity} from '../services/api'

export const WeatherPage = () => {
  const [cities, setCities] = useState([]);
  const [weatherData, setWeatherData] = useState([]);
  const { user, getAccessTokenSilently } = useAuth0();

  const fetchWeatherData = async () => {
    const accessToken = await getAccessTokenSilently();
    let data = await fetchWeatherDataAPI(cities,accessToken)
    data=data.filter((value) => value !== undefined);
    
    setWeatherData(data);

  };

  useEffect(() => {
    const loadData = async () => {
      const accessToken = await getAccessTokenSilently();
        
      const data = await getSearch(accessToken);
        
      setCities(data);
    };
    loadData();
  }, []);

  useEffect(() => {
    if (cities) {

      const interval = setInterval(() => {
        fetchWeatherData();
      }, 5000);
      
      fetchWeatherData()

      return () => clearInterval(interval); 
    }
  }, [cities]);




  const addCity = async (city) => {
    if(!cities.includes(city)) {


      
      const accessToken = await getAccessTokenSilently();

      const data = await postSearch(city, accessToken)
      


      setCities([...cities, city]);
      
      rememberCity(city)
      
    }
  };

  const removeCity = async (cityName) => {
    setCities(cities.filter((city) => city !== cityName));
    const accessToken = await getAccessTokenSilently();

    const data = await deleteSearch(cityName, accessToken)
  };

  const addNotificationFunc = async (city,date) => {

    const accessToken = await getAccessTokenSilently();

    const data = await addNotification(city, date, accessToken)
      
  };


  return (
    <PageLayout>
      <Autocomplete onSelectedCity={addCity} />
      <div style={{display: 'flex',flexDirection: 'row'}}>
      {weatherData.map((data) => (
        <Weather key={data.name} data={data} onRemove={removeCity} onAddNotification={addNotificationFunc}/>
))}
      </div>
    </PageLayout>
  );
}

