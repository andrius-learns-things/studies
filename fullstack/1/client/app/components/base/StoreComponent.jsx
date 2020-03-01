import React from 'react';
import allStores from '../../stores/AllStores.js';
import $ from 'jquery';


let getAllStoreStateTree = function () {
    let appState = {};

    Object.keys(allStores).forEach((storeKey) => {
        let storeInstance = allStores[storeKey];
        appState[storeKey] = storeInstance.getState();
    });

    return appState;
};

class StoreComponent extends React.Component {
    constructor(props) {
        super(props);

        let appStateTree = getAllStoreStateTree();

        let initialState = this.getCustomInitialState();

        this.state = initialState
            ? Object.assign({}, initialState, appStateTree)
            : appStateTree;
    }

    componentDidMount() {
        // Simple solution - only one listener is added - it listen to the changes to counter store.
        // This way:
        // - Component will rerender on each action and no more than once
        // - All other stores already handled their actions (counter store is the last one)

        this.storeSubscription = allStores['counter'].addListener(() => {
            this.onAnyAction();
        });

    }

    componentDidUpdate() {
        $('[data-toggle="tooltip"]').tooltip({
            trigger: 'hover',
            // animation is disabled due to transition error from bootstrap
            animation: false
        });
    }

    componentWillUnmount() {
        this.storeSubscription.remove();
    }

    onAnyAction() {
        let state = getAllStoreStateTree();
        this.setState(state);
    }

    // Override this method when custom initial state fields are neeeded, in addition to the ones, provided by stores
    getCustomInitialState() {
        return null;
    }

    // This method will allways be overridden
    render() {

        let sharedStoreState = this.state.shared;

        if (sharedStoreState.authInfo && !sharedStoreState.loadingAuthInfo) {
            return this.renderWhenReady();
        }

        return null;
    }
}

export default StoreComponent;
