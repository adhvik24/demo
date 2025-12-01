class TodoApp {
    constructor() {
        this.todos = this.loadFromLocalStorage();
        this.currentFilter = 'all';
        this.editingId = null;
        
        this.initElements();
        this.attachEventListeners();
        this.render();
    }

    initElements() {
        this.todoInput = document.getElementById('todoInput');
        this.addBtn = document.getElementById('addBtn');
        this.todoList = document.getElementById('todoList');
        this.emptyState = document.getElementById('emptyState');
        this.filterBtns = document.querySelectorAll('.filter-btn');
        this.clearCompletedBtn = document.getElementById('clearCompleted');
        this.totalCount = document.getElementById('totalCount');
        this.activeCount = document.getElementById('activeCount');
        this.completedCount = document.getElementById('completedCount');
    }

    attachEventListeners() {
        // Add todo
        this.addBtn.addEventListener('click', () => this.addTodo());
        this.todoInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.addTodo();
        });

        // Filter buttons
        this.filterBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.currentFilter = e.target.dataset.filter;
                this.updateFilterButtons();
                this.render();
            });
        });

        // Clear completed
        this.clearCompletedBtn.addEventListener('click', () => this.clearCompleted());
    }

    addTodo() {
        const text = this.todoInput.value.trim();
        
        if (text === '') {
            this.todoInput.focus();
            return;
        }

        const todo = {
            id: Date.now(),
            text: text,
            completed: false,
            createdAt: new Date().toISOString()
        };

        this.todos.push(todo);
        this.todoInput.value = '';
        this.todoInput.focus();
        
        this.saveToLocalStorage();
        this.render();
    }

    deleteTodo(id) {
        this.todos = this.todos.filter(todo => todo.id !== id);
        this.saveToLocalStorage();
        this.render();
    }

    toggleComplete(id) {
        const todo = this.todos.find(todo => todo.id === id);
        if (todo) {
            todo.completed = !todo.completed;
            this.saveToLocalStorage();
            this.render();
        }
    }

    startEdit(id) {
        this.editingId = id;
        this.render();
    }

    saveEdit(id, newText) {
        const text = newText.trim();
        
        if (text === '') {
            this.deleteTodo(id);
            return;
        }

        const todo = this.todos.find(todo => todo.id === id);
        if (todo) {
            todo.text = text;
            this.editingId = null;
            this.saveToLocalStorage();
            this.render();
        }
    }

    cancelEdit() {
        this.editingId = null;
        this.render();
    }

    clearCompleted() {
        this.todos = this.todos.filter(todo => !todo.completed);
        this.saveToLocalStorage();
        this.render();
    }

    getFilteredTodos() {
        switch (this.currentFilter) {
            case 'active':
                return this.todos.filter(todo => !todo.completed);
            case 'completed':
                return this.todos.filter(todo => todo.completed);
            default:
                return this.todos;
        }
    }

    updateFilterButtons() {
        this.filterBtns.forEach(btn => {
            if (btn.dataset.filter === this.currentFilter) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
    }

    updateStats() {
        const total = this.todos.length;
        const active = this.todos.filter(todo => !todo.completed).length;
        const completed = this.todos.filter(todo => todo.completed).length;

        this.totalCount.textContent = `Total: ${total}`;
        this.activeCount.textContent = `Active: ${active}`;
        this.completedCount.textContent = `Completed: ${completed}`;
    }

    createTodoElement(todo) {
        const li = document.createElement('li');
        li.className = `todo-item ${todo.completed ? 'completed' : ''}`;
        li.dataset.id = todo.id;

        const isEditing = this.editingId === todo.id;

        if (isEditing) {
            li.innerHTML = `
                <input 
                    type="text" 
                    class="todo-edit-input" 
                    value="${this.escapeHtml(todo.text)}"
                    autofocus
                >
                <div class="todo-actions">
                    <button class="icon-btn save-btn" title="Save">✓</button>
                    <button class="icon-btn cancel-btn" title="Cancel">✕</button>
                </div>
            `;

            const input = li.querySelector('.todo-edit-input');
            const saveBtn = li.querySelector('.save-btn');
            const cancelBtn = li.querySelector('.cancel-btn');

            // Auto-select text
            setTimeout(() => input.select(), 0);

            // Save on Enter
            input.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    this.saveEdit(todo.id, input.value);
                }
            });

            // Cancel on Escape
            input.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') {
                    this.cancelEdit();
                }
            });

            saveBtn.addEventListener('click', () => {
                this.saveEdit(todo.id, input.value);
            });

            cancelBtn.addEventListener('click', () => {
                this.cancelEdit();
            });
        } else {
            li.innerHTML = `
                <input 
                    type="checkbox" 
                    class="todo-checkbox" 
                    ${todo.completed ? 'checked' : ''}
                >
                <span class="todo-text">${this.escapeHtml(todo.text)}</span>
                <div class="todo-actions">
                    <button class="icon-btn edit-btn" title="Edit">✎</button>
                    <button class="icon-btn delete-btn" title="Delete">🗑</button>
                </div>
            `;

            const checkbox = li.querySelector('.todo-checkbox');
            const editBtn = li.querySelector('.edit-btn');
            const deleteBtn = li.querySelector('.delete-btn');

            checkbox.addEventListener('change', () => {
                this.toggleComplete(todo.id);
            });

            editBtn.addEventListener('click', () => {
                this.startEdit(todo.id);
            });

            deleteBtn.addEventListener('click', () => {
                this.deleteTodo(todo.id);
            });

            // Double-click to edit
            li.querySelector('.todo-text').addEventListener('dblclick', () => {
                this.startEdit(todo.id);
            });
        }

        return li;
    }

    render() {
        const filteredTodos = this.getFilteredTodos();

        // Clear list
        this.todoList.innerHTML = '';

        // Show/hide empty state
        if (filteredTodos.length === 0) {
            this.emptyState.classList.add('show');
            this.todoList.style.display = 'none';
        } else {
            this.emptyState.classList.remove('show');
            this.todoList.style.display = 'block';

            // Render todos
            filteredTodos.forEach(todo => {
                const todoElement = this.createTodoElement(todo);
                this.todoList.appendChild(todoElement);
            });
        }

        // Update stats
        this.updateStats();

        // Update filter buttons
        this.updateFilterButtons();
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    saveToLocalStorage() {
        localStorage.setItem('todos', JSON.stringify(this.todos));
    }

    loadFromLocalStorage() {
        const stored = localStorage.getItem('todos');
        return stored ? JSON.parse(stored) : [];
    }
}

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new TodoApp();
});
