import { ReduceStore } from "flux/utils";
import dispatcher from "./Dispatcher.js";
import ActionTypes from "./actions/ActionTypes.js";

class SharedStore extends ReduceStore {
  getInitialState() {
    return {
      timesNavigated: 0
    };
  }

  reduce(state, action) {
    let newState = Object.assign({}, state);

    if (this[action.type]) {
      this[action.type](newState, action);
    }

    return newState;
  }

  [ActionTypes.ROUTE_ENTERED](state) {
    state.timesNavigated = state.timesNavigated + 1;
  }
}

let sharedStore = new SharedStore(dispatcher);

export default sharedStore;
