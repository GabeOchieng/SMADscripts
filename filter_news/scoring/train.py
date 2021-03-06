import os
import sys
DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(DIR)))
from ml_utils import load_data
from ml_utils import train


def main(data, train_data, test_data):

    train_text, train_labels, test_text, test_labels = load_data(data, train_data, test_data, text_key='article', id_key=['source', 'source_index'])
    train(train_text, train_labels, test_text, test_labels)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("\nUsage: \n\tpython train.py DATA TRAIN TEST\n\n\t"
              "DATA: source chr(1)-separated .csv file that contains all metadata"
              "\n\tTRAIN: .json file with train labels"
              "\n\tTEST: .json file with test labels"
              "\n\nExample:"
              "\n\tpython train.py ../test_in.csv examples/train_labels.json examples/test_labels.json\n")
    else:
        main(*sys.argv[1:])
