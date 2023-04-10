import { useAuth0 } from "@auth0/auth0-react";
import React, { useState, useEffect } from "react";
import { NavBarTab } from "./nav-bar-tab";
import {check} from '../../../services/api'

export const NavBarTabs = () => {
  const { user, isAuthenticated,getAccessTokenSilently } = useAuth0();
  
  const [isAuthorized, setIsAuthorized] = useState(false);
  
  useEffect(() => {
    
    const checkPermission = async () => {
      const accessToken = await getAccessTokenSilently();
      
      const data = await check(accessToken);
      
      data.status==404?setIsAuthorized(false):setIsAuthorized(true);
      
    };

    checkPermission();

  }, []);


  return (
    <div className="nav-bar__tabs">
      {isAuthenticated && (
        <>
          <NavBarTab path="/profile" label="Profile" />
          <NavBarTab path="/search" label="Search" />
          <NavBarTab path="/history" label="History" />
          {isAuthorized && <NavBarTab path="/users" label="Users List" />}
        </>
      )}
    </div>
  );
};
