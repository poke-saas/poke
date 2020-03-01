import React, {useEffect, useState} from 'react';
import axios from 'axios';
import RewardCard from '../RewardCard/RewardCard';
import './Rewards.css';
import {faTrophy} from "@fortawesome/free-solid-svg-icons";
import { useSelector, useDispatch } from 'react-redux';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

const Rewards = () => {

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
                    <FontAwesomeIcon className="vis" icon={faTrophy} style={{color: "orange", padding: "20px"}} />
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
            <main className="container" style={{paddingTop: "8em"}}>
                {rewards.map(reward => (
                    <RewardCard
                        id={reward.id}
                        name={reward.name}
                        cost={reward.cost}
                        img={reward.img}
                        claimed={reward.claimed}
                    />
                ))}
            </main>
        </>
    );
};

export default Rewards;