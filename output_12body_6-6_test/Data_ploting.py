import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text',usetex=True)
rc('text.latex', preamble=r'\usepackage{amsmath}')

print('Hello')

def making_plot(data_file):

    fig, (ax1)=plt.subplots(1,1, figsize=(10,5))
    sns.lineplot(ax=ax1, data=data_file)

    plt.savefig(f'plot.png', dpi=500)
    print('Plot is ready')
    plt.clf()
