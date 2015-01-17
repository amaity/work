import matplotlib.pyplot as plt
from plot_pdf import brnflow, trfflow, mybusdat, brn_trace, trn_trace, bus_trace

fig, ax = plt.subplots()

if __name__ == '__main__':
    brn_trace(brnflow)  
    trn_trace(trfflow)
    bus_trace(mybusdat)

    ax.set_xlim(0,410)
    ax.set_ylim(0,287)
    ax.axes.get_xaxis().set_visible(True)
    ax.axes.get_yaxis().set_visible(True)
    #ax.set_title('load flow plot')
    plt.text(300, 270, 'Damodar Valley Corporation', fontsize=12)
    plt.text(300, 265, 'Gen in MW,', fontsize=10)
    plt.text(327, 265, 'Brnchflow in MVA,', fontsize=10)
    plt.text(368, 265, 'Load in MVA', fontsize=10)
    plt.text(300, 260, '--400KV', color='red', fontsize=10)
    plt.text(320, 260, '--220KV', color='blue', fontsize=10)
    plt.text(340, 260, '--132KV', color='green', fontsize=10)
    plt.show()

    fig.set_size_inches(16.5,11.7)
    extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig("loadflow.pdf", bbox_inches=extent)
