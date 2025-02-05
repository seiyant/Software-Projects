# Multi-Project Showcase: GUI, Multithreading, Games & Sudoku Validator

**Student Name:** Seiya Nozawa-Temchenko  
**Student Number:** 34838482

---

## Overview

This repository contains several projects that demonstrate various aspects of Python programming, including:
- **GUI Applications** (using Tkinter) for arithmetic operations on rational and complex numbers.
- **Multithreading** for both sorting and concurrent file (comic) downloads.
- **Command-line Games** featuring a 2048 game with progressively enhanced features.
- **Sudoku Puzzle Validation** using both single-process and multiprocessing approaches.

Each project is divided into two parts (Part 1 and Part 2) where applicable, to illustrate an initial implementation and an enhanced or modified version.

---

## Projects

### 1. Arithmetic GUI

#### Part 1: Rational Numbers Calculator
- **Description:**  
  A simple GUI application that allows a user to perform arithmetic operations (addition, subtraction, multiplication, and division) on rational numbers. The rational numbers are stored in their lowest terms.
- **Key Features:**
  - Custom `Rational` class implementing arithmetic.
  - GUI built using Tkinter.
  - Error handling (e.g., division by zero, invalid input → displays "NaN").
- **Usage:**  
  Run the file (e.g., `arithmetic_gui_rational.py`) to launch the GUI.

#### Part 2: Complex Numbers Calculator
- **Description:**  
  An extension of the Part 1 GUI, modified to perform arithmetic with complex numbers (in Cartesian notation).  
- **Key Features:**
  - Custom `Complex` class with methods for addition, subtraction, multiplication, and division.
  - Consistent and user-friendly display format (e.g., omitting the coefficient 1 in the imaginary part).
- **Usage:**  
  Run the file (e.g., `arithmetic_gui_complex.py`) to launch the complex number calculator.

---

### 2. Multithreading Projects

#### a. Multithreaded Sorting Program (Part 1)
- **Description:**  
  This program sorts a list of integers by dividing it into two halves. Two separate threads sort each half using a custom quicksort algorithm, and a third thread merges the sorted halves.
- **Key Features:**
  - Custom implementation of quicksort.
  - No use of Python's built-in sort functions.
  - Shared variables for inter-thread communication (sorting and merging).
- **Usage:**  
  Run `multithreaded_sort.py` to see the final sorted list output on the console.

#### b. File Download Comparison with Multithreading (Part 2)
- **Description:**  
  The program downloads comic images from [xkcd.com](http://xkcd.com) in two ways:
  1. **Sequential Download:** One comic at a time.
  2. **Multithreaded Download:** Each comic is downloaded in its own thread.
- **Key Features:**
  - Uses `requests` for HTTP requests and `bs4` for HTML parsing.
  - Measures and compares the download time between the two methods.
- **Usage:**  
  Run `multithreaded_download.py` to see timing comparisons and the downloaded comic images in your working directory.

---

### 3. Simple 2048 Game

#### Part 1: Basic Command-line 2048
- **Description:**  
  A text-based version of the popular 2048 game. The game initializes a 4x4 board with two starting numbers (2’s) and allows moves (W, A, S, D) with sliding and merging logic.
- **Key Features:**
  - Board initialization, display, and user input handling.
  - Simple sliding/merging algorithm for updating the board.
- **Usage:**  
  Run `game_2048_part1.py` in your terminal to play the basic version.

#### Part 2: Enhanced Command-line 2048
- **Description:**  
  An improved version of the 2048 game that includes additional features:
  - New cell values are 2 or 4 (with probabilities 2/3 and 1/3, respectively).
  - A smarter placement algorithm to make immediate merges less likely.
  - (Optional) Additional improvements such as undo functionality.
- **Usage:**  
  Run `game_2048_part2.py` in your terminal to play the enhanced game.

---

### 4. Sudoku Validator

#### Part 1: Single-Process Sudoku Validator
- **Description:**  
  A script that validates a 9x9 Sudoku solution. It checks each row, each column, and each 3×3 subgrid for validity.
- **Key Features:**
  - Validates number ranges (1–9) and checks for duplicates.
  - Prints validation results for each row, column, and subgrid.
- **Usage:**  
  Run `sudoku_validator_part1.py` to validate a given Sudoku puzzle.

#### Part 2: Multiprocessing Sudoku Validator
- **Description:**  
  An enhanced version of the Sudoku validator that leverages Python's `multiprocessing` module.  
  It creates 27 separate processes (9 for rows, 9 for columns, and 9 for subgrids) to perform validation concurrently.
- **Usage:**  
  Run `sudoku_validator_part2.py` to observe parallel validation results.
