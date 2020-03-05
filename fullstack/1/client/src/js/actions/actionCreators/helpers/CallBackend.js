import request from "superagent";

import dispatcher from "../../../Dispatcher.js";

let prepareAbsoluteUrl = function(url) {
  return "/api" + url;
};

let getEndFunction = function(successActionType, errorActionType) {
  return function(err, res) {
    if (!err) {
      // Success
      let action = {
        type: successActionType,
        result: res.body.result,
        endOfAjaxRequest: true
      };
      dispatcher.dispatch(action);
    } else {
      if (err.status) {
        // Server error:
        let action = {
          type: errorActionType,
          errorData: err
        };
        dispatcher.dispatch(action);
      } else {
        // Unfinished request warning
        console.log("Warning: Unfinished request.");
      }
    }
  };
};

export function getFromBackend(url, successActionType, errorActionType) {
  let req = request.get(prepareAbsoluteUrl(url));
  req.end(getEndFunction(successActionType, errorActionType));
}
