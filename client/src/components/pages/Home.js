import React, { useState } from 'react';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';
import axios from 'axios';
import base64Img from 'base64-img';
import { Link } from 'react-router-dom';

const fs = require('fs');

const getImgFrom64 = base => {
  //let base64String = `data:image/png;base64,${base}`;
  //var buf = new Buffer(base, 'base64');
  //let base64Image = base64String.split(';base64,').pop();

  //fs.writeFile('newImg1.png', base64Image, function(err) {
  //  console.log('File created');
  //});
  //Base64ToImage(`data:image/png;base64,${base}`, function(img) {});

  console.log('ok');
};
/*
function Base64ToImage(base64img, callback) {
  var img = new Image();
  img.onload = function() {
    callback(img);
  };
  img.src = base64img;
}*/
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
    files[count++] = e.target.files[0];
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

  const fileSubmit = async () => {
    // console.log(files[0], files[1], files[2]);
    // let image1 = toBase64(files[0]);
    // let image2 = toBase64(files[1]);
    // let image3 = toBase64(files[2]);

    // console.log(image1);

    // console.log(files);
    // const fd = new FormData();
    // fd.append('image', files[0], files[0].name);
    // fd.append('image', files[1], files[1].name);
    // fd.append('image', files[2], files[2].name);
    // console.log(fd);
    var image1, image2, image3;

    const config = {
      headers: {
        'Content-Type': 'application/json'
      }
    };

    var reader = new FileReader();
    reader.readAsDataURL(files[0]);
    reader.onloadend = function() {
      image1 = reader.result.replace(/^data:.+;base64,/, '');
      var reader1 = new FileReader();
      reader1.readAsDataURL(files[1]);
      reader1.onloadend = function() {
        image2 = reader1.result.replace(/^data:.+;base64,/, '');
        var reader2 = new FileReader();
        reader2.readAsDataURL(files[0]);
        reader2.onloadend = async () => {
          image3 = reader.result.replace(/^data:.+;base64,/, '');
          const form = {
            img1: image1,
            img2: image2,
            img3: image3,
            brand: brand,
            size: size,
            style: style
          };
          try {
            // This is the posting

            // const res = await axios.post(
            //   'http://10.254.162.232:8000/fit',
            //   form,
            //   config
            // );
            // console.log(res);
            // getImgFrom64(res.image);

            getImgFrom64(image1);

            // overall, fit_description, image
          } catch (error) {
            console.log(error);
          }
        };
      };
    };
  };

  return (
    <div className='container'>
      <ul>
        <li>
          {/** Might need to change this to icon */}
          <input type='file' onChange={fileClicked} />
        </li>
        <li>
          <input type='file' onChange={fileClicked} />
        </li>
        <li>
          <input type='file' onChange={fileClicked} />
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
          <Link to='/display' onClick={fileSubmit}>
            <input
              type='submit'
              value='Submit'
              className='btn btn-primary btn-indent'
              style={{ textAlign: '25.5rem' }}
            />
          </Link>
        </li>
      </ul>
    </div>
  );
};

export default Home;
