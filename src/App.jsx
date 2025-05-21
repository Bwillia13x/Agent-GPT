import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar/Navbar';
import Button from './components/Button/Button';
import Card from './components/Card/Card';

function App() {
  const [count, setCount] = useState(0);
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    fetch('https://jsonplaceholder.typicode.com/users/1')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setUserData(data);
        setError(null);
      })
      .catch(error => {
        console.error('Fetch error:', error);
        setError(error.message);
        setUserData(null);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []); // Empty dependency array means this effect runs once on mount

  return (
    <div className="min-h-screen bg-background text-text">
      <Navbar />
      <main className="container mx-auto p-4 sm:p-6 lg:p-8">
        <h1 className="text-3xl font-bold text-primary mb-8 text-center">Welcome to NovaFlow (React Edition)</h1>

        <div className="grid md:grid-cols-2 gap-8">
          {/* Counter Card */}
          <Card title="Interactive Counter">
            <div className="text-center">
              <p className="text-lg text-text-light mb-4">You clicked {count} times</p>
              <Button onClick={() => setCount(count + 1)}>
                Click me
              </Button>
            </div>
          </Card>

          {/* User Data Card */}
          <Card title="Fetched User Data">
            {loading && <p className="text-text-light">Loading user data...</p>}
            {error && <p className="text-red-500">Error fetching data: {error}</p>}
            {userData && (
              <div className="space-y-2">
                <p><span className="font-semibold text-text-light">Name:</span> {userData.name}</p>
                <p><span className="font-semibold text-text-light">Email:</span> {userData.email}</p>
                <p><span className="font-semibold text-text-light">Phone:</span> {userData.phone}</p>
                <p><span className="font-semibold text-text-light">Website:</span> {userData.website}</p>
              </div>
            )}
          </Card>
        </div>

        <div className="mt-12 text-center">
          <Card title="More Components">
            <p className="text-text-light mb-4">This is another card demonstrating component reuse.</p>
            <Button onClick={() => alert('Button inside a card clicked!')}>Another Action</Button>
          </Card>
        </div>

      </main>

      <footer className="bg-surface mt-12 py-6 text-center border-t border-neutral">
        <p className="text-sm text-text-light">&copy; {new Date().getFullYear()} NovaFlow React. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;
