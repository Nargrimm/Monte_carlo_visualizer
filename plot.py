import subprocess
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

current_iteration = 100
iteration_max = 10000000
dot_per_iteration = 10
result_array = []
x = []
y = []
min_max_x_array = []
max_y_array = []
min_y_array = []
max_y = float('-inf')
min_y = float('inf')

while  current_iteration <= iteration_max:
  for i in range (0, dot_per_iteration):
    result = subprocess.run(['./monteCarlo', str(current_iteration), str(1)], stdout=subprocess.PIPE)
    result_array.append((current_iteration, float(result.stdout)))
    tmp_res = float(result.stdout)
    x.append(current_iteration)
    y.append(tmp_res)
    if (tmp_res > max_y):
      max_y = tmp_res
    if (tmp_res < min_y):
      min_y = tmp_res
  max_y_array.append(max_y)
  min_y_array.append(min_y)
  min_max_x_array.append(current_iteration)
  max_y = float('-inf')
  min_y = float('inf')
  current_iteration *= 10

print(result_array)

trace = go.Scatter(
  x = x,
  y = y,
  mode = 'markers',
  marker = dict(
        size = 10,
        color = 'rgb(0, 0, 0)',
        ),
  name = 'Monte Carlo'
)

pi = go.Scatter(
  x = [0, iteration_max],
  y = [3.14159265359, 3.14159265359],
  mode = 'lines',
  name = 'PI'
)

high = go.Scatter(
  x = min_max_x_array,
  y = max_y_array,
  mode = 'lines',
  fill = None,
  line = dict(
        color='rgb(66, 134, 244)',
  ),
  name = 'Max'
)

low = go.Scatter(
  x = min_max_x_array,
  y = min_y_array,
  mode = 'lines',
  fill ='tonexty',
  line=dict(
        color='rgb(66, 134, 244)',
  ),
  name = 'Min'
)

data = [high, low, pi, trace]

layout = go.Layout(
    xaxis = dict(
        type = 'log',
        autorange = True
    ),
    yaxis = dict(
        type = 'log',
        autorange = True
    )
)

fig = go.Figure(data = data, layout = layout)
plot(fig, filename = 'monteCarlo.html')
