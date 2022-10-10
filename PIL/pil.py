__author__ = 'XF'
__date__ = '2022/10/04'

'''
The script provides some plotting functions!
'''
import numpy as np
import time
from matplotlib import pyplot as plt


# self-defined library
from configs import default_args_point, default_args_line, default_args_lims, default_args_ticks, default_args_title, default_args_sphere, default_args_cube, default_args_bar


class PyImg(object):

    def __init__(self, x=None, y=None, z=None, rc=None, label=None, title=None, suffix='.pdf', save_img=False, 
                one_subplot=False, lim={'x': None, 'y': None, 'z': None}, ticks={'x': None, 'y': None, 'z':None}):

        self.x = x
        self.y = y
        self.z = z
        self.rc = rc
        self.label = label
        self.title = title
        self.suffix = suffix
        self.save_img = save_img
        self.lim = lim
        self.ticks = ticks
        self.one_subplot = one_subplot
        self.subplot_gate = True
    
        self.fig = plt.figure()
        # 设置子图之间的空隙
        plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.6, hspace=0.6)

    def _pen(self, brush='line', **kwargs):

        if self.label is None:
            self.label = [None for _ in range(len(self.x))]
        if self.title['title'] is None:
            self.title = {'title': [None for _ in range(len(self.x))]}
        if self.z is None:
            self.z = [None for _ in range(len(self.x))]
        if self.rc is None:
            self.r = int(np.sqrt(len(self.x)))
            self.c = int(len(self.x) / self.r)  + 1 if int(len(self.x) / self.r) * self.r < len(self.x) else int(len(self.x) / self.r)
        else:
            self.r = self.rc[0]
            self.c = self.rc[1]
        
        if self.one_subplot:
            self.r = 1
            self.c = 1

        for idx, (_x, _y, _z, _label, _title) in enumerate(zip(self.x, self.y, self.z, self.label, self.title['title'])):
            if _z is not None and self.subplot_gate:
                ax = self.fig.add_subplot(self.r, self.c, idx + 1, projection='3d')
                if self.one_subplot:
                    self.subplot_gate = False
            elif self.subplot_gate:
                ax = self.fig.add_subplot(self.r, self.c, idx + 1)
                if self.one_subplot:
                    self.subplot_gate = False

            if brush == 'line':
                pen = ax.plot
            elif brush == 'point':
                pen = ax.scatter
            elif brush == 'wireframe':
                pen = ax.plot_wireframe
            elif brush == 'surface':
                pen = ax.plot_surface
            elif brush == 'bar':
                pen = ax.bar
            else:
                raise Exception(f'Unknown pen [{brush}].')

            if _z is not None:
                pen(_x, _y, _z, label=_label, **kwargs)
            else:
                pen(_x, _y, label=_label, **kwargs)
            
            if _label is not None:
                ax.legend()
            if _title is not None:
                self.set_title(ax, _title)
            self.set_axes(ax)
        return ax
    
    def lines(self, **kwargs):

        ax = self._pen(brush='line', **kwargs)

        return ax

    def points(self, **kwargs):
        
        ax = self._pen(brush='point', **kwargs)

        return ax
    
    def circle(self, center, r, dense=100, **kwargs):

        t = np.linspace(0, np.pi, dense)
    
        x = center[0] + r * np.cos(t)
        y = center[1] + r * np.sin(t)
        self.x = [x, x]
        self.y = [y, -1 * y]
        self.one_subplot = True
        ax = self._pen(brush='line', **kwargs)
        ax.set_aspect('equal')
        # plt.gca().set_aspect(1)

        return ax

    def rectangle(self, lu, rd, **kwargs):
        '''
        lu: left upper point(x, y)
        rd: right down point(x, y)
        '''
        self.x = [
            [lu[0], lu[0], rd[0], rd[0], lu[0]]
        ]
        self.y = [
            [lu[1], rd[1], rd[1], lu[1], lu[1]]
        ]
        ax = self._pen(brush='line', **kwargs)
        ax.set_aspect('equal')

        return ax

    def sphere(self, center, r, dense=100, style='wireframe', lim_ratio = 1.1, **kwargs):

        t = np.linspace(0, np.pi * 2, dense)
        s = np.linspace(0, np.pi, dense)
        t, s = np.meshgrid(t, s)             # 生成稠密网格点
        x = center[0] + r * np.sin(s) * np.cos(t)    # 球面坐标公式
        y = center[1] + r * np.sin(s) * np.sin(t)
        z = center[2] + r * np.cos(s)
        self.x = [x]
        self.y = [y]
        self.z = [z]
        self.lim['x'] = [-1 * lim_ratio * r, lim_ratio * r]
        self.lim['y'] = [-1 * lim_ratio * r, lim_ratio * r]
        self.lim['z'] = [-1 * lim_ratio * r, lim_ratio * r]

        ax = self._pen(brush=style, **kwargs)
        ax.set_box_aspect((1, 1, 1))
        # plt.gca().set_box_aspect((1, 1, 1))

        return ax

    def cube(self, center, length, width, height, style='wireframe', dense=100, lim_ratio = 1.1, **kwargs):
        
        ax = self.fig.add_subplot(111, projection='3d')
        x = np.linspace(-0.5 * length, 0.5 * length, dense)
        y = np.linspace(-0.5 * width, 0.5 * width, dense)
        z = np.linspace(-0.5 * height, 0.5 * height, dense)

        if style == 'wireframe':
            pen = ax.plot_wireframe
        elif style == 'surface':
            pen = ax.plot_surface
        else:
            raise Exception(f'Unkonwn style [{style}].')

        xx, yy = np.meshgrid(x, y)
        pen(xx + center[0], yy + center[1], np.full_like(xx, -0.5 * height) + center[2], **kwargs)
        pen(xx + center[0], yy + center[1], np.full_like(xx,  0.5 * height) + center[2], **kwargs)
        
        xx, zz = np.meshgrid(x, z)
        pen(xx + center[0], np.full_like(xx, -0.5 * width) + center[1], zz + center[2], **kwargs)
        pen(xx + center[0], np.full_like(xx,  0.5 * width) + center[1], zz + center[2], **kwargs)

        yy, zz = np.meshgrid(y, z)
        pen(np.full_like(yy, -0.5 * length) + center[0], yy + center[1], zz + center[2], **kwargs)
        pen(np.full_like(yy,  0.5 * length) + center[0], yy + center[1], zz + center[2], **kwargs)

        self.lim['x'] = [-0.5 * lim_ratio * length + center[0], 0.5 * lim_ratio * length + center[0]]
        self.lim['y'] = [-0.5 * lim_ratio * width + center[1],  0.5 * lim_ratio * width + center[1]]
        self.lim['z'] = [-0.5 * lim_ratio * height + center[2], 0.5 * lim_ratio * height + center[2]]
        self.set_axes(ax)
        ax.set_box_aspect((length, width, height))

        return ax

    def bar(self, y, **kwargs):

        self.y = y
        self.x = []
        for _y in self.y:
            self.x.append(list(range(len(_y))))
        ax = self._pen(brush='bar', **kwargs)
        return ax

    def set_axes(self, ax):

        if self.lim['x'] is not None:
            ax.set_xlim(self.lim['x'])
        if self.lim['y'] is not None:
            ax.set_ylim(self.lim['y'])

        if self.ticks['x'] is not None:
            ax.set_xticks(self.ticks['x'][0])
            ax.set_xticklabels(self.ticks['x'][1])
        if self.ticks['y'] is not None:
            ax.set_yticks(self.ticks['y'][0])
            ax.set_yticklabels(self.ticks['y'][1])
        
        if self.z is not None:
            if self.lim['z'] is not None:
                ax.set_zlim(self.lim['z'])
            if self.ticks['z'] is not None:
                ax.set_zticks(self.ticks['z'][0])
                ax.set_zticklabels(self.ticks['z'][1])
        
    def set_title(self, ax, _title):

        ax.set_title(_title, fontfamily=self.title['fontfamily'], 
                fontsize=self.title['fontsize'], y=self.title['y'], fontweight=self.title['fontweight'])

    def set_axes_left_upper(ax):
        '''
        setting the (0, 0) to left upper
        '''
        ax.xaxis.set_ticks_position('top')
        ax.invert_yaxis() 

    def show_save(self, save_img=False):
        if save_img:
            plt.savefig(generate_filename(self.suffix, timestamp=True), bbox_inches='tight')
        plt.show()


def generate_filename(suffix, *args, sep='_', timestamp=False):

    '''

    :param suffix: suffix of file
    :param sep: separator, default '_'
    :param timestamp: add timestamp for uniqueness
    :param args:
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

if __name__ == '__main__':

    x = np.linspace(0, 10, 100)
    y = 2 * x
    z = x

    X = [x, x]
    Y = [y, y]
    Z = [z, z]

    # points ================================
    # 2-d
    # pyimg = PyImg(X, Y, lim=default_args_lims, ticks=default_args_ticks, title=default_args_title)
    # pyimg.points(**default_args_point)
    # pyimg.show_save()
    # 3-d
    # pyimg = PyImg(X, Y, Z, lim=default_args_lims, ticks=default_args_ticks, title=default_args_title)
    # pyimg.points(**default_args_point)
    # pyimg.show_save()

    # lines =================================
    # 2-d
    # pyimg = PyImg(X, Y, lim=default_args_lims, ticks=default_args_ticks, title=default_args_title)
    # pyimg.lines(**default_args_line)
    # pyimg.show_save()
    # 3-d
    # pyimg = PyImg(X, Y, Z, lim=default_args_lims, ticks=default_args_ticks, title=default_args_title)
    # pyimg.lines(**default_args_line)
    # pyimg.show_save()

    # circle =================================
    # pyimg = PyImg(lim=default_args_lims, ticks=default_args_ticks, title=default_args_title)
    # pyimg.circle(center=(0, 0), r=1, **default_args_line)
    # pyimg.show_save()
    
    # rectangle =================================
    # pyimg = PyImg(lim=default_args_lims, ticks=default_args_ticks, title=default_args_title)
    # pyimg.rectangle(lu = (5, 10), rd=(10, 5), **default_args_line)
    # pyimg.show_save()

    # sphere =================================
    # pyimg = PyImg(lim=default_args_lims, ticks=default_args_ticks, title=default_args_title)
    # pyimg.sphere(center=(0, 0, 0), r=1, style='surface', **default_args_sphere) # style: wireframe/surface
    # pyimg.show_save()

    # cube ==================================
    # pyimg = PyImg(lim=default_args_lims, ticks=default_args_ticks, title=default_args_title)
    # pyimg.cube(center=(1, 2, 3), length=2, width=3, height=4, style='wireframe', **default_args_cube) # style: wireframe/surface
    # pyimg.show_save()

    # bar ===================================
    pyimg = PyImg(lim=default_args_lims, ticks=default_args_ticks, title=default_args_title)
    pyimg.bar(y=Y, **default_args_bar) # style: wireframe/surface
    pyimg.show_save()