# Mini Militia - 2D Shooter Game

A fully functional 2D side-scrolling shooter game inspired by Mini Militia, built with HTML5 Canvas and vanilla JavaScript.

## 🎮 Features

- **Platform-based Movement**: Jump and navigate across multiple platforms
- **Jetpack System**: Fly using jetpack fuel that recharges when grounded
- **Combat System**: Aim and shoot at enemies with mouse/touch controls
- **Enemy AI**: Intelligent enemies that track and shoot at the player
- **Power-ups**: Collect health and ammo power-ups during gameplay
- **Level Progression**: Increasing difficulty with more enemies each level
- **Score System**: Earn points by defeating enemies and completing levels
- **High Score Persistence**: Your best score is saved in browser localStorage
- **Responsive Design**: Works on desktop and mobile devices
- **Mobile Controls**: Touch-based joysticks and action buttons for mobile play
- **Sound Effects**: Procedurally generated audio for game events

## 🎯 Game Mechanics

### Player Controls

**Desktop:**
- **WASD** or **Arrow Keys**: Move left/right and jump
- **Mouse**: Aim your weapon
- **Left Click**: Shoot

**Mobile:**
- **Left Joystick**: Move character
- **Right Joystick**: Aim weapon
- **Jump Button**: Jump/activate jetpack
- **Shoot Button**: Fire weapon

### Gameplay

- Start with 100 health and 30 ammo
- Defeat all enemies to progress to the next level
- Each level spawns more enemies (3 + level number)
- Collect power-ups to restore health and ammo
- Avoid enemy projectiles to survive
- Earn 100 points per enemy defeated
- Earn 500 × level number bonus points per level completed

## 🚀 How to Run

### Option 1: Simple HTTP Server (Python)
```bash
python3 -m http.server 8000
```
Then open `http://localhost:8000` in your browser.

### Option 2: Node.js HTTP Server
```bash
npx http-server -p 8000
```
Then open `http://localhost:8000` in your browser.

### Option 3: Direct File Access
Simply open `index.html` in a modern web browser (Chrome, Firefox, Safari, Edge).

## 📁 Project Structure

```
mini-militia-game/
├── index.html          # Main HTML file with game structure
├── styles.css          # Styling for UI, HUD, and mobile controls
├── game.js            # Complete game logic and entity classes
└── README.md          # This file
```

## 🎨 Game Classes

### MiniMilitiaGame
Main game controller that manages:
- Game state (menu, playing, paused, gameover)
- Canvas rendering
- Input handling (keyboard, mouse, touch)
- Game loop and updates
- Screen transitions

### Player
The player character with:
- Movement and jumping mechanics
- Jetpack fuel system
- Health and ammo management
- Collision detection with platforms

### Enemy
AI-controlled opponents that:
- Track and move toward the player
- Shoot projectiles at the player
- Navigate platforms
- Have their own health system

### Projectile
Bullets fired by player and enemies with:
- Physics-based movement
- Gravity effects
- Collision detection

### PowerUp
Collectible items that:
- Restore health or ammo
- Float with animation
- Spawn randomly during gameplay

## 🎵 Audio System

The game uses the Web Audio API to generate procedural sound effects for:
- Shooting
- Enemy hits
- Explosions
- Power-up collection
- Level completion
- Game over

## 🐛 Bug Fixes Applied

- Fixed levelup sound duration assignment (changed `!==` to `=` in the original code)
- Ensured proper canvas sizing for responsive layouts
- Optimized collision detection for better performance

## 🌟 Future Enhancements

Potential features to add:
- Multiplayer support
- Different weapon types
- More enemy varieties
- Boss battles
- Map editor
- Particle effects
- Better graphics and animations
- Sound on/off toggle
- Pause menu

## 📱 Browser Compatibility

Works on all modern browsers that support:
- HTML5 Canvas
- ES6 JavaScript
- Web Audio API
- Touch Events (for mobile)

Tested on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 📄 License

This is a demonstration project created for educational purposes.

## 🎮 Enjoy the Game!

Have fun playing Mini Militia! Try to beat your high score and survive as many levels as possible!
