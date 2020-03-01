import React, {useState} from 'react';
import './ConnectButton.css';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faTwitter} from '@fortawesome/free-brands-svg-icons';
import {faLink} from '@fortawesome/free-solid-svg-icons';
import {useDispatch, useSelector} from "react-redux";
import {Link} from "react-router-dom";

const TwitterButton = () => {

    const dispatch = useDispatch();

    const twitterToken = useSelector(state => state.twitterToken);

    return (
        <>
            <Link className="connect" id={twitterToken != null ? "twitter-connected" : "twitter"} to="/connect-twitter">
                { twitterToken != null ?
                    (<><FontAwesomeIcon icon={faLink} />&nbsp; Connected to Twitter</>)
                    :
                    (<><FontAwesomeIcon icon={faTwitter} />&nbsp; Connect to Twitter</>)
                }
            </Link>
        </>
    );
};

export default TwitterButton;