import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text',usetex=True)
rc('text.latex', preamble=r'\usepackage{amsmath}')

print('Hello')

def making_plot(data_file, x_axis=True, y_axis=True):

    fig, ((ax11, ax12, ax13))=plt.subplots(1,3, sharex=False, figsize=(12,5))
    sns.lineplot(ax=ax11, data=data_file)
    ax11.set_xlabel(r'$t$')
    #ax11.set_yscale('log')
    ax11.set_xlim(2000,10000)
    #ax11.set_ylim()

    sns.scatterplot(ax=ax12, x=x_axis, y=y_axis)
    ax12.set_xlabel(r'$\dot{M}$')
    ax12.set_ylabel(r'$\phi$')

    sns.kdeplot(ax=ax13, x=x_axis, fill=True)
    ax13.set_xlabel(r'$\dot{M}$')
    ax13.set_ylabel(r'$\rm Density$')
    ax13.set_xlim(0,500)

    plt.savefig(f'plot.png', dpi=500)
    print('Plot is ready')
    plt.clf()
