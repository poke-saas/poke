import React, {useState} from 'react';
import RewardCard from '../RewardCard/RewardCard';
import './Rewards.css';
import {faTrophy} from "@fortawesome/free-solid-svg-icons";
import { useSelector, useDispatch } from 'react-redux';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

const Rewards = () => {

    const dispatch = useDispatch();
    const points = useSelector(state => state.points);

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