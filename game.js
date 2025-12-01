class MiniMilitiaGame {
    constructor() {
        this.canvas = document.getElementById('gameCanvas');
        this.ctx = this.canvas.getContext('2d');
        this.gameState = 'menu';
        this.score = 0;
        this.level = 1;
        this.entities = [];
        this.projectiles = [];
        this.powerUps = [];
        this.keys = {};
        this.mouse = { x: 0, y: 0, pressed: false };
        this.touch = { x: 0, y: 0, active: false, shoot: false, jump: false };
        
        // Mobile joystick state
        this.joystickLeft = { x: 0, y: 0, active: false };
        this.joystickRight = { x: 0, y: 0, active: false };
        
        this.lastTime = 0;
        this.deltaTime = 0;
        
        this.setupCanvas();
        this.setupEventListeners();
        this.loadHighScore();
        this.showScreen('menuScreen');
        
        // Game audio context
        this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
        
        this.gameLoop();
    }

    setupCanvas() {
        this.canvas.width = Math.min(1200, window.innerWidth - 40);
        this.canvas.height = Math.min(700, window.innerHeight - 40);
        
        // Add resize handler
        window.addEventListener('resize', () => {
            this.canvas.width = Math.min(1200, window.innerWidth - 40);
            this.canvas.height = Math.min(700, window.innerHeight - 40);
        });
    }

    setupEventListeners() {
        // Keyboard events
        document.addEventListener('keydown', (e) => {
            this.keys[e.code] = true;
            if (e.code === 'Escape') this.togglePause();
        });
        
        document.addEventListener('keyup', (e) => {
            this.keys[e.code] = false;
        });

        // Mouse events
        this.canvas.addEventListener('mousemove', (e) => {
            const rect = this.canvas.getBoundingClientRect();
            this.mouse.x = (e.clientX - rect.left) * (this.canvas.width / rect.width);
            this.mouse.y = (e.clientY - rect.top) * (this.canvas.height / rect.height);
        });

        this.canvas.addEventListener('mousedown', (e) => {
            this.mouse.pressed = true;
            if (this.gameState === 'playing') {
                this.shoot();
            }
        });

        this.canvas.addEventListener('mouseup', () => {
            this.mouse.pressed = false;
        });

        // Touch events
        this.canvas.addEventListener('touchstart', (e) => {
            e.preventDefault();
            const rect = this.canvas.getBoundingClientRect();
            const touch = e.touches[0];
            this.touch.x = (touch.clientX - rect.left) * (this.canvas.width / rect.width);
            this.touch.y = (touch.clientY - rect.top) * (this.canvas.height / rect.height);
            this.touch.active = true;
        });

        this.canvas.addEventListener('touchmove', (e) => {
            e.preventDefault();
            const rect = this.canvas.getBoundingClientRect();
            const touch = e.touches[0];
            this.touch.x = (touch.clientX - rect.left) * (this.canvas.width / rect.width);
            this.touch.y = (touch.clientY - rect.top) * (this.canvas.height / rect.height);
        });

        this.canvas.addEventListener('touchend', () => {
            this.touch.active = false;
        });

        // UI button events
        document.getElementById('startButton').addEventListener('click', () => this.startGame());
        document.getElementById('restartButton').addEventListener('click', () => this.restartGame());

        // Mobile controls
        this.setupMobileControls();
    }

    setupMobileControls() {
        const leftJoystick = document.getElementById('leftJoystick');
        const rightJoystick = document.getElementById('rightJoystick');
        const jumpButton = document.getElementById('jumpButton');
        const shootButton = document.getElementById('shootButton');

        // Left joystick for movement
        this.setupJoystick(leftJoystick, 'left');
        
        // Right joystick for aiming
        this.setupJoystick(rightJoystick, 'right');

        // Action buttons
        jumpButton.addEventListener('touchstart', (e) => {
            e.preventDefault();
            this.touch.jump = true;
        });

        jumpButton.addEventListener('touchend', (e) => {
            e.preventDefault();
            this.touch.jump = false;
        });

        shootButton.addEventListener('touchstart', (e) => {
            e.preventDefault();
            this.touch.shoot = true;
            if (this.gameState === 'playing') {
                this.shoot();
            }
        });

        shootButton.addEventListener('touchend', (e) => {
            e.preventDefault();
            this.touch.shoot = false;
        });
    }

    setupJoystick(joystickElement, type) {
        const base = joystickElement.querySelector('.joystick-base');
        const handle = joystickElement.querySelector('.joystick-handle');
        
        let isDragging = false;

        const startDrag = (clientX, clientY) => {
            isDragging = true;
            if (type === 'left') this.joystickLeft.active = true;
            else this.joystickRight.active = true;
        };

        const drag = (clientX, clientY) => {
            if (!isDragging) return;

            const rect = base.getBoundingClientRect();
            const centerX = rect.left + rect.width / 2;
            const centerY = rect.top + rect.height / 2;
            
            let deltaX = clientX - centerX;
            let deltaY = clientY - centerY;
            
            // Limit to joystick radius
            const maxRadius = rect.width / 2;
            const distance = Math.sqrt(deltaX * deltaX + deltaY * deltaY);
            
            if (distance > maxRadius) {
                deltaX = (deltaX / distance) * maxRadius;
                deltaY = (deltaY / distance) * maxRadius;
            }
            
            // Update handle position
            handle.style.transform = `translate(calc(-50% + ${deltaX}px), calc(-50% + ${deltaY}px))`;
            
            // Normalize values
            const normalizedX = deltaX / maxRadius;
            const normalizedY = deltaY / maxRadius;
            
            if (type === 'left') {
                this.joystickLeft.x = normalizedX;
                this.joystickLeft.y = normalizedY;
            } else {
                this.joystickRight.x = normalizedX;
                this.joystickRight.y = normalizedY;
            }
        };

        const endDrag = () => {
            isDragging = false;
            handle.style.transform = 'translate(-50%, -50%)';
            
            if (type === 'left') {
                this.joystickLeft.active = false;
                this.joystickLeft.x = 0;
                this.joystickLeft.y = 0;
            } else {
                this.joystickRight.active = false;
                this.joystickRight.x = 0;
                this.joystickRight.y = 0;
            }
        };

        // Touch events
        joystickElement.addEventListener('touchstart', (e) => {
            e.preventDefault();
            startDrag(e.touches[0].clientX, e.touches[0].clientY);
        });

        joystickElement.addEventListener('touchmove', (e) => {
            e.preventDefault();
            drag(e.touches[0].clientX, e.touches[0].clientY);
        });

        joystickElement.addEventListener('touchend', (e) => {
            e.preventDefault();
            endDrag();
        });
    }

    showScreen(screenId) {
        document.querySelectorAll('.screen').forEach(screen => {
            screen.classList.remove('active');
        });
        document.getElementById(screenId).classList.add('active');
    }

    startGame() {
        this.gameState = 'playing';
        this.score = 0;
        this.level = 1;
        this.entities = [];
        this.projectiles = [];
        this.powerUps = [];
        
        // Create player
        this.player = new Player(this.canvas.width / 2, this.canvas.height / 2);
        this.entities.push(this.player);
        
        // Create enemies
        this.spawnEnemies(3 + this.level);
        
        // Create map platforms
        this.generateMap();
        
        this.showScreen('gameScreen');
        this.updateHUD();
    }

    restartGame() {
        this.startGame();
    }

    spawnEnemies(count) {
        for (let i = 0; i < count; i++) {
            const x = 100 + Math.random() * (this.canvas.width - 200);
            const y = 100 + Math.random() * (this.canvas.height - 200);
            const enemy = new Enemy(x, y);
            this.entities.push(enemy);
        }
    }

    generateMap() {
        // Create some platforms
        const platforms = [
            { x: 0, y: this.canvas.height - 50, width: this.canvas.width, height: 50 },
            { x: 100, y: 400, width: 200, height: 20 },
            { x: 500, y: 300, width: 200, height: 20 },
            { x: 300, y: 200, width: 150, height: 20 },
            { x: 700, y: 400, width: 200, height: 20 }
        ];

        this.platforms = platforms;
    }

    shoot() {
        if (this.player.ammo <= 0) return;
        
        this.player.ammo--;
        
        // Calculate direction from player to mouse
        const angle = Math.atan2(this.mouse.y - this.player.y, this.mouse.x - this.player.x);
        
        const projectile = new Projectile(
            this.player.x,
            this.player.y,
            Math.cos(angle) * 10,
            Math.sin(angle) * 10,
            'player'
        );
        
        this.projectiles.push(projectile);
        this.playSound('shoot');
        this.updateHUD();
    }

    update(deltaTime) {
        if (this.gameState !== 'playing') return;

        // Handle input
        this.handleInput();

        // Update player
        this.player.update(deltaTime, this.platforms, this.canvas.width, this.canvas.height);

        // Update enemies
        this.entities.forEach(entity => {
            if (entity instanceof Enemy) {
                entity.update(deltaTime, this.player, this.platforms, this.canvas.width, this.canvas.height);
                
                // Enemy shooting
                if (Math.random() < 0.01) {
                    const angle = Math.atan2(this.player.y - entity.y, this.player.x - entity.x);
                    const projectile = new Projectile(
                        entity.x,
                        entity.y,
                        Math.cos(angle) * 8,
                        Math.sin(angle) * 8,
                        'enemy'
                    );
                    this.projectiles.push(projectile);
                }
            }
        });

        // Update projectiles
        this.projectiles.forEach((projectile, index) => {
            projectile.update(deltaTime);
            
            // Remove projectiles that are off-screen
            if (projectile.x < 0 || projectile.x > this.canvas.width || 
                projectile.y < 0 || projectile.y > this.canvas.height) {
                this.projectiles.splice(index, 1);
                return;
            }
            
            // Check collisions
            this.entities.forEach(entity => {
                if (projectile.owner === 'player' && entity instanceof Enemy) {
                    if (this.checkCollision(projectile, entity)) {
                        entity.health -= 10;
                        this.projectiles.splice(index, 1);
                        if (entity.health <= 0) {
                            this.score += 100;
                            this.entities.splice(this.entities.indexOf(entity), 1);
                            this.playSound('explosion');
                        }
                    }
                } else if (projectile.owner === 'enemy' && entity instanceof Player) {
                    if (this.checkCollision(projectile, entity)) {
                        entity.health -= 5;
                        this.projectiles.splice(index, 1);
                        this.playSound('hit');
                        if (entity.health <= 0) {
                            this.gameOver();
                        }
                    }
                }
            });
        });

        // Update power-ups
        this.powerUps.forEach((powerUp, index) => {
            powerUp.update(deltaTime);
            if (this.checkCollision(this.player, powerUp)) {
                if (powerUp.type === 'health') {
                    this.player.health = Math.min(100, this.player.health + 30);
                } else if (powerUp.type === 'ammo') {
                    this.player.ammo = Math.min(30, this.player.ammo + 15);
                }
                this.powerUps.splice(index, 1);
                this.playSound('powerup');
            }
        });

        // Spawn power-ups occasionally
        if (Math.random() < 0.002 && this.powerUps.length < 3) {
            const type = Math.random() < 0.5 ? 'health' : 'ammo';
            const powerUp = new PowerUp(
                Math.random() * this.canvas.width,
                Math.random() * this.canvas.height,
                type
            );
            this.powerUps.push(powerUp);
        }

        // Check if level is complete
        const enemiesLeft = this.entities.filter(e => e instanceof Enemy).length;
        if (enemiesLeft === 0) {
            this.level++;
            this.spawnEnemies(3 + this.level);
            this.score += 500 * this.level;
            this.playSound('levelup');
        }

        this.updateHUD();
    }

    handleInput() {
        // Keyboard controls
        if (this.keys['KeyW'] || this.keys['ArrowUp'] || this.touch.jump) {
            this.player.jump();
        }
        
        if (this.keys['KeyA'] || this.keys['ArrowLeft'] || this.joystickLeft.x < -0.3) {
            this.player.moveLeft();
        }
        
        if (this.keys['KeyD'] || this.keys['ArrowRight'] || this.joystickLeft.x > 0.3) {
            this.player.moveRight();
        }
        
        // Mobile joystick aiming
        if (this.joystickRight.active) {
            this.mouse.x = this.player.x + this.joystickRight.x * 100;
            this.mouse.y = this.player.y + this.joystickRight.y * 100;
        }
    }

    checkCollision(obj1, obj2) {
        return obj1.x < obj2.x + obj2.width &&
               obj1.x + obj1.width > obj2.x &&
               obj1.y < obj2.y + obj2.height &&
               obj1.y + obj1.height > obj2.y;
    }

    render() {
        // Clear canvas
        this.ctx.fillStyle = '#87CEEB';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        if (this.gameState !== 'playing') return;

        // Draw platforms
        this.ctx.fillStyle = '#8B4513';
        if (this.platforms) {
            this.platforms.forEach(platform => {
                this.ctx.fillRect(platform.x, platform.y, platform.width, platform.height);
            });
        }

        // Draw entities
        this.entities.forEach(entity => {
            entity.render(this.ctx);
        });

        // Draw projectiles
        this.projectiles.forEach(projectile => {
            projectile.render(this.ctx);
        });

        // Draw power-ups
        this.powerUps.forEach(powerUp => {
            powerUp.render(this.ctx);
        });

        // Draw aiming line
        if (this.player) {
            this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
            this.ctx.lineWidth = 2;
            this.ctx.beginPath();
            this.ctx.moveTo(this.player.x + this.player.width / 2, this.player.y + this.player.height / 2);
            this.ctx.lineTo(this.mouse.x, this.mouse.y);
            this.ctx.stroke();
        }
    }

    updateHUD() {
        if (this.gameState !== 'playing') return;
        
        document.getElementById('healthFill').style.width = this.player.health + '%';
        document.getElementById('ammoCount').textContent = this.player.ammo;
        document.getElementById('scoreDisplay').textContent = this.score;
        
        const enemiesLeft = this.entities.filter(e => e instanceof Enemy).length;
        document.getElementById('enemyCount').textContent = enemiesLeft;
    }

    gameOver() {
        this.gameState = 'gameover';
        document.getElementById('finalScore').textContent = 'Score: ' + this.score;
        this.saveHighScore();
        this.showScreen('gameOverScreen');
        this.playSound('gameover');
    }

    playSound(type) {
        try {
            const oscillator = this.audioContext.createOscillator();
            const gainNode = this.audioContext.createGain();
            
            oscillator.connect(gainNode);
            gainNode.connect(this.audioContext.destination);
            
            let frequency, duration;
            
            switch(type) {
                case 'shoot':
                    frequency = 800;
                    duration = 0.1;
                    break;
                case 'hit':
                    frequency = 300;
                    duration = 0.2;
                    break;
                case 'explosion':
                    frequency = 100;
                    duration = 0.5;
                    break;
                case 'powerup':
                    frequency = 1200;
                    duration = 0.3;
                    break;
                case 'levelup':
                    frequency = 1500;
                    duration = 0.5;
                    break;
                case 'gameover':
                    frequency = 200;
                    duration = 1;
                    break;
                default:
                    frequency = 440;
                    duration = 0.1;
            }
            
            oscillator.frequency.setValueAtTime(frequency, this.audioContext.currentTime);
            gainNode.gain.setValueAtTime(0.1, this.audioContext.currentTime);
            gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + duration);
            
            oscillator.start(this.audioContext.currentTime);
            oscillator.stop(this.audioContext.currentTime + duration);
        } catch (e) {
            console.log('Audio not supported');
        }
    }

    loadHighScore() {
        const highScore = localStorage.getItem('minimilitia_highscore') || 0;
        document.getElementById('highScore').textContent = 'High Score: ' + highScore;
    }

    saveHighScore() {
        const currentHighScore = localStorage.getItem('minimilitia_highscore') || 0;
        if (this.score > currentHighScore) {
            localStorage.setItem('minimilitia_highscore', this.score);
        }
    }

    gameLoop(currentTime = 0) {
        this.deltaTime = (currentTime - this.lastTime) / 1000;
        this.lastTime = currentTime;
        
        this.update(this.deltaTime);
        this.render();
        
        requestAnimationFrame((time) => this.gameLoop(time));
    }

    togglePause() {
        if (this.gameState === 'playing') {
            this.gameState = 'paused';
        } else if (this.gameState === 'paused') {
            this.gameState = 'playing';
        }
    }
}

// Game Entities
class Player {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.width = 30;
        this.height = 50;
        this.velocityX = 0;
        this.velocityY = 0;
        this.health = 100;
        this.ammo = 30;
        this.isGrounded = false;
        this.jetpackFuel = 100;
        this.facing = 1; // 1 for right, -1 for left
    }

    update(deltaTime, platforms, canvasWidth, canvasHeight) {
        // Apply gravity
        this.velocityY += 0.5;
        
        // Apply friction
        this.velocityX *= 0.9;
        
        // Update position
        this.x += this.velocityX;
        this.y += this.velocityY;
        
        // Boundary checking
        this.x = Math.max(0, Math.min(this.x, canvasWidth - this.width));
        this.y = Math.max(0, Math.min(this.y, canvasHeight - this.height));
        
        // Platform collision
        this.isGrounded = false;
        platforms.forEach(platform => {
            if (this.y + this.height >= platform.y && 
                this.y + this.height <= platform.y + 10 &&
                this.x + this.width > platform.x && 
                this.x < platform.x + platform.width &&
                this.velocityY > 0) {
                
                this.y = platform.y - this.height;
                this.velocityY = 0;
                this.isGrounded = true;
                this.jetpackFuel = Math.min(100, this.jetpackFuel + 20 * deltaTime);
            }
        });
        
        // Recharge jetpack fuel when grounded
        if (this.isGrounded) {
            this.jetpackFuel = Math.min(100, this.jetpackFuel + 10 * deltaTime);
        }
    }

    moveLeft() {
        this.velocityX = -5;
        this.facing = -1;
    }

    moveRight() {
        this.velocityX = 5;
        this.facing = 1;
    }

    jump() {
        if (this.isGrounded || this.jetpackFuel > 0) {
            this.velocityY = -8;
            if (!this.isGrounded) {
                this.jetpackFuel -= 15;
            }
        }
    }

    render(ctx) {
        // Body
        ctx.fillStyle = this.facing === 1 ? '#3498db' : '#2980b9';
        ctx.fillRect(this.x, this.y, this.width, this.height);
        
        // Head
        ctx.fillStyle = '#f39c12';
        ctx.fillRect(this.x + 5, this.y - 10, this.width - 10, 10);
        
        // Jetpack
        ctx.fillStyle = '#2c3e50';
        ctx.fillRect(this.x - 5, this.y + 10, 5, 30);
        
        // Health bar
        ctx.fillStyle = '#e74c3c';
        ctx.fillRect(this.x, this.y - 5, (this.width * this.health) / 100, 3);
    }
}

class Enemy {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.width = 30;
        this.height = 50;
        this.velocityX = 0;
        this.velocityY = 0;
        this.health = 50;
        this.isGrounded = false;
        this.lastDirectionChange = 0;
        this.direction = Math.random() < 0.5 ? -1 : 1;
    }

    update(deltaTime, player, platforms, canvasWidth, canvasHeight) {
        // Simple AI: move toward player occasionally
        this.lastDirectionChange += deltaTime;
        
        if (this.lastDirectionChange > 2) {
            this.direction = player.x > this.x ? 1 : -1;
            this.lastDirectionChange = 0;
        }
        
        this.velocityX = this.direction * 2;
        
        // Apply gravity
        this.velocityY += 0.5;
        
        // Update position
        this.x += this.velocityX;
        this.y += this.velocityY;
        
        // Boundary checking
        this.x = Math.max(0, Math.min(this.x, canvasWidth - this.width));
        this.y = Math.max(0, Math.min(this.y, canvasHeight - this.height));
        
        // Platform collision
        this.isGrounded = false;
        platforms.forEach(platform => {
            if (this.y + this.height >= platform.y && 
                this.y + this.height <= platform.y + 10 &&
                this.x + this.width > platform.x && 
                this.x < platform.x + platform.width &&
                this.velocityY > 0) {
                
                this.y = platform.y - this.height;
                this.velocityY = 0;
                this.isGrounded = true;
            }
        });
        
        // Jump occasionally
        if (this.isGrounded && Math.random() < 0.02) {
            this.velocityY = -10;
        }
    }

    render(ctx) {
        // Body
        ctx.fillStyle = '#e74c3c';
        ctx.fillRect(this.x, this.y, this.width, this.height);
        
        // Head
        ctx.fillStyle = '#c0392b';
        ctx.fillRect(this.x + 5, this.y - 10, this.width - 10, 10);
        
        // Health bar
        ctx.fillStyle = '#e74c3c';
        ctx.fillRect(this.x, this.y - 5, (this.width * this.health) / 50, 3);
    }
}

class Projectile {
    constructor(x, y, velocityX, velocityY, owner) {
        this.x = x;
        this.y = y;
        this.width = 8;
        this.height = 8;
        this.velocityX = velocityX;
        this.velocityY = velocityY;
        this.owner = owner;
    }

    update(deltaTime) {
        this.x += this.velocityX;
        this.y += this.velocityY;
        
        // Apply gravity slightly
        this.velocityY += 0.1;
    }

    render(ctx) {
        ctx.fillStyle = this.owner === 'player' ? '#f1c40f' : '#e74c3c';
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.width / 2, 0, Math.PI * 2);
        ctx.fill();
    }
}

class PowerUp {
    constructor(x, y, type) {
        this.x = x;
        this.y = y;
        this.width = 20;
        this.height = 20;
        this.type = type;
        this.animationTime = 0;
    }

    update(deltaTime) {
        this.animationTime += deltaTime;
        // Float up and down
        this.y += Math.sin(this.animationTime * 3) * 0.5;
    }

    render(ctx) {
        ctx.save();
        ctx.translate(this.x, this.y);
        
        if (this.type === 'health') {
            ctx.fillStyle = '#e74c3c';
            ctx.beginPath();
            ctx.moveTo(10, 0);
            ctx.lineTo(18, 8);
            ctx.lineTo(10, 16);
            ctx.lineTo(2, 8);
            ctx.closePath();
            ctx.fill();
        } else {
            ctx.fillStyle = '#3498db';
            ctx.fillRect(5, 5, 10, 10);
        }
        
        ctx.restore();
    }
}

// Initialize game when page loads
window.addEventListener('DOMContentLoaded', () => {
    new MiniMilitiaGame();
});
