
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Header from "./components/Header";
import Home from "./components/Home";
import AboutMe from "./components/AboutMe";
import Contact from "./components/Contact";
import Categories from "./components/Categories";
import Blog from "./components/Blog";
import BlogDetail from "./components/BlogDetails";
import BlogByCategory from "./components/BlogByCategory";
import Test from "./components/test";
import NoPage from "./components/NoPage";

function App() {
  return (
    <BrowserRouter>
     <Header/>
      <Routes>
         <Route exact={true} path="/" element={<Home/>} />
         <Route exact="true"  path="/blog/categories" element={<Categories/>} />
         <Route exact={true} path="/blogs" element={<Blog/>} />
         <Route  path='/blog/:slug' element={<BlogDetail />} />
         <Route  path='/blog/category/:category' element={<BlogByCategory/>} />
         <Route exact={true} path='/about' element={<AboutMe/>} />
         <Route exact={true} path='/contact' element={<Contact/>} />
         <Route path="*" element={<NoPage />} />
       </Routes>
    </BrowserRouter>
  );
}

export default App;