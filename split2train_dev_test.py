import argparse
import os
import random
from shutil import copyfile

def split2train_dev_test(source_dir, target_dir, train_r, dev_r, test_r):
    os.mkdir(target_dir)
    
    train_path = os.path.join(target_dir, 'train')
    dev_path = os.path.join(target_dir, 'dev')
    test_path = os.path.join(target_dir, 'test')
    
    os.mkdir(train_path)
    os.mkdir(dev_path)
    os.mkdir(test_path)
    
    dir_list = os.listdir(source_dir)
    
    for file in dir_list:
        r_value = random.random()
        if r_value < train_r:
            copyfile(os.path.join(source_dir, file), os.path.join(train_path, file))
        elif r_value < train_r + dev_r:
            copyfile(os.path.join(source_dir, file), os.path.join(dev_path, file))
        else:
            copyfile(os.path.join(source_dir, file), os.path.join(test_path, file))

parser = argparse.ArgumentParser(description='split items in source_dir to train, dev, test 3 sub_dir in the target_dir')
parser.add_argument('source_dir')
parser.add_argument('target_dir')
parser.add_argument('train_r', type=float)
parser.add_argument('dev_r', type=float)
parser.add_argument('test_r', type=float)
args = parser.parse_args()

split2train_dev_test(args.source_dir, args.target_dir, args.train_r, args.dev_r, args.test_r)
