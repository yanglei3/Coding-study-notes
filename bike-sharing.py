import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

#Load data, observation. rides
data_path = 'Bike-Sharing-Dataset/hour.csv'
rides = pd.read_csv(data_path) 
rides.head()
rides[:24*10].plot(x='dteday', y='cnt')

#Data preparation, rides-data-(test_data, data)-(features, targets)-(test_, train_, val_)
dummy_fields = [’season’, ‘weathersit’, ‘mnth’, ‘hr’, ‘weekday’]
for each in  dummy_fields:
        dummies = pd.get_dummies(rides[each], prefix = each, drop_first = False)
        rides = pd.concat([rides, dummies], axis = 1)
fields_to_drop = [‘instant’, ‘dteday’, ‘season’, ‘weathersit’, ‘weekday’, ‘atemp’, ‘mnth’, ‘workingday’, ‘hr’]
data = rides.drop(fields_to_drop, axis = 1)
data.head()
quant_feature = ['casual', 'registered', 'cnt', 'temp', 'hum', 'windspeed']
scaled_feature = {}
for each in quant_feature:
	mean, std = data[each].mean(), data[each].std()
	scaled_feature[each]=[mean, std]
	data.loc[:, each] = (data[each] - mean) / std
test_data = data[-21 * 24:]
data = data [: -21 * 24]
target_fields = ['cnt', 'casual', 'registered']
features, targets = data.drop(target_fields, axis = 1), data[target_fields]
test_features, test_targets = test_data.drop(target_fields, axis = 1), test_data[target_fields]
train_features, train_targets = features[: -60*24], targets[: -60*24]
val_features, val_targets = features[-60*24:], targets[-60*24:]

#NN building
Class NeuralNetwork(object):
	def__init__(self, input_nodes_n, hidden_nodes_n, output_nodes_n, learning_rate):
		self.input_nodes_n = input_nodes_n
		self.hidden_nodes_n = hidden_nodes_n
		self.output_nodes_n = output_nodes_n
		self.weights_input = np.random.normal(0.0, self.input_nodes_n**-0.5, (self.input_nodes_n, self.hidden_nodes_n))
		self.weights_hidden = np.random.normal(0.0, self.hidden_nodes_n**-0.5, (self.hidden_nodes_n, self.output_nodes_n))
		self.lr = learnin_rate
		self.activation_function = lambda x : 1 / (1 + np.exp(-x))
