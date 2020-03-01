import React, {useState} from 'react';
import './LoginModal.css';
import {useDispatch, useSelector} from "react-redux";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faChevronLeft, faChevronRight} from '@fortawesome/free-solid-svg-icons';
import {faInstagram} from '@fortawesome/free-brands-svg-icons';
import {Link} from "react-router-dom";
import axios from 'axios';
import { useHistory } from "react-router-dom";

const InstagramLoginModal = (props) => {
    let history = useHistory();
    const dispatch = useDispatch();
    const uid = useSelector(state => state.uid);

    const submitInstagram = () => {
        let user = document.getElementById("ig-username").value;
        let pass = document.getElementById("ig-password").value;
        axios.get("https://us-central1-poke-app-269623.cloudfunctions.net/poke-add-social-integration?uid=" + uid + "&s_type=1&s_uname=" + user + "&s_pwd=" + pass)
            .then(res => {
                console.log(res);
                dispatch({type: "UPDATE_INSTAGRAM_TOKEN", instagramToken: "TEMP_VAL"});
                history.push("/user");
            })
    };

    return (
        <main>
            <header>
                <Link to="/user"><FontAwesomeIcon color={"white"} icon={faChevronLeft} /></Link>&nbsp;&nbsp;&nbsp; Connect to Instagram
            </header>
            <div className="login-card" id={"instagram-login-card"}>
                <h3>Connect to <span style={{color: "#c13584"}}>&nbsp;<FontAwesomeIcon icon={faInstagram} /> Instagram</span></h3>
                <input id="ig-username" type="text"/>
                <input id="ig-password" type="password"/>
                <button className="submit" onClick={() => submitInstagram()}>Submit &nbsp;<FontAwesomeIcon icon={faChevronRight} /></button>
            </div>
        </main>
    );
};

export default InstagramLoginModal;