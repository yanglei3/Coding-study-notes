import numpy as np

#NN building
Class NeuralNetwork(object):
        def __init__(self, input_nodes_n, hidden_nodes_n, output_nodes_n, learning_rate):
                self.input_nodes_n = input_nodes_n
                self.hidden_nodes_n = hidden_nodes_n
                self.output_nodes_n = output_nodes_n
		self.weights_input = np.random.normal(0.0, self.input_nodes_n**-0.5, (self.input_nodes_n, self.hidden_nodes_n))
                self.weights_hidden = np.random.normal(0.0, self.hidden_nodes_n**-0.5, (self.hidden_nodes_n, self.output_nodes_n))
                self.lr = learnin_rate
                self.activation_function = lambda x : 1 / (1 + np.exp(-x))
	
	def forward_pass(self, X):
		

	def train(self, features, targets):
		n_records = features.shape[0]
		delta_weights_i_h = np.zeros(self.input_nodes_n.shape)
		delta_weights_h_o = np.zeros(self.hidden_nodes_n.shape)
		for x, y in zip(features, targets):
		final_outputs, hidden_outputs = self.forward_pass_train(X)

				









		
