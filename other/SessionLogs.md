# Session Logs

This file will contain all the things we've done during the sessions to keep track of the progress we made.

## Preparations (Session 0)
- To start off the work, we certainly needed to plan what will we need and order it. The first thing we chose was the control unit as it will define all the other elements we need. We wanted to use Raspberry Pi as it is lightweight, easily managable, and can run not just a limited micro python like LEGO hubs.
- We planned the whole run, like we will run the wheels at a constant speed and steer the car based off the value we get from the controller. The controller will have two aspects: the walls' distances and the pillars (color, distance and relative place). If we are making it the right way, PID factors will provide us many parameters to finetune it.
- For motors, we had LEGO Spike motors, which are extremly precise. So we bought a Build Hat for Raspberry Pi as it provides the Raspberry 4 LEGO Spike ports (two motors and two ultrasonic sensors).
- We already had a camera which is wide enough and can be connected to the Raspberry Pi directly.
- For starting the program in the competition, we will need a button and a LED as well, for signing the status of the car. For this we will need GPIO extenders, just as bigger spacers for the Build Hat.
- For power supply we planned to use power bank or 9V batteries so we ordered different gadgets to test out the proper way of powering the car.
- So for driving we are using 2 LEGO Spike motors, and for sensing the environment, we planned to use two ultrasonic sensors detecting the walls on the left and right and a camera looking for the pillars.


## Foundations (Session 1) 2025.05.17
- We started the session with planning our GitHub repository and the whole workflow. For the workflow we decided on listing larger tasks in a backlog and breaking it down into subtasks. Then we have a PDCA cycle (plan-do-check-act) which we iterate through until we are finished with the subtask and start it again. Trello is handy when it comes to managing projects' workflow, so we made a Trello board. 
- After the planning we started building the car itself from LEGO. First off, we designed the position of the sensors and motors. After putting them together, we made the steering mechanism. In the next step we found the proper place for the camera where it can see the most in front of the car. We placed the Raspberry next to it as the ribbon cable is limited.
- Then as we didn't have a proper power supply for the Build Hat, the most we could do was to detect the pillars with the camera (as the camera is independent from the Build Hat). Successfully we got to making an image, masking it, and get the corners of the green pillar. In a short time we can use this tool for making the PID controller for the car.
- Right after the session, we made a Discord server for communication as it's customisable and can handle any type of files. For making it possible to work independently, we shot some pictures with the camera of the car, so we can work with them. Finally we created a `version-0` branch so each branch will show the state of the repo to a milestone.