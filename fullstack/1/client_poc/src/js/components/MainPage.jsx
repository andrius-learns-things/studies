import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import ReactDOM from "react-dom";

import routeEntered from "../actions/actionCreators/RouteEntered.js";
import Home from "./Home.jsx";
import About from "./About.jsx";

let routeOnEnterHook = function(nextRouterState) {
  routeEntered(nextRouterState);
};

class RouterComponent extends Component {
  render() {
    return (
      <div>
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
              <Home />
            </Route>
          </Switch>
        </Router>
      </div>
    );
  }
}

const wrapper = document.getElementById("container");
wrapper ? ReactDOM.render(<RouterComponent />, wrapper) : false;

export default RouterComponent;
