from DfScatterplot import DfScatterplot


# class Df which contains a call to class DfScatterplot, which plots the dataframe
class Df:
    def __init__(self, df):
        self.df = df
        self.plot = DfScatterplot()

    # Respects Single Responsibility Principle
    def scatter(self, col1, col2):
        self.plot.scatter(df=self.df, x=col1, y=col2)
