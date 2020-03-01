import React, {useState} from 'react';
import './PokePullup.css';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faTimesCircle, faCheckSquare, faSpinner} from '@fortawesome/free-solid-svg-icons'
import {faSquare} from '@fortawesome/free-regular-svg-icons'
import {useDispatch, useSelector} from "react-redux";
import axios from 'axios';

const PokePullup = () => {

    const pokePullup = useSelector(state => state.pokePullup);
    const dispatch = useDispatch();
    const [step, updateStep] = useState(1);
    const [loading, setLoading] = useState(false);
    const uid = useSelector(state => state.uid);

    const handleTogglePokePullup = () => {
        console.log("TOGGLED");
        dispatch({type: "TOGGLE_POKEPULLUP"});
    };

    const handleVerifyingTweet = () => {
        if(step === 2) {
            setLoading(true);
            console.log(pokePullup.job.pokeID);
            axios.get('https://us-central1-poke-app-269623.cloudfunctions.net/function-1?function=check_poke&uid=' + uid + '&poke_id=' + pokePullup.job.pokeID)
            .then(res => {
                const checkPoke = res.data;
                console.log(checkPoke);
                setLoading(false);
                updateStep(step + 1);
                window.document.getElementById("rewardModal").innerHTML = "You've earned " + pokePullup.job.reward + " points!";
            })
        }
    };

    let step1, step2 = <></>;

    switch (pokePullup.job.type) {
        case "verifyTweet":
            step1 = (
                <>
                    <button style={step === 1 ? {} : {backgroundColor: "lightGrey", color: "grey", opacity: 0.5}} onClick={() => {window.open(pokePullup.job.step1, "_blank"); setTimeout(function() {updateStep(step + 1)}, 1500)}}>Tweet to Claim Points</button>
                </>
            );
            step2 = (
                <>
                    <button style={step === 2 ? {} : {backgroundColor: "lightGrey", color: "grey", opacity: 0.5}}  onClick={() => handleVerifyingTweet()}>Confirm Posted Tweet</button>
                </>
            );
            break;
        default:
            break;
    }

    return (
        <>
            <div onClick={() => handleTogglePokePullup()} className="false-screen" style={pokePullup.open ? {display: "none", opacity: 0} : {display: "block", opacity: 0.1}} />
            <section id="PokePullup" style={pokePullup.open ? {marginBottom: "-67vh"} : {marginBottom: "0"}}>
                {/*<button onClick={() => handleTogglePokePullup()}><FontAwesomeIcon icon={faTimesCircle} /></button>*/}

                <div className="step">
                    <FontAwesomeIcon className="checkbox" icon={step > 1 ? faCheckSquare : faSquare} />
                    {step1}
                </div>
                <div className="step">
                    <FontAwesomeIcon spin={loading} animation icon={loading ? faSpinner : (step > 2 ? faCheckSquare : faSquare)} />{step2}
                </div>
                <div id="rewardModal" />
            </section>
        </>
    )
};

export default PokePullup;