// src/components/Card/Card.jsx
import React from 'react';

const Card = ({ title, children }) => {
  return (
    <div className="bg-surface p-6 rounded-2xl shadow-neutral-soft">
      {title && <h3 className="text-xl font-semibold text-text mb-4">{title}</h3>}
      <div>{children}</div>
    </div>
  );
};
export default Card;
