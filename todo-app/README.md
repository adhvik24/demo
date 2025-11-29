# Todo App

A beautiful, modern todo application built with React and Tailwind CSS.

## Features

✨ **Core Functionality**
- Add new tasks with a simple input field
- Mark tasks as complete/incomplete by clicking the checkbox
- Delete individual tasks
- Clear all completed tasks at once
- Task counter showing remaining active items

🎨 **User Interface**
- Clean, modern design with smooth animations
- Beautiful gradient backgrounds
- Responsive layout that works on all devices
- Hover effects and transitions for better UX
- Empty state messages with emojis

🌓 **Dark Mode**
- Toggle between light and dark themes
- Smooth theme transitions
- Preferences saved to localStorage

🔍 **Filtering**
- View all tasks
- Filter to show only active tasks
- Filter to show only completed tasks

💾 **Data Persistence**
- All tasks are automatically saved to localStorage
- Tasks persist across browser sessions
- Dark mode preference is remembered

## Technologies Used

- **React** - UI library
- **Tailwind CSS** - Utility-first CSS framework
- **localStorage** - Client-side data persistence

## Getting Started

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn

### Installation

1. Navigate to the project directory:
```bash
cd todo-app
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser

### Build for Production

```bash
npm run build
```

This creates an optimized production build in the `build` folder.

## Usage

1. **Add a Task**: Type your task in the input field and click "Add" or press Enter
2. **Complete a Task**: Click the checkbox next to a task to mark it as complete
3. **Delete a Task**: Hover over a task and click the trash icon
4. **Filter Tasks**: Use the "All", "Active", or "Completed" buttons to filter your view
5. **Clear Completed**: Click "Clear completed" to remove all finished tasks
6. **Toggle Dark Mode**: Click the moon/sun icon in the top-right corner

## Project Structure

```
todo-app/
├── public/
├── src/
│   ├── App.js          # Main application component
│   ├── index.css       # Global styles with Tailwind directives
│   └── index.js        # Application entry point
├── tailwind.config.js  # Tailwind CSS configuration
├── postcss.config.js   # PostCSS configuration
└── package.json        # Project dependencies
```

## Features in Detail

### Task Management
- Tasks are displayed in reverse chronological order (newest first)
- Each task shows a checkbox, text, and delete button (on hover)
- Completed tasks have strikethrough text and grayed-out appearance

### Filters
- **All**: Shows all tasks regardless of status
- **Active**: Shows only incomplete tasks
- **Completed**: Shows only completed tasks

### Persistence
All data is stored in the browser's localStorage:
- Tasks array with id, text, completed status, and creation timestamp
- Dark mode preference

## Browser Compatibility

Works on all modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Opera (latest)

## License

This project is open source and available under the MIT License.
