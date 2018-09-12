import pandas
import sklearn.linear_model
import matplotlib.pyplot
#
# read data
dataframe = pandas.read_fwf('../data/brain-body.txt')
x_values = dataframe[['brain']]
y_values = dataframe[['body']]
#
# train model on data
body_reg = sklearn.linear_model.LinearRegression()
body_reg.fit(x_values, y_values)
#
# visualize results
matplotlib.pyplot.scatter(x_values, y_values)
matplotlib.pyplot.plot(x_values, body_reg.predict(x_values))
matplotlib.pyplot.show()
