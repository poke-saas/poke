import React from 'react';
import PokeCard from '../PokeCard/PokeCard';
import './Pokes.css';

const Pokes = () => {
    return (
        <>
            <header>
                Pokes
            </header>
            <main className="container">
                <PokeCard 
                    name="Poke Name"
                    platform="fb"
                    reward={15}
                />
                <PokeCard 
                    name="Poke Name"
                    platform="ig"
                    reward={10}
                />
                <PokeCard 
                    name="Poke Name"
                    platform="fb"
                    reward={25}
                />
                <PokeCard 
                    name="Poke Name"
                    platform="fb"
                    reward={15}
                />
                <PokeCard 
                    name="Poke Name"
                    platform="ig"
                    reward={10}
                />
                <PokeCard 
                    name="Poke Name"
                    platform="fb"
                    reward={25}
                />
                <PokeCard 
                    name="Poke Name"
                    platform="fb"
                    reward={15}
                />
                <PokeCard 
                    name="Poke Name"
                    platform="ig"
                    reward={10}
                />
                <PokeCard 
                    name="Poke Name"
                    platform="fb"
                    reward={25}
                />
            </main>
        </>
    );
}

export default Pokes;