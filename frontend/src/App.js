import React from 'react';
import './App.css';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import Pokes from './components/Pokes/Pokes';
import Rewards from './components/Rewards/Rewards'
import Users from './components/User/User';
import BottomNav from './components/BottomNav/BottomNav'
import PokeModal from './components/PokeModal/PokeModal'
import PokePullup from "./components/PokePullup/PokePullup";
import TwitterLoginModal from "./components/LoginModal/TwitterLoginModal";
import SignIn from "./components/LoginModal/SignIn";

function App() {
  return (
    <div className="App">
        <BrowserRouter>
            <Switch>
              <Route exact={true} path='/pokes' render={() => (
                  <Pokes />
              )}/>
              <Route exact={true} path='/rewards' render={() => (
                  <Rewards />
              )}/>
              <Route exact={true} path='/user' render={() => (
                  <Users />
              )}/>
                <Route exact={true} path='/connect-twitter' render={() => (
                    <TwitterLoginModal />
                )}/>
                <Route exact={true} path='/login' render={() => (
                    <SignIn />
                )}/>
              <Route component={Pokes} />
            </Switch>
          <BottomNav />
          <PokeModal />
          <PokePullup/>
       </BrowserRouter>
    </div>
  );
}

export default App;
