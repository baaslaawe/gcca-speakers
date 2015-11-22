'''
Driver for performing generalized CCA on speech data

'''

from gcca import *

import os

if __name__ == '__main__':
    data_directory = 'data/speech/'

    data_locations = list()
    file_idx_location = None

    for file in os.listdir(data_directory):
        if file.startswith('JW') and file.endswith('.mat'):
            data_locations.append(os.path.join(data_directory, file))
        if file.endswith('fileidx.mat'):
            file_idx_location = os.path.join(data_directory, file)

    data_locations.sort()

    file_blocks = [1, 2, 3] # i.e. Use these blocks for training

    data_pre_processor = DataPreProcessor(data_locations, file_idx_location,
            file_blocks)
    training_data_per_view = data_pre_processor.process()

    gcca_model = GeneralizedCCA(training_data_per_view)
    G = gcca_model.solve()

