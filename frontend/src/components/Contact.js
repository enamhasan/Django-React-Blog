import React, { useState } from 'react';
import { Form, Button, Alert } from 'react-bootstrap';
import axios from 'axios';



const Contact = () => {
  const [formData, setFormData] = useState({
    senderName: '',
    senderEmail: '',
    subject: '',
    message: '',
  });

 const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post(`${process.env.REACT_APP_API_URL}/blog/contact/`, formData)
    .then((response) => {
      // Handle the successful response
      console.log(response.data);
      // Reset the form fields
      setFormData({ senderName: '', senderEmail: '', subject: '', message: '' });
      setSuccessMessage('Your message has been sent successfully!');
      setErrorMessage('');
    })
    .catch((error) => {
     setErrorMessage('Oops! Something went wrong. Please try again.');
      setSuccessMessage('');
      console.error(error);
    });
};

  return (
    <div className="container">
    <div className="contact-form-wrapper mt-5 mb-5">
    {successMessage && <Alert variant="success">{successMessage}</Alert>}
      {errorMessage && <Alert variant="danger">{errorMessage}</Alert>}


        <div className="col-sm-12">
                <h2>Welcome!</h2>
                <p className="mb-3"> I'm delighted to hear from you. Please use the form below to get in touch.
                I'll get back to you promptly. Thank you for reaching out!"
                </p>
        </div>


      <Form onSubmit={handleSubmit}>
        <Form.Group controlId="senderName" className="mb-3">
          <div className="col-sm-6">
              <Form.Control
                type="text"
                name="senderName"
                value={formData.senderName}
                onChange={handleChange}
                placeholder="Enter your name"
                required
              />
             </div>
        </Form.Group>

        <Form.Group controlId="senderEmail" className="mb-3">
            <div className="col-sm-6">
              <Form.Control
                type="email"
                name="senderEmail"
                value={formData.senderEmail}
                onChange={handleChange}
                placeholder="Enter your email"
                required
              />
            </div>
        </Form.Group>

        <Form.Group controlId="subject" className="mb-3">
        <div className="col-sm-12">

          <Form.Control
            type="text"
            name="subject"
            value={formData.subject}
            onChange={handleChange}
            placeholder="Enter the subject"
          />
         </div>
        </Form.Group>

        <Form.Group controlId="message" className="mb-3">
            <div className="col-sm-12">
              <Form.Control
                as="textarea"
                name="message"
                value={formData.message}
                onChange={handleChange}
                placeholder="Enter your message"
                rows={6}
                required
              />
            </div>
        </Form.Group>

        <div className="col-sm-12 d-flex justify-content-end">
        <Button variant="primary" type="submit" className="mb-3">
          Submit
        </Button>
        </div>
      </Form>
    </div>
    </div>
  );
};

export default Contact;
