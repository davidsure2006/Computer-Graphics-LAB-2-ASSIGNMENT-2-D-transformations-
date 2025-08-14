# Computer-Graphics-LAB-2-ASSIGNMENT-2-D-transformations-triangle

This program is designed to fulfill the objective of performing and visualizing **2D transformations** on a triangle. It serves as an interactive tool to demonstrate the effects of **translation, scaling, rotation, reflection, and shearing**. The user can observe these transformations in real-time, making it an effective educational and lab-based assignment.

---

### Key Features

* **Interactive Controls**: Buttons at the bottom of the window allow the user to select a specific transformation.
* **User Input**: For transformations that require parameters (like `Translate` or `Rotate`), an input box appears at the top of the screen to let the user define the values.
* **Undo Functionality**: A `Back` button uses a history stack to revert the shape to its previous state.
* **Cancel Button**: A `Cancel` button is available when entering parameters to easily clear the input and stop the operation.
* **Visual Feedback**: The original shape is shown in blue, and the transformed shape is in red. The coordinates of the transformed shape are displayed on the screen for better understanding.
* **Error Handling**: The program displays an on-screen message if the user enters invalid input, guiding them to correct their mistake.

---

### 2D Transformations Explained

* **Translation**: A transformation that **moves** an object to a new location on the screen without changing its size, shape, or orientation. It's essentially shifting the object along a straight line.
* **Scaling**: A transformation that **changes the size** of an object. It can make the object larger or smaller, and can be applied uniformly (same scale factor for X and Y) or non-uniformly (different scale factors).
* **Rotation**: A transformation that **rotates** an object around a fixed point (in this case, the center of the shape). The object maintains its shape and size but changes its orientation.
* **Reflection**: A transformation that creates a **mirror image** of an object across a line, such as the X-axis or Y-axis. The reflected object is the same size and shape as the original but is flipped.
* **Shearing**: A transformation that **skews** or slants an object. It shifts points in a direction proportional to their distance from a fixed axis, making the object appear tilted or stretched.

---

### Code Structure

The code is organized into several logical parts to make it easy to understand and modify:

* **`Button` Class**: Manages the appearance and click detection for all interactive buttons.
* **`InputBox` Class**: Handles all logic for the on-screen text input field, including drawing, capturing keyboard input, and managing its active state.
* **Transformation Functions**: A set of dedicated functions (`translate`, `scale`, `rotate`, etc.) that implement the mathematical logic for each geometric transformation.
* **Main Game Loop**: The central `while` loop that handles drawing the screen, processing user events (mouse clicks, keyboard input), and updating the game state.

---

### How to Run on a Local Computer

To run this program, you will need to have Python and the Pygame library installed.

1.  **Install Python**: If you don't have Python installed, download and install it from the official [Python website](https://www.python.org/).
2.  **Install Pygame**: Open your terminal or command prompt and use pip, the Python package installer, to install the Pygame library.

    ```bash
    pip install pygame
    ```

3.  **Save the Code**: Save the provided Python code into a file named `transformations.py` on your computer.
4.  **Run the Program**: Navigate to the directory where you saved the file and run the following command in your terminal.

    ```bash
    python transformations.py
    ```

A new window will open, and you can begin interacting with the program.
