import ActionTypes from "../ActionTypes.js";
import dispatcher from "../../Dispatcher.js";

let getItemsBtnClicked = function() {
  dispatcher.dispatch({
    type: ActionTypes.GET_ITEMS_BTN_CLICKED
  });
};

export default getItemsBtnClicked;
