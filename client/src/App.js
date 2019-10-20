import React, { Fragment } from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Navbar from './components/layout/Navbar';
import Home from './components/pages/Home';

const App = () => {
  return (
    <div className='App'>
      <Router>
        <Fragment>
          <Navbar />
          <div className='container'>
            <Route exact path='/' component={Home} />
          </div>
        </Fragment>
      </Router>
    </div>
  );
};

export default App;
