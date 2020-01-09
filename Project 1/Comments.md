# Project 1 Comments

## **Project1 - Part 1A**

1. Rung: Initial State for Input0 and Output1
 - Comment: Input0 and Output1 are both deactivated
2. Rung: Activate Output1
 - Comment: Toggling Input0, activates Output1
3. Rung: Activate Output0
 - Comment: Untoggled Input1 activates Output0
4. Rung: Deactivate Output0
 - Comment: Toggled Input1 deactivates Output0

## **Project1 - Part 1B**

1. Rung: Initial State
 - Initially, Input0 and Output0 are both deactivated.
2. Rung: Activate Output0
 - When Input0 is toggled, Output0 is immediately activated for 5 seconds and then deactivated.

## **Project1 - Part 1C**

1. Rung: On state
 - Comment: Turn output on, based on initial state
2. Rung: Off state
 - Comment: Turn output off (reset coil)
3. Rung: Timer On State
 - Comment: Set coil (%M1)
4. Rung: Reset
 - Comment: Reset coils (%M0 and %M1)
5. Rung: Set timer TM0
 - Comment: Set timer to control LED-ON portion of loop and map to %IW0.0
6. Rung: Set timer TM1
 - Comment: Set timer to control LED-OFF portion of loop and map to %IW0.1
