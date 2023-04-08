import { useAuth0 } from "@auth0/auth0-react";
import React from "react";
import { NavBarTab } from "./nav-bar-tab";

export const NavBarTabs = () => {
  const { isAuthenticated } = useAuth0();
  
  return (
    <div className="nav-bar__tabs">
      {isAuthenticated && (
        <>
          <NavBarTab path="/profile" label="Profile" />
          <NavBarTab path="/search" label="Search" />
          <NavBarTab path="/history" label="History" />
          <NavBarTab path="/users" label="Users List" />
        </>
      )}
    </div>
  );
};
