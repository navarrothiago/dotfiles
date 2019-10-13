from src.efc2 import csv_reader
# #%pycat efc2/csv_reader.py
data = csv_reader.load_csv()
#data.head(data.shape[0])

data = data.drop("Unnamed: 0", 1)
data.head(data.shape[0])
columns = list(data)

plot_rows = int(len(columns) / 2)
if(len(columns) % 2 != 0):
    plot_rows = plot_rows + 1


print(plot_rows)
fig1, axs = plt.subplots(plot_rows, 2, constrained_layout=True, figsize=(20,30))

colors = ['red', 'green']
labels = data.label.unique
#data.hist(ax=axs, label=labels, bins=100);
_= data.loc[data['label'] == 1].hist(ax=axs, bins=100, label='1', color="royalblue", density = False, alpha = 0.7);
_= data.loc[data['label'] == 0].hist(ax=axs, bins=100,  label='0', color="orange", density = False,  alpha = 0.7);

## ---(Sat Oct 12 17:20:02 2019)---
from IPython.core.debugger import set_trace
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import pandas as pd
import matplotlib.pyplot as plt
import pdb;
from src.efc2 import csv_reader
# #%pycat efc2/csv_reader.py
ls
from IPython.core.debugger import set_trace
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import pandas as pd
import matplotlib.pyplot as plt
import pdb;
from src.efc2 import csv_reader
# #%pycat efc2/csv_reader.py
data = csv_reader.load_csv()
#data.head(data.shape[0])

data = data.drop("Unnamed: 0", 1)
data.head(data.shape[0])
from IPython.core.debugger import set_trace
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import pandas as pd
import matplotlib.pyplot as plt
import pdb;
columns = list(data)

plot_rows = int(len(columns) / 2)
if(len(columns) % 2 != 0):
    plot_rows = plot_rows + 1


print(plot_rows)
fig1, axs = plt.subplots(plot_rows, 2, constrained_layout=True, figsize=(20,30))

colors = ['red', 'green']
labels = data.label.unique
#data.hist(ax=axs, label=labels, bins=100);
_= data.loc[data['label'] == 1].hist(ax=axs, bins=100, label='1', color="royalblue", density = False, alpha = 0.7);
_= data.loc[data['label'] == 0].hist(ax=axs, bins=100,  label='0', color="orange", density = False,  alpha = 0.7);
f = plt.figure(figsize=(30, 30))
plt.matshow(data.corr(), fignum=f.number)

for (i, j), z in np.ndenumerate(data.corr()):
    plt.text(j, i, '{:0.1f}'.format(z), ha='center', va='center', color="r")


plt.xticks(range(data.shape[1]), data.columns, fontsize=14, rotation=45)
plt.yticks(range(data.shape[1]), data.columns, fontsize=14)

cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)

plt.title('Correlation Matrix', fontsize=16);
plt.margins(x=0, y=0);
import pandas as pd
import matplotlib.pyplot as plt
import pdb;
import numpy as np
f = plt.figure(figsize=(30, 30))
plt.matshow(data.corr(), fignum=f.number)

for (i, j), z in np.ndenumerate(data.corr()):
    plt.text(j, i, '{:0.1f}'.format(z), ha='center', va='center', color="r")


plt.xticks(range(data.shape[1]), data.columns, fontsize=14, rotation=45)
plt.yticks(range(data.shape[1]), data.columns, fontsize=14)

cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)

plt.title('Correlation Matrix', fontsize=16);
plt.margins(x=0, y=0);