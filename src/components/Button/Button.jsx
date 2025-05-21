// src/components/Button/Button.jsx
import React from 'react';

const Button = ({ onClick, children }) => {
  return (
    <button
      onClick={onClick}
      className="bg-primary text-white px-6 py-3 rounded-2xl hover:bg-primary-light shadow-primary-soft transition duration-300 text-lg font-medium"
    >
      {children}
    </button>
  );
};
export default Button;
