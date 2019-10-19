import React, { useState } from 'react';
import Dropdown from 'react-dropdown';
import PropTypes from 'prop-types';
import 'react-dropdown/style.css';

/**
 * - Add state for the photo array
 * - Figure out how to send a photo array to backend
 * - Change the dropdown state on change
 * - Send
 */
const Home = () => {
  const brands = ['Gap', 'Abercrombie', 'Old Navy', 'Roots', 'Forever 21'];
  const sizes = ['XS', 'S', 'M', 'L', 'XL'];

  const [file, setFile] = useState({
    fileArray: []
  });

  const { fileArray } = file;

  const [dropdown, setVal] = useState({
    brand: '',
    size: ''
  });

  const { brand, size } = dropdown;

  const fileClicked = event => {
    setFile({ ...fileArray, [e.target.name]: event.target.files[0] });
  };

  const fileSubmit = () => {
    const form = new FormData();
    form.append('image', state.file, state.file.name);
    axios.post('LINK', form);
  };

  return (
    <div className='container'>
      <ul>
        <li>
          {/** Might need to change this to icon */}
          <div className='far fa-plus-square' onChange={fileClicked}>
            <input type='file' />
          </div>
        </li>
        <li>
          <div className='far fa-plus-square' onChange={fileClicked}>
            <input type='file' />
          </div>
        </li>
        <li>
          <div className='far fa-plus-square' onChange={fileClicked}>
            <input type='file' />
          </div>
        </li>
        <li>
          <Dropdown
            options={brands}
            onChange={_onSelect}
            value={brandsDropdown}
            placeholder='Select a Brand'
          />
        </li>
        <li>
          <Dropdown
            options={sizes}
            onChange={_onSelect}
            value={sizeDropdown}
            placeholder='Select a Size'
          />
        </li>
        <li>
          <input
            type='submit'
            value='Submit'
            className='btn btn-primary btn-indent'
            onClick={fileSubmit}
          />
        </li>
      </ul>
    </div>
  );
};

Home.propTypes = {
  brandsDropdown: PropTypes.string,
  sizeDropdown: PropTypes.string
};

Home.defaultProps = {
  brandsDropdown: brands[0],
  sizeDropdown: sizes[0]
};

export default Home;
