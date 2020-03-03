import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import ReactDOM from "react-dom";

import routeEntered from "../actions/actionCreators/RouteEntered.js";
import MainPage from "./MainPage.jsx";
import About from "./About.jsx";

let routeOnEnterHook = function(nextRouterState) {
  routeEntered(nextRouterState);
};

class RouterComponent extends Component {
  render() {
    return "WTF";
  }

  render2() {
    return (
      <Router>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
          </ul>
        </nav>

        <Switch>
          <Route path="/about">
            <About />
          </Route>
          <Route path="/">
            <MainPage />
          </Route>
        </Switch>
      </Router>
    );
  }
}

const wrapper = document.getElementById("container");
wrapper ? ReactDOM.render(<MainPage />, wrapper) : false;

export default RouterComponent;
