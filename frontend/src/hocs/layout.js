import react from 'react';
import header from '../components/header';
import footer from '../components/footer';

const layout = (props) => {
    return (
        <div>
            <header />
            {props.children}
            <footer />
        </div>
    );
}

export default layout;
