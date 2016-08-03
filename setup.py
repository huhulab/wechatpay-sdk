# -*- coding:utf-8 -*-

import sys

from distutils.core import setup
from wechatpay_sdk import __version__

setup(name='wechatpay-sdk',
      version=__version__,
      description='Wechat pay server side sdk',
      long_description='Wechat pay server side sdk',
      author='weet',
      author_email='thewawar@gmail.com',
      packages=['wechatpay_sdk'],
      package_dir={'wechatpay_sdk': 'wechatpay_sdk'},
      package_data={'wechatpay_sdk': ['wechatpay_sdk']},
      license="MIT",
      platforms=["any"],
      url='https://github.com/huhulab/wechatpay-sdk')
