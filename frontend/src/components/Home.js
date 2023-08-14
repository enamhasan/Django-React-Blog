import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import ProfilePic from '../static/profile.jpeg';


const Home = () => {

const [recentPosts, setRecentPosts] = useState([]);
  const [postList, setPostList] = useState([]);

  useEffect(() => {
    const fetchRecentPosts = async () => {
      try {
        const response = await axios.get(`${process.env.REACT_APP_API_URL}/api/recent/`);
        setRecentPosts(response.data);
      } catch (error) {
        console.error('Error fetching recent posts:', error);
      }
    };

    const fetchPostList = async () => {
      try {
        const response = await axios.get('/api/posts');
        setPostList(response.data);
      } catch (error) {
        console.error('Error fetching post list:', error);
      }
    };

    fetchRecentPosts();
    fetchPostList();
  }, []);

  return (
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
                                <img className="about-author-img img-fluid rounded-circle mb-3" src={ProfilePic} alt="enamhasan profile picture"/>
                                <h5 className="mb-20">Hello, I'm Enam</h5>
                                <p className="font-medium text-muted">Hi, I’m Enam, I am a Full Stack Python Developer with more than 10 years of professional experience in Software and web application development, e-commerce solutions, teamwork, and team management. Higher education IT background. Ability to understand project requirements easily, and define solutions from abstract concepts. Quick learner, adapt to new ideas quickly.</p>
                                <strong>Follow me: </strong>
                                <ul className="header-social-network d-inline-block list-inline color-white mb-20">
                                    <li className="list-inline-item"><a className="fb" href="#" target="_blank" title="Facebook"><i className="elegant-icon social_facebook"></i></a></li>
                                    <li className="list-inline-item"><a className="tw" href="#" target="_blank" title="Tweet now"><i className="elegant-icon social_twitter"></i></a></li>
                                    <li className="list-inline-item"><a className="pt" href="#" target="_blank" title="Pin it"><i className="elegant-icon social_pinterest"></i></a></li>
                                </ul>
                            </div>
		    </div>
		     <div className="recent-posts">
        <h2>Recent Posts</h2>
        <ul>
          {recentPosts.map(post => (
            <li key={post.id}>
              <h3>{post.title}</h3>
              <p>{post.content}</p>
              <p>{post.created_at}</p>
            </li>
          ))}
        </ul>
      </div>
		</div>
    </div>
    </div>

);
};

export default Home;