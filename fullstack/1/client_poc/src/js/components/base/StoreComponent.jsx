import { Component } from "react";
import sharedStore from "../../SharedStore.js";

class StoreComponent extends Component {
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
