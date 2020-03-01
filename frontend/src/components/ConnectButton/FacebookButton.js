import React, {useState} from 'react';
import './ConnectButton.css';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faFacebook} from '@fortawesome/free-brands-svg-icons';
import {faLink} from '@fortawesome/free-solid-svg-icons';
import {Link} from "react-router-dom";

const FacebookButton = () => {

    const [isConnected, toggleConnected] = useState(false);

    return (
        <Link className="connect" id={isConnected ? "facebook-connected" : "facebook"} onClick={() => toggleConnected(!isConnected)}>
            { isConnected ? 
                (<><FontAwesomeIcon icon={faLink} />&nbsp; Connected to Facebook</>)
                :
                (<><FontAwesomeIcon icon={faFacebook} />&nbsp; Connect to Facebook</>)
            }
        </Link>
    );
}

export default FacebookButton;