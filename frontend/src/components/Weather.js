import React, { useEffect, useState } from 'react';
import axios from 'axios';
import DatePicker from "react-datepicker";
import {addNotification} from '../services/api'
import { useAuth0 } from "@auth0/auth0-react";
import "react-datepicker/dist/react-datepicker.css";

const Weather = ( props ) => {
  const [startDate, setStartDate] = useState(new Date()); 
  const [hideDate, setHideDate] = useState(false);
  const { user, getAccessTokenSilently } = useAuth0();

  const sendNotification = async (city) => {
    const accessToken = await getAccessTokenSilently();
    addNotification(user.email, city, startDate, accessToken)

    setHideDate(!hideDate)

    
  }

  const temperature = Math.round(props.data.main.temp - 273.15);
  const icon = `https://openweathermap.org/img/wn/${props.data.weather[0].icon}.png`;

  return (
    <div style={{borderRight: '3px solid white', width: '20%', textAlign: 'center'}}>
      <h2 style={{color:'white'}}>{props.data.name}</h2>
      <img src={icon} alt={props.data.weather[0].description} /> 
       <p>{temperature}°C</p>
       <button onClick={() => props.onRemove(props.data.name)}>Remove</button>
       <button onClick={() => setHideDate(!hideDate)}>Remind</button>
  
       {hideDate && (
       <div style={{marginTop:"50px"}}>
        <DatePicker
          style={{marginTop:'50px'}}
          selected={startDate}
          onChange={(date) => setStartDate(date)}
          timeInputLabel="Time:"
          dateFormat="MM/dd/yyyy h:mm aa"
          showTimeInput
        />
        <button onClick={() => sendNotification(props.data.name) }>Submit</button>
        </div>
        )
        }

    </div>
  );
};

export default Weather;
