import { ReduceStore } from "flux/utils";
import dispatcher from "./Dispatcher.js";
import ActionTypes from "./actions/ActionTypes.js";
import {
  getFromBackend,
  postToBackend
} from "./actions/actionCreators/CallBackend.js";

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
    getFromBackend("/items", ActionTypes.GET_ITEMS_SUCCESS);
  }

  [ActionTypes.BTN_CLICKED](state, action) {
    switch (action.btn) {
      case "addItem":
        postToBackend("/items", {}, ActionTypes.ADD_ITEM_SUCCESS);
        break;
      case "addItemToTheQueue":
        postToBackend("/queued-items", {});
        break;
      case "addItemsFromQueue":
        postToBackend(
          "/add-items-from-queue",
          {},
          ActionTypes.ADD_ITEMS_FROM_QUEUE_SUCCESS
        );
        break;
      case "addItemAfterDelay":
        postToBackend("/add-item-after-delay", {});
        break;
    }
  }

  [ActionTypes.GET_ITEMS_SUCCESS](state, action) {
    state.items = action.result;
  }

  [ActionTypes.ADD_ITEM_SUCCESS](state, action) {
    state.items = action.result;
  }

  [ActionTypes.ADD_ITEMS_FROM_QUEUE_SUCCESS](state, action) {
    state.items = action.result;
  }
}

let sharedStore = new SharedStore(dispatcher);

export default sharedStore;
