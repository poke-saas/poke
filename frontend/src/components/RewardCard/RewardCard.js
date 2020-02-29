import React from 'react';
import './RewardCard.css';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faCheck as check, faTrophy} from '@fortawesome/free-solid-svg-icons'

const handleOnClick = (e) => {
    e.preventDefault();
    console.log("Button clicked listener")
}

const RewardCard = (props) => {

    return (
        <>
            <div className="RewardCard">
                <img src="https://via.placeholder.com/400x175" />
                <div className="info">
                    <h2>{props.name}</h2>
                    <p>Sample text, description of info.</p>
                    <div className="claim-wrapper">
                        <div className="cost"><FontAwesomeIcon icon={faTrophy} />&nbsp; Costs {props.cost} pts</div>
                        <div className="claim">
                            <button><FontAwesomeIcon icon={check} />&nbsp; Claim Reward</button>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}

export default RewardCard;