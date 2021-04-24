from sklearn import svm
import pandas as pd
from canvasFile import *
from sklearn.model_selection import train_test_split
from sklearn import neural_network as nn

def trainModel():

    train_df = pd.read_csv("mnist_train.csv")
    test_df = pd.read_csv("mnist_test.csv")

    trainLabels = train_df['label']
    trainImages = train_df.drop('label', 1)

    model = nn.MLPClassifier(verbose=True, max_iter=100)
    '''unused model'''
    #model = svm.SVC()
    
    model.fit(trainImages, trainLabels)

    return model


def predictWithModel(model, image):
    ''' 
    models needs to be an sklearn model
    image needs to be flattened - reshape

    '''

    return model.predict(image)

if __name__ == "__main__":
    model = trainModel()
