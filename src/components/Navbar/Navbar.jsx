// src/components/Navbar/Navbar.jsx
import React from 'react';

const Navbar = () => {
  return (
    <nav className="bg-surface shadow-neutral-soft">
      <div className="container mx-auto px-6 py-4 flex justify-between items-center">
        <a href="#" className="text-2xl font-bold text-primary">NovaFlow (React)</a>
        <div className="space-x-4">
          {/* TODO: Add nav links */}
          <a href="#" className="text-text-light hover:text-primary">Features</a>
          <a href="#" className="text-text-light hover:text-primary">Login</a>
        </div>
      </div>
    </nav>
  );
};
export default Navbar;
