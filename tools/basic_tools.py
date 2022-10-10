# -*- coding: utf8 -*-

__author__ = 'XF'
__date__ = '2022/07/11'

'saving some tiny but useful functions that would be used frequently.'

# built-in library
import os
import os.path as osp
import time
import pickle
import json
from builtins import print as b_print

# third-party library
import pandas as pd
import torch as th


# 保存文件
def savefile(savepath, content):
    with open(savepath, "a", encoding='utf-8') as fp:
        fp.write(content)


# 读取文件
def readfile(path):
    with open(path, "r", encoding='utf-8') as fp:
        content = fp.read()
    return content


def obj_save(path, obj):

    if obj:
        with open(path, 'wb') as file:
            pickle.dump(obj, file)
    else:
        print('object is None!')


def obj_load(path):

    if os.path.exists(path):
        with open(path, 'rb') as file:
            obj = pickle.load(file)
        return obj
    else:
        raise OSError('no such path:%s' % path)


# xls to csv
def xls2csv(excel_path):

    data_xls = pd.read_excel(excel_path, index_col=0)
    csv_path = excel_path[0: excel_path.find('.')] + '.csv'
    data_xls.to_csv(csv_path, encoding='utf-8')
    print('xls->csv 转换完成')
    return csv_path


# 输出函数
def print(*args, file=None, end='\n'):

    with open(file=file, mode='a', encoding='utf-8') as console:
        b_print(*args, file=console, end=end)
    b_print(*args, end=end)


# 文件名自动生成
def generate_filename(suffix, *args, sep='_', timestamp=False):

    '''

    :param suffix: 文件后缀名
    :param sep: 文件名中的不同量之间的分隔符，默认为'_'
    :param timestamp: 是否需要在文件名中添加时间戳
    :param args: 其他需要在文件名中体现的值
    :return:
    '''

    filename = sep.join(args).replace(' ', '_')
    if timestamp:
        filename += time.strftime('_%Y%m%d%H%M%S')
    if suffix[0] == '.':
        filename += suffix
    else:
        filename += ('.' + suffix)

    return filename


# check a variable whether or not in a iterable element
def exist(elements, element):

    flag = False
    for e in elements:
        if e == element:
            flag = True
            break
    return flag


begining_line = '=============================== Begin ======================================='
ending_line =   '================================ End ========================================'
class Log(object):

    def __init__(self, log_dir, log_name):
        self.log_path = osp.join(log_dir, generate_filename('.txt', *log_name, timestamp=True))
        self.print(begining_line)
        self.print('date: %s' % time.strftime('%Y/%m/%d-%H:%M:%S'))
    
    def print(self, *args, end='\n'):

        with open(file=self.log_path, mode='a', encoding='utf-8') as console:
            b_print(*args, file=console, end=end)
        b_print(*args, end=end)
    
    @property
    def ending(self):
        self.print('date: %s' % time.strftime('%Y/%m/%d-%H:%M:%S'))
        self.print(ending_line)


def linux_command(command, info_file):

    assert isinstance(command, str)

    command = ' '.join([command, '>', info_file])

    os.system(command=command)


def new_dir(father_dir):

    new_path = osp.join(father_dir, time.strftime('%Y%m%d%H%M%S'))
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    return new_path


def save_checkpoint(checkpoint_dict, save_path, myprint=None):

    assert checkpoint_dict['model'] is not None
    default_checkpoint = {
        'model': None,
        'optimizer': None,
        'epoch': None,
        'min_loss': None,
        'best_epoch': None
    }
    default_checkpoint.update(checkpoint_dict)
    th.save(default_checkpoint, save_path)
    if myprint is not None:
        myprint(f'model save in [{save_path}]')
    else:
        print(f'model save in [{save_path}]')


def load_checkpoint(checkpoint_path, model, optimizer):

    model_ckpt = th.load(checkpoint_path)
    
    model.load_state_dict(model_ckpt['model'])
    optimizer.load_state_dict(model_ckpt['optimizer'])

    return model, optimizer, model_ckpt['epoch'] + 1, model_ckpt['min_loss'], model_ckpt['best_epoch']


def json_load(path):
    
    with open(path, 'r', encoding='utf8') as f:
        content = json.load(f)
    return content


def json_dump(path, dict_obj):

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(dict_obj, f, indent=4, ensure_ascii=False)