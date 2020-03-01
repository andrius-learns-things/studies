import "intl";
import React from 'react';
import ReactDOM from 'react-dom';
import '../styles/styles.scss';
import Routes from './Routes.js';
import { AppContainer } from 'react-hot-loader';

window.addEventListener('error', function (e) {
    // HERE we handle errors
});

const render = () => {
    ReactDOM.render(
        <AppContainer>
            <Routes />
        </AppContainer>,
        document.getElementById('container')
    );
};

render(Routes);

