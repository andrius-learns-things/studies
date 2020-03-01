import React from "react";
import sharedStore from "../../stores/SharedStore.js";

class StoreComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = sharedStore.getState();
  }

  componentDidMount() {
    this.storeSubscription = sharedStore.addListener(() => {
      let state = sharedStore.getState();
      this.setState(state);
    });
  }

  componentWillUnmount() {
    this.storeSubscription.remove();
  }
}

export default StoreComponent;
