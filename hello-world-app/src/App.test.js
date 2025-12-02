import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

describe('Tic Tac Toe Game', () => {
  test('renders game title', () => {
    render(<App />);
    const titleElement = screen.getByText(/Tic Tac Toe/i);
    expect(titleElement).toBeInTheDocument();
  });

  test('renders 9 game cells', () => {
    const { container } = render(<App />);
    const cells = container.querySelectorAll('button[class*="aspect-square"]');
    expect(cells.length).toBe(9);
  });

  test('player X goes first', () => {
    render(<App />);
    const statusElement = screen.getByText(/Player X's Turn/i);
    expect(statusElement).toBeInTheDocument();
  });

  test('clicking a cell places X mark', () => {
    const { container } = render(<App />);
    const cells = container.querySelectorAll('button[class*="aspect-square"]');
    fireEvent.click(cells[0]);
    expect(cells[0].textContent).toBe('X');
  });

  test('players alternate turns', () => {
    const { container } = render(<App />);
    const cells = container.querySelectorAll('button[class*="aspect-square"]');
    
    fireEvent.click(cells[0]); // X
    expect(cells[0].textContent).toBe('X');
    
    fireEvent.click(cells[1]); // O
    expect(cells[1].textContent).toBe('O');
    
    fireEvent.click(cells[2]); // X
    expect(cells[2].textContent).toBe('X');
  });

  test('cannot click on occupied cell', () => {
    const { container } = render(<App />);
    const cells = container.querySelectorAll('button[class*="aspect-square"]');
    
    fireEvent.click(cells[0]); // X
    expect(cells[0].textContent).toBe('X');
    
    fireEvent.click(cells[0]); // Try to click again
    expect(cells[0].textContent).toBe('X'); // Should still be X
  });

  test('detects horizontal win', () => {
    const { container } = render(<App />);
    const cells = container.querySelectorAll('button[class*="aspect-square"]');
    
    // X wins with top row
    fireEvent.click(cells[0]); // X
    fireEvent.click(cells[3]); // O
    fireEvent.click(cells[1]); // X
    fireEvent.click(cells[4]); // O
    fireEvent.click(cells[2]); // X wins
    
    const winMessage = screen.getByText(/Player X Wins/i);
    expect(winMessage).toBeInTheDocument();
  });

  test('detects vertical win', () => {
    const { container } = render(<App />);
    const cells = container.querySelectorAll('button[class*="aspect-square"]');
    
    // X wins with left column
    fireEvent.click(cells[0]); // X
    fireEvent.click(cells[1]); // O
    fireEvent.click(cells[3]); // X
    fireEvent.click(cells[2]); // O
    fireEvent.click(cells[6]); // X wins
    
    const winMessage = screen.getByText(/Player X Wins/i);
    expect(winMessage).toBeInTheDocument();
  });

  test('detects diagonal win', () => {
    const { container } = render(<App />);
    const cells = container.querySelectorAll('button[class*="aspect-square"]');
    
    // X wins with diagonal
    fireEvent.click(cells[0]); // X
    fireEvent.click(cells[1]); // O
    fireEvent.click(cells[4]); // X
    fireEvent.click(cells[2]); // O
    fireEvent.click(cells[8]); // X wins
    
    const winMessage = screen.getByText(/Player X Wins/i);
    expect(winMessage).toBeInTheDocument();
  });

  test('detects draw', () => {
    const { container } = render(<App />);
    const cells = container.querySelectorAll('button[class*="aspect-square"]');
    
    // Create a draw scenario
    fireEvent.click(cells[0]); // X
    fireEvent.click(cells[1]); // O
    fireEvent.click(cells[2]); // X
    fireEvent.click(cells[4]); // O
    fireEvent.click(cells[3]); // X
    fireEvent.click(cells[5]); // O
    fireEvent.click(cells[7]); // X
    fireEvent.click(cells[6]); // O
    fireEvent.click(cells[8]); // X - Draw
    
    const drawMessage = screen.getByText(/It's a Draw/i);
    expect(drawMessage).toBeInTheDocument();
  });

  test('new game button resets the board', () => {
    const { container } = render(<App />);
    const cells = container.querySelectorAll('button[class*="aspect-square"]');
    
    // Make some moves
    fireEvent.click(cells[0]); // X
    fireEvent.click(cells[1]); // O
    
    // Click new game - use getAllByText and get the button element
    const newGameButtons = screen.getAllByText(/New Game/i);
    const newGameButton = newGameButtons.find(el => el.tagName === 'BUTTON');
    fireEvent.click(newGameButton);
    
    // Check all cells are empty
    cells.forEach(cell => {
      expect(cell.textContent).toBe('');
    });
  });

  test('renders scoreboard', () => {
    const { container } = render(<App />);
    const scoreboard = container.querySelector('.grid.grid-cols-3.gap-4.mb-8');
    expect(scoreboard).toBeInTheDocument();
    expect(scoreboard.textContent).toContain('Player X');
    expect(scoreboard.textContent).toContain('Player O');
    expect(scoreboard.textContent).toContain('Draws');
  });

  test('renders game rules', () => {
    render(<App />);
    expect(screen.getByText(/How to Play/i)).toBeInTheDocument();
  });

  test('renders theme toggle button', () => {
    const { container } = render(<App />);
    const themeButton = container.querySelector('button[aria-label="Toggle theme"]');
    expect(themeButton).toBeInTheDocument();
  });
});
