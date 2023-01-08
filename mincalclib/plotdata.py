##import matplotlib.pyplot as plt ## 2 nov

##plt.style.use('seaborn-whitegrid') 2 nov
##import seaborn as sns ##2 nov


#
#
#
# Year = [1,3,5,2,12,5,65,12,4,76,45,23,98,67,32,12,90]
# Profit = [80, 75.8, 74, 65, 99.5, 19, 33.6,23,45,12,86,34,567,21,80,34,54]
# data_plot = pd.DataFrame({"Year": Year, "Profit": Profit})
#
# sns.scatterplot(x="Year", y="Profit", data=data_plot)
# plt.show()
# x = np.linspace(0, 10, 30)
# y = np.sin(x)
# sns.relplot(x,y)

#
# plt.plot(x, y, 'o', color='black');
# plt.show()
#
# rng = np.random.RandomState(0)
# for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
#     plt.plot(rng.rand(5), rng.rand(5), marker,
#              label="marker='{0}'".format(marker))
# plt.legend(numpoints=1)
# plt.xlim(0, 1.8);
#
# plt.show()

# class plotdata:
#
#     def __init__(self):
#
#         return
#
#     def plotdata_min(self):
#         self.data1 = dataset.dataset.return_recalculated_data()
#         print("ciao")

def plot_scatter(pd_data):
    print("plot scatter")
    print("dati")
    print(pd_data)
    print("visti i dati?")
    ##sns.pairplot(pd_data, hue="Mineral", height=1.5)
    ##plt.show()

