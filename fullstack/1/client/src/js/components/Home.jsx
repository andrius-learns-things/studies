import React from "react";
import StoreComponent from "./base/StoreComponent.jsx";

class Home extends StoreComponent {
  render() {
    return (
      <p>
        Home. Navigated{" "}
        {this.state.timesNavigated ? this.state.timesNavigated : "?"} number of
        times.
      </p>
    );
  }
}

export default Home;
