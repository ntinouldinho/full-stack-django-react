import React, { useState, useEffect } from 'react';
import Autocomplete from '../components/Autocomplete';
import Weather from '../components/Weather';
import axios from 'axios';
import { useAuth0 } from "@auth0/auth0-react";
import { PageLayout } from "../components/page-layout";
import {getSearchHistory} from '../services/api'

export const HistoryPage= () => {
  const [cities, setCities] = useState([]);

  const { user, isAuthenticated, getAccessTokenSilently } = useAuth0();
  
  useEffect(() => {
    let isMounted = true;

    const getMessage = async () => {

      const accessToken = await getAccessTokenSilently();
        
      const data = await getSearchHistory(accessToken);
        
      setCities(data);

        if (!isMounted) {
          return;
        }
    };

    getMessage();

    return () => {
      isMounted = false;
    };
  }, [getAccessTokenSilently]);


  return (
    isAuthenticated && (<PageLayout>
        <ul>
          {cities.length>0?(cities?.map((item,i) => 
            <li key={i} style={{marginBottom: '50px'}}>
                <p>City: {item.fields.city}</p>
                <p>Date: {item.fields.date}</p>
                <p>IP: {item.fields.ip}</p>
                
                
            </li>
            )):<div> no data </div>}
        </ul>
    </PageLayout>)
  );
}



