import React from 'react';
import navbar from '../components/NavBar';
import Header from '../components/Header';

const layout = (props) => (
    <div>
        <Header />
        {props.children}
    </div>
);

export default layout;