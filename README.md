# pcp-problem-game
PCP Problem Domino Sorting Game!  
Uses pygame-ce

## Overview
This project is an interactive game designed to display randomly generated Post Correspondence Problem (PCP) dominoes using coloured squares. 
Each domino consists of a top and bottom sequence of colours chosen from three possible colours: red, green, and blue. 
The purpose of the game is not to solve PCP (which is undecidable), but to allow users to experiement with randomly-generated dominoes and try to construct a matching sequence on the top and bottom strings. 

## Features
- Random domino generation
- Visual domino rendering
- Display layout
- Drag-and-Drop manipulation
- Working area to build sequences
- Highlighting of valid next dominoes

## Project Structure

### domino.py
- Defines the colours
- Generates random top/bottom sequences
- Ensures no duplicate domino pairs
- Draws each domino with its coloured squares

### game.py
- Initializes Pygame
- Creates a list of 10 domino objects
- Prints domino data for debugging
- Displays dominoes on screen 

## Group Members
- Noor Sidhu
- Elijah Duchak
- Jasmine Seerha
- Harry Rai
- Tanisha Ahuja
- Zac Adams
- Jasraj Gosal