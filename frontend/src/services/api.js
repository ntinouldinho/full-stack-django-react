export const getSearchHistory = async (accessToken) => {
    const data = await (
        await fetch('/history', {
        method: "GET",
        headers: {
        "content-type": "application/json",
        Authorization: `Bearer ${accessToken}`
        },
      })).json()

      return JSON.parse(data)
}


export const getUsers = async (accessToken) => {
    return await (
        await fetch(`/users`, {
        method: "GET",
        headers: {
        "content-type": "application/json",
        Authorization: `Bearer ${accessToken}`
        },
      })).json()

}

export const deleteUser = async (user_id, accessToken) => {
    return await (
        await fetch(`/user/${user_id}`, {
        method: "DELETE",
        headers: {
        "content-type": "application/json",
        Authorization: `Bearer ${accessToken}`
        },
    })).json()

}

export const check = async (accessToken) => {
  return await (
      await fetch(`/check`, {
      method: "GET",
      headers: {
      "content-type": "application/json",
      Authorization: `Bearer ${accessToken}`
      },
    }))

}


export const postSearch = async (city, accessToken) => {
    const data = {
        city: city,
      };

    return await (
        await fetch(`/search/`, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${accessToken}`
        }
    })).json()
}

export const getSearch = async (accessToken) => {
    return await (
        await fetch(`/search`, {
        method: "GET",
        headers: {
        "content-type": "application/json",
        Authorization: `Bearer ${accessToken}`
        },
      })).json()

}

export const deleteSearch = async (city, accessToken) => {

    return await (
        await fetch(`/search/${city}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${accessToken}`
        }
    })).json()
}

export const storeData = async (city, info, accessToken) => {
  const data = {
      city: city,
      data: info,
    };

  return await (
      await fetch(`/store/`, {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${accessToken}`
      }
  })).json()
}

export const addNotification = async (email, city, date, accessToken) => {

    const data = {
        email: email,
        city: city,
        date: date,
      };
      
      return await (
            await fetch(`/notification/`, {
                method: 'POST',
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${accessToken}`
            }
        })).json()


}


export const fetchWeatherDataAPI = async (cities, accessToken) => {
    return Promise.all(
        cities.map(async (city) => {
          const response = await fetch(
            `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=3579138b0fe249866d7145e5314136ef`
          );
          const data = await response.json();

          if(data.cod===404) return;

          await storeData(city, data, accessToken)

          return { ...data, name: city};
        })
      );
}

export const rememberCity = (city) => {
    const saved = localStorage.getItem("preload_cities");
    const parsedArray = saved ? JSON.parse(saved) : [];
    if(!parsedArray.includes(city)) {
    
    const newArray = [...parsedArray, city];
    localStorage.setItem("preload_cities", JSON.stringify(newArray));
    }
}