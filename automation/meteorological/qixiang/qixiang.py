# -*- encoding:utf-8 -*-
"""
@File   :qixiang.py
@Time   :2021/2/22 9:49
@Author :Chen
@Software:PyCharm
"""
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter


def map_make(scale, box, xstep, ystep):
    ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
    a = (box[1] - box[0]) // xstep
    x_start = box[1] - a * xstep
    a = (box[3] - box[2]) // ystep
    y_start = box[3] - a * ystep
    ax.set_extent(box, crs=ccrs.PlateCarree())
    # ax.add_feature(cfeature.LAKES.with_scale(scale))
    # ax.add_feature(cfeature.OCEAN.with_scale(scale))
    # ax.add_feature(cfeature.RIVERS.with_scale(scale))
    # ax.add_feature(cfeature.LAND.with_scale(scale),lw=0.5)
    ax.add_feature(cfeature.COASTLINE.with_scale(scale), lw=2)
    ax.set_xticks(np.arange(x_start, box[1] + xstep, xstep), crs=ccrs.PlateCarree())
    ax.set_yticks(np.arange(y_start, box[3] + ystep, ystep), crs=ccrs.PlateCarree())
    # zero_direction_label用来设置经度的0度加不加E和W
    lon_formatter = LongitudeFormatter(zero_direction_label=False)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    # 添加网格线
    ax.grid()
    ax.outline_patch.set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
    ax.spines['bottom'].set_linewidth(2.5)  #设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2.5)  #设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2.5)  #设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2.5)  #设置上部坐标轴的粗细
    return ax


if __name__ == '__main__':
    plt.figure(figsize=(6, 3))
    ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
    ax.coastlines(resolution='110m')
    ax.gridlines()
    nc = Dataset(r'E:\qixiang\gfs190604.t12z.nc',  mode='r')
    # 获取每个变量的值
    # 经度
    lons = nc.variables['longitude'][:]
    # 纬度
    lats = nc.variables['latitude'][:]
    time = nc.variables['time'][:]

    # 经纬度平均值
    lon_0 = lons.mean()
    lat_0 = lats.mean()
    ax.set_xticks(np.arange(0, 361, 40), crs=ccrs.PlateCarree())
    ax.set_yticks(np.arange(-90, 90 + 30, 30), crs=ccrs.PlateCarree())
    # zero_direction_label用来设置经度的0度加不加E和W
    lon_formatter = LongitudeFormatter(zero_direction_label=False)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    ax.set_title('Night time shading for {}'.format(time))
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.LAKES, alpha=0.5)
    ax.add_feature(cfeature.RIVERS)
    # 放置背景图像以进行漂亮的海洋渲染。
    ax.stock_img()
    plt.show()
    # print(nc.variables.keys())
    # time = nc.variables['time'][:].data
    # print(time[:10])
    # for var in nc.variables.keys():
    #     data = nc.variables[var][:].data
    #     print(var, data.shape)