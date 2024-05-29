# README

This is the readme. It has nothing in it yet.

Statistics with Python: https://uqstatsssp.github.io/statistics_with_python




Presentation: https://uqstatsssp.github.io/statistics_with_python.pdf

Machine Learning FAQs: https://uqstatsssp.github.io/machine_learning_faqs

Algorithms for Automated Driving
============================

![](book/Introduction/carla_vehicle_lanes.jpg "")

Each chapter of this (mini-)book guides you in programming one important software component for automated driving. 
Currently, this book contains three chapters: **Lane Detection**, **Control** and **Camera Calibration**. You will implement software that 
* detects lane boundaries from a camera image using deep learning
* controls steering wheel and throttle to keep the vehicle within the detected lane at the desired speed
* determines how the camera is positioned and oriented with respect to the vehicle (a prerequisite to properly join the lane detection and the control module)

The software you will write is in python, and you will apply it in the [open-source driving simulator CARLA](https://carla.org/). Ideally, your computer is powerful enough to run CARLA, but if it is not, you can still work through the exercises. For the exercise on control there is a simplistic simulator that comes with this course. We recommend to work through the chapters in order, but if you want to, you can read the **Control** chapter, before the **Lane Detection** chapter.

To work through this book, you
* should understand the following math and physics concepts: derivative, integral, trigonometry, sine/cosine of an angle, matrix, vector, coordinate system, velocity, acceleration, angular velocity, cross product, rotation matrix
* should be familiar with programming in python. In particular, you should be comfortable with multidimensional arrays in numpy. You do **not** need a powerful computer (see [Exercise Setup](https://thomasfermi.github.io/Algorithms-for-Automated-Driving/Appendix/ExerciseSetup.html))
* need to know what supervised learning is, and how to train a neural network with a deep learning framework like pytorch, fastai, tensorflow, keras, or something similar. This prerequisite is only necessary for the chapter on lane detection. If you do not fulfill it, you can skip this chapter, or study one of the [courses I recommend](https://thomasfermi.github.io/Algorithms-for-Automated-Driving/LaneDetection/Segmentation.html) and then come back here.

If you find a bug in the exercise code or some confusing explanations in the book, please [raise an issue on github](https://github.com/thomasfermi/Algorithms-for-Automated-Driving). If you have questions about the material or want to connect with me or other students, please use [github discussions](https://github.com/thomasfermi/Algorithms-for-Automated-Driving/discussions). Once you finish the book or decide to stop working through it, please consider giving me some feedback by filling out [this questionnaire](https://forms.gle/TioqZiUsB5e5wSVG7) (If you open the link in your browser's incognito mode, the questionnaire should be anonymous).

## Read the book!
Please follow this [link](https://thomasfermi.github.io/Algorithms-for-Automated-Driving/Introduction/intro.html)!

## Discord
As of 2021, we have a discord server 🥳. Please follow this [link](https://discord.gg/57YEzkCFHN) to join the community!

## Help wanted!
Are you interested in contributing to the book by adding a new chapter? Or do you have other ideas for improvements? Please let us know by joining the discussion [on github](https://github.com/thomasfermi/Algorithms-for-Automated-Driving/discussions/4)!
