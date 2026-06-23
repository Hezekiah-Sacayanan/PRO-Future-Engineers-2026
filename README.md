# Content

This repository is organized into several folders, each containing a specific set of project files and documentation:

- **`t-photos/`** – Includes two team photographs: one official image and one creative team photo.
  
- **`v-photos/`** – Contains six detailed photographs of the vehicle, showing every side: front, back, left, right, top, and bottom.

- **`video/`** – Contains a file named `video.md` that links to a demonstration video of the robot in motion.
  
- **`schemes/`** – Includes electromechanical schematics (in PDF format). These diagrams illustrate the complete wiring setup including sensors, motors, controllers, and power management.

- **`src/`** – Contains all source code required to operate the vehicle. The code is written in _ and includes modular functions for sensor reading, motor control, decision logic, lap detection, and more.

- **`other/`** – Supplementary documentation during the development of the project.

---

## Table of Contents

* [Introduction](#introduction)
* [PSHS-CARC Future Engineers Team](#pshs-carc-future-engineers-team)
* [1. Robot Design and Construction](#1-robot-design-and-construction)

  * [1.1 Overall Robot Design](#11-overall-robot-design)
  * [1.2 Chassis Design and Construction](#12-chassis-design-and-construction)
* [2. Power and Sensor Systems](#2-power-and-sensor-systems)

  * [2.1 Power Management System](#21-power-management-system)
  * [2.2 Sensor Configuration and Integration](#22-sensor-configuration-and-integration)
  * [2.3 Bill of Materials (BOM)](#23-bill-of-materials-bom)
  * [2.4 Wiring and Electrical Layout](#24-wiring-and-electrical-layout)
* [3. Navigation and Obstacle Management](#3-navigation-and-obstacle-management)

  * [3.1 Open Challenge Strategy](#31-open-challenge-strategy)
  * [3.2 Obstacle Challenge Strategy](#32-obstacle-challenge-strategy)
* [4. Engineering Design Considerations](#4-engineering-design-considerations)
* [5. Improvements and Future Enhancements](#5-improvements-and-future-enhancements)

  * [5.1 Hardware Improvements](#51-hardware-improvements)
  * [5.2 Software Improvements](#52-software-improvements)
* [Credits and Acknowledgments](#credits-and-acknowledgments)

---

# Introduction

This document presents our robot for the WRO/PRO Future Engineers 2026 challenge. The robot is designed to autonomously navigate the arena, detect obstacles, complete laps, and perform the required parking task.

Our robot uses an EV3 brick for control, an EV3 gyro sensor for heading, two EV3 ultrasonic sensors for wall distance measurement, an EV3 servo motor for steering, an NXT motor for driving, and a HuskyLens AI camera for obstacle detection in the traffic block round.

---

# PSHS-CARC Future Engineers Team

The PSHS-CARC Future Engineers Team is composed of students from the Philippine Science High School – Cordillera Administrative Region Campus. The team collaborated in all stages of the project, including research, mechanical construction, programming, testing, troubleshooting, and documentation.

This section includes two team photographs: one formal photo and one creative photo that reflect both the professional and collaborative side of the team.

[Formal team photo to be inserted here]

[Creative team photo to be inserted here]

---

# 1. Robot Design and Construction

The robot was designed with a focus on stability, modularity, and ease of maintenance. Since the competition requires consistent autonomous operation, the vehicle's mechanical structure was carefully planned to support accurate sensor readings and predictable movement.

## 1.1 Overall Robot Design

The vehicle follows a four-wheeled rear-wheel-drive configuration with front-wheel steering, allowing precise control while navigating corners and avoiding obstacles. This layout provides a good balance between stability and maneuverability, which is important for both the open challenge and obstacle challenge rounds.

This section includes six photographs showing the robot from different views: front, back, left side, right side, top, and bottom view.

[Front view photo to be inserted here]

[Back view photo to be inserted here]

[Left side view photo to be inserted here]

[Right side view photo to be inserted here]

[Top view photo to be inserted here]

[Bottom view photo to be inserted here]

Sensors and processing components are strategically positioned to maximize detection accuracy while maintaining a balanced center of gravity. The EV3 gyro sensor helps the robot maintain orientation, while the left and right ultrasonic sensors provide distance feedback from the arena walls. The HuskyLens AI camera is mounted to support obstacle detection during the traffic block avoidance task.

## 1.2 Chassis Design and Construction

The chassis is constructed primarily from LEGO Mindstorms components, providing a lightweight yet durable framework. The modular nature of the LEGO system allowed rapid prototyping and easy adjustment of component placement throughout development.

Particular attention was given to wheel alignment, weight distribution, and sensor mounting locations to ensure consistent vehicle behavior and accurate environmental sensing. The steering mechanism was designed to work smoothly with the EV3 servo motor, while the NXT motor was integrated to deliver reliable driving power to the rear wheels.

### 1.2.1 Front Wheel Assembly

Due to limited materials, the team had to improvise using the components available at the time. The front wheels were originally soft, which caused unwanted flexing and bending during movement. This affected steering stability and made the robot less predictable when turning.

To solve this, each front wheel was rebuilt by combining three solid wheel pieces into one rigid wheel assembly. The front wheels were also made smaller than the rear wheels so that steering and turning would be better. This smaller size helped reduce steering resistance and improved the robot's turning response.

[Front wheel assembly photo to be inserted here]

### 1.2.2 Rear Wheel Assembly

The rear wheels also started as soft wheels, and this caused another bending issue. Because of this flexing, the robot had more difficulty moving forward smoothly. Since we did not have other replacement components, we decided to remove the wheel rubber entirely and leave the rear wheels without rubber treads.

This was a practical compromise based on the materials we had available. A possible future improvement would be to test tape or another traction material as a replacement for the missing rubber tread, although this has not yet been verified.

[Rear wheel assembly photo to be inserted here]

### 1.2.3 Rear Differential System

Aside from the wheel modifications, the robot also includes a differential system for the rear wheels. This system allows the left and right rear wheels to rotate at different speeds during turns, which helps the robot move more smoothly and reduces wheel scrubbing.

The differential system improves stability during cornering and supports more efficient motion when the robot changes direction. This is especially useful for maintaining consistent movement in both the open challenge and obstacle challenge rounds.

[Rear differential system photo to be inserted here]

---

# 2. Power and Sensor Systems

The robot relies on an integrated network of electrical and sensing components to perceive its surroundings and execute autonomous actions.

## 2.1 Power Management System

A centralized power system supplies energy to the EV3 brick, motors, sensors, and vision system. The power configuration was designed to provide stable operation throughout an entire competition run while minimizing electrical noise and voltage fluctuations.

### 2.1.1 EV3 Power Distribution

The EV3 brick serves as the main controller of the robot and provides power to the EV3-based components, including the servo motor, ultrasonic sensors, and gyro sensor. Stable power distribution is important because the robot must operate continuously and reliably during autonomous runs.

Proper cable management and power routing were implemented to reduce interference and make the system easier to maintain and troubleshoot.

[EV3 power distribution photo to be inserted here]

### 2.1.2 HuskyLens Power Supply

The HuskyLens AI camera required a separate power supply from the EV3 system. To support this, the team used two lithium-ion batteries connected to a buck converter, which regulated the voltage before supplying power to the camera. This ensured that the camera received a stable and appropriate voltage level during operation.

This separate power setup allowed the HuskyLens to function reliably while remaining integrated with the rest of the robot's control system.

[HuskyLens power supply photo to be inserted here]

## 2.2 Sensor Configuration and Integration

The robot utilizes multiple sensors that work together to provide information about the environment. Each sensor has a specific role in helping the robot navigate and respond to obstacles.

### 2.2.1 EV3 Gyro Sensor

The EV3 gyro sensor is used to measure rotation and heading changes, helping the robot maintain directional stability. It is especially useful when the robot needs to keep a straight path or make accurate turns.

By monitoring heading changes, the gyro sensor supports more consistent navigation and improves the robot's overall control.

[Gyro sensor photo to be inserted here]

### 2.2.2 EV3 Ultrasonic Sensors

The two EV3 ultrasonic sensors, placed on the left and right sides, are used to measure distances from the arena walls and support wall-following behavior. These sensors help the robot estimate its position relative to the track boundaries.

The distance data from both sensors is used to make steering corrections in real time, allowing the robot to stay aligned with the arena walls during movement.

[Ultrasonic sensor setup photo to be inserted here]

### 2.2.3 HuskyLens AI Camera

For the obstacle round, the HuskyLens AI camera performs object recognition to detect the traffic blocks that the robot must avoid. This allows the robot to identify obstacles visually and make navigation decisions based on their position.

The HuskyLens works together with the ultrasonic sensors to improve obstacle detection and decision-making reliability under varying conditions.

[HuskyLens camera photo to be inserted here]

## 2.3 Wiring and Electrical Layout

The wiring layout was designed to ensure reliable communication between sensors, motors, controllers, and power sources. Special consideration was given to cable routing in order to prevent interference with moving components and simplify troubleshooting.

To connect the HuskyLens AI camera to the EV3 brick, the team had to create its own breakout board because the commercially available EV3 Smart Camera Breakout board is only sold abroad and could not be ordered in time. The team therefore built a custom adapter using an RJ12 head to split the wires of the EV3 RJ12 cable. The wires were then soldered onto a copper-clad PCB to form a stable and organized connection point. This custom wiring solution made it possible to integrate the camera into the EV3-based system while maintaining a clean and functional electrical layout.

A complete wiring diagram is included below to illustrate all electrical connections used in the robot.

[Wiring and electrical layout photo to be inserted here]

---

# 3. Navigation and Obstacle Management

The robot's navigation system combines sensor feedback, computer vision, and programmed control logic to complete competition tasks autonomously.

## 3.1 Open Challenge Strategy

For the Open Challenge, the robot must complete multiple laps while maintaining a consistent path around the arena. Distance measurements from the left and right ultrasonic sensors are used to estimate the vehicle's position relative to the walls, allowing steering corrections to be made in real time.

The EV3 gyro sensor is used to help maintain heading stability and improve turning accuracy. Control algorithms were refined through extensive testing to improve cornering performance, maintain stable trajectories, and minimize navigation errors.

## 3.2 Obstacle Challenge Strategy

For the Obstacle Challenge, the HuskyLens AI camera identifies the traffic blocks encountered along the course. Based on the detected obstacle type and position, the robot determines the appropriate avoidance maneuver while maintaining forward progress around the track.

The obstacle management system combines visual recognition from the HuskyLens with distance measurements from the ultrasonic sensors to improve decision-making reliability under varying conditions. This combination allows the robot to react more accurately when navigating around obstacles.

---

# 4. Engineering Design Considerations

Throughout development, the team considered several engineering factors, including reliability, modularity, maintainability, weight distribution, sensor accuracy, and electrical stability. Design decisions were evaluated through repeated testing and performance analysis.

A major engineering challenge was integrating the HuskyLens AI camera with the EV3-based system. Since the camera required both a communication adapter and a separate power source, the team had to design a custom electrical solution that would work reliably during autonomous operation. The use of an RJ12 head, a copper-clad PCB, soldered wire connections, two lithium-ion batteries, and a buck converter was an important part of this integration process.

Trade-offs between complexity and reliability were carefully considered to ensure that the final design remained robust while meeting competition requirements. Lessons learned from each testing iteration were incorporated into subsequent revisions of both hardware and software systems.

---

# 5. Improvements and Future Enhancements

Continuous testing revealed several opportunities for improvement. Feedback gathered during development was used to refine both the mechanical and software aspects of the vehicle.

## 5.1 Hardware Improvements

Hardware improvements focused on optimizing sensor placement, strengthening structural components, improving cable management, and refining weight distribution. These changes contributed to increased consistency and reliability during autonomous operation.

Future improvements may include more suitable wheel materials, a more refined traction solution for the rear wheels, more compact component arrangements, a more refined mounting system for the HuskyLens AI camera, and purchasing the pre-made EV3 Smart Camera Breakout board if it becomes available locally or can be ordered in advance.

## 5.2 Software Improvements

Software improvements focused on refining navigation algorithms, improving obstacle detection accuracy, and enhancing decision-making logic. Multiple revisions were implemented to improve consistency and reduce the effects of environmental variation.

Future work may involve more advanced control strategies and additional sensor fusion techniques to further improve vehicle performance.

---

# Credits and Acknowledgments

The PSHS-CARC Future Engineers Team would like to thank our coach for the continuous guidance and support throughout the development of this project. We are also grateful to our school for allowing us to use its facilities and LEGO kits, which were essential to the construction and testing of our robot. We would also like to thank our parents for their encouragement, patience, and unwavering support throughout the entire process.

Their help and support played an important role in the successful completion of the vehicle and its participation in the competition.
