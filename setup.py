#!/usr/bin/env python
# coding: utf-8
from setuptools import setup

from sentry_work_weixin import __version__


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='sentry_work_weixin',
    version=__version__,
    packages=['sentry_work_weixin'],
    url='https://github.com/EugeneLiu/sentry-work-weixin',
    author='Eugene Liu',
    author_email='eugene.liujing.zh@gmail.com',
    description='Plugin for Sentry which allows sending notification via Work Weixin messenger.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    entry_points={
        'sentry.plugins': [
            'sentry_work_weixin = sentry_work_weixin.plugin:WorkWeixinNotificationPlugin',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Bug Tracking',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: System :: Monitoring',
    ],
    include_package_data=True,
)