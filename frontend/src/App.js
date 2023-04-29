import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import layout from './hocs/layout';
import header from './components/header';
import categories from './components/categories';


const App = () => (
    <Router>
        <layout>
            <Routes>
                <Route exact path='/' component={categories} />
                <Route exact path='/api/categories' component={categories} />

            </Routes>
        </layout>
    </Router>
);

export default App;