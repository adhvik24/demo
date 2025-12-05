#!/usr/bin/env python3
"""
Demonstration script for Rubik's Cube Solver enhancements
Showcases all new features including visualization, optimization, and metrics
"""

from rubiks_cube_solver import RubiksCube


def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print('=' * 60)


def demo_basic_operations():
    """Demonstrate basic cube operations"""
    print_section("1. Basic Cube Operations")

    cube = RubiksCube()
    print("Created a new cube. Is it solved?", cube.is_solved())

    cube.execute_moves("R U R' U'")
    print("\nAfter executing 'R U R' U':")
    print("Is solved?", cube.is_solved())


def demo_double_moves():
    """Demonstrate double move notation"""
    print_section("2. Double Move Notation (NEW!)")

    cube1 = RubiksCube()
    cube2 = RubiksCube()

    cube1.execute_moves("U2")
    cube2.execute_moves("U U")

    print("Cube 1 executed: U2")
    print("Cube 2 executed: U U")
    print("States match?", cube1.get_state() == cube2.get_state())

    # Demonstrate mixed notation
    cube3 = RubiksCube()
    cube3.execute_moves("R U2 R' F2 D' L2")
    print("\nMixed notation example: R U2 R' F2 D' L2")
    print("Move history:", cube3.move_history)


def demo_visualization():
    """Demonstrate cube visualization"""
    print_section("3. Cube Visualization (NEW!)")

    cube = RubiksCube()
    print("Solved cube display:")
    print(cube)

    cube.execute_moves("R U R' U'")
    print("\nAfter 'R U R' U':")
    print(cube)


def demo_state_management():
    """Demonstrate state serialization and copying"""
    print_section("4. State Management (NEW!)")

    # Serialization
    cube1 = RubiksCube()
    cube1.execute_moves("R U2 R' U'")
    state = cube1.to_dict()

    print("Saved cube state to dictionary")
    print(f"Is solved: {state['is_solved']}")

    cube2 = RubiksCube()
    cube2.from_dict(state)
    print("Loaded state into new cube")
    print("States match?", cube1.get_state() == cube2.get_state())

    # Deep copy
    print("\nDeep copy demonstration:")
    cube3 = cube1.copy()
    print("Created copy of cube1")

    cube3.execute_moves("U")
    print("Modified copy with U move")
    print("Original and copy are different?", cube1.get_state() != cube3.get_state())


def demo_optimization():
    """Demonstrate move sequence optimization"""
    print_section("5. Move Optimization (NEW!)")

    cube = RubiksCube()

    # Test various optimization scenarios
    test_cases = [
        ("U U U U", "Cancels out (full rotation)"),
        ("U U", "Combines to U2"),
        ("U U U", "Converts to U'"),
        ("R U U' R'", "Cancels U U'"),
        ("F F F2", "Combines to F'"),
    ]

    for moves, description in test_cases:
        optimized = cube.optimize_moves(moves)
        print(f"{moves:15s} -> {optimized:10s} ({description})")


def demo_performance_tracking():
    """Demonstrate performance metrics"""
    print_section("6. Performance Tracking (NEW!)")

    cube = RubiksCube(track_metrics=True)

    print("Executing moves with timing...")
    cube.execute_moves("R U R' U'", track_time=True)
    cube.execute_moves("R U R' U'", track_time=True)
    cube.execute_moves("R U R' U'", track_time=True)

    print(f"\nMetrics: {cube.metrics}")
    print(f"Move history: {cube.move_history}")


def demo_scrambling():
    """Demonstrate enhanced scrambling"""
    print_section("7. Enhanced Scrambling (NEW!)")

    cube = RubiksCube()
    scramble = cube.scramble(15)

    print(f"Generated scramble: {scramble}")
    print(f"Cube is solved? {cube.is_solved()}")
    print(f"Total moves in history: {len(cube.move_history)}")

    # Show first few colors of scrambled cube
    print("\nScrambled cube preview (Up face):")
    for row in cube.faces['U']:
        print('  ' + ' '.join(row))


def demo_advanced_patterns():
    """Demonstrate known cube patterns"""
    print_section("8. Advanced Patterns")

    # Checkerboard pattern
    cube1 = RubiksCube()
    cube1.execute_moves("U2 D2 F2 B2 L2 R2")
    print("Checkerboard pattern: U2 D2 F2 B2 L2 R2")
    print("Is solved?", cube1.is_solved())

    # T-perm (returns to solved when applied twice)
    cube2 = RubiksCube()
    t_perm = "R U R' U' R' F R2 U' R' U' R U R' F'"
    cube2.execute_moves(t_perm)
    cube2.execute_moves(t_perm)
    print(f"\nT-perm applied twice returns to solved: {cube2.is_solved()}")


def main():
    """Run all demonstrations"""
    print("\n" + "=" * 60)
    print("  RUBIK'S CUBE SOLVER - ENHANCED FEATURES DEMO")
    print("=" * 60)

    demo_basic_operations()
    demo_double_moves()
    demo_visualization()
    demo_state_management()
    demo_optimization()
    demo_performance_tracking()
    demo_scrambling()
    demo_advanced_patterns()

    print("\n" + "=" * 60)
    print("  DEMO COMPLETE!")
    print("=" * 60)
    print("\nFor more information, see RUBIKS_CUBE_README.md")
    print("To run tests: python3 test_rubiks_cube.py\n")


if __name__ == '__main__':
    main()
