---
title: CV-coarse2fine
---

These files are my first test to achieve the pyramid template matching with python openCV.

[referrence web](https://zone.ni.com/reference/en-XX/help/370281AC-01/nivisionconcepts/pattern_matching_techniques/)

This algorithm is achieved in the labview vision, but it takes a long time to compute the result. 

The temp3.py shows the compute time for full template matching, which cost 0.5s but this will cost more than 4s. 




# the framework for cam read & detection clss and its TCP server

- tcp server side 
- - initial tcp server
- - handle define
- - - call the cam read&od class 


- cam read& od class
- - initial cam 
- - add a processor to display the imges and detection result 
- - diplay the control commands 
- - select running mode (continue/request)
- - continue mode
- - - add a processor to capture and detect
- - request mode
- - - request and detecte


<!-- Up to now, I could match the template and make pyramids for images.
But there are several points that they are too closed to each other.
I need to define a compare function to select the best ones. -->
