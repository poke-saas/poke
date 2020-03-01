import React, {useState} from 'react';
import './LoginModal.css';
import {useDispatch, useSelector} from "react-redux";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faChevronRight, faSpinner, faExclamationTriangle} from '@fortawesome/free-solid-svg-icons';
import axios from 'axios';
import { useHistory } from "react-router-dom";

const SignIn = (props) => {
    let history = useHistory();
    const dispatch = useDispatch();
    let isLoading = false;

    const submitLogin = () => {
        document.getElementById("error").style.display = "none";
        isLoading = true;
        let user = document.getElementById("username").value;
        let pass = document.getElementById("password").value;
        axios.get("https://us-central1-poke-app-269623.cloudfunctions.net/function-1?function=login&uname=" + user + "&pwd=" + pass)
            .then(res => {
                const data = res.data;
                if (data.user != null) {
                    dispatch({type: "LOGIN", user: data.user});
                    setTimeout(function(){isLoading = false;}, 3000);
                    history.push("/pokes");
                }
                else {
                    isLoading = false;
                    document.getElementById("error").style.display = "block";
                }
            })
    };

    return (
        <main>
            <header>
                Login
            </header>
            <div className="login-card" id={"login-card"}>
                <h1>Welcome to Poke!</h1>
                <h3>Login</h3>
                <p id="error" style={{color: "red", fontWeight: 600, margin: 0, display: "none"}}>
                    <FontAwesomeIcon icon={faExclamationTriangle} /> Invalid Credentials</p>
                <input id="username" type="text"/>
                <input id="password" type="password"/>
                <button className="submit" onClick={() => submitLogin()}>Submit &nbsp;
                    <FontAwesomeIcon spin={isLoading} icon={isLoading ? faSpinner : faChevronRight} /></button>
            </div>
        </main>
    );
};

export default SignIn;