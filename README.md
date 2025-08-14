# Computer-Graphics-LAB-2-ASSIGNMENT-2-D-transformations-triangle
2D Transformations with Pygame
This program is a simple educational tool built with Pygame to demonstrate fundamental 2D geometric transformations on a triangle. The user can interactively apply transformations like translation, scaling, rotation, reflection, and shearing, and observe the results in real-time.

Key Features
Interactive Controls: Buttons at the bottom of the window allow the user to select a specific transformation.

User Input: For transformations that require parameters (like Translate or Rotate), an input box appears at the top of the screen to let the user define the values.

Undo Functionality: A Back button uses a history stack to revert the shape to its previous state.

Cancel Button: A Cancel button is available when entering parameters to easily clear the input and stop the operation.

Visual Feedback: The original shape is shown in blue, and the transformed shape is in red. The coordinates of the transformed shape are displayed on the screen for better understanding.

Error Handling: The program displays an on-screen message if the user enters invalid input, guiding them to correct their mistake.

Code Structure
The code is organized into several logical parts to make it easy to understand and modify:

Button Class: Manages the appearance and click detection for all interactive buttons.

InputBox Class: Handles all logic for the on-screen text input field, including drawing, capturing keyboard input, and managing its active state.

Transformation Functions: A set of dedicated functions (translate, scale, rotate, etc.) that implement the mathematical logic for each geometric transformation.

Main Game Loop: The central while loop that handles drawing the screen, processing user events (mouse clicks, keyboard input), and updating the game state.

How to Run on a Local Computer
To run this program, you will need to have Python and the Pygame library installed.

Install Python: If you don't have Python installed, download and install it from the official Python website.

Install Pygame: Open your terminal or command prompt and use pip, the Python package installer, to install the Pygame library.

pip install pygame

Save the Code: Save the provided Python code into a file named transformations.py on your computer.

Run the Program: Navigate to the directory where you saved the file and run the following command in your terminal.

python transformations.py

A new window will open, and you can begin interacting with the program.
