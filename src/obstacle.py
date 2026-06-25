#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port
from pybricks.hubs import EV3Brick
from pyhuskylens import HuskyLens, ALGORITHM_COLOR_RECOGNITION  
import time

# Initialize EV3 Brick and Sensors
ev3 = EV3Brick()
us1 = UltrasonicSensor(Port.S1) 
us2 = UltrasonicSensor(Port.S2) 
gyro = GyroSensor(Port.S3)       

# Initialize HuskyLens on Port 4 (Adjust Port.S4 if needed)
hl = HuskyLens(Port.S4)
hl.set_alg(ALGORITHM_COLOR_RECOGNITION)

# Initialize Motors
steer_motor = Motor(Port.A)     
drive_motor = Motor(Port.D)     

# Global Navigation Variables
main_turns_amt = 0
anti_col_turn_deg = 20          
main_turn_deg = 35              
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
    if angle < -2:        
        target = -anti_col_turn_deg
        speed = 350
    elif angle > 2:     
        target = anti_col_turn_deg
        speed = 350
    else:             
        target = 0
        speed = 600

    # Only fire command if target destination shifts to save CPU cycles
    if target != last_steer_target:
        drive_motor.run(speed)
        steer_motor.run_target(1000, target_angle=target, wait=False)
        last_steer_target = target

def check_camera_color():
    """Processes color blocks up to a max of 2 per straightaway.

    Uses an entry/exit vertical screen gate to prevent duplicate triggers on both blocks.
    """
    global blocks_checked_this_straight, is_avoiding, last_steer_target, active_latch_id
    
    # Stop checking if we already handled t
    # he 2-block maximum or are mid-maneuver
    if blocks_checked_this_straight >= 2 or is_avoiding:
        gyro_straight()
        return

    blocks = hl.get_blocks(learned=True)
    id_found = False

    # AUTOMATIC LATCH RESET GATE:
    # If the camera feed becomes completely clear or the block we just handled 
    # drops out of sight or moves to the far background (Y < 80), release the lock.
    if active_latch_id is not None:
        latch_still_visible = any(b.ID == active_latch_id and b.y >= 80 for b in blocks)
        if not latch_still_visible:
            print("Block cleared from view. Unlocking latch for ID:", active_latch_id)
            active_latch_id = None # Ready to accept a new block (even of the same color!)

    for block in blocks:
        # FILTER: Ignore this frame completely if it belongs to the block we are currently passing
        if block.ID == active_latch_id:
            continue

        # CRITICAL TRIGGER GATE: Only initiate a dodge when the block is close (Y > 100)
        if (block.ID == 1 or block.ID == 2) and block.y > 60:
            ev3.speaker.beep()
            id_found = True
            is_avoiding = True
            blocks_checked_this_straight += 1
            active_latch_id = block.ID  # Lock this ID immediately to block double-triggering
            
            print("Dodge Triggered! Block #", blocks_checked_this_straight, "| ID:", block.ID, "at Y:", block.y)
            drive_motor.run(300) 
            
            if block.ID == 1:
                avoid_red()
            else:
                avoid_green()

            last_steer_target = 0
            is_avoiding = False
            break
            
    if not id_found:
        gyro_straight()

def avoid_green():
    steer_motor.run_target(1000, target_angle=35, wait=True)
    time.sleep(1)
    steer_motor.run_target(1000, target_angle=0, wait=False)
    while us2.distance() > 400:
        time.sleep(0.01)
    steer_motor.run_target(1000, target_angle=-35, wait=True)
    time.sleep(0.5)
    steer_motor.run_target(1000, target_angle=0, wait=True)
    time.sleep(0.5)
    steer_motor.run_target(1000, target_angle=-35, wait=True)
    time.sleep(0.5)
    steer_motor.run_target(1000, target_angle=0, wait=True)
    time.sleep(0.5)
    steer_motor.run_target(1000, target_angle=35, wait=True)
    time.sleep(0.5)
    steer_motor.run_target(1000, target_angle=0, wait=False)

def avoid_red():
    steer_motor.run_target(1000, target_angle=-35, wait=True)
    time.sleep(1)
    steer_motor.run_target(1000, target_angle=0, wait=False)
    while us1.distance() > 400:
        time.sleep(0.01)
    steer_motor.run_target(1000, target_angle=35, wait=True)
    time.sleep(0.5)
    steer_motor.run_target(1000, target_angle=0, wait=True)
    time.sleep(0.5)
    steer_motor.run_target(1000, target_angle=35, wait=True)
    time.sleep(0.5)
    steer_motor.run_target(1000, target_angle=0, wait=True)
    time.sleep(0.5)
    steer_motor.run_target(1000, target_angle=-35, wait=True)
    time.sleep(0.5)
    steer_motor.run_target(1000, target_angle=0, wait=False)

def rt():
    global main_turns_amt, last_steer_target, blocks_checked_this_straight, is_avoiding, active_latch_id
    print("Executing Turn towards Open Space 1...")
    drive_motor.run(350)
    
    if active_latch_id == "1":
        time.sleep(1)
        drive_motor.run(-600)
        steer_motor.run_target(1000, target_angle=main_turn_deg, wait=False)
        while gyro.angle() < 75: 
            time.sleep(0.01)

        # Re-align wheels to physical center
        steer_motor.run_target(1000, target_angle=0, wait=True)
        drive_motor.run(600)
        gyro.reset_angle(0) 
        last_steer_target = 0 
        main_turns_amt += 1
        
        # Reset tracking registers completely for the new straightaway segment
        blocks_checked_this_straight = 0
        active_latch_id = None
        is_avoiding = False
        ev3.speaker.beep()
        

    if active_latch_id == "2":
        # Initiate sharp turn sequence
        steer_motor.run_target(1000, target_angle=-main_turn_deg, wait=False)
        while gyro.angle() < 75: 
            time.sleep(0.01)

        # Re-align wheels to physical center
        steer_motor.run_target(1000, target_angle=0, wait=True)
        drive_motor.run(-600)
        time.sleep(1)
        drive_motor.run(600)
        gyro.reset_angle(0) 
        last_steer_target = 0 
        main_turns_amt += 1
        
        # Reset tracking registers completely for the new straightaway segment
        blocks_checked_this_straight = 0
        active_latch_id = None
        is_avoiding = False
        ev3.speaker.beep()


def lt():
    global main_turns_amt, last_steer_target, blocks_checked_this_straight, is_avoiding, active_latch_id
    drive_motor.run(350)
    
    # Initiate sharp turn sequence
    if active_latch_id == "2":
        time.sleep(1)
        drive_motor.run(-350)
        steer_motor.run_target(1000, target_angle=-main_turn_deg, wait=False)
        while gyro.angle() < 75: 
            time.sleep(0.01)

        # Re-align wheels to physical center
        steer_motor.run_target(1000, target_angle=0, wait=True)
        drive_motor.run(600)
        gyro.reset_angle(0) 
        last_steer_target = 0 
        main_turns_amt += 1
        
        # Reset tracking registers completely for the new straightaway segment
        blocks_checked_this_straight = 0
        active_latch_id = None
        is_avoiding = False
        ev3.speaker.beep()
        

    if active_latch_id == "1":
        # Initiate sharp turn sequence
        steer_motor.run_target(1000, target_angle=main_turn_deg, wait=False)
        while gyro.angle() < 75: 
            time.sleep(0.01)

        # Re-align wheels to physical center
        steer_motor.run_target(1000, target_angle=0, wait=True)
        drive_motor.run(-350)
        time.sleep(1)
        drive_motor.run(600)
        gyro.reset_angle(0) 
        last_steer_target = 0 
        main_turns_amt += 1
        
        # Reset tracking registers completely for the new straightaway segment
        blocks_checked_this_straight = 0
        active_latch_id = None
        is_avoiding = False
        ev3.speaker.beep()

# -------------------------------------------------------------
# MAIN TIMELINE RUNTIME
# -------------------------------------------------------------
# Initialize Device
ev3.speaker.beep()
steer_motor.run_target(1000, 0, wait=True) 
steer_motor.reset_angle(0)
gyro.reset_angle(0)
time.sleep(0.5) 

drive_motor.run(700) 

# DIRECTION DETERMINATION

while  us1.distance() < 800 and us2.distance() < 800:
    check_camera_color()          

if us1.distance() > 800 and blocks_checked_this_straight != 0:
    direction = "CW"
    rt()
elif us2.distance() > 800 and blocks_checked_this_straight != 0:
    direction = "CCW"
    lt()

# MASTER LAP ROUTINE
while main_turns_amt < 12:
    if direction == "CW":
        if us1.distance() > 800 and blocks_checked_this_straight != 0:
            rt()
        else:
            check_camera_color() 
            
    elif direction == "CCW":
        if us2.distance() > 800 and blocks_checked_this_straight != 0:
            lt()
        else: 
            check_camera_color()  
            
    time.sleep(0.01)

# MISSION COMPLETE
time.sleep(2)
drive_motor.stop()
steer_motor.run_target(1000, 0, wait=True)
ev3.speaker.beep(frequency=800, duration=1000)
