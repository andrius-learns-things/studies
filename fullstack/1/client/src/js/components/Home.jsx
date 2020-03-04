import React from "react";
import StoreComponent from "./base/StoreComponent.jsx";
import { Button } from "react-bootstrap";

class Home extends StoreComponent {
  render() {
    return (
      <p>
        Home. Navigated{" "}
        {this.state.timesNavigated ? this.state.timesNavigated : "?"} number of
        times.
        <Button bsStyle="primary" bsSize="large">
          Great
        </Button>
      </p>
    );
  }
}

export default Home;
