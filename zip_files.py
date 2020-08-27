#!/usr/bin/python3
# -*- coding: utf-8 -*-
# mingzhe.xiang
# 2020/8/26 15:58
import os, sys
import zipfile


def zip_dir(target_dir=os.getcwd(), include_empty_dir=True):
    zip_file_name = target_dir + '.zip'
    parent_path = os.path.split(target_dir)[0]
    try:
        zip_file = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(target_dir):
            if root.startswith(os.path.join(target_dir, '.idea')):
                continue

            # 定义压缩目录起始
            new_file_path = root.replace(parent_path, '')
            new_file_path = new_file_path and new_file_path + os.sep

            # 压缩空目录
            if include_empty_dir and not dirs and not files:
                zip_file.write(os.path.join(root), new_file_path)
                continue
            # 压缩文件
            for file in files:
                zip_file.write(os.path.join(root, file), new_file_path + file)
    finally:
        if zip_file:
            zip_file.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        zip_dir(sys.argv[1], False)
    else:
        zip_dir()
