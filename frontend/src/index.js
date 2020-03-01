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
    user: null,
    uid: null,
    rewardsEarned: 0,
    twitterToken: null,
    facebookToken: null,
    instagramToken: null,
    declined: [],
    points: 10,
    rewards: [],
    pokes: [],
    claimedRewards: [],
    pokeModal: {
        type: "",
        open: true
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
        case "HARD_RESET":
            state = initialState;
            break;
        case "LOGIN":
            state = {
                ...state,
                uid: action.user.id,
                points: action.user.points,
                user: action.user
            };
            console.log(state);
            break;
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
            let currentRewards = state.rewards;
            for (const reward of currentRewards) {
                console.log(reward);
                if (reward.id == action.thisReward) {
                    reward["claimed"] = true;
                    break;
                }
            }
            state = {
                ...state,
                points: action.points - action.cost,
                rewardsEarned: state.rewardsEarned + 1
            };
            break;
        case "ADD_POINTS":
            state = {
                ...state,
                points: state.points + action.points
                // claimedRewards: state.rewards.push(action.reward)
            };
            break;
        case "USE_POKE":
            let delPoke = -1;
            for (let i = 0; i < state.pokes.length; i++) {
                if (state.pokes[i].id == action.pokeID) {
                    delPoke = i;
                    break;
                }
            }
            console.log(delPoke);
            let newUsePokes = state.pokes.splice(delPoke);
            console.log(newUsePokes);
            state = {
                ...state,
                points: state.points + action.reward,
                pokes: newUsePokes
            };
            //console.log(state.pokes);
            break;
        case "REFRESH_REWARDS":
            // let newRewards = state.rewards;
            // let allRewards = action.rewards;
            // for (const reward of allRewards) {
            //     let isSame = false;
            //     for (const oldReward of newRewards)
            //         if (reward.id == oldReward.id) {
            //             isSame = true;
            //         }
            //     if (!isSame) {
            //         reward.claimed = false;
            //         newRewards.push(reward);
            //     }
            // }
            for (let reward of action.rewards) {
                reward["claimed"] = false;
            }
            state = {
                ...state,
                rewards: action.rewards
            };
            console.log(state.rewards);
            break;
        case "REFRESH_POKES":
            // let newPokes = state.pokes;
            // let allPokes = action.pokes;
            // for (const poke of allPokes) {
            //     let isSame = false;
            //     for (const oldPoke of newPokes)
            //         if (poke.id == oldPoke.id) {
            //             isSame = true;
            //         }
            //     if (!isSame) {
            //         newPokes.push(poke);
            //     }
            // };
            state = {
                ...state,
                pokes: action.pokes
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
                    pokeID: action.pokeID,
                    reward: action.reward
                }
            };
            break;
        case "CLEAR_POKEPULLUP":
            state={
                ...state,
                pokePullup: {
                    ...state.pokePullup,
                    job: {},
                    pokeID: -1,
                    reward: 0
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
