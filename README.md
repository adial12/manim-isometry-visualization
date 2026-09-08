# Manim Isometry Visualization

> An animated example of the different types of 2D Isometries (reflection, rotations, glide reflections). 

![Preview Animation Placeholder](path/to/preview.gif)

## Overview
This project provides a visual example for different types of Isometries in 2D space. Every isometry h:R^2->R^2 can be written uniquely as h(v) = Av + w , where A is an orthogonal matrix and w is a vector in the space. This project explores 2D isometries and provides visual examples for how the different choices of orthogonal matrices and vector choices create different types of isometries. This project was built as part of extracaricular work for an advanced Algabareic Structures class in Ben Gurion University Mathematics department, fall semester 2026.

## Included Scenes
The project features several distinct modular scenes demonstrating different mathematical properties:
* **Glide:** Demonstrates glide reflections ($\det A = -1, w \ne 0$).
* **NoneZeroTranslation:** Demonstrates pure translations using identity matrices and none zero vector translation.
* **NoneZeroRotation:** Demonstrates isometries formed by a rotation matrix and none zero translation vector.
* **Rotation:** Demonstrates rotation transformations centered on (0,0).
* **Reflection** Demonstrates reflection transformation over the x-axis.
* **ReflectionComposition:** Visualizes the sequential composition of 3 reflections.

## Code Architecture
Built using a custom `BaseTransformationScene` inheriting from Manim's `MovingCameraScene`. This avoids repetitive code by standardizing:
* Dynamic viewport and camera tracking.
* Text anchoring and frame locking.
* Modular mathematical helper methods for calculating matrix reflections and vector translations.

## Getting Started

### Prerequisites
Make sure you have Python installed along with Manim's system dependencies (like FFmpeg and Cairo).

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/manim-geometric-transformations.git](https://github.com/your-username/manim-geometric-transformations.git)
   cd manim-geometric-transformations