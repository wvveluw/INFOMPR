import pandas as pd
import matplotlib.pyplot as plt

mnist_data = pd.read_csv("data/mnist.csv").values

labels = mnist_data[:, 0]
digits = mnist_data[:, 1:]
img_size = 28
plt.imshow(digits[0].reshape(img_size, img_size))
plt.show()


print(mnist_data)
