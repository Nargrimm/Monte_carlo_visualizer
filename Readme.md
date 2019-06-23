#Monte Carlo method visualizer

This project goal in to provide a visualization of the monte-carlo method use to get an approximation of PI.

### Usage
Compile the cpp backend

`make`

 Launch the python front end

`python3 plot.py`

This will output and HTML file called monteCarlo.html with the desired representation.


### Front end
The front end program is a written in Python, it calls then CPP backend several times with various parameter and then, using plotly, plots the results and export it.

### Back end
The programe back end is written in CPP, it allows fast calculation of the PI approximation.
It can be used as a standalone tool to get an approximation of PI
The program takes two arguments, the number of desired iteration and the number of thread we want to used.
If the number of desired thread is above 1, we will launch multiple times the calculation on the various thread and then average the results. This allows us to get a better approximation while not impacting the performance.

#### Using the backend only

The point of the project was to produce a visualization for the monte carlo methode but you can use the backend as a standalone tool to get a PI approximation.

Compile the cpp backend

`make`

Launch it

`./monteCarlo 1000000 8`

NB: If your goal is to get the best approximation of PI, use a really high value for the first parameter (the number of iteration), this will drastically increase the computing time but will improve your results. The second parameter (number of used thread) optimal value will depend on your CPU, increase it shall not increase the computing time (or barely) but will increase the precision.

