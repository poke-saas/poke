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
    auth: "",
    twitterToken: "val",
    facebookToken: null,
    instagramToken: null,
    declined: [],
    points: 10,
    claimedRewards: [],
    pokeModal: {
        type: "",
        open: false
    },
    pokePullup: {
        job: "",
        pokeID: null,
        open: true
    }
  };

const reducer = (state = initialState, action) => {
  //  console.log(action);
    switch (action.type) {
        case "UPDATE_FACEBOOK_TOKEN":
            state = {
                ...state,
                facebookToken: action.facebookToken
            };
            break;
        case "UPDATE_TWITTER_TOKEN":
            state = {
                ...state,
                twitterToken: action.twitterToken
            };
            break;
        case "UPDATE_INSTAGRAM_TOKEN":
            state = {
                ...state,
                instagramToken: action.instagramToken
            };
            break;
        case "CLAIM_REWARD":
            state = {
                ...state,
                points: action.points - action.cost
                // claimedRewards: state.rewards.push(action.reward)
            };
            break;
        case "ADD_POINTS":
            state = {
                ...state,
                points: state.points + action.points
                // claimedRewards: state.rewards.push(action.reward)
            };
            break;
        case "TOGGLE_POKEMODAL":
            state = {
                ...state,
                pokeModal: {
                    ...state.pokeModal,
                    open: !state.pokeModal.open
                }
            };
            break;
        case "SET_POKEMODAL_TYPE":
            state = {
                ...state,
                pokeModal: {
                    ...state.pokeModal,
                    type: action.pokeModalType
                }
            };
            break;
        case "TOGGLE_POKEPULLUP":
            state = {
                ...state,
                pokePullup: {
                    ...state.pokePullup,
                    open: !state.pokePullup.open
                }
            };
            break;
        case "SET_POKEPULLUP_JOB":
            state = {
                ...state,
                pokePullup: {
                    ...state.pokePullup,
                    job: action.pokePullupJob,
                    pokeID: action.pokeID
                }
            };
            break;
        default:
            console.error("Invalid Action");
            break;
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
