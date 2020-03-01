import React, {useEffect} from 'react';
import PokeCard from '../PokeCard/PokeCard';
import './Pokes.css';
import RewardCard from "../RewardCard/RewardCard";
import {useDispatch, useSelector} from "react-redux";
import axios from "axios";

const Pokes = () => {

    const fetchRewards = () => {
        axios.get(`https://us-central1-poke-app-269623.cloudfunctions.net/function-1?function=poke_refresh&uid=1076440981d44efb`)
            .then(res => {
                const pokes = res.data;
                console.log(pokes.pokes);
                dispatch({type: "REFRESH_POKES", pokes: pokes.pokes});
            })
    };

    useEffect(() => fetchRewards(), []);

    const dispatch = useDispatch();
    const pokes = useSelector(state => state.pokes);


    return (
        <>
            <header>
                Pokes
            </header>
            <main className="container">
                {pokes.map(poke => (
                    <PokeCard
                        key={poke.id + "xx"}
                        id={poke.id}
                        name={poke.name}
                        reward={poke.pts}
                        cta={poke.cta}
                        desc={poke.desc}
                        data={poke.data}
                    />
                ))}
                <PokeCard 
                    name="Poke Name"
                    platform="fb"
                    reward={15}
                    type={"tw_tweet"}
                    data={{
                            text: "This is tweet! Crazy isn't it? #tweet #cool"
                        }}
                    id={"testHash45356"}
                />
            </main>
        </>
    );
}

export default Pokes;