# PCP-Problem-Game
PCP Problem Domino Sorting Game!  

## What is the Post Correspondence Problem (PCP)?
The PCP is a classic computer science problem that's **undecidable**, meaning there's no algorithm that can determine if ANY given set of dominoes has a solution. But that makes it perfect for a game!

## Overview
This project is an interactive game designed to display randomly generated Post Correspondence Problem (PCP) dominoes using coloured squares, by using the **pygame-ce** library.
Each domino consists of a top and bottom sequence of colours chosen from three possible colours: red, green, and blue. 
The purpose of the game is not to solve PCP (which is undecidable), but to allow users to experiement with randomly-generated dominoes and try to construct a matching sequence on the top and bottom strings. 

## Requirements
- Python 3.10 or later
- pygame-ce

## How to Install and Run
1. Install Python from https://www.python.org/downloads/ (if you don’t already have it)
2. Open a terminal (or command prompt) and run:
   ```bash
   pip install pygame-ce
   ```
3. From the project directory, run:
   ```bash
   python main.py
   ```

## Features
- Random domino generation (no duplicates)
- Visual domino rendering with coloured squares
- Drag-and-Drop manipulation
- Automatic left-to-right sequencing in working area
- Highlighting of valid next dominoes (yellow border)
- Real-time display of concatenated sequences
- Win condition detection and feedback
- Clear and New Game buttons
- Timer system tracking 

## Project Structure

### domino.py
- Defines the colours (RED, GREEN, BLUE)
- Generates random top/bottom sequences (1-3 squares each)
- Ensures no duplicate domino pairs
- Draws each domino with its coloured squares
- Implements highlighting for valid next moves

### game.py
- Initializes Pygame
- Creates a list of 10 domino objects
- Manages drag-and-drop interactions
- Implements sequencing logic for working area
- Calculates concatenated top/bottom sequences
- Updates highlights based on current game state
- Checks win condition and displays feedback
- Handles UI buttons (Clear, New Game)
- Visual timer display

### main.py
- Entry point of application

## Work Log

|   **Student**   | **Task** 
|    --------     | -------- 
| Noor Sidhu      | -Drag and drop manipulation<br> -Create working space area  
| Elijah Duchak   |                  
| Jasmine Seerha  | -Implemented win timer
| Harry Rai       | -Level difficulty manipulation
| Tanisha Ahuja   | -Win condition detection and feedback<br> -Highlighting of next valid dominoes<br> -Calculation of Concatenated top/bottom sequences
| Zac Adams       | -Random domino generation<br> -Visual domino rendering with random coloured squares
| Jasraj Gosal    |

## How the Game Works
### The Goal
**Arrange ALL dominoes left-to-right so that the ENTIRE top string matches the ENTIRE bottom string.**

It's NOT about matching 2 dominoes at a time. It's about building a long sequence.

## How to Play
1. **Objective**: Arrange dominoes from the set into the working area so that the concatenated TOP sequence matches the concatenated BOTTOM sequence
2. **Drag & Drop**: Click and drag dominoes from the top set into the working area
3. **Valid Moves**: Dominoes in the set will be **highlighted in yellow** if they can be placed next (their top matches the current bottom sequence)
4. **Sequencing**: Dominoes automatically arrange left-to-right in the working area
5. **Visual Feedback**: See the concatenated sequences displayed at the bottom of the screen
6. **Win Condition**: When top and bottom sequences match, you'll see a "MATCH! YOU WIN!" message
7. **Controls**: 
   - **Clear**: Remove all dominoes from working area
   - **New Game**: Generate a new set of random dominoes

## Step-by-Step Example

### Starting State (Empty Working Area)
```
Domino Set (all highlighted in YELLOW - any can start):
A: Top=[BLUE, BLUE] Bottom=[BLUE, BLUE, BLUE]
B: Top=[RED, GREEN] Bottom=[RED]
C: Top=[BLUE, BLUE, BLUE] Bottom=[GREEN]
D: Top=[RED] Bottom=[BLUE, BLUE]
```

### Step 1: Drag Domino A
```
Working Area: [A]

Top String:    BLUE, BLUE
Bottom String: BLUE, BLUE, BLUE

Match? NO (2 vs 3 colors)

What can go next? Look for dominoes where TOP = [BLUE, BLUE, BLUE]
→ Domino C is HIGHLIGHTED! 
```

### Step 2: Drag Domino C
```
Working Area: [A, C]

Top String:    BLUE, BLUE + BLUE, BLUE, BLUE = BLUE, BLUE, BLUE, BLUE, BLUE (5 colors)
Bottom String: BLUE, BLUE, BLUE + GREEN = BLUE, BLUE, BLUE, GREEN (4 colors)

Match? NO (different lengths and last color is different)

What can go next? Look for dominoes where TOP = [BLUE, BLUE, BLUE, GREEN]
→ NO matches! Nothing highlighted! 

This sequence is a DEAD END - click Clear and try a different combination!
```

### Better Approach: Start with Domino D
```
Working Area: [D]

Top String:    RED
Bottom String: BLUE, BLUE

What can go next? Look for dominoes where TOP = [BLUE, BLUE]
→ Domino A is HIGHLIGHTED! 
```

## Why Is Nothing Highlighted Sometimes?

This is normal and actually demonstrates why PCP is undecidable!

When no dominoes are highlighted, it means:
- Your current bottom sequence doesn't match ANY domino's top
- You've reached a DEAD END
- This sequence can't lead to a solution
- Click "Clear" and try a different order

## Tips for Playing

1. **Start simple** - Try each domino as a starting piece
2. **Watch the highlights** - Only highlighted dominoes can continue the sequence
3. **Dead ends are ok** - Part of the challenge!
4. **Some sets might be unsolvable** - That's the nature of PCP
5. **Click "New Game"** if you want a fresh set of dominoes

## Why This is Valuable for Computer Science

### The Problem's Importance
1. **Undecidability**: Proves there are problems computers CANNOT solve algorithmically
2. **Theoretical Foundation**: One of the first problems proven undecidable
3. **Practical Implications**: Helps us understand limits of computation

