import React from 'react';
import './PokeCard.css';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faTimesCircle, faCheck} from '@fortawesome/free-solid-svg-icons'

const PokeCard = (props) => {

    const getHashTags = (inputText) => {
        let regex = /(?:^|\s)(?:#)([a-zA-Z\d]+)/gm;
        let matches = [];
        let match;
        while ((match = regex.exec(inputText))) {
            matches.push(match[1]);
        }
        for (let match of matches) {
            inputText = inputText.replace("#" + match, "");
        }
        return [matches, inputText];
    };

    const handlePoke = () => {
        switch (props.type) {
            case "tw_tweet":
                let tweetHashtags = getHashTags(props.data.text)[0];
                let tweetURL = "https://twitter.com/intent/tweet?text=" + getHashTags(props.data.text)[1];
                    if (tweetHashtags.length > 0) {
                        tweetURL += "&hashtags=";
                        for (let i = 0; i < tweetHashtags.length - 1; i++) {
                            tweetURL += tweetHashtags[i] + ",";
                        }
                        tweetURL += tweetHashtags[tweetHashtags.length - 1];
                    }
                window.location.href = tweetURL;
                break;
            default:
                console.error("Invalid Claim Type");
        }
    };

    const deferPoke = () => {
        console.log("Poke deferred")
    };

    return (
        <>
            <div className="PokeCard">
                <div className="info">
                    <h2>{props.name}</h2>
                    <p>On {props.platform}</p>
                    <p>For {props.reward} pts</p>
                </div>
                <div className="action">
                    <div className="delete" onClick={() => deferPoke()}>
                        <FontAwesomeIcon icon={faTimesCircle} />
                    </div>
                    <div className="claim" onClick={() => handlePoke()}>
                     <FontAwesomeIcon icon={faCheck} />&nbsp; Claim
                    </div>
                </div>


            </div>
        </>
    );
};

export default PokeCard;