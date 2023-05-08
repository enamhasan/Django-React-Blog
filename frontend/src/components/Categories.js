import React, { useEffect, useState } from 'react';
import { Table } from 'react-bootstrap';
import { getCategories } from '../services/categoryServices';
import "../App.css";

const Categories = () => {
  const [categories, setCategories] = useState([]);
  useEffect(() => {
   let mounted = true;
   getCategories()
     .then(data => {
       if(mounted) {
         setCategories(data)
       }
     })
   return () => mounted = false;
 }, [])

  return(
   <div className="container-fluid side-container">
   <div className="row side-row" >
    <p id="before-table"></p>
        <Table striped bordered hover className="react-bootstrap-table" id="dataTable">
        <thead>
            <tr>
            <th>ID</th>
            <th>Name</th>
            <th>slug</th>
            <th>enabled</th>

            </tr>
        </thead>
        <tbody>
            {categories.map((cat) =>
            <tr key={cat.id}>
                <td>{cat.id}</td>
                <td>{cat.name}</td>
                <td>{cat.slug}</td>
                <td>{cat.enabled}</td>

            </tr>)}
        </tbody>
    </Table>
    </div>
  </div>
  );
};

export default Categories;