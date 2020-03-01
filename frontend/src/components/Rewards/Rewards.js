import React, {useEffect, useState} from 'react';
import axios from 'axios';
import RewardCard from '../RewardCard/RewardCard';
import './Rewards.css';
import {faTrophy} from "@fortawesome/free-solid-svg-icons";
import { useSelector, useDispatch } from 'react-redux';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

const Rewards = () => {

    const uid = useSelector(state => state.uid);

    const fetchRewards = () => {
        axios.get("http://us-central1-poke-app-269623.cloudfunctions.net/poke-get-rewards?uid=" + uid)
            .then(res => {
                const rewards = res.data;
                dispatch({type: "REFRESH_REWARDS", rewards: rewards.rewards});
            })
    };

    useEffect(() => fetchRewards(), []);

    const dispatch = useDispatch();
    const points = useSelector(state => state.points);
    const rewards = useSelector(state => state.rewards);

    return (
        <>
            <header>
                Rewards
            </header>
            <div className="point-display">
                <div className="display-table">
                    <FontAwesomeIcon className="vis" icon={faTrophy} style={{color: "orange", marginLeft: "10px"}} />
                    <div className="info">

                        { points === 0
                            ?
                                <>
                                    <h2>Try to earn some points by doing pokes!</h2>
                                    <p>Use points to claim awards from your organization.</p>
                                </>
                            :
                                <>
                                    <h2>You currently have {points} points!</h2>
                                    <p>Use your points to claim rewards.</p>
                                </>
                        }
                    </div>
                </div>
            </div>
            <button onClick={() => dispatch({type: "ADD_POINTS", points: 1})}>
                Add 1 pt
            </button>
            <main className="container">
                {rewards.map(reward => (
                    <RewardCard
                        key={reward.id}
                        name={reward.name}
                        cost={reward.cost}
                        img={reward.img}
                    />
                ))}
                <RewardCard 
                    name="Reward Name"
                    cost={4}
                    image="hi"
                />
            </main>
        </>
    );
};

export default Rewards;