import React from 'react';
import navbar from '../components/navbar';

const layout = (props) => (
    <div>
        <navbar />
        {props.children}
    </div>
);

export default layout;