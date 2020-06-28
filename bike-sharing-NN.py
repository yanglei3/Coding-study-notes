import numpy as np
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
