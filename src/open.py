#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port
from pybricks.hubs import EV3Brick 
import time

# Initialize EV3 Brick and Sensors
ev3 = EV3Brick()
us1 = UltrasonicSensor(Port.S1) 
us2 = UltrasonicSensor(Port.S2) 
gyro = GyroSensor(Port.S3)       

# Initialize Motors
steer_motor = Motor(Port.A)     
drive_motor = Motor(Port.D)     

# Global Navigation Variables
main_turns_amt = 0
anti_col_turn_deg = 20          
main_turn_deg = 45              
last_steer_target = 0
direction = None               

# Advanced Latch Filters to eliminate duplicate triggers on both blocks
blocks_checked_this_straight = 0  
is_avoiding = False               
active_latch_id = None           # Tracks the ID of the block currently being dodged

# -------------------------------------------------------------
# NAVIGATION & CAMERA FUNCTIONS
# -------------------------------------------------------------
def gyro_straight():
    """Keeps the robot aligned to its current 0-degree gyro heading."""
    global last_steer_target
    angle = gyro.angle()
    
    # Determine corrective actions based on drift
    if angle < -3:        
        target = -anti_col_turn_deg
        speed = 700
    elif angle > 3:     
        target = anti_col_turn_deg
        speed = 700
    else:             
        target = 0
        speed = 1000

    # Only fire command if target destination shifts to save CPU cycles
    if target != last_steer_target:
        drive_motor.run(speed)
        steer_motor.run_target(1000, target_angle=target, wait=False)
        last_steer_target = target

def rt():
    global main_turns_amt, last_steer_target
    print("Executing Turn towards Open Space 1...")
    drive_motor.run(350)
    
    # Initiate sharp turn sequence
    steer_motor.run_target(1000, target_angle=-main_turn_deg, wait=False)
    while gyro.angle() < 77: 
        time.sleep(0.01)

    # Re-align wheels to physical center
    steer_motor.run_target(1000, target_angle=0, wait=True)
    gyro.reset_angle(0) 
    last_steer_target = 0 
    main_turns_amt += 1
    ev3.speaker.beep()
    
    # CLEARANCE CONTROL: Move forward past the corner until walls return
    drive_motor.run(1000)
    while us1.distance() > 700:
        gyro_straight()
        time.sleep(0.01)

def lt():
    global main_turns_amt, last_steer_target
    drive_motor.run(350)
    
    # Initiate sharp turn sequence
    steer_motor.run_target(1000, target_angle=main_turn_deg, wait=False)
    while gyro.angle() > -75: 
        time.sleep(0.01)

    # Re-align wheels to physical center
    steer_motor.run_target(1000, target_angle=0, wait=True)
    gyro.reset_angle(0) 
    last_steer_target = 0 
    main_turns_amt += 1
    ev3.speaker.beep()
    
    # CLEARANCE CONTROL: Move forward past the corner until walls return
    drive_motor.run(1000)
    while us2.distance() > 700:
        gyro_straight()
        time.sleep(0.01)
                                                                                                         
# -------------------------------------------------------------
# MAIN TIMELINE RUNTIME
# -------------------------------------------------------------
# Initialize Device
ev3.speaker.beep()
steer_motor.run_target(1000, target_angle = 0, wait=True) 
steer_motor.reset_angle(0)
gyro.reset_angle(0)
time.sleep(0.5) 

drive_motor.run(1000) 
# DIRECTION DETERMINATION
while True:
    gyro_straight()       
    
    if us1.distance() > 750:
        direction = "CW"
        rt()
        break
    elif us2.distance() > 750:
        direction = "CCW"
        lt()
        break
        
    time.sleep(0.01)

# MASTER LAP ROUTINE
while main_turns_amt < 12:
    if direction == "CW":
        if us1.distance() > 750:
            rt()
        else:
            gyro_straight() 
            
    elif direction == "CCW":
        if us2.distance() > 750:
            lt()
        else: 
            gyro_straight()  
            
    time.sleep(0.01)

# MISSION COMPLETE
time.sleep(2)
drive_motor.stop()
steer_motor.run_target(1000, 0, wait=True)
ev3.speaker.beep(frequency=800, duration=1000)
