# pcp-problem-game
PCP Problem Domino Sorting Game!  
Uses pygame-ce

## Overview
This project is an interactive game designed to display randomly generated Post Correspondence Problem (PCP) dominoes using coloured squares. 
Each domino consists of a top and bottom sequence of colours chosen from three possible colours: red, green, and blue. 
The purpose of the game is not to solve PCP (which is undecidable), but to allow users to experiement with randomly-generated dominoes and try to construct a matching sequence on the top and bottom strings. 

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

## Features
- Random domino generation (no duplicates)
- Visual domino rendering with colored squares
- Drag-and-Drop manipulation
- **Automatic left-to-right sequencing in working area**
- **Highlighting of valid next dominoes (yellow border)**
- **Real-time display of concatenated sequences**
- **Win condition detection and feedback**
- Clear and New Game buttons

## Project Structure

### domino.py
- Defines the colours (RED, GREEN, BLUE)
- Generates random top/bottom sequences (1-3 squares each)
- Ensures no duplicate domino pairs
- Draws each domino with its coloured squares
- **Implements highlighting for valid next moves**

### game.py
- Initializes Pygame
- Creates a list of 10 domino objects
- Manages drag-and-drop interactions
- **Implements sequencing logic for working area**
- **Calculates concatenated top/bottom sequences**
- **Updates highlights based on current game state**
- **Checks win condition and displays feedback**
- Handles UI buttons (Clear, New Game)

## Group Members
- Noor Sidhu
- Elijah Duchak
- Jasmine Seerha
- Harry Rai
- Tanisha Ahuja
- Zac Adams
- Jasraj Gosal