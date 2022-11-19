import matplotlib.pyplot as plt
import numpy as np
loss_gru = np.loadtxt("loss_gru.txt")
loss_lstm = np.loadtxt("loss_lstm.txt")
loss_gru = loss_gru.astype(np.float)
loss_lstm = loss_lstm.astype(np.float)
two_loss = np.vstack((loss_gru, loss_lstm))
plt.xlabel("Iteration")
plt.ylabel("Loss (CrossEntropyLoss)")
plt.title("MNIST Learning curve for LSTM and GRU")
plt.plot(two_loss.T[:,0],label="GRU")
plt.plot(two_loss.T[:,1], label="LSTM")
plt.legend()
plt.show()
