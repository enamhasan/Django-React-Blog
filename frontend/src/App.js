
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Header from "./components/Header";
import Home from "./components/Home";
import Categories from "./components/Categories";
import Blog from "./components/Blog";
import BlogDetail from "./components/BlogDetails";
import Test from "./components/test";
import NoPage from "./components/NoPage";

function App() {
  return (
    <BrowserRouter>
     <Header/>
      <Routes>
         <Route exact={true} path="/" element={<Home/>} />
         <Route exact="true"  path="/blog/categories" element={<Categories/>} />
         <Route exact={true} path="/blog" element={<Blog/>} />
         <Route  path='/blog/:slug' element={<BlogDetail />} />
         <Route exact={true} path='/test' element={<Test/>} />
         <Route path="*" element={<NoPage />} />
       </Routes>
    </BrowserRouter>
  );
}

export default App;