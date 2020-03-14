import ActionTypes from "../ActionTypes.js";
import dispatcher from "../../Dispatcher.js";

let getBtnClickedHandler = function(btn) {
  return function() {
    dispatcher.dispatch({
      type: ActionTypes.BTN_CLICKED,
      btn: btn
    });
  };
};

export default getBtnClickedHandler;
