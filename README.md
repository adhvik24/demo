# Mini Militia - 2D Shooter Game

A fully functional 2D side-scrolling shooter game inspired by Mini Militia, built with HTML5 Canvas and vanilla JavaScript.

## Features

### Core Gameplay
- **Player Character**: Blue soldier with jetpack capabilities
- **Enemy AI**: Red enemy soldiers that track and shoot at the player
- **Platform-based Movement**: Jump and fly using jetpack fuel
- **Shooting Mechanics**: Aim with mouse, shoot projectiles with gravity physics
- **Health & Ammo System**: Manage resources to survive
- **Power-ups**: Health and ammo pickups spawn randomly
- **Level Progression**: Increasing difficulty with more enemies per level
- **Score System**: Earn points for defeating enemies and completing levels
- **High Score Persistence**: Saves your best score using localStorage

### Controls

#### Desktop
- **WASD** or **Arrow Keys**: Move left/right and jump
- **Mouse**: Aim at enemies
- **Left Click**: Shoot
- **ESC**: Pause game

#### Mobile
- **Left Joystick**: Movement control
- **Right Joystick**: Aiming control
- **JUMP Button**: Jump/use jetpack
- **SHOOT Button**: Fire weapon

### Game Mechanics

1. **Physics System**
   - Gravity affects player, enemies, and projectiles
   - Jetpack fuel system for flying
   - Platform collision detection
   - Friction for realistic movement

2. **Combat System**
   - Player starts with 100 health and 30 ammo
   - Enemies have 50 health each
   - Projectiles deal damage on hit
   - Enemy AI shoots at player automatically

3. **Level System**
   - Start with 4 enemies (3 + level)
   - Each level adds more enemies
   - Bonus points for completing levels
   - Enemies respawn when all are defeated

4. **Audio**
   - Procedural sound effects using Web Audio API
   - Sounds for shooting, hits, explosions, power-ups, and level completion

## How to Play

1. **Start the Game**
   - Open `index.html` in a web browser
   - Click "START GAME" button

2. **Objective**
   - Eliminate all enemies to progress to the next level
   - Survive as long as possible
   - Achieve the highest score

3. **Strategy Tips**
   - Use platforms for cover
   - Manage your jetpack fuel wisely
   - Collect power-ups to restore health and ammo
   - Keep moving to avoid enemy fire
   - Aim carefully to conserve ammunition

## Technical Details

### Files Structure
```
├── index.html          # Main HTML file with game structure
├── styles.css          # Responsive styling and UI design
├── game.js            # Complete game logic and classes
└── README.md          # This file
```

### Game Classes

- **MiniMilitiaGame**: Main game controller
- **Player**: Player character with movement and combat
- **Enemy**: AI-controlled enemy soldiers
- **Projectile**: Bullets with physics
- **PowerUp**: Health and ammo pickups

### Browser Compatibility
- Modern browsers with HTML5 Canvas support
- Chrome, Firefox, Safari, Edge (latest versions)
- Mobile browsers with touch support

### Responsive Design
- Adapts to different screen sizes
- Mobile-friendly touch controls
- Optimized for both desktop and mobile gameplay

## Development

The game was built using:
- **HTML5 Canvas** for rendering
- **Vanilla JavaScript** (ES6+) for game logic
- **CSS3** for styling and animations
- **Web Audio API** for sound effects
- **localStorage** for high score persistence

### Key Features Implemented
✅ Complete game loop with delta time
✅ Entity-component system
✅ Collision detection
✅ Physics simulation
✅ AI pathfinding
✅ Responsive UI/UX
✅ Mobile touch controls
✅ Sound system
✅ Score tracking
✅ Multiple game states (menu, playing, game over)

## Credits

Based on the Mini Militia game concept, implemented as a web-based 2D shooter with custom graphics and mechanics.

## License

This is a demonstration project created for educational purposes.

---

**Enjoy the game and try to beat your high score!** 🎮
