import { ReduceStore } from "flux/utils";
import dispatcher from "../Dispatcher.js";

class SharedStore extends ReduceStore {
  getInitialState() {
    let state = {};
    return state;
  }

  reduce(state, action) {
    let newState = Object.assign({}, state);

    if (this[action.type]) {
      this[action.type](newState, action);
    }

    return newState;
  }
}

let sharedStore = new SharedStore(dispatcher);

export default sharedStore;
