import React from 'react';
import newImg from './newImg.png';

const Display = () => {
  if (newImg) {
    return (
      <div>
        <h1>How you will look:</h1>
        <img src={newImg} />
      </div>
    );
  }
};

export default Display;
