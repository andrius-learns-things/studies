import { ReduceStore } from "flux/utils";
import dispatcher from "./Dispatcher.js";

class SharedStore extends ReduceStore {
  getInitialState() {
    let state = {
      timesNavigated: 0
    };
    return state;
  }

  reduce(state, action) {
    let newState = Object.assign({}, state);

    if (this[action.type]) {
      this[action.type](newState, action);
    }

    return newState;
  }

  [ActionTypes.ROUTE_ENTERED](state, action) {
    state.timesNavigated = state.timesNavigated + 1;
  }
}

let sharedStore = new SharedStore(dispatcher);

export default sharedStore;
