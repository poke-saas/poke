import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore } from 'redux';
import './index.css';
import { persistStore, persistReducer } from 'redux-persist'
import { PersistGate } from 'redux-persist/integration/react'
import storage from 'redux-persist/lib/storage'
import App from './App';
import * as serviceWorker from './serviceWorker';


const initialState = {
    twitterToken: null,
    facebookToken: null,
    instagramToken: null,
    declined: []
  };
  
  const reducer = (state = initialState, action) => {
  //  console.log(action);
    switch (action.type) {
        case "UPDATE_FACEBOOK_TOKEN":
            state = {
                ...state,
                facebookToken: action.facebookToken
            }
        case "UPDATE_TWITTER_TOKEN":
            state = {
                ...state,
                twitterToken: action.twitterToken
            }
        case "UPDATE_INSTAGRAM_TOKEN":
            state = {
                ...state,
                instagramToken: action.instagramToken
            }
    }
    return state;
  };
  
  const persistConfig = {
    key: 'root',
    storage
  };
  
  const persistedReducer = persistReducer(persistConfig, reducer);
  
  let store = createStore(persistedReducer);
  let persistor = persistStore(store);
  
  
  ReactDOM.render(
      <Provider store={store}>
        <PersistGate loading={null} persistor={persistor}>
          <App />
        </PersistGate>
      </Provider>,
      document.getElementById('root')
  );
  

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.register();
