import React from 'react';
import './PokeCard.css';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faTimesCircle, faFlag} from '@fortawesome/free-solid-svg-icons'

const handleOnClick = (e) => {
    e.preventDefault();
    console.log("Button clicked listener")
}

const PokeCard = (props) => {

    return (
        <>
            <div className="PokeCard">
                <div className="info">
                    <h2>{props.name}</h2>
                    <p>On {props.platform}</p>
                    <p>For {props.reward} pts</p>
                </div>
                <div className="action">
                    <div className="delete" onClick={handleOnClick}>
                        <FontAwesomeIcon icon={faTimesCircle} />
                    </div>
                    <div className="claim">
                     <FontAwesomeIcon icon={faFlag} />&nbsp; Post
                    </div>
                </div>


            </div>
        </>
    );
}

export default PokeCard;