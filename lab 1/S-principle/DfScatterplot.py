from matplotlib import pyplot as plt


# class DfScatterplot containing a method for plotting the dataframe which can be modified without affecting the Df class
class DfScatterplot:
    def scatter(self, df, x, y):
        plt.scatter(df[x], df[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()
