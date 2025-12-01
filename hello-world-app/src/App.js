import React, { useState } from 'react';

function App() {
  const [isDark, setIsDark] = useState(false);

  return (
    <div className={isDark ? 'dark' : ''}>
      <div className="min-h-screen bg-gradient-to-br from-blue-50 via-purple-50 to-pink-50 dark:from-gray-900 dark:via-purple-900 dark:to-gray-900 transition-colors duration-500">
        <div className="min-h-screen flex flex-col items-center justify-center p-4">
          <button
            onClick={() => setIsDark(!isDark)}
            className="absolute top-8 right-8 p-3 rounded-full bg-white dark:bg-gray-800 shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-110"
            aria-label="Toggle dark mode"
          >
            {isDark ? (
              <span className="text-2xl">☀️</span>
            ) : (
              <span className="text-2xl">🌙</span>
            )}
          </button>

          <div className="text-center space-y-8 animate-fade-in">
            <div className="space-y-4">
              <h1 className="text-7xl md:text-9xl font-bold bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 dark:from-blue-400 dark:via-purple-400 dark:to-pink-400 bg-clip-text text-transparent animate-gradient">
                Hello World
              </h1>
              <p className="text-xl md:text-2xl text-gray-700 dark:text-gray-300 font-light">
                Welcome to your beautiful React app
              </p>
            </div>

            <div className="flex flex-wrap gap-4 justify-center mt-12">
              <a
                href="https://react.dev"
                target="_blank"
                rel="noopener noreferrer"
                className="px-8 py-4 bg-blue-600 hover:bg-blue-700 text-white rounded-full font-semibold shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-105"
              >
                Learn React
              </a>
              <a
                href="https://tailwindcss.com"
                target="_blank"
                rel="noopener noreferrer"
                className="px-8 py-4 bg-purple-600 hover:bg-purple-700 text-white rounded-full font-semibold shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-105"
              >
                Learn Tailwind
              </a>
            </div>

            <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl">
              <div className="p-6 bg-white dark:bg-gray-800 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-105">
                <div className="text-4xl mb-4">⚡</div>
                <h3 className="text-xl font-semibold text-gray-800 dark:text-white mb-2">Fast</h3>
                <p className="text-gray-600 dark:text-gray-400">Built with modern React for optimal performance</p>
              </div>
              <div className="p-6 bg-white dark:bg-gray-800 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-105">
                <div className="text-4xl mb-4">🎨</div>
                <h3 className="text-xl font-semibold text-gray-800 dark:text-white mb-2">Beautiful</h3>
                <p className="text-gray-600 dark:text-gray-400">Styled with Tailwind CSS for stunning designs</p>
              </div>
              <div className="p-6 bg-white dark:bg-gray-800 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-105">
                <div className="text-4xl mb-4">📱</div>
                <h3 className="text-xl font-semibold text-gray-800 dark:text-white mb-2">Responsive</h3>
                <p className="text-gray-600 dark:text-gray-400">Works perfectly on all devices and screen sizes</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
