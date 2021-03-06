from keras.models import Sequential
from keras.layers import Dense
from src.classifier.prepareData import Classifier_dataset


csvPath = "train_dnn.csv"
DNNPath = "data/model/youtube.h5"
dataColRanges = ('1-ZCRm', '34-ChromaDeviationm')
labelCol = 'class'
data_set = Classifier_dataset(csvPath)
label, data = data_set.prepareData(dataColRanges, labelCol, True)

data = data.astype(float)


# train a model here and save it in .h5 file
print("Construct the model")

Dnn = Sequential()
Dnn.add(Dense(50, activation='relu', input_dim = 34))
Dnn.add(Dense(50, activation='relu'))
Dnn.add(Dense(100, activation='relu'))
Dnn.add(Dense(50, activation='relu'))
# Dnn_3.add(Dense(100, activation='relu'))
# Dnn_3.add(Dense(100, activation='relu'))
# Dnn_3.add(Dense(50, activation='relu'))
Dnn.add(Dense(50, activation='relu'))
Dnn.add(Dense(23, activation = 'softmax'))

Dnn.compile(metrics=['accuracy'], optimizer='Adam', loss='mean_squared_error')

print("Start training")
Dnn.fit(data, label, validation_split = 0.0, epochs = 100, batch_size=100, shuffle = True)

# try training your own package!
Dnn.save(DNNPath)
