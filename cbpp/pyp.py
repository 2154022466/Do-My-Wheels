# -*- coding=utf-8 -*-

__author__ = 'XF'
__date__ = '2022/03/10'

'The script is to create a basic python project.'

# built-in library
import os
import os.path as osp
from re import search
import sys

# third-party libraty

# self-defined library
from configs import ROOT_DIR, BASIC_DIRS, BASIC_FILES, TEMPALTE_FILE_DIR, DIR_PATTERN, SHOHT_LINE, FOUR_SPACE


def tree_structure(sub, dir_structure):

    if sub is None:
        return []

    (begin, end) = search(DIR_PATTERN, sub).span()

    first_sub = sub[begin: end]
    if len(sub) > end + 1:
        other_sub = sub[end + 1:]
    else:
        other_sub = None

    for exist_dir in dir_structure:
        if len(exist_dir) == 0:
            return [first_sub, tree_structure(other_sub, [[]])]
        elif exist_dir[0] == first_sub:
            return [first_sub, tree_structure(other_sub, exist_dir[1:])]

def print_tree_structure(dir_structure, height=0):

    if len(dir_structure) == 0:
        pass
    else:

        prefix = ''.join([FOUR_SPACE for _ in range(height)]) + SHOHT_LINE
        print('%s %s' % (prefix, dir_structure[0]))
        for sub_dir in dir_structure[1:]:
            print_tree_structure(sub_dir, height + 1)
            

if __name__ == '__main__':

    project_name = None
    dir_structure = None
    project_dir = ROOT_DIR
    try:
        project_name = sys.argv[1]   
    except Exception as e:
        raise Exception('project name need to be provided!')

    try:
        project_dir = sys.argv[2]
    except Exception as e:
        print('The project will be created in the current path.')

    # create project working dir
    project_path = osp.join(project_dir, project_name)
    os.makedirs(project_path)
    dir_structure = [project_name, []]

    # create basic dir
    for _dir in BASIC_DIRS:
        dir_structure.append(tree_structure(_dir, dir_structure[1:]))
        os.makedirs(osp.join(project_path, _dir))

    # create basic file
    for _file in BASIC_FILES:
        with open(osp.join(project_path, _file), mode='wb') as fw:
            try:
                fr = open(osp.join(TEMPALTE_FILE_DIR, _file), mode='rb')
            except FileNotFoundError:
                dir_structure.append(tree_structure(_file, dir_structure[1:]))
                pass
            else:
                fw.write(fr.read())
                dir_structure.append(tree_structure(_file, dir_structure[1:]))

    # print tree-shaped working dir
    print('Working Dir: %s:' % (project_path))
    print_tree_structure(dir_structure)
    print('Create is OK!')

    pass
