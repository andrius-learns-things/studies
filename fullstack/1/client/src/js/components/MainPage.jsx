import React from "react";
import {
  HashRouter as Router,
  Switch,
  Route,
  Link,
  useLocation
} from "react-router-dom";
import ReactDOM from "react-dom";

import routeEntered from "../actions/actionCreators/RouteEntered.js";
import Home from "./Home.jsx";
import About from "./About.jsx";

function RouterComponent() {
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

const wrapper = document.getElementById("container");
wrapper ? ReactDOM.render(<RouterComponent />, wrapper) : false;

export default RouterComponent;
