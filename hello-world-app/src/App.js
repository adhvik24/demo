import React, { useState } from 'react';
import './App.css';

function App() {
  const [isDark, setIsDark] = useState(false);

  return (
    <div className={isDark ? 'dark' : ''}>
      <div className="min-h-screen bg-gradient-to-br from-blue-900 via-blue-800 to-blue-950 dark:from-gray-900 dark:via-purple-900 dark:to-gray-900 transition-colors duration-500">
        <div className="min-h-screen flex flex-col items-center justify-center p-4">
          
          {/* Theme Toggle */}
          <button
            onClick={() => setIsDark(!isDark)}
            className="absolute top-8 right-8 p-3 rounded-full bg-blue-800 dark:bg-gray-800 shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-110"
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
              <div className="absolute inset-0 bg-gradient-to-r from-blue-400 via-cyan-400 to-blue-500 rounded-full animate-spin-slow opacity-75 blur-md"></div>
              <div className="relative bg-blue-800 dark:bg-gray-800 rounded-full w-full h-full flex items-center justify-center shadow-2xl">
                <span className="text-6xl">👋</span>
              </div>
            </div>

            {/* Hello World Text */}
            <h1 className="text-7xl md:text-8xl font-bold bg-gradient-to-r from-cyan-400 via-blue-400 to-cyan-300 bg-clip-text text-transparent animate-gradient">
              नमस्ते दुनिया
            </h1>
            <h2 className="text-4xl md:text-5xl font-semibold text-blue-200 dark:text-gray-300 mt-4">
              Hello World
            </h2>

            {/* Subtitle */}
            <p className="text-xl md:text-2xl text-blue-100 dark:text-gray-300 max-w-2xl mx-auto leading-relaxed">
              आपके सुंदर React एप्लिकेशन में आपका स्वागत है
            </p>
            <p className="text-lg md:text-xl text-blue-200 dark:text-gray-400 max-w-2xl mx-auto leading-relaxed mt-2">
              Welcome to your beautiful React application with Tailwind CSS
            </p>

            {/* Decorative Elements */}
            <div className="flex gap-4 justify-center mt-12">
              <div className="w-3 h-3 bg-cyan-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
              <div className="w-3 h-3 bg-blue-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
              <div className="w-3 h-3 bg-cyan-300 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
            </div>

            {/* Info Cards */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-16 max-w-4xl mx-auto">
              <div className="bg-blue-800 dark:bg-gray-800 p-6 rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
                <div className="text-4xl mb-4">⚛️</div>
                <h3 className="text-lg font-semibold text-white dark:text-white mb-2">React</h3>
                <p className="text-blue-200 dark:text-gray-400 text-sm">यूजर इंटरफेस बनाने के लिए आधुनिक JavaScript लाइब्रेरी</p>
              </div>
              
              <div className="bg-blue-800 dark:bg-gray-800 p-6 rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
                <div className="text-4xl mb-4">🎨</div>
                <h3 className="text-lg font-semibold text-white dark:text-white mb-2">Tailwind CSS</h3>
                <p className="text-blue-200 dark:text-gray-400 text-sm">तेज़ UI विकास के लिए उपयोगिता-प्रथम CSS फ्रेमवर्क</p>
              </div>
              
              <div className="bg-blue-800 dark:bg-gray-800 p-6 rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
                <div className="text-4xl mb-4">✨</div>
                <h3 className="text-lg font-semibold text-white dark:text-white mb-2">सुंदर</h3>
                <p className="text-blue-200 dark:text-gray-400 text-sm">स्मूथ एनिमेशन के साथ साफ, आधुनिक डिज़ाइन</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
