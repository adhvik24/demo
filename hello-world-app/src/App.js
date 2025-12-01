import React from 'react';

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-600 via-pink-500 to-orange-400 flex items-center justify-center p-4">
      <div className="text-center">
        <div className="animate-fade-in">
          <h1 className="text-6xl md:text-8xl font-bold text-white mb-6 drop-shadow-2xl animate-bounce-slow">
            Hello World!
          </h1>
          <p className="text-xl md:text-2xl text-white/90 font-light tracking-wide drop-shadow-lg">
            Welcome to your beautiful React application
          </p>
          <div className="mt-8 flex justify-center gap-4">
            <div className="w-16 h-1 bg-white/50 rounded-full animate-pulse"></div>
            <div className="w-16 h-1 bg-white/50 rounded-full animate-pulse delay-75"></div>
            <div className="w-16 h-1 bg-white/50 rounded-full animate-pulse delay-150"></div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
