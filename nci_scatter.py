# @author: Q. Liu, D. Yang
# @desc: Plot RDG vs sign(lambda2)rho scatter
# @date: 2020/1/13

import re
import sys
import numpy as np
import matplotlib.pyplot as plt


def ReadXSF(string):
    loop = True
    while loop:
        try:
            fname = input('input ' + string + ' grid data (*.xsf):\n')
            if fname.lower() == 'exit':
                loop = False
            f = open(fname, 'r')
            text = f.read()
            f.close()
            text = re.findall(
                r'BEGIN_DATAGRID_3D_\w+\n(.*)\nEND_DATAGRID_3D', text, re.S)
            text = text[0].split('\n')[5:]
            data = []
            for t in text:
                data += t.split()
            data = np.array(data, dtype=float)
            loop = False
        except BaseException:
            data = []
            loop = True
        if fname.lower() == 'exit':
            exit()
    return data


def PlotScatter(rho, rdg):
    if len(rho) != len(rdg):
        exit('data grid is not matched')
    plt.figure('NCI Scatter')
    index = np.where((rdg <= 2) & (abs(rho) <= 0.05), True, False)
    x = rho[index]
    y = rdg[index]
    plt.scatter(x, y, s=0.1, c=x, cmap='jet')
    plt.colorbar()
    plt.xlabel(r'$sign(\lambda_2)\rho$ (a.u.)')
    plt.ylabel(r'$RDG$')
    plt.xlim([-0.05, 0.05])
    plt.ylim([0, 2])
    plt.show()


def main():
    loop = True
    while loop:
        rdg = ReadXSF('RDG')
        rho = ReadXSF('sign(lambda2)rho')
        loop = (len(rdg) != len(rho))
        if loop:
            print('data grid is not matched')
        else:
            PlotScatter(rho, rdg)


if __name__ == '__main__':
    main()
