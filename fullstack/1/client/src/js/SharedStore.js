import { ReduceStore } from "flux/utils";
import dispatcher from "./Dispatcher.js";
import ActionTypes from "./actions/ActionTypes.js";
import getItems from "./actions/actionCreators/GetItems.js";
import addItem from "./actions/actionCreators/AddItem.js";

class SharedStore extends ReduceStore {
  getInitialState() {
    return {
      timesNavigated: 0
    };
  }

  reduce(state, action) {
    let newState = Object.assign({}, state);

    console.log("Action happened");
    console.log(action);

    if (this[action.type]) {
      this[action.type](newState, action);
    }

    return newState;
  }

  [ActionTypes.ROUTE_ENTERED](state) {
    state.timesNavigated = state.timesNavigated + 1;
    getItems();
  }

  [ActionTypes.GET_ITEMS_SUCCESS](state, action) {
    state.items = action.result;
  }

  [ActionTypes.ADD_ITEM_BTN_CLICKED]() {
    addItem({});
  }

  [ActionTypes.ADD_ITEM_SUCCESS](state, action) {
    state.items = action.result;
  }
}

let sharedStore = new SharedStore(dispatcher);

export default sharedStore;