# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 12:59:26 2020

@author: Sean


This model uses Tkinter to create a standard GUI.
When you run the code, two windows should appear
on your screen ('Figure 1' and 'Model').
In the top right of the 'Model' window, please select
either 'Start the drunk model' (to run the model) or 'Quit'
to close the GUI. 
"""

# import libraries 
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.backends.backend_tkagg
import csv
import drunkframework # import the second python file containing the agent class
import matplotlib.pyplot 
import matplotlib.animation
from IPython import get_ipython # import IPython to get the density map to appear inline



# Set up the containers and define number of drunks and number of iterations 
environment = []
drunks = []
num_of_drunks = 25 # Number of drunks should not be changed, as their are only 25 houses
print("This is the list of drunks = " + str(list(range(num_of_drunks)))) # Test how many drunks there are in the model
num_of_iterations = 9999
print("This is the number of iterations = " +str(num_of_iterations)) # Test the number of iterations

# Read in the 'drunk.plan' data file - this initialises the environment
# The pub is denoted by 1s, the houses by the numbers 10-250, and the empty spaces zeros.
f = open('drunk.plan.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist =[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

# Initialise the GUI and set up the figure size and axes
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_autoscale_on(False)

# Sets up a new environment to store how many drunks pass through each point on the map.
# Only the number '0' is counted in the 'drunk.plan' data file when mapping the density of drunks.
density_environment = []

for i in range(len(environment)):
    rowlist = []
    for j in range(len(environment[0])):
        rowlist.append(0)  
    density_environment.append(rowlist)
    
# Assign each drunk a specific house number.
# The houses are denoted by the numbers 10-250 in the 'drunk.plan' data file.
for i in range (num_of_drunks):
    house_number = ((1+i))*10 # 25 drunks each get assigned to an individual house (in range 10-250)
    drunks.append(drunkframework.Drunk(environment, drunks, house_number)) 
    print(house_number) # Check the number of house numbers is correct
print("The house numbers should range from 10-250, adding 10 each time.")
carry_on = True

def update(frame_number):
    '''
    This function initialises the drunks. Each drunk moves randomly around the environment
    until they reach their (assigned) home. 
    To view the final model (i.e when all drunks have reached their homes), please 
    uncomment line 82 (below) and run the model.
    '''   
    fig.clear()
    global carry_on 
    
    for i in range (num_of_drunks):                                                                     
        #while drunks[i].home == False: 
            drunks[i].move() # Drunks move around randomly - as defined in drunk.framework
            density_environment[drunks[i].y][drunks[i].x] += 1 # Adds 1 to the density map for every iteration
            if drunks[i].house_number == drunks[i].environment[drunks[i].y][drunks[i].x]:
                drunks[i].home = True # Drunks will stop moving if they reach their home 
                
    # Plots the environment - to show the houses and pub       
    matplotlib.pyplot.xlim(0, len(environment))
    matplotlib.pyplot.ylim(0, len(environment[0]))
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_drunks):
        if drunks[i].home == True:
            matplotlib.pyplot.scatter(drunks[i].x,drunks[i].y, c='white') # If drunks reach their homes, they turn white.
        else:
            matplotlib.pyplot.scatter(drunks[i].x,drunks[i].y, c='red', marker = 'X') #If drunks have not reached their homes, they are depicted as a red cross.

def gen_function():
    """A stopping function for the animation"""
    a = 0
    global carry_on
    while (a < 1000) & (carry_on):
        yield a			
        a = a + 1

def run():
    """ Run model to animate plot for GUI interface"""
    global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

def close():
    """
    This function closes the model.
    """
    root.destroy()

# Sets up the GUI
root = tkinter.Tk()
root.wm_title("Model")
menubar = tkinter.Menu(root)
root.config(menu=menubar)
model_menu = tkinter.Menu(menubar)
menubar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run, state="normal")
model_menu.add_command(label="Close model", command=close)

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)

# Defines the "run" button to start the model
butt1=tkinter.Button(root, command=run, text="Start the drunk model")
butt1.pack(padx=5, pady=5)

# Defines the "quit" button to stop the model
butt2=tkinter.Button(root, command=close, text="Quit")
butt2.pack(padx=5, pady=5)

tkinter.mainloop()

# Saves the density map to a csv file as text.
f2 = open('density_environment.txt', 'w', newline='')
writer = csv.writer(f2, delimiter=',')
for row in density_environment:
    writer.writerow(row)
f2.close()

# From the IPython Magic Commands - this allows the matplotlib figure to appear inline
get_ipython().magic("matplotlib inline") # Make the density map appear within python console

# Initialise the GUI and set up the figure size and axes 
fig = matplotlib.pyplot.figure(figsize=(8, 8))
ax = fig.add_axes([0, 0, 1, 1])


# Plots the environment - to show the density map 
matplotlib.pyplot.xlim(0, len(environment)) 
matplotlib.pyplot.ylim(0, len(environment[0]))
matplotlib.pyplot.imshow(density_environment, vmin=0, vmax=250)
matplotlib.pyplot.colorbar(shrink = 0.85, label='Density of drunks') # Initialise colour bar

# Shows the density environment in the console
matplotlib.pyplot.imshow(density_environment)
matplotlib.pyplot.show()
    
    
