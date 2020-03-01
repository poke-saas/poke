import React from 'react';
import './User.css';
import {useSelector, useDispatch} from "react-redux";
import * as pic from '../../profile_davis.jpg'
import FacebookButton from '../ConnectButton/FacebookButton';
import TwitterButton from '../ConnectButton/TwitterButton';
import InstagramButton from '../ConnectButton/InstagramButton';
import axios from "axios";
import { useHistory } from "react-router-dom";

const User = () => {

    let history = useHistory();
    const points = useSelector(state => state.points);
    const uid = useSelector(state => state.uid);
    const user = useSelector(state => state.user);
    const rewardsEarned = useSelector(state => state.rewardsEarned);
    const dispatch = useDispatch();

    const fetchPokes = () => {
        axios.get(`https://us-central1-poke-app-269623.cloudfunctions.net/function-1?function=poke_refresh&uid=1076440981d44efb`)
            .then(res => {
                const pokes = res.data;
                console.log(pokes.pokes);
                dispatch({type: "REFRESH_POKES", pokes: pokes.pokes});
            })
    };

    const fetchRewards = () => {
        axios.get("https://us-central1-poke-app-269623.cloudfunctions.net/poke-get-rewards?uid=" + uid)
            .then(res => {
                const rewards = res.data;
                dispatch({type: "REFRESH_REWARDS", rewards: rewards.rewards});
            })
    };

    const resetAPI = () => {
        axios.get("https://us-central1-poke-app-269623.cloudfunctions.net/function-1?function=reset&uid=" + uid)
            .then(res => {
                const userInfo = res.data;
                console.log(userInfo);
            })
    };

    const fullReset = () => {
        dispatch({type: "HARD_RESET"});
        history.push("/login");
        fetchPokes();
        fetchRewards();
        resetAPI();
    };

    return (
        <>
            <header>
                User
            </header>
            <main className="container">
                <div className="user-info-card">
                    <img className="user-image" src={pic} />
                    <div className="user-info">
                        <h3>@{user.full_name}</h3>
                        <p style={{opacity: 0.6}}><span>Member of </span><span style={{fontWeight: 600}}>Founders</span></p>
                    </div>
                </div>
                <table>
                    <name>Your Stats</name>
                    <tr>
                        <th>Point Balance</th>
                        <td>{points} pts</td>
                    </tr>
                    <tr>
                        <th>All Time Points</th>
                        <td>63 pts</td>
                    </tr>
                    <tr>
                        <th>Rewards Earned</th>
                        <td>{rewardsEarned} Rewards</td>
                    </tr>
                </table>
                <FacebookButton 

                />
                <TwitterButton

                />
                <InstagramButton

                />
                <br />
                <button onClick={() => fullReset()}>
                    RESET DEMO
                </button>
            </main>
        </>
    );
}

export default User;