import React, {useState} from 'react';
import './ConnectButton.css';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faInstagram} from '@fortawesome/free-brands-svg-icons';
import {faLink} from '@fortawesome/free-solid-svg-icons';

const InstagramButton = () => {

    const [isConnected, toggleConnected] = useState(false);

    return (
        <button className="connect" id={isConnected ? "instagram-connected" : "instagram"} onClick={() => toggleConnected(!isConnected)}>
            { isConnected ? 
                (<><FontAwesomeIcon icon={faLink} />&nbsp; Connected to Instagram</>)
                :
                (<><FontAwesomeIcon icon={faInstagram} />&nbsp; Connect to Instagram</>)
            }
        </button>
    );
}

export default InstagramButton;