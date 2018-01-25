# -*- coding:utf-8 -*-
import os
import math
from PIL import Image

def splitimage(src, colwidth, rowheight, dstpath):
    img = Image.open(src)
    w, h = img.size
    rownum = math.ceil(h / rowheight)
    colnum = math.ceil(w / colwidth)
    if rownum <= h and colnum <= w:
        print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
        print('开始处理图片切割, 请稍候...')

        s = os.path.split(src)
        if dstpath == '':
            dstpath = s[0]
        fn = s[1].split('.')
        basename = fn[0]
        ext = fn[-1]

        num = 0
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, h - (r+1) * rowheight, (c + 1) * colwidth, h - (r) * rowheight)
                p = dstpath + "/" + basename + '_' + str(r + 1) + '_' + str(c + 1) + '.' + ext
                img.crop(box).save(p, "jpeg")
                num = num + 1

        print('图片切割完毕，共生成 %s 张小图片。' % num)
    else:
        print('不合法的行列切割参数！')

src = input('input path:')
if os.path.isfile(src):
    dstpath = input('请输入图片输出目录（不输入路径则表示使用源图片所在目录）：')
    if (dstpath == '') or os.path.exists(dstpath):
        splitimage(src, 512, 512, dstpath)
    else:
        print('图片输出目录 %s 不存在！' % dstpath)
else:
    print('图片文件 %s 不存在！' % src)