import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)

class TimeProfilerLogger(object):

    __instance = None

    @staticmethod
    def getInstance():
        if TimeProfilerLogger.__instance == None:
            TimeProfilerLogger()
        return TimeProfilerLogger.__instance

    def __init__(self):
        """ Virtually private constructor. """

        if TimeProfilerLogger.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            TimeProfilerLogger.__instance = self
            self.times = dict()

    def add_time(self, name, time):

        if name in self.times.keys():
            self.times[name].append(time)
        else:
            self.times[name] = list()
            self.times[name].append(time)

    def show_times(self):

        dataframe = pd.DataFrame.from_dict({ key:pd.Series(value) for key, value in self.times.items()})
        print(dataframe.describe())



