function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-600 via-pink-500 to-orange-400 flex items-center justify-center p-4">
      <div className="text-center">
        <h1 className="text-6xl md:text-8xl font-bold text-white mb-6 drop-shadow-2xl animate-pulse">
          Hello World
        </h1>
        <p className="text-xl md:text-2xl text-white/90 font-light tracking-wide">
          Welcome to your beautiful React app
        </p>
        <div className="mt-8 flex gap-4 justify-center">
          <div className="w-16 h-16 bg-white/20 backdrop-blur-sm rounded-full animate-bounce"></div>
          <div className="w-16 h-16 bg-white/20 backdrop-blur-sm rounded-full animate-bounce delay-100"></div>
          <div className="w-16 h-16 bg-white/20 backdrop-blur-sm rounded-full animate-bounce delay-200"></div>
        </div>
      </div>
    </div>
  );
}

export default App;
