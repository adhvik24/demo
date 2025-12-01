import React from 'react';

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-600 via-pink-500 to-orange-400 flex items-center justify-center p-4">
      <div className="text-center">
        <div className="mb-8 animate-bounce">
          <div className="w-24 h-24 mx-auto bg-white rounded-full shadow-2xl flex items-center justify-center">
            <span className="text-5xl">👋</span>
          </div>
        </div>
        
        <h1 className="text-6xl md:text-8xl font-bold text-white mb-6 drop-shadow-2xl animate-fade-in">
          Hello World
        </h1>
        
        <p className="text-xl md:text-2xl text-white/90 mb-8 drop-shadow-lg">
          Welcome to your beautiful React application
        </p>
        
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <button className="px-8 py-3 bg-white text-purple-600 font-semibold rounded-full shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-200">
            Get Started
          </button>
          <button className="px-8 py-3 bg-transparent border-2 border-white text-white font-semibold rounded-full shadow-lg hover:bg-white hover:text-purple-600 transform hover:scale-105 transition-all duration-200">
            Learn More
          </button>
        </div>
      </div>
      
      <style>{`
        @keyframes fade-in {
          from {
            opacity: 0;
            transform: translateY(-20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        
        .animate-fade-in {
          animation: fade-in 1s ease-out;
        }
      `}</style>
    </div>
  );
}

export default App;
