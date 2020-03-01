import React, {useState} from 'react';
import './LoginModal.css';
import {useDispatch, useSelector} from "react-redux";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faChevronRight} from '@fortawesome/free-solid-svg-icons';
import axios from 'axios';
import { useHistory } from "react-router-dom";

const SignIn = (props) => {
    let history = useHistory();
    const dispatch = useDispatch();

    const submitLogin = () => {
        let user = document.getElementById("username").value;
        let pass = document.getElementById("password").value;
        axios.get("https://us-central1-poke-app-269623.cloudfunctions.net/function-1?function=login&uname=" + user + "&pwd=" + pass)
            .then(res => {
                const data = res.data;
                if (data.user != null) {
                    console.log("error");
                    dispatch({type: "LOGIN", user: data.user});
                    history.push("/pokes");
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
                <input id="username" type="text"/>
                <input id="password" type="password"/>
                <button className="submit" onClick={() => submitLogin()}>Submit &nbsp;<FontAwesomeIcon icon={faChevronRight} /></button>
            </div>
        </main>
    );
};

export default SignIn;