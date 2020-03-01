import React from 'react';
import './PokeModal.css'
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faTimesCircle} from '@fortawesome/free-solid-svg-icons'
import {useDispatch, useSelector} from "react-redux";

const PokeModal = () => {

    const pokeModal = useSelector(state => state.pokeModal);
    const dispatch = useDispatch();

    const handleTogglePokeModal = () => {
        console.log("TOGGLED");
        dispatch({type: "TOGGLE_POKEMODAL"});
    };

    let content = <>Sample Notification</>;
    console.log(pokeModal);
    switch (pokeModal.type) {
        case "connectToTwitter":
            content = (
                <>
                    <p>To use this poke connect your Twitter account!</p>
                </>
            );
            break;
        case "connectToInstagram":
            content = (
                <>
                    <p>To use this poke connect your Instagram account!</p>
                </>
            );
            break;
        default:
            break;
    }

    return (
        <>
            <div onClick={() => handleTogglePokeModal()} className="false-screen" style={pokeModal.open ? {display: "none", opacity: 0} : {display: "block", opacity: 0.1}} />
            <section id="PokeModal" style={pokeModal.open ? {marginTop: "-200px"} : {marginTop: "10px"}}>
                <button onClick={() => handleTogglePokeModal()}><FontAwesomeIcon icon={faTimesCircle} /></button>
                {content}
            </section>
        </>
    )
};

export default PokeModal;
