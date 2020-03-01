import React, {useState} from 'react';
import './ConnectButton.css';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faInstagram} from '@fortawesome/free-brands-svg-icons';
import {faLink} from '@fortawesome/free-solid-svg-icons';
import {Link} from "react-router-dom";
import {useDispatch, useSelector} from "react-redux";

const InstagramButton = () => {

    const dispatch = useDispatch();

    const instagramToken = useSelector(state => state.instagramToken);

    return (
        <>
            <Link className="connect" id={instagramToken != null ? "instagram-connected" : "instagram"} to="/connect-instagram">
                { instagramToken != null ?
                    (<><FontAwesomeIcon icon={faLink} />&nbsp; Connected to Instagram</>)
                    :
                    (<><FontAwesomeIcon icon={faInstagram} />&nbsp; Connect to Instagram</>)
                }
            </Link>
        </>
    );
}

export default InstagramButton;