import React, {useState} from 'react';
import './ConnectButton.css';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faTwitter} from '@fortawesome/free-brands-svg-icons';
import {faLink} from '@fortawesome/free-solid-svg-icons';

const TwitterButton = () => {

    const [isConnected, toggleConnected] = useState(false);

    return (
        <button className="connect" id={isConnected ? "twitter-connected" : "twitter"} onClick={() => toggleConnected(!isConnected)}>
            { isConnected ? 
                (<><FontAwesomeIcon icon={faLink} />&nbsp; Connected to Twitter</>)
                :
                (<><FontAwesomeIcon icon={faTwitter} />&nbsp; Connect to Twitter</>)
            }
        </button>
    );
}

export default TwitterButton;