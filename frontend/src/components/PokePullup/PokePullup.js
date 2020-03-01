import React, {useState} from 'react';
import './PokePullup.css';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faTimesCircle, faCheckSquare} from '@fortawesome/free-solid-svg-icons'
import {faSquare} from '@fortawesome/free-regular-svg-icons'
import {useDispatch, useSelector} from "react-redux";

const PokePullup = () => {

    const pokePullup = useSelector(state => state.pokePullup);
    const dispatch = useDispatch();
    const [step, updateStep] = useState(1);

    const handleTogglePokePullup = () => {
        console.log("TOGGLED");
        dispatch({type: "TOGGLE_POKEPULLUP"});
    };

    let step1, step2 = <></>;

    console.log(pokePullup);
    switch (pokePullup.job.type) {
        case "verifyTweet":
            step1 = (
                <>
                    <button style={step === 1 ? {} : {backgroundColor: "lightGrey", color: "grey", opacity: 0.5}} onClick={() => {window.location.href = pokePullup.job.step1; updateStep(step + 1)}}>Tweet to Claim Points</button>
                </>
            );
            step2 = (
                <>
                    <button style={step === 2 ? {} : {backgroundColor: "lightGrey", color: "grey", opacity: 0.5}}  onClick={() => console.log("RUN JOB")}>Confirm Posted Tweet</button>
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
                    <FontAwesomeIcon icon={step > 2 ? faCheckSquare : faSquare} />{step2}
                </div>
            </section>
        </>
    )
};

export default PokePullup;