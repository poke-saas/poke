import React, {useEffect} from 'react';
import PokeCard from '../PokeCard/PokeCard';
import './Pokes.css';
import {useDispatch, useSelector} from "react-redux";

const Pokes = () => {

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
            </main>
        </>
    );
}

export default Pokes;