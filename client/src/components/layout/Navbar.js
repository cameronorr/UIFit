import React, { Fragment, useContext } from 'react';
import PropTypes from 'prop-types';

// Make the add question button, redirect it to the login page if they aren't logged in - if there is no current
const Navbar = ({ title, slogan, icon }) => {
  return (
    <div className='navbar bg-primary'>
      <h1>
        <i className={icon} /> {title}
      </h1>
      <h2>{slogan}</h2>
    </div>
  );
};

Navbar.propTypes = {
  title: PropTypes.string.isRequired,
  icon: PropTypes.string
};

Navbar.defaultProps = {
  title: 'UIFit',
  slogan: 'The Virtual Fitting Room',
  icon: 'fas fa-person-booth'
};

export default Navbar;
