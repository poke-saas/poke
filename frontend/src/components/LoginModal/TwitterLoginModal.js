import React, {useState} from 'react';
import './LoginModal.css';
import {useDispatch, useSelector} from "react-redux";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faChevronLeft, faChevronRight} from '@fortawesome/free-solid-svg-icons';
import {faTwitter} from '@fortawesome/free-brands-svg-icons';
import {Link} from "react-router-dom";
import axios from 'axios';
import { useHistory } from "react-router-dom";

const TwitterLoginModal = (props) => {
    let history = useHistory();
    const dispatch = useDispatch();
    const uid = useSelector(state => state.uid);

    const submitTwitter = () => {
        let user = document.getElementById("tw-username").value;
        let pass = document.getElementById("tw-password").value;
        axios.get("https://us-central1-poke-app-269623.cloudfunctions.net/poke-add-social-integration?uid=" + uid + "&s_type=2&s_uname=" + user + "&s_pwd=" + pass)
            .then(res => {
                console.log(res);
                dispatch({type: "UPDATE_TWITTER_TOKEN", twitterToken: "TEMP_VAL"})
                history.push("/user");
            })
    };

    return (
        <main>
            <header>
                <Link to="/user"><FontAwesomeIcon color={"white"} icon={faChevronLeft} /></Link>&nbsp;&nbsp;&nbsp; Connect to Twitter
            </header>
            <div className="login-card" id={"twitter-login-card"}>
                <h3>Connect to <span style={{color: "#1da1f2"}}>&nbsp;<FontAwesomeIcon icon={faTwitter} /> Twitter</span></h3>
                <input id="tw-username" type="text"/>
                <input id="tw-password" type="password"/>
                <button className="submit" onClick={() => submitTwitter()}>Submit &nbsp;<FontAwesomeIcon icon={faChevronRight} /></button>
            </div>
        </main>
    );
};

export default TwitterLoginModal;