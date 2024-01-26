# InMoov Face 

Repository for my custom software for InMoov's Face. InMoov is an open source 3D Printed life size humanoid robot. 
This Repository only focuses on the face of InMoov.  

This software is ROS based and runs on Raspberry Pi 3.  

## Notes

### Raspberry Pi 3 Model B GPIO Pinout  

| GPIO # | Pin | Device | 
| ---------- | ----------| ---------- |
| 17 | 11 | Jaw Servo |
| 27 | 13 | Eyes Tilt |
| 22 | 15 | Eyes Pan |
| 5 | 29 | Neck turn |

### Servo motor angle thresholds

|Joint | Min Angle | Max Angle| Notes | 
| ----------| ----------| ---------- |---------- |
| Jaws | 40| 90 | min -> mouth closes |
| Eyes Pan | 40 | 120 | min is left, 90 is straight, max is right |
| Eyes Tilt | 70 | 120 | min is up, max is down |
| Neck | | | TBD|

