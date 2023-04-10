import React, { useState, useEffect } from 'react';
import Autocomplete from '../components/Autocomplete';
import Weather from '../components/Weather';
import axios from 'axios';
import { useAuth0 } from "@auth0/auth0-react";
import { PageLayout } from "../components/page-layout";
import {getUsers, deleteUser} from '../services/api'

export const AllUsersPage = () => {
  const [users, setUsers] = useState([]);
  const [isAuthorized, setIsAuthorized] = useState(false);

  const { user, isAuthenticated, getAccessTokenSilently } = useAuth0();
  
  useEffect(() => {
    let isMounted = true;

    const getMessage = async () => {
      const accessToken = await getAccessTokenSilently();
      
      const data = await getUsers(accessToken)
      if(!data.error){
        setUsers(data);
        setIsAuthorized(true)
      }
      
      

      if (!isMounted) {
        return;
      }
    };

    getMessage();

    return () => {
      isMounted = false;
    };
  }, [getAccessTokenSilently]);

  
  const deleteUserId = async (user_id) => {
    const accessToken = await getAccessTokenSilently();

    const data = await deleteUser(user_id, accessToken);
    
    if(data.status === 'success'){
      window.location.reload(false);
    }

  }

  return (
    isAuthenticated && (<PageLayout>
        <div>
          {users.map((item,i) => 
            <div key={i} style={{marginBottom: '100px'}}>
                <p>Nickname: {item.nickname}</p>
                <p>Email: {item.email}</p>
                <p>Last Login: {item.last_login}</p>
                <p>Last IP: {item.last_ip}</p>
                {user.sub!=item.user_id && <button onClick={()=>deleteUserId(item.user_id)}>Delete User</button>}
                
                
            </div>
            )}
        </div>
    </PageLayout>)
  );
}



