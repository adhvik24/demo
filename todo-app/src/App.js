import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [todos, setTodos] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [filter, setFilter] = useState('all');

  useEffect(() => {
    const savedTodos = localStorage.getItem('todos');
    if (savedTodos) {
      setTodos(JSON.parse(savedTodos));
    }
  }, []);

  useEffect(() => {
    localStorage.setItem('todos', JSON.stringify(todos));
  }, [todos]);

  const addTodo = (e) => {
    e.preventDefault();
    if (inputValue.trim()) {
      const newTodo = {
        id: Date.now(),
        text: inputValue,
        completed: false,
        createdAt: new Date().toISOString(),
      };
      setTodos([newTodo, ...todos]);
      setInputValue('');
    }
  };

  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  const filteredTodos = todos.filter(todo => {
    if (filter === 'active') return !todo.completed;
    if (filter === 'completed') return todo.completed;
    return true;
  });

  const activeCount = todos.filter(todo => !todo.completed).length;
  const completedCount = todos.filter(todo => todo.completed).length;

  return (
    <div className="flex h-screen bg-gray-50">
      {/* Sidebar */}
      <div className="w-64 bg-white border-r border-gray-200 flex flex-col">
        <div className="p-6 border-b border-gray-200">
          <h1 className="text-xl font-semibold text-gray-900">Tasks</h1>
        </div>
        
        <div className="flex-1 p-4">
          <div className="space-y-1">
            <button
              onClick={() => setFilter('all')}
              className={`w-full text-left px-4 py-2 rounded-lg text-sm transition-colors ${
                filter === 'all'
                  ? 'bg-gray-100 text-gray-900 font-medium'
                  : 'text-gray-600 hover:bg-gray-50'
              }`}
            >
              All Tasks
              <span className="float-right text-gray-400">{todos.length}</span>
            </button>
            
            <button
              onClick={() => setFilter('active')}
              className={`w-full text-left px-4 py-2 rounded-lg text-sm transition-colors ${
                filter === 'active'
                  ? 'bg-gray-100 text-gray-900 font-medium'
                  : 'text-gray-600 hover:bg-gray-50'
              }`}
            >
              Active
              <span className="float-right text-gray-400">{activeCount}</span>
            </button>
            
            <button
              onClick={() => setFilter('completed')}
              className={`w-full text-left px-4 py-2 rounded-lg text-sm transition-colors ${
                filter === 'completed'
                  ? 'bg-gray-100 text-gray-900 font-medium'
                  : 'text-gray-600 hover:bg-gray-50'
              }`}
            >
              Completed
              <span className="float-right text-gray-400">{completedCount}</span>
            </button>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 flex flex-col">
        <div className="bg-white border-b border-gray-200 px-8 py-6">
          <h2 className="text-2xl font-semibold text-gray-900 mb-6">
            {filter === 'all' && 'All Tasks'}
            {filter === 'active' && 'Active Tasks'}
            {filter === 'completed' && 'Completed Tasks'}
          </h2>
          
          <form onSubmit={addTodo} className="flex gap-3">
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              placeholder="Add a new task..."
              className="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-900 focus:border-transparent text-sm"
            />
            <button
              type="submit"
              className="px-6 py-3 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors text-sm font-medium"
            >
              Add Task
            </button>
          </form>
        </div>

        <div className="flex-1 overflow-y-auto px-8 py-6">
          {filteredTodos.length === 0 ? (
            <div className="text-center py-12">
              <p className="text-gray-400 text-sm">
                {filter === 'completed' && todos.length > 0
                  ? 'No completed tasks yet'
                  : filter === 'active' && todos.length > 0
                  ? 'No active tasks'
                  : 'No tasks yet. Add one to get started!'}
              </p>
            </div>
          ) : (
            <div className="space-y-2">
              {filteredTodos.map(todo => (
                <div
                  key={todo.id}
                  className="group bg-white border border-gray-200 rounded-lg p-4 hover:shadow-sm transition-shadow"
                >
                  <div className="flex items-start gap-3">
                    <button
                      onClick={() => toggleTodo(todo.id)}
                      className={`mt-0.5 w-5 h-5 rounded border-2 flex-shrink-0 transition-colors ${
                        todo.completed
                          ? 'bg-gray-900 border-gray-900'
                          : 'border-gray-300 hover:border-gray-400'
                      }`}
                    >
                      {todo.completed && (
                        <svg
                          className="w-full h-full text-white"
                          fill="none"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                        >
                          <path d="M5 13l4 4L19 7"></path>
                        </svg>
                      )}
                    </button>
                    
                    <div className="flex-1 min-w-0">
                      <p
                        className={`text-sm ${
                          todo.completed
                            ? 'text-gray-400 line-through'
                            : 'text-gray-900'
                        }`}
                      >
                        {todo.text}
                      </p>
                      <p className="text-xs text-gray-400 mt-1">
                        {new Date(todo.createdAt).toLocaleDateString('en-US', {
                          month: 'short',
                          day: 'numeric',
                          year: 'numeric',
                        })}
                      </p>
                    </div>
                    
                    <button
                      onClick={() => deleteTodo(todo.id)}
                      className="opacity-0 group-hover:opacity-100 text-gray-400 hover:text-red-500 transition-all text-sm px-2"
                    >
                      Delete
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
