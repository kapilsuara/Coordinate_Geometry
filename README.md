# Coordinate_Geometry

---

# Line Class Utility

This Python script provides a `Line` class that allows users to perform various operations related to lines in 2D geometry, including finding line equations, calculating distances, and more. The class offers multiple methods to handle different cases such as two points, a point and slope, or slope and intercept.

## Features

- **Find Line Equation Given Two Points**: Calculate the equation of a line that passes through two given points.
- **Find Line Equation Given Point and Slope**: Determine the line equation given a point and the slope.
- **Find Line Equation Given Point and Intercept**: Calculate the line equation using a point and y-intercept.
- **Find Line Equation Given Slope and Intercept**: Directly get the line equation using slope and intercept.
- **Calculate Distance Between Two Points**: Find the Euclidean distance between two points.
- **Calculate Distance from a Point to a Line**: Compute the shortest distance from a point to a line represented by its equation.

## How to Use

### 1. **Initialization**

Simply instantiate the `Line` class to start using it. When the class is instantiated, a menu will be displayed prompting you to choose the operation you want to perform.

```python
line = Line()
```

### 2. **Methods**

The `Line` class supports the following operations:

- **Two Points**: Calculates the line equation that passes through two points.
    - Usage:
        - Choose option `1` when prompted.
        - Input the coordinates of two points (e.g., `1 2 3 4`).

- **Point and Slope**: Calculates the line equation from a given point and slope.
    - Usage:
        - Choose option `2` when prompted.
        - Input the slope and the coordinates of the point (e.g., slope: `2`, point: `1 3`).

- **Point and Intercept**: Calculates the line equation using a point and y-intercept.
    - Usage:
        - Choose option `3` when prompted.
        - Input the y-intercept and the coordinates of the point (e.g., intercept: `4`, point: `2 3`).

- **Slope and Intercept**: Directly provides the line equation using the slope and intercept form.
    - Usage:
        - Choose option `4` when prompted.
        - Input the slope and y-intercept (e.g., slope: `2`, intercept: `3`).

- **Distance Between Two Points**: Calculates the distance between two points.
    - Usage:
        - Choose option `5` when prompted.
        - Input the coordinates of two points (e.g., `1 2 3 4`).

- **Distance from a Point to a Line**: Calculates the distance from a point to a line using the line equation `ax + by + c = 0`.
    - Usage:
        - Choose option `6` when prompted.
        - Input the coefficients `a`, `b`, `c`, and the point coordinates (e.g., `1 2 3` for the line equation and `2 4` for the point).

### 3. **Example Usage**

```python
line = Line()
```

You will be prompted with options, and depending on your selection, you can input the required data to perform the operation.

### 4. **Dependencies**

This script only requires Python's built-in `math` module, so no external dependencies are needed.

## Error Handling

The `Line` class includes basic error handling to manage invalid inputs. It will prompt users to enter valid data if they input something unexpected (e.g., non-numeric values where numbers are expected).

## Contribution

Feel free to contribute to this script by adding more features, improving error handling, or optimizing the existing code.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it as you like.

---


