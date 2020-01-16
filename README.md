## GEOG5990M - Programming for GIS: Core Skills 
### Assessment 2 - Drunk Model
This part of the online portfolio contains the [independent project](https://github.com/Seanj15/Assessment-2-) produced for the ['*GEOG5990M - Programming for GIS: Core Skills*'](https://www.geog.leeds.ac.uk/courses/computing/) course at the University of Leeds. The model has been coded in python, using an open source cross-platform IDE called '*Spyder*' (downloaded as part of the [Anaconda Distribution](https://www.anaconda.com/distribution/)). 
### About the model
The aim of the project was to build up a simple model, application or analysis from scratch. I chose to select the ['Planning for drunks'](https://www.geog.leeds.ac.uk/courses/computing/study/core-python/assessment2/drunk.html) project from Andy Turner's list of project ideas. Here, the aim was to build a model that monitors the movement of drunk people, as they leave a pub in the centre of a town (environment) and attempt to navigate their way home.  At a basic level, the model does the following:
- Pulls in a (‘drunk.plan’) data file and finds out the pub point and the home points.
- Draws the pub and homes on the screen.
- Models the drunks leaving the pub and reaching their homes, and stores how many drunks pass through each point on the map.
- Draws the density of drunks passing through each point on a map.
- Saves the density map to a file as text.

### Running the model
To run the model:
- Open up Spyder (Anaconda).
- Make sure your Graphics backend is set to "*Tkinter*". If not, select "*Tools*", then "*Preferences*". Scroll down on the menu bar (left-hand side) and select "*IPython console*". Select "*Graphics*" from the top, and then select "*Tkinter*" from the Backend drop down.
- You may then have to restart Spyder.
- Once you've done this , click on "*Run File*" (large green arrow).
- Two windows will appear. One entitled "*Figure 1*" (ignore this) and another entitled "*Model*" (the GUI).
- Open up the "*Model*" window.
- Then select "*Start the drunk model*" to run the model.
- If you want to stop the model, select "*Quit*" and close both windows.

### Link to the model
The model can be found in this [repository](https://github.com/Seanj15/Assessment-2-).
Here you will find three files:
- **drunk.model3.py** = a file than contains the core of the code.
- **drunkframework.py** = a file that initialises the agents (drunks).
- **drunk.plan.txt** = a file containing raster data which is used as the agents (drunks) environment.
- **density_environment.txt** = a file showing the density of drunks passing through each point on a map.
- **Assessment 2.docx** = a word document that contains a brief context for the software.
- **Assessment 2 UML Diagram** = a word document that contains a UML diagram (showing the code structure/flow).
