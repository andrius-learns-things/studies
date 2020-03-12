import keymirror from "keymirror";

const ActionTypes = keymirror({
  ROUTE_ENTERED: null,
  ADD_ITEM_BTN_CLICKED: null,
  ADD_ITEM_SUCCESS: null,
  ADD_ITEM_ERROR: null,
  ADD_ITEM_TO_THE_QUEUE_BTN_CLICKED: null,
  ADD_ITEM_TO_THE_QUEUE_SUCCESS: null,
  ADD_ITEM_TO_THE_QUEUE_ERROR: null,
  ADD_ITEMS_FROM_QUEUE_BTN_CLICKED: null,
  ADD_ITEMS_FROM_QUEUE_SUCCESS: null,
  ADD_ITEMS_FROM_QUEUE_ERROR: null,
  GET_ITEMS_SUCCESS: null,
  GET_ITEMS_ERROR: null
});

export default ActionTypes;
