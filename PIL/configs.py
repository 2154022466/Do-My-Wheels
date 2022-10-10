__author__ = 'XF'
__date__ = '2022/10/01'

'''
The configration files for the project.
'''

import os.path as osp


ROOT_DIR = osp.dirname(osp.abspath(__file__))


# basic settings
COLOR = ['orange', 'purple', 'gray', 'red', 'green', 'blue', 'black']
MARKER = {
    'point': '.',
    'pixel': ',',
    'circle': 'o',
    'triangle down': 'v',
    'triangle up': '^',
    'triangle left': '<',
    'triangle right': '>',
    'tripod down': '1',
    'tripod up': '2',
    'tripod left': '3',
    'tripod right': '4',
    'square': 's',
    'pentagon': 'p',
    'star': 's',
    'hexagon': 'h',
    'Hexagon': 'H',
    'diamand': 'd',
    'Diamand': 'D',
    'plus': '+',
    'multiple': 'x',
    'horizontal_line': '_',
    'vertical_line': '|'
}

# some settings for lines
LINE_STYLE = ['-', '--', '-.', ':']

default_args_point = {

    'color': COLOR[0],
    's': 1,
    'marker': list(MARKER.values())[2]
}

default_args_line = {
    
    'linestyle': LINE_STYLE[0],
    'color': COLOR[0],
    'linewidth': 1,
    # 'marker': list(MARKER.values())[2],
    # 'markerfacecolor': COLOR[1],
    # 'markersize': 1
}

default_args_lims = {

        'x': None,
        'y': None,
        'z': None
}

default_args_ticks = {

        'x': None, # ([0, 1000, 2000], ['0', '1k', '2k'])
        'y': None,
        'z': None
}

default_args_title = {

        'title': None,
        'y': -0.15,
        'loc': 'center',
        'fontfamily': 'Times New Roman',
        'fontweight': 'normal', # 0-1000, normal, bold
        'fontsize': 15,
}

default_args_sphere = {
        'rstride': 3, 
        'cstride': 3, 
        'color': COLOR[0],
        # 'cmap': 'autumn',
        'alpha': 0.5
    }

default_args_cube = {
        'rstride': 3, 
        'cstride': 3, 
        'color': COLOR[0],
        # 'cmap': 'autumn',
        'alpha': 0.5
    }

default_args_bar = {
    'width': 0.8,
    'bottom': 0,
    'align': 'center',
    'color': COLOR[0]
}