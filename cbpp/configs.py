# -*- coding: utf-8 -*-
__author__ = 'XF'
__date__ = '2022/05/02'

'the configration file for cbpp'

# built-in library
import os.path as osp


ROOT_DIR = osp.dirname(osp.abspath(__file__))
TEMPALTE_FILE_DIR = osp.join(ROOT_DIR, 'templates')
DIR_SPLIT = '/'
DIR_PATTERN = r'[\w|\.]+'
SHOHT_LINE = '----'
FOUR_SPACE = '    '

BASIC_DIRS =[
    'core/tempDir',
    'tools',
    'data',
    'results',
    'log'
]

BASIC_FILES = [
    
    'main.py',
    'configs.py',
]

if __name__ == '__main__':
    pass