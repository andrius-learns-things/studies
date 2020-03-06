import keymirror from "keymirror";

const ActionTypes = keymirror({
  ROUTE_ENTERED: null,
  ADD_ITEM_BTN_CLICKED: null,
  ADD_ITEM_SUCCESS: null,
  ADD_ITEM_ERROR: null,
  GET_ITEMS_SUCCESS: null,
  GET_ITEMS_ERROR: null
});

export default ActionTypes;
