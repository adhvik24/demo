import React, { useState } from 'react';
import './App.css';

function App() {
  const [isDark, setIsDark] = useState(false);

  return (
    <div className={isDark ? 'dark' : ''}>
      <div className="min-h-screen bg-gradient-to-br from-blue-50 via-purple-50 to-pink-50 dark:from-gray-900 dark:via-purple-900 dark:to-gray-900 transition-colors duration-500">
        <div className="min-h-screen flex flex-col items-center justify-center p-4">
          
          {/* Theme Toggle */}
          <button
            onClick={() => setIsDark(!isDark)}
            className="absolute top-8 right-8 p-3 rounded-full bg-white dark:bg-gray-800 shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-110"
            aria-label="Toggle theme"
          >
            {isDark ? (
              <span className="text-2xl">☀️</span>
            ) : (
              <span className="text-2xl">🌙</span>
            )}
          </button>

          {/* Main Content */}
          <div className="text-center space-y-8 animate-fade-in">
            
            {/* Animated Circle */}
            <div className="relative mx-auto w-32 h-32 mb-8">
              <div className="absolute inset-0 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 rounded-full animate-spin-slow opacity-75 blur-md"></div>
              <div className="relative bg-white dark:bg-gray-800 rounded-full w-full h-full flex items-center justify-center shadow-2xl">
                <span className="text-6xl">👋</span>
              </div>
            </div>

            {/* Hello World Text */}
            <h1 className="text-7xl md:text-8xl font-bold bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 bg-clip-text text-transparent animate-gradient">
              Hello World
            </h1>

            {/* Subtitle */}
            <p className="text-xl md:text-2xl text-gray-700 dark:text-gray-300 max-w-2xl mx-auto leading-relaxed">
              Welcome to your beautiful React application with Tailwind CSS
            </p>

            {/* Decorative Elements */}
            <div className="flex gap-4 justify-center mt-12">
              <div className="w-3 h-3 bg-blue-500 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
              <div className="w-3 h-3 bg-purple-500 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
              <div className="w-3 h-3 bg-pink-500 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
            </div>

            {/* Info Cards */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-16 max-w-4xl mx-auto">
              <div className="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
                <div className="text-4xl mb-4">⚛️</div>
                <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-2">React</h3>
                <p className="text-gray-600 dark:text-gray-400 text-sm">Modern JavaScript library for building user interfaces</p>
              </div>
              
              <div className="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
                <div className="text-4xl mb-4">🎨</div>
                <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-2">Tailwind CSS</h3>
                <p className="text-gray-600 dark:text-gray-400 text-sm">Utility-first CSS framework for rapid UI development</p>
              </div>
              
              <div className="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
                <div className="text-4xl mb-4">✨</div>
                <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-2">Beautiful</h3>
                <p className="text-gray-600 dark:text-gray-400 text-sm">Clean, modern design with smooth animations</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
