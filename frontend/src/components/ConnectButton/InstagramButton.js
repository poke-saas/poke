import React, {useState} from 'react';
import './ConnectButton.css';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faInstagram} from '@fortawesome/free-brands-svg-icons';
import {faLink} from '@fortawesome/free-solid-svg-icons';
import {Link} from "react-router-dom";

const InstagramButton = () => {

    const [isConnected, toggleConnected] = useState(false);

    return (
        <Link className="connect" id={isConnected ? "instagram-connected" : "instagram"} onClick={() => toggleConnected()}>
            { isConnected ? 
                (<><FontAwesomeIcon icon={faLink} />&nbsp; Connected to Instagram</>)
                :
                (<><FontAwesomeIcon icon={faInstagram} />&nbsp; Connect to Instagram</>)
            }
        </Link>
    );
}

export default InstagramButton;