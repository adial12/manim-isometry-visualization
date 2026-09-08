# Manim Isometry Visualization

> An animated example of the different types of 2D Isometries (reflection, rotations, glide reflections). 

![Preview Animation Placeholder](path/to/preview.gif)

## Overview
This project provides a visual example of different types of isometries in 2D space. Every isometry $h: \mathbb{R}^2 \to \mathbb{R}^2$ can be written uniquely as $h(v) = Av + w$ , where $A$ is an orthogonal matrix and $w$ is a translation vector. This can be concluded from this following lemma: The group of isometries over $\mathbb{R}^n$ is a semi direct product of the group of translation maps with the group of orthogonal matrices ($\mathbb{O}_n$), that is: $Iso(\mathbb{R}^n) \cong T(n) \rtimes \mathbb{O}_n$.
By demonstrating how different choices of orthogonal matrices and translations shape these transformations, the project bridges abstract algebra with geometric intuition. It was built as extracurricular work for the Algebraic Structures course in the Ben-Gurion University Department of Mathematics, Fall semester 2026.

## Included Scenes
The project features several distinct modular scenes demonstrating different mathematical properties:
* **Glide:** Demonstrates glide reflections.
* **NoneZeroTranslation:** Demonstrates pure translations using identity matrices and none zero vector translation.
* **NoneZeroRotation:** Demonstrates isometries formed by a rotation matrix and none zero translation vector.
* **Rotation:** Demonstrates rotation transformations centered on (0,0).
* **Reflection** Demonstrates reflection transformation over the x-axis.
* **ReflectionComposition:** Visualizes the sequential composition of 3 reflections.

## Code Architecture
Built using a custom `BaseTransformationScene` inheriting from Manim's `MovingCameraScene`. This avoids repetitive code by standardizing:
* Dynamic viewport and camera tracking.
* Text anchoring and frame locking.
* Modular mathematical helper methods for calculating matrix transformations and vector translations.

## Getting Started

### Prerequisites
1. Python >= 3.13 
2. manim >= 0.19.1
3. LaTeX


### Installation
1. Clone the repository:
 ``` bash
git clone https://github.com/adial12/manim-isometry-visualization.git
 ```
Navigate into the directory:
 ``` bash
cd manim-isometry-visualization
 ```
Install manim:
 ``` python
pip install manim
 ```


For full documentation and installation instructions, please refer to the offical manim documentation for full installation explanations: https://docs.manim.community/en/stable/installation.html

2. To render and view the visual demonstrations of the 2D isometries, run the command in your terminal:
 ``` bash
manim -pql isometries.py IsometryScene
 ```
Make sure to replace the file and class names if they differ.
For example:
 ``` bash
manim -pql isometries.py Glide
 ```

You can use these helpful render flags: 
* `-p` to automatically play or preview the video once rendering is complete
* `-ql` to render in low quality (480p, 15fps) for fast iteration and testing
* `-qh` to render in high quality (1080p, 60fps) for final presentation outputs

## Structure
 ``` text
manim-isometry-visualization/
├── isometries.py     # Python script containing the Manim scene classes
└── README.md         # Project documentation and mathematical overview
 ```