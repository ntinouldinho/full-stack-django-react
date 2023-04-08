import React, { useState } from 'react';
import Autosuggest from 'react-autosuggest';

const Autocomplete = (props) => {
  const [value, setValue] = useState('');
  const [suggestions, setSuggestions] = useState([]);

  const [cities, setCities] = useState(() => {
    // getting stored value
    const saved = localStorage.getItem("preload_cities");
    const initialValue = JSON.parse(saved);
    return initialValue || [];
  });

  const getSuggestions = (value) => {
    const inputValue = value.trim().toLowerCase();
    const inputLength = inputValue.length;

    return inputLength === 0
      ? []
      : cities.filter(
          (city) =>
            city.toLowerCase().slice(0, inputLength) === inputValue
        );
  };

  const onSuggestionSelected = (event, { suggestion }) => {
    console.log('Selected:', suggestion);
    setValue(suggestion);
    props.onSelectedCity(suggestion);
  };

  const renderSuggestion = (suggestion) => <div>{suggestion}</div>;

  const onChange = (event, { newValue, method }) => {
    setValue(newValue);
  };

  const onSuggestionsFetchRequested = ({ value }) => {
    setSuggestions(getSuggestions(value));
  };

  const onSuggestionsClearRequested = () => {
    setSuggestions([]);
  };

  const onClickSearch = () => {
    setCities([...cities,value])
    props.onSelectedCity(value);
  }
  const inputProps = {
    placeholder: 'Search for a city',
    value,
    onChange,
  };

  return (
    <div style={{display: 'flex',flexDirection: 'row'}}>
    <Autosuggest
      suggestions={suggestions}
      onSuggestionSelected={onSuggestionSelected}
      onSuggestionsFetchRequested={onSuggestionsFetchRequested}
      onSuggestionsClearRequested={onSuggestionsClearRequested}
      getSuggestionValue={(suggestion) => suggestion}
      renderSuggestion={renderSuggestion}
      inputProps={inputProps}
    />
    <button
    className='button-search'
    onClick={onClickSearch}>Search</button>
    </div>
  );
};

export default Autocomplete;
