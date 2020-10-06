import pandas as pd
import matplotlib.pyplot as plt
import os

color = ['blue', 'green', 'red', 'orange', 'purple']


def plot(data, titles, path, ylabels, ylims, marker, linestyle):
    _, (ax1, ax2) = plt.subplots(2, 1, figsize=(12.4, 7.2))


    ax1.set_title(titles[0])
    ax1.set_ylabel(ylabels[0])
    ax1.set_ylim(ylims[0])
    i_color = 0
    for c in data['Commodity'].unique():
        d = data[data['Commodity'] == c]
        ax1.plot(d['date'], d['Price'], color[i_color], label=c)
        i_color += 1
    ax1.legend(loc='upper right')

    i_color = 0
    ax2.set_title(titles[1])
    ax2.set_ylabel(ylabels[1])
    ax2.grid(True)
    ax2.set_ylim(ylims[1])
    for c in data['Commodity'].unique():
        d = data[data['Commodity'] == c]
        ax2.plot(d['date'], d['change'], color[i_color],
                 label=c, marker=marker, linestyle=linestyle)
        i_color += 1

    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.savefig(path)
    plt.clf()


def main():
    data = pd.read_csv('.\src\CommodityPrice.csv')
    data['date'] = [d.split('/', 1)[1] for d in data['Date']]
    data['change'] = [float(d[:-1]) for d in data['Change%']]
    data_price_1000 = data.query('Price>=1000')
    data_price_500_to_999 = data.query('Price>=500 & Price<1000')

    plot(data_price_1000, ['Commodity Price(>=1000)',
                           'Commodity Change%(>=1000)'], os.path.join('.\img\commodity price', 'terry_1000up.png'), ['Price', 'Change%'], [(1000, 3000), (-15, 15)], marker='*', linestyle='--')

    plot(data_price_500_to_999, ['Commodity Price(>=500 and <1000)',
                                 'Commodity Change%(>=500 and <1000)'], os.path.join('.\img\commodity price', 'terry_500to999.png'), ['Price', 'Change%'], [(500, 1000), (-5, 5)], marker='^', linestyle='-.')


if __name__ == "__main__":
    main()
