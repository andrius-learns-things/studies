import React from "react";
import {
  HashRouter as Router,
  Switch,
  Route,
  useLocation
} from "react-router-dom";
import ReactDOM from "react-dom";
import { Container, Row, Nav } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

import routeEntered from "../actions/actionCreators/RouteEntered.js";
import Home from "./Home.jsx";
import About from "./About.jsx";

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
        <Row className="mt-5">
          <Nav variant="pills" defaultActiveKey="/home" as="ul">
            <Nav.Item as="li">
              <LinkContainer to="/home">
                <Nav.Link>Home</Nav.Link>
              </LinkContainer>
            </Nav.Item>
            <Nav.Item as="li">
              <LinkContainer to="/about">
                <Nav.Link>About</Nav.Link>
              </LinkContainer>
            </Nav.Item>
          </Nav>
        </Row>
        <Row className="mt-5">
          <RouterContents />
        </Row>
      </Router>
    </Container>
  );
}

const wrapper = document.getElementById("container");
wrapper ? ReactDOM.render(<RouterComponent />, wrapper) : false;

export default RouterComponent;
