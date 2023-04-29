import axios from 'axios';

export function getCategories() {
  return axios.get('http://127.0.0.1:8000/api/categories')
    .then(response => response.data)
}