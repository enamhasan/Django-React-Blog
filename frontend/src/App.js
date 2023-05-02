import Home from "./components/home";
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Header from "./components/header";
import categories from "./components/categories";

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
         <Route exact path="/" element={<Home/>} />
         <Route exact path="/api/categories" element={<categories/>} />
       </Routes>
    </BrowserRouter>
  );
}

export default App;