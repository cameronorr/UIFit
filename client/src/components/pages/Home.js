import React, { useState } from 'react';
import Dropdown from 'react-dropdown';
import PropTypes from 'prop-types';
import 'react-dropdown/style.css';
import axios from 'axios';

const toBase64 = file => {
  let document = '';
  let reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = function() {
    document = reader.result;
  };
  reader.onerror = function(error) {
    console.log('Error: ', error);
  };

  return document;
};

/**
 * - Add state for the photo array
 * - Figure out how to send a photo array to backend
 * - Change the dropdown state on change
 * - Send
 */
const Home = () => {
  const brands = ['Gap', 'Abercrombie', 'Old Navy', 'Roots', 'Forever 21'];
  const sizes = ['XS', 'S', 'M', 'L', 'XL'];
  const genders = ['Men', 'Women'];

  const [files, setFile] = useState([]);

  const [brand, changeBrand] = useState('');
  const [size, changeSize] = useState('');
  const [style, changeStyle] = useState('');

  const fileClicked = e => {
    setFile({ ...files, files: e.files[0] });
  };

  const onBChange = e => {
    changeBrand({ brand: e.target.value });
  };

  const onSChange = e => {
    changeSize({ size: e.target.value });
  };

  const onStyChange = e => {
    changeStyle({ style: e.target.value });
  };

  const fileSubmit = () => {
    let image1 = toBase64(files[0]);
    let image2 = toBase64(files[1]);
    let image3 = toBase64(files[2]);

    console.log(image1);
    console.log(image2);
    console.log(image3);

    const form = {
      img1: image1,
      img2: image2,
      img3: image3,
      brand: brand,
      size: size,
      style: style
    };
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
            onChange={onBChange}
            value={brand}
            placeholder='Select a Brand'
          />
        </li>
        <li>
          <Dropdown
            options={sizes}
            onChange={onSChange}
            value={size}
            placeholder='Select a Size'
          />
        </li>
        <li>
          <Dropdown
            options={genders}
            onChange={onStyChange}
            value={style}
            placeholder='Select a Style'
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

export default Home;
