import React from 'react';
import { Link } from 'react-router-dom';
import ProfilePic from '../static/profile.jpeg';

const home = () => (
    <div className="container">
    <div className="row site-content">
        <div className="col-md-9 col-lg-9 main-content">
            <div className="content">
                <h1 className="display-4">Hey Nice to see you here.</h1>
                <p className="lead">We make all kinds of awesome blog about various topics.</p>
                <hr className="my-4" />
                <p>Click the button below to check out our awesome blog.</p>
                <Link className="btn btn-primary btn-lg" to='/blog' role="button">Check out our Blog</Link>
            </div>
        </div>

       <div className="widget-area sidebar is-right-sidebar col-md-3 col-lg-3" id="right-sidebar">
	        <div className="inside-right-sidebar">
	            <div class="sidebar-widget widget-about mb-50 pt-30 pr-30 pb-30 pl-30 bg-white border-radius-5 has-border  wow fadeInUp  animated">
                                <img className="about-author-img mb-25" src={ProfilePic} alt="enamhasan profile pic"/>
                                <h5 className="mb-20">Hello, I'm Enam</h5>
                                <p className="font-medium text-muted">Hi, I’m Enam, a Florida native, who left my career in corporate wealth management six years ago to embark on a summer of soul searching that would change the course of my life forever.</p>
                                <strong>Follow me: </strong>
                                <ul className="header-social-network d-inline-block list-inline color-white mb-20">
                                    <li className="list-inline-item"><a className="fb" href="#" target="_blank" title="Facebook"><i className="elegant-icon social_facebook"></i></a></li>
                                    <li className="list-inline-item"><a className="tw" href="#" target="_blank" title="Tweet now"><i className="elegant-icon social_twitter"></i></a></li>
                                    <li className="list-inline-item"><a className="pt" href="#" target="_blank" title="Pin it"><i className="elegant-icon social_pinterest"></i></a></li>
                                </ul>
                            </div>
		    </div>
		</div>
    </div>
    </div>
);

export default home;