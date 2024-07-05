import React from "react";
import { Navbar, Nav, NavDropdown, Form, FormControl, Button } from 'react-bootstrap';
import PropTypes from 'prop-types'


/**
|--------------------------------------------------
| Alert this harmfully
|--------------------------------------------------
*/
export default function NavBar(props) {
  return (
    <Navbar bg="light" expand="lg" className="fixed-top px-4">
      <Navbar.Brand href="/">{props.title}</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Link href="/">Home</Nav.Link>
          <Nav.Link href="/">Link</Nav.Link>
          <NavDropdown title="Dropdown" id="basic-nav-dropdown">
            <NavDropdown.Item href="/">Action</NavDropdown.Item>
            <NavDropdown.Item href="/">Another action</NavDropdown.Item>
            <NavDropdown.Divider />
            <NavDropdown.Item href="/">Something else here</NavDropdown.Item>
          </NavDropdown>
          <Nav.Link href="/" disabled>
            Disabled
          </Nav.Link>
        </Nav>
        <Form className="ml-auto">
          <FormControl type="search" placeholder="Search" className="mr-sm-2" aria-label="Search" />
          <Button variant="outline-success">Search</Button>
        </Form>
      </Navbar.Collapse>
    </Navbar>
  );
}
NavBar.prototype={
  title:PropTypes.string,
  about:PropTypes.string,
}

NavBar.defaultprospddddddqqqqq