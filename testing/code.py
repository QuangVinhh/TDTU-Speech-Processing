import os
import numpy as np
from hmmlearn.base import BaseHMM
from hmmlearn import hmm
import librosa
from librosa.feature import mfcc
import warnings
warnings.filterwarnings('ignore')

#-----
def get_mfcc(dir):
    input_data, sample_rate =  librosa.load(dir)
    features = mfcc(input_data, sample_rate )
    return features

#-----
def get_dataset(dir):
    files_train = [f for f in os.listdir(dir+"train/") if os.path.splitext(f)[1] == '.wav']
    files_test = [f for f in os.listdir(dir+"test/") if os.path.splitext(f)[1] == '.wav']
    dataset_train = {}
    dataset_test = {}
    
    for fileName in files_train:
        label = fileName.split('_')[0]
        feature = get_mfcc(dir+"train/"+fileName).T

        if label not in dataset_train.keys():
            dataset_train[label] = []
            dataset_train[label].append(feature)
        else:
            dataset_train[label].append(feature)

    for fileName in files_test:
        label = fileName.split('_')[0]
        feature = get_mfcc(dir+"test/"+fileName).T

        if label not in dataset_test.keys():
            dataset_test[label] = []
            dataset_test[label].append(feature)
        else:
            dataset_test[label].append(feature)
    
    return dataset_train,dataset_test

#-----
def HMM_train(dataset):
    Models = {}
    for label in dataset.keys():
        model = hmm.GaussianHMM()
#         model = BaseHMM()
        trainData = dataset[label]
        trData = np.vstack(trainData)
        model.fit(trData)
        Models[label] = model
    return Models

#-----
dir = 'data/'
print('Data loading started')
dataset_train,dataset_test = get_dataset(dir)
print(dataset_train.keys())


print('Training HMM')
hmmModels = HMM_train(dataset_train)

print('Predicting')
acc_count = 0
all_data_count = 0
for label in dataset_test.keys():
    feature = dataset_test[label]
    for index in range(len(feature)):
        all_data_count+=1
        scoreList = {}
        for model_label in hmmModels.keys():
            model = hmmModels[model_label]
            score = model.score(feature[index])
            scoreList[model_label] = score
        predict = max(scoreList, key=scoreList.get)
        if predict == label:
            acc_count+=1

accuracy = ((acc_count/all_data_count)*100.0)

print("Accuracy: ",accuracy,"%")