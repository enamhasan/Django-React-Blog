import React from 'react';
import { Link } from 'react-router-dom';

const test = () => (
    <div className='container'>
        <div className="jumbotron mt-5">
            <h1 className="display-4">Hey Nice to see you here.</h1>
            <p className="lead">We make all kinds of awesome blog about various topics.</p>
            <hr className="my-4" />
            <p>Click the button below to check out our awesome blog.</p>
            <Link className="btn btn-primary btn-lg" to='/blog' role="button">Check out our Blog</Link>
        </div>
    </div>
);

export default test;