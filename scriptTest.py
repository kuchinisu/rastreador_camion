from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

imagen = Image.open("imgTest/fot_0.jpg")

imagen = imagen.convert('RGB')


input_data = np.array(imagen)
input_data.shape

plt.imshow(input_data/255)
plt.show()

