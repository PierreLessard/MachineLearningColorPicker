import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import pickle


def open_batch_data(filename):
    with open (filename, 'rb') as fp:
        batch_data = pickle.load(fp)
        return(batch_data)

def overwrite_model_file():
    with open('color_model.pkl', 'wb') as output:  # Overwrites any existing file.
        pickle.dump(model, output, pickle.HIGHEST_PROTOCOL)
        print("file overwrited")

colors = open_batch_data('batch_data_color.txt')
rgb = open_batch_data('batch_data_rgb.txt')
print(len(rgb))
#do not un-comment unless model is to be retrained

model=MLPClassifier(alpha=0.01, batch_size=932, epsilon=1e-08, hidden_layer_sizes=(300,), learning_rate='adaptive', max_iter=500)

model.fit(rgb, colors)
accuracy = 0
while accuracy < .87:
    model.fit(rgb, colors)

    rgb_pred = model.predict(rgb)
    accuracy=accuracy_score(y_true=colors, y_pred=rgb_pred)
    print(accuracy)

#overwrite_model_file()