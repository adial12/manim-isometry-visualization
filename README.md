# Manim Isometry Visualization

<img width="400" height="225" alt="ZeroRotation" src="https://github.com/user-attachments/assets/da7389eb-7aff-4e98-81da-4efd096835a3" />



## Overview
This project provides a visual example of different types of isometries in 2D space. Every isometry $h: \mathbb{R}^2 \to \mathbb{R}^2$ can be written uniquely as $h(v) = Av + w$ , where $A$ is an orthogonal matrix and $w$ is a translation vector.

By demonstrating how different choices of orthogonal matrices and translations shape these transformations, the project bridges abstract algebra with geometric intuition. It was built as extracurricular work for the Algebraic Structures course in the Ben-Gurion University Department of Mathematics, Fall semester 2026.


## Included Scenes
This project features the following modular scenes showcasing different mathematical properties:
* **Glide:** Demonstrates glide reflections.
* **NoneZeroTranslation:** Demonstrates pure translations using identity matrices and none zero vector translation.
* **NoneZeroRotation:** Demonstrates isometries formed by a rotation matrix and none zero translation vector.
* **Rotation:** Demonstrates rotation transformations centered on (0,0).
* **Reflection** Demonstrates reflection transformation over the x-axis.
* **ReflectionComposition:** Visualizes the sequential composition of 3 reflections.


To render and view the visual demonstrations of the 2D isometries, run the command in your terminal:
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

## Citations
```bibtex
@article{conrad_isometries_rn,
  author = {Conrad, Keith},
  title = {Isometries of $\mathbb{R}^n$},
  journal = {Expository Notes, University of Connecticut},
  url = {https://kconrad.math.uconn.edu/blurbs/grouptheory/isometryRn.pdf}
}
```
