import matplotlib.pyplot as py
import pandas as px
from operator import itemgetter


def main():
    data = px.read_csv('dat.csv')
    tuples = [[row[col] for col in data.columns] for row in data.to_dict('records')]
    x = map(itemgetter(0), tuples)
    y = map(itemgetter(1), tuples)
    py.scatter(list(x),list(y), s= 1000)
    py.show()





if __name__ == '__main__':
    main()
