import React, { useState } from 'react';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';
import axios from 'axios';
import image2base64 from 'image-to-base64';

const toBase64 = async file => {
  try {
    let res = await image2base64(file);
    console.log(res);
    return res;
  } catch (error) {
    console.log(error);
  }
};

/**
 * - Add state for the photo array
 * - Figure out how to send a photo array to backend
 * - Change the dropdown state on change
 * - Send
 */
let files = ['', '', ''];
const Home = () => {
  const brands = ['Gap', 'Abercrombie', 'Old Navy', 'Roots', 'Forever 21'];
  const sizes = ['XS', 'S', 'M', 'L', 'XL'];
  const genders = ['Men', 'Women'];

  let count = 0;

  // const [files, changeFiles] =
  const [brand, changeBrand] = useState('');
  const [size, changeSize] = useState('');
  const [style, changeStyle] = useState('');

  const fileClicked = e => {
    files[count++] = e.target.files[0].name;
  };

  const onBChange = e => {
    changeBrand({ brand: e.value });
  };

  const onSChange = e => {
    changeSize({ size: e.value });
  };

  const onStyChange = e => {
    changeStyle({ style: e.value });
  };

  const fileSubmit = () => {
    console.log(files[0], files[1], files[2]);
    let image1 = toBase64(files[0]);
    let image2 = toBase64(files[1]);
    let image3 = toBase64(files[2]);

    console.log(image1);

    const form = {
      img1: image1,
      img2: image2,
      img3: image3,
      brand: brand,
      size: size,
      style: style
    };
    //axios.post('localhost', form);
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
