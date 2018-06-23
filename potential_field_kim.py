# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def plot3d(U,xm,ym):
    # グラフ表示の設定
    fig = plt.figure(2,facecolor="w")
    ax = fig.add_subplot(111, projection="3d", axisbg="w")
    ax.tick_params(labelsize=15)    # 軸のフォントサイズ
    ax.set_xlabel("$x$", fontsize=30, fontname="Times New Roman")
    ax.set_ylabel("$y$", fontsize=30, fontname="Times New Roman")
    ax.set_zlabel("$U$", fontsize=30, fontname="Times New Roman")
    surf = ax.plot_surface(xm, ym, U, rstride=1, cstride=1,linewidth=1, antialiased=True, cmap=cm.jet)
    plt.show()


def main():
    # ポテンシャル場を求める範囲
    x = np.arange(-8, 8, 0.3)
    y = np.arange(0, 18, 0.3)
    xm, ym = np.meshgrid(x, y)

    # 障害物と壁の座標を取得
    o = np.loadtxt("obstacle.txt", delimiter=",")

    # ポテンシャル関数のパラメータ
    Uo, Ug = 0.0, 0.0    # ポテンシャルの初期化
    lo, lg = 1.0, 10.0   # パラメータ1(形状)
    co, cg =1.0, 3.0    # パラメータ2(重み)
    # 目標のポテンシャルを計算
    xg, yg = 4.0, 14.0          # 目標地の座標
    Ug = cg*(1-np.exp(-((xg-xm)**2+(yg-ym)**2)/lg**2))
    # 障害物のポテンシャルを計算
    for i in xrange(o.shape[0]):
        Uo = 0.0
        #Uo += co*np.exp(-((o[i][0]-xm)**2+(o[i][1]-ym)**2)/lo**2)
    # 各ポテンシャルの重ねあわせ
    U = (Uo/cg + 1)*Ug
    #print(np.gradient(U))

    a = np.array([0,1,2,3,4,5])
    #b = np.array([0.5,-1,0,1,-0.5])
    b = np.array([0.0,1,2,3,4])
    aa, bb = np.meshgrid(a,b)
    f = aa*bb
    print(f)
    print(np.gradient(f))
    (grad_f_x, grad_f_y) =np.gradient(f)
    print(grad_f_x)
    print(grad_f_y)

    plt.figure(1)
    plt.quiver(aa,bb,-grad_f_x, -grad_f_y,angles="xy",headwidth=3,scale=20,color="#444444")
    plt.xlim([-1, 7])
    plt.ylim([-1, 7])
    plt.grid()
    plt.legend()
    #plt.show()

    plot3d(f,aa,bb)
    #plot3d(grad_f,aa,bb)


    #print("U:")
    #print(U)


    # グラフの描画
    #plot3d(U,xm,ym)


if __name__ == '__main__':
    main()
