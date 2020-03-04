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

import { Container, Row } from "react-bootstrap";

import "bootstrap/dist/css/bootstrap.css";

function RouterContents() {
  let location = useLocation();
  React.useEffect(() => {
    routeEntered(location.pathname);
  }, [location]);

  return (
    <Switch>
      <Route path="/about">
        <About />
      </Route>
      <Route path="/">
        <Home />
      </Route>
    </Switch>
  );
}

function RouterComponent() {
  return (
    <Container>
      <Router>
        <Row>
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
        </Row>
        <Row>
          <RouterContents />
        </Row>
      </Router>
    </Container>
  );
}

const wrapper = document.getElementById("container");
wrapper ? ReactDOM.render(<RouterComponent />, wrapper) : false;

export default RouterComponent;
