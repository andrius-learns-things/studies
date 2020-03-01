import React from 'react';
import { Router, Route, hashHistory } from 'react-router';
import routeOnEnterHook from './helpers/RouteOnEnterHook.js';
import MainPage from './components/MainPage.jsx';


class Routes extends React.Component {

    render() {
        return (
            <Router history={hashHistory}>
                <Route path="/" onEnter={routeOnEnterHook} component={MainPage}>
                </Route>
            </Router>
        );
    }
}

export default Routes;
