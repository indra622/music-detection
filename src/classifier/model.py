# from keras.models import Sequential
# from keras.layers import Dense
import keras
import numpy as np
from .prepareData import Classifier_dataset

class MusicClassifier:
    """
    This class is used for applying the exist model to the project
    It has to be loaded from a existing model (file or keras model object)
    You can retrain 

    _model : keras model loaded from .h5 file
    _dataset : instance of classifier_dataset, contains info of dataset
    _result : result of model prediction
    """


    def __init__(self, filename):
        """
        init from keras model obj
        """
        self._model = keras.models.load_model(filename)

    def loadModel(self, filename, type = 'w'):
        """
        type:
            'm' : whole model
            'l' : model's layer params
            'w' : model's weight

        right now only support .h5 file
        """
        if type == 'w':
            self._model = keras.models.load_model(filename)

        return self._model

    def getDataInfo(self, filename):
        """
        get the basic infomation of dataset
        """
        data_set = Classifier_dataset(filename)
        dataColRanges = ('1-ZCRm', '34-ChromaDeviationm')
        labelCol = 'class'
        data_set.divideLabelAndData(dataColRanges, labelCol)
        data_set.generateMapping()
        self._dataset = data_set
        

    

    # def trianModel(self, filename):
    #     """
    #     Load .h5 file, extract the model

    #     """
    #     frame_data = MusicClassifier(filename)
    #     # self._dataset = 
    #     pass


    
    
    def saveModel(self, filename, type = 'm'):
        """
        type:
            'm' : whole model
            'l' : model's layer params
            'w' : model's weight

        .h5 is auto added
        layer param is json file
        """
        # if type == 'l':
        #     self._model.to_json()
        # elif type == 'w':
        #     self._model.save_weights(filename + 'h5')
        # elif type == 'm':
        #     self._model.save(filename + 'h5')
        # else:
        #     print("wrong type")
        #     return
        pass



    def predict(self, data):
        """
        data is the output of last layer of model, ndarray
        """
        softmax_o = self._model.predict(data)
        max_ele = max(softmax_o)
        ohk_out = np.where(softmax_o >= max_ele, 1, 0)
        result = self._dataset.one_hot_key_decode(ohk_out)
        self._result = result
        print("Huh, this file sounds like " + result)
        return result

    def detect(self, data):
        """
        data is the output of last layer of model, ndarray
        """
        for datum in data:
            softmax_o = self._model.predict(datum)
            max_ele = max(softmax_o)
            ohk_out = np.where(softmax_o >=max_ele, 1, 0)
            result = self._dataset.one_hot_key_decode(ohk_out)
            print(result)
            #print(ohk_out)
            #print(ohk_out.shape)
            
            if result == 1:
                print("Music contained")
                return True
            #ohk_out = np.where(softmax_o >= 0.4 , 1, 0)
            #for ele in ohk_out[0]:
            #    if ele == 1:
            #        print("Music contained")
            #        return True
            #    else:
            #        continue
        
        return False
                
    def predict_softmax(self, data):
        """
        data is the output of last layer of model, ndarray
        """
        
        results = []
        for datum in data:
            #print(type(np.array(datum)))
            dd = np.array(datum).reshape(1,34)
            softmax_o = self._model.predict(dd)
            softmax_o = softmax_o[0]
            max_ele = max(softmax_o)
            #print(max_ele)
            ohk_out = np.where(softmax_o >= max_ele, 1, 0)
            #ohk_out = np.where(softmax_o >=0.8, 1, 0)
            #print(ohk_out)
            result = self._dataset.one_hot_key_decode(ohk_out)
            print(result)
            results.append(result)
            #ohk_out.flatten()
            #print(ohk_out)
            #re
            #print(ohk_out.shape)
            
            #if ohk_out[0][0] == 1:
            #    print("Music contained")
            #    return True
            
            
        return results




if __name__ == "__main__":
    # filename = "./example.h5"
    # a = MusicClassifier.loadModel(filename)

    # example = np.random.random_sample(23)
    # a.predict(example)
    # b = MusicClassifier(model)
    pass
    