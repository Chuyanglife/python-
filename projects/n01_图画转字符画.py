# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 02:21:11 2022

@author: User
"""

from PIL import Image
from PIL import ImageDraw,ImageFont
import numpy as np
import os
import time

def timeit(func):
    """
    Decorator for measuring function's running time.
    """
    def measure_time(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        print("Processing time of %s(): %.2f seconds."
              % (func.__qualname__, time.time() - start_time))
        return result

    return measure_time

@timeit
def func():
    def img2char(img_path):

        im = Image.open(img_path) # 读取文件

        img_width = im.size[0] # 提取照片宽度
        img_height = im.size[1] # 提取照片高度

        pix = im.load() # 提取像素值（输出pixel对象）

        print("The width of original Image is: %d, the height is %d" % (img_width,img_height))

        # 创建图像大小的三维数组
        # 将数组内数值设为255 （空白图像）
        create_array = np.ndarray([img_height,img_width,3], np.uint8)
        create_array[:,:,:] = 255

        # 从数组创建图片
        create_img = Image.fromarray(create_array)

        # 创建要绘制的类和字符串

        chart = list("EVA this is Asuka ! ")
        font = ImageFont.truetype("arial.ttf", 15, encoding='unic')

        pix_count = 0 # 统计像素数量，初始值设为0
        sample_step = 5 # 采样步长，因为原始图片过大，不用每个像素都采。
        len_chart = len(chart) # 字符串长度
        Draw = ImageDraw.Draw(create_img) # 创建图片绘制对象

        for x in range(img_width):
            for y in range(img_height):
                if x % sample_step == 0 and y % sample_step == 0:

                    # 按像素和采样率，将字符串绘制入前面所创建的空白图像
                    Draw.text([x,y], chart[pix_count % len_chart], pix[x,y], font)
                    print(pix_count)

                    pix_count +=1
        # 保存图像
        create_img.save("C:\\Users\\Admin\\Downloads\\IG_poster2.png")

        return create_img

    img2char("C:\\Users\\Admin\\Downloads\\IG_poster.png")

if __name__ == "__main__":
    func()