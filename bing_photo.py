# coding:utf-8

import urllib
import urllib.request
import requests
import os.path
import shutil
import fire
import ctypes


def save_img(img_url, dirname):
    try:
        if not os.path.exists(dirname):
            print('文件夹', dirname, '不存在，重新建立')
            os.makedirs(dirname)

        basename = os.path.basename(img_url)
        filepath = os.path.join(dirname, basename)

        urllib.request.urlretrieve(img_url, filepath)
    except IOError as e:
        print('文件操作失败', e)
    except Exception as e:
        print('错误 ：', e)

    print('Save: ' + filepath + ' successfully!')

    return filepath


def get_img_url(raw_img_url='https://area.sinaapp.com/bingImg/'):
    r = requests.get(raw_img_url)
    img_url = r.url
    print('img_url: ' + img_url)
    return img_url


def set_img_as_wallpaper(filepath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)


def resave_in_github_pages(filepath):
    github_img_path = '/Users/JiajieZhuo/Documents/Blog/img/background.jpg'
    shutil.copy(filepath, github_img_path)
    print('Copy image: ' + github_img_path + ' successfully!')


def download_bing_photo(dirname='/Users/JiajieZhuo/Documents/Python/BingPhoto'):
    img_url = get_img_url()
    filepath = save_img(img_url, dirname)
    resave_in_github_pages(filepath)
    # set_img_as_wallpaper(filepath)

if __name__ == '__main__':
    fire.Fire(download_bing_photo)
