# UIFit
(Featured in Harvard's Engineering & Sciences Paper: https://www.seas.harvard.edu/news/2019/11/ode-code)  
Our hack for HackHarvard tackles optimizing online shopping.
Given 3 photos of the user, using machine learning, our program will be able to use body part detection with coordinates to find the relative size of the person and see how well clothing will fit them.
With a front-end based in React.JS and a back-end based in Python, our project began with the essence of image detection and recognition of the key parameters of the body. 
As such, we utilized a machine-learning model named open-pose (https://github.com/CMU-Perceptual-Computing-Lab/openpose) to take in a full-body image of a user and plot markers on the aforementioned body parameters. 
Our program then accurately calculates and obtains measurements tailored to each body. These are then used in the analysis stage where the fitting is determined. 
Finally, the user's inputs are compared with online measurements stored in JSON, and a fit output with specific details is computed.
What you are left with is a chosen article of clothing that has been superimposed onto your body, so that you can get a virtual sense of how well it fits your body!
