import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [isDark, setIsDark] = useState(false);
  const [board, setBoard] = useState(Array(9).fill(null));
  const [isXNext, setIsXNext] = useState(true);
  const [winner, setWinner] = useState(null);
  const [winningLine, setWinningLine] = useState([]);
  const [scores, setScores] = useState({ X: 0, O: 0, draws: 0 });
  const [gameOver, setGameOver] = useState(false);

  // Load scores from localStorage on mount
  useEffect(() => {
    const savedScores = localStorage.getItem('tictactoe-scores');
    if (savedScores) {
      setScores(JSON.parse(savedScores));
    }
  }, []);

  // Save scores to localStorage whenever they change
  useEffect(() => {
    localStorage.setItem('tictactoe-scores', JSON.stringify(scores));
  }, [scores]);

  // Check for winner whenever board changes
  useEffect(() => {
    const result = calculateWinner(board);
    if (result) {
      setWinner(result.winner);
      setWinningLine(result.line);
      setGameOver(true);
      
      // Update scores
      if (result.winner === 'Draw') {
        setScores(prev => ({ ...prev, draws: prev.draws + 1 }));
      } else {
        setScores(prev => ({ ...prev, [result.winner]: prev[result.winner] + 1 }));
      }
    }
  }, [board]);

  const calculateWinner = (squares) => {
    const lines = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8], // rows
      [0, 3, 6], [1, 4, 7], [2, 5, 8], // columns
      [0, 4, 8], [2, 4, 6]             // diagonals
    ];

    for (let i = 0; i < lines.length; i++) {
      const [a, b, c] = lines[i];
      if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
        return { winner: squares[a], line: lines[i] };
      }
    }

    // Check for draw
    if (squares.every(square => square !== null)) {
      return { winner: 'Draw', line: [] };
    }

    return null;
  };

  const handleClick = (index) => {
    if (board[index] || gameOver) return;

    const newBoard = [...board];
    newBoard[index] = isXNext ? 'X' : 'O';
    setBoard(newBoard);
    setIsXNext(!isXNext);
  };

  const resetGame = () => {
    setBoard(Array(9).fill(null));
    setIsXNext(true);
    setWinner(null);
    setWinningLine([]);
    setGameOver(false);
  };

  const resetScores = () => {
    setScores({ X: 0, O: 0, draws: 0 });
    localStorage.removeItem('tictactoe-scores');
  };

  const getStatusMessage = () => {
    if (winner === 'Draw') {
      return "It's a Draw! 🤝";
    } else if (winner) {
      return `Player ${winner} Wins! 🎉`;
    } else {
      return `Player ${isXNext ? 'X' : 'O'}'s Turn`;
    }
  };

  const getCellClass = (index) => {
    let baseClass = "aspect-square rounded-2xl bg-white dark:bg-gray-800 shadow-lg hover:shadow-xl transition-all duration-300 flex items-center justify-center text-6xl font-bold cursor-pointer transform hover:scale-105";
    
    if (board[index]) {
      baseClass += " cursor-not-allowed";
    }
    
    if (winningLine.includes(index)) {
      baseClass += " winning-cell";
    }
    
    if (board[index] === 'X') {
      baseClass += " text-indigo-600 dark:text-indigo-400";
    } else if (board[index] === 'O') {
      baseClass += " text-purple-600 dark:text-purple-400";
    }
    
    return baseClass;
  };

  return (
    <div className={isDark ? 'dark' : ''}>
      <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 dark:from-gray-900 dark:via-purple-900 dark:to-gray-900 transition-colors duration-500">
        <div className="min-h-screen py-8 px-4">
          
          {/* Theme Toggle */}
          <button
            onClick={() => setIsDark(!isDark)}
            className="fixed top-6 right-6 p-3 rounded-full bg-white dark:bg-gray-800 shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-110 z-10"
            aria-label="Toggle theme"
          >
            {isDark ? (
              <span className="text-2xl">☀️</span>
            ) : (
              <span className="text-2xl">🌙</span>
            )}
          </button>

          {/* Main Container */}
          <div className="max-w-2xl mx-auto">
            
            {/* Header */}
            <div className="text-center mb-8 animate-fade-in">
              <h1 className="text-6xl md:text-7xl font-bold bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 bg-clip-text text-transparent mb-4">
                Tic Tac Toe
              </h1>
              <p className="text-gray-600 dark:text-gray-400 text-lg">
                Challenge your friend to a classic game
              </p>
            </div>

            {/* Status Message */}
            <div className={`text-center mb-6 p-4 rounded-2xl ${
              winner 
                ? 'bg-gradient-to-r from-green-500 to-emerald-500 text-white' 
                : 'bg-white dark:bg-gray-800 text-gray-800 dark:text-white'
            } shadow-lg transition-all duration-300`}>
              <div className="text-2xl font-bold">
                {getStatusMessage()}
              </div>
            </div>

            {/* Scoreboard */}
            <div className="grid grid-cols-3 gap-4 mb-8">
              <div className="bg-white dark:bg-gray-800 rounded-xl p-4 shadow-md text-center transform hover:scale-105 transition-all duration-300">
                <div className="text-4xl font-bold text-indigo-600 dark:text-indigo-400">{scores.X}</div>
                <div className="text-sm text-gray-600 dark:text-gray-400 font-medium mt-1">Player X</div>
              </div>
              <div className="bg-white dark:bg-gray-800 rounded-xl p-4 shadow-md text-center transform hover:scale-105 transition-all duration-300">
                <div className="text-4xl font-bold text-gray-600 dark:text-gray-400">{scores.draws}</div>
                <div className="text-sm text-gray-600 dark:text-gray-400 font-medium mt-1">Draws</div>
              </div>
              <div className="bg-white dark:bg-gray-800 rounded-xl p-4 shadow-md text-center transform hover:scale-105 transition-all duration-300">
                <div className="text-4xl font-bold text-purple-600 dark:text-purple-400">{scores.O}</div>
                <div className="text-sm text-gray-600 dark:text-gray-400 font-medium mt-1">Player O</div>
              </div>
            </div>

            {/* Game Board */}
            <div className="grid grid-cols-3 gap-4 mb-8 max-w-md mx-auto">
              {board.map((cell, index) => (
                <button
                  key={index}
                  onClick={() => handleClick(index)}
                  className={getCellClass(index)}
                  disabled={!!cell || gameOver}
                >
                  {cell && <span className="cell-content">{cell}</span>}
                </button>
              ))}
            </div>

            {/* Action Buttons */}
            <div className="flex gap-4 justify-center">
              <button
                onClick={resetGame}
                className="px-8 py-3 bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded-xl hover:from-indigo-700 hover:to-purple-700 transition-all duration-300 font-medium shadow-md hover:shadow-lg transform hover:scale-105"
              >
                New Game
              </button>
              <button
                onClick={resetScores}
                className="px-8 py-3 bg-gradient-to-r from-red-500 to-pink-500 text-white rounded-xl hover:from-red-600 hover:to-pink-600 transition-all duration-300 font-medium shadow-md hover:shadow-lg transform hover:scale-105"
              >
                Reset Scores
              </button>
            </div>

            {/* Game Rules */}
            <div className="mt-12 bg-white dark:bg-gray-800 rounded-2xl p-6 shadow-md">
              <h2 className="text-2xl font-bold text-gray-800 dark:text-white mb-4">How to Play</h2>
              <ul className="space-y-2 text-gray-600 dark:text-gray-400">
                <li className="flex items-start gap-2">
                  <span className="text-indigo-600 dark:text-indigo-400 font-bold">•</span>
                  <span>Players take turns placing their mark (X or O) on the board</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-purple-600 dark:text-purple-400 font-bold">•</span>
                  <span>Get three of your marks in a row (horizontal, vertical, or diagonal) to win</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-pink-600 dark:text-pink-400 font-bold">•</span>
                  <span>If all squares are filled and no one has won, the game is a draw</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-green-600 dark:text-green-400 font-bold">•</span>
                  <span>Click "New Game" to start over or "Reset Scores" to clear the scoreboard</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
