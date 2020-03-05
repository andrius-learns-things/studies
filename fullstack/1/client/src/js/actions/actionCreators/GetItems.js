import ActionTypes from "../ActionTypes.js";
import { getFromBackend } from "./helpers/CallBackend.js";

let getItems = function() {
  getFromBackend(
    "/items",
    ActionTypes.GET_ITEMS_SUCCESS,
    ActionTypes.GET_ITEMS_ERROR
  );
};

export default getItems;
