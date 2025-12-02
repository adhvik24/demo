import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [isDark, setIsDark] = useState(false);
  const [todos, setTodos] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [filter, setFilter] = useState('all');
  const [editingId, setEditingId] = useState(null);
  const [editingText, setEditingText] = useState('');

  // Load todos from localStorage on mount
  useEffect(() => {
    const savedTodos = localStorage.getItem('todos');
    if (savedTodos) {
      setTodos(JSON.parse(savedTodos));
    }
  }, []);

  // Save todos to localStorage whenever they change
  useEffect(() => {
    localStorage.setItem('todos', JSON.stringify(todos));
  }, [todos]);

  const addTodo = (e) => {
    e.preventDefault();
    if (inputValue.trim() === '') return;

    const newTodo = {
      id: Date.now(),
      text: inputValue.trim(),
      completed: false,
      createdAt: new Date().toISOString()
    };

    setTodos([newTodo, ...todos]);
    setInputValue('');
  };

  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  const startEditing = (id, text) => {
    setEditingId(id);
    setEditingText(text);
  };

  const saveEdit = (id) => {
    if (editingText.trim() === '') {
      deleteTodo(id);
    } else {
      setTodos(todos.map(todo =>
        todo.id === id ? { ...todo, text: editingText.trim() } : todo
      ));
    }
    setEditingId(null);
    setEditingText('');
  };

  const cancelEdit = () => {
    setEditingId(null);
    setEditingText('');
  };

  const clearCompleted = () => {
    setTodos(todos.filter(todo => !todo.completed));
  };

  const getFilteredTodos = () => {
    switch (filter) {
      case 'active':
        return todos.filter(todo => !todo.completed);
      case 'completed':
        return todos.filter(todo => todo.completed);
      default:
        return todos;
    }
  };

  const filteredTodos = getFilteredTodos();
  const activeTodosCount = todos.filter(todo => !todo.completed).length;
  const completedTodosCount = todos.filter(todo => todo.completed).length;

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
          <div className="max-w-3xl mx-auto">
            
            {/* Header */}
            <div className="text-center mb-8 animate-fade-in">
              <h1 className="text-6xl md:text-7xl font-bold bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 bg-clip-text text-transparent mb-4">
                Todo App
              </h1>
              <p className="text-gray-600 dark:text-gray-400 text-lg">
                Organize your tasks beautifully
              </p>
            </div>

            {/* Add Todo Form */}
            <form onSubmit={addTodo} className="mb-8">
              <div className="relative">
                <input
                  type="text"
                  value={inputValue}
                  onChange={(e) => setInputValue(e.target.value)}
                  placeholder="What needs to be done?"
                  className="w-full px-6 py-4 text-lg rounded-2xl bg-white dark:bg-gray-800 text-gray-800 dark:text-white placeholder-gray-400 dark:placeholder-gray-500 shadow-lg focus:shadow-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-purple-500 transition-all duration-300"
                />
                <button
                  type="submit"
                  className="absolute right-2 top-1/2 -translate-y-1/2 px-6 py-2 bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded-xl hover:from-indigo-700 hover:to-purple-700 transition-all duration-300 font-medium shadow-md hover:shadow-lg"
                >
                  Add
                </button>
              </div>
            </form>

            {/* Stats */}
            {todos.length > 0 && (
              <div className="grid grid-cols-3 gap-4 mb-6">
                <div className="bg-white dark:bg-gray-800 rounded-xl p-4 shadow-md text-center">
                  <div className="text-2xl font-bold text-indigo-600 dark:text-indigo-400">{todos.length}</div>
                  <div className="text-sm text-gray-600 dark:text-gray-400">Total</div>
                </div>
                <div className="bg-white dark:bg-gray-800 rounded-xl p-4 shadow-md text-center">
                  <div className="text-2xl font-bold text-blue-600 dark:text-blue-400">{activeTodosCount}</div>
                  <div className="text-sm text-gray-600 dark:text-gray-400">Active</div>
                </div>
                <div className="bg-white dark:bg-gray-800 rounded-xl p-4 shadow-md text-center">
                  <div className="text-2xl font-bold text-green-600 dark:text-green-400">{completedTodosCount}</div>
                  <div className="text-sm text-gray-600 dark:text-gray-400">Done</div>
                </div>
              </div>
            )}

            {/* Filter Tabs */}
            {todos.length > 0 && (
              <div className="flex gap-2 mb-6 bg-white dark:bg-gray-800 rounded-xl p-2 shadow-md">
                <button
                  onClick={() => setFilter('all')}
                  className={`flex-1 py-2 px-4 rounded-lg font-medium transition-all duration-300 ${
                    filter === 'all'
                      ? 'bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-md'
                      : 'text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700'
                  }`}
                >
                  All
                </button>
                <button
                  onClick={() => setFilter('active')}
                  className={`flex-1 py-2 px-4 rounded-lg font-medium transition-all duration-300 ${
                    filter === 'active'
                      ? 'bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-md'
                      : 'text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700'
                  }`}
                >
                  Active
                </button>
                <button
                  onClick={() => setFilter('completed')}
                  className={`flex-1 py-2 px-4 rounded-lg font-medium transition-all duration-300 ${
                    filter === 'completed'
                      ? 'bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-md'
                      : 'text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700'
                  }`}
                >
                  Completed
                </button>
              </div>
            )}

            {/* Todo List */}
            <div className="space-y-3">
              {filteredTodos.length === 0 && todos.length === 0 && (
                <div className="text-center py-16 bg-white dark:bg-gray-800 rounded-2xl shadow-md">
                  <div className="text-6xl mb-4">📝</div>
                  <p className="text-gray-500 dark:text-gray-400 text-lg">No todos yet. Add one above!</p>
                </div>
              )}

              {filteredTodos.length === 0 && todos.length > 0 && (
                <div className="text-center py-16 bg-white dark:bg-gray-800 rounded-2xl shadow-md">
                  <div className="text-6xl mb-4">✨</div>
                  <p className="text-gray-500 dark:text-gray-400 text-lg">
                    No {filter} todos
                  </p>
                </div>
              )}

              {filteredTodos.map((todo) => (
                <div
                  key={todo.id}
                  className="group bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-lg transition-all duration-300 overflow-hidden"
                >
                  <div className="flex items-center gap-4 p-4">
                    {/* Checkbox */}
                    <button
                      onClick={() => toggleTodo(todo.id)}
                      className={`flex-shrink-0 w-6 h-6 rounded-full border-2 transition-all duration-300 ${
                        todo.completed
                          ? 'bg-gradient-to-r from-green-500 to-emerald-500 border-green-500'
                          : 'border-gray-300 dark:border-gray-600 hover:border-indigo-500 dark:hover:border-purple-500'
                      }`}
                    >
                      {todo.completed && (
                        <span className="text-white text-sm">✓</span>
                      )}
                    </button>

                    {/* Todo Text */}
                    {editingId === todo.id ? (
                      <input
                        type="text"
                        value={editingText}
                        onChange={(e) => setEditingText(e.target.value)}
                        onKeyDown={(e) => {
                          if (e.key === 'Enter') saveEdit(todo.id);
                          if (e.key === 'Escape') cancelEdit();
                        }}
                        onBlur={() => saveEdit(todo.id)}
                        autoFocus
                        className="flex-1 px-3 py-2 bg-gray-50 dark:bg-gray-700 rounded-lg text-gray-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-purple-500"
                      />
                    ) : (
                      <div
                        onDoubleClick={() => startEditing(todo.id, todo.text)}
                        className={`flex-1 text-lg cursor-pointer ${
                          todo.completed
                            ? 'line-through text-gray-400 dark:text-gray-500'
                            : 'text-gray-800 dark:text-white'
                        }`}
                      >
                        {todo.text}
                      </div>
                    )}

                    {/* Action Buttons */}
                    <div className="flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                      {editingId !== todo.id && (
                        <>
                          <button
                            onClick={() => startEditing(todo.id, todo.text)}
                            className="p-2 text-blue-600 dark:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/30 rounded-lg transition-all duration-300"
                            title="Edit"
                          >
                            ✏️
                          </button>
                          <button
                            onClick={() => deleteTodo(todo.id)}
                            className="p-2 text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-900/30 rounded-lg transition-all duration-300"
                            title="Delete"
                          >
                            🗑️
                          </button>
                        </>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>

            {/* Clear Completed Button */}
            {completedTodosCount > 0 && (
              <div className="mt-6 text-center">
                <button
                  onClick={clearCompleted}
                  className="px-6 py-3 bg-red-500 hover:bg-red-600 text-white rounded-xl font-medium shadow-md hover:shadow-lg transition-all duration-300"
                >
                  Clear Completed ({completedTodosCount})
                </button>
              </div>
            )}

            {/* Footer */}
            {todos.length > 0 && (
              <div className="mt-8 text-center text-sm text-gray-500 dark:text-gray-400">
                Double-click a todo to edit it
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
