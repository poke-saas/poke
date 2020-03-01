import React, {useState} from 'react';
import './RewardCard.css';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faCheck as check, faTrophy, faTimes} from '@fortawesome/free-solid-svg-icons'
import {useDispatch, useSelector} from "react-redux";
import axios from "axios";

const RewardCard = (props) => {

    const points = useSelector(state => state.points);
    const uid = useSelector(state => state.uid);
    const dispatch = useDispatch();

    const handleClaimReward = () => {
        console.log(points >= props.cost);
        if (points >= props.cost) {
            axios.get("https://us-central1-poke-app-269623.cloudfunctions.net/poke-send-reward-verification-text?uid=" + uid + "&rid=" + props.id)
                .then(res => {
                    const resData = res;
                });
            console.log("Point balance: " + points + "\nCost: " + props.cost);
            dispatch({type: "CLAIM_REWARD", points: points, cost: props.cost, thisReward: props.id});
        }
        else console.error("Not enough points!\nPoint Balance: " + points);
    };

    return (
        <>
            <div className="RewardCard">
                <img src={props.img} alt="Reward Card Image" onError={"https://via.placeholder.com/400x175"} />
                <div className="info">
                    <h2>{props.name}</h2>
                    <p>Sample text, description of info.</p>
                    <div className="claim-wrapper">
                        <div className="cost"><FontAwesomeIcon icon={faTrophy} />&nbsp; Costs {props.cost} pts</div>
                        <div className="claim">
                            <button onClick={() => handleClaimReward()} className={!props.claimed && points >= props.cost ? "" : "unclaimable"}>
                                {props.claimed ?
                                    <><FontAwesomeIcon icon={check} />&nbsp; Reward Claimed</>
                                    : (points >= props.cost ?
                                    <><FontAwesomeIcon icon={check} />&nbsp; Claim Reward</>
                                    :
                                    <><FontAwesomeIcon icon={faTimes} />&nbsp; Insufficient Points</>)
                                }

                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
};

export default RewardCard;