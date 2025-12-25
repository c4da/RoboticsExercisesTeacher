# Robotics Exercises - Forward Kinematics

This repository contains educational materials for learning forward kinematics for robotic arms.

## Contents

- `forward_kinematics.ipynb` - Interactive Jupyter notebook teaching forward kinematics for a 3-joint robot in 3D

## Prerequisites

- Python 3.7 or higher
- Jupyter Notebook or JupyterLab

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Launch Jupyter Notebook:
```bash
jupyter notebook
```

3. Open `forward_kinematics.ipynb` and start learning!

## What You'll Learn

This notebook covers:

1. **Basic Transformations**: Rotation matrices and homogeneous transformation matrices
2. **Denavit-Hartenberg (DH) Convention**: Systematic way to describe robot kinematics
3. **Forward Kinematics**: Computing end-effector position from joint angles
4. **3D Visualization**: Interactive plots of robot configurations
5. **Workspace Analysis**: Understanding the robot's reachable space
6. **Trajectory Planning**: Moving the robot through waypoints
7. **Jacobian Matrix**: Relating joint velocities to end-effector velocities

## Features

- ✅ Interactive 3D visualizations with sliders
- ✅ Step-by-step mathematical explanations
- ✅ Practical exercises with solutions
- ✅ Workspace analysis tools
- ✅ Trajectory planning demonstrations

## Topics Covered

### Part 1: Basic Transformations
Learn about rotation matrices around X, Y, and Z axes, and how to combine rotation and translation using homogeneous transformation matrices.

### Part 2: Denavit-Hartenberg Convention
Understand the systematic DH convention for describing robot kinematics using 4 parameters per joint.

### Part 3: 3-Joint Robot Arm
Implement a 3-DOF (Degree-of-Freedom) robot arm class with forward kinematics computation.

### Part 4: 3D Visualization
Visualize robot configurations in 3D space with coordinate frames.

### Part 5: Interactive Visualization
Control the robot with sliders and see real-time updates of the end-effector position.

### Part 6: Workspace Analysis
Understand the robot's workspace by sampling random configurations.

### Part 7: Trajectory Planning
Plan and visualize trajectories through multiple waypoints.

### Part 8: Exercises
Practice exercises including:
- Reachability testing
- Custom robot design
- Jacobian matrix computation (advanced)

## Next Steps

After completing this notebook, you can explore:
- Inverse kinematics
- Velocity kinematics
- Robot dynamics
- Path planning algorithms
- Different robot configurations (SCARA, 6-DOF arms, etc.)

## References

- Craig, J.J. "Introduction to Robotics: Mechanics and Control"
- Spong, M.W., Hutchinson, S., Vidyasagar, M. "Robot Modeling and Control"
- [Modern Robotics textbook](http://hades.mech.northwestern.edu/index.php/Modern_Robotics)

## License

This educational material is provided for learning purposes.

