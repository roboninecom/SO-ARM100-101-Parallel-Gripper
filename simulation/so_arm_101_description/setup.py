import os
from glob import glob

from setuptools import setup

package_name = 'so_arm_101_description'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml', 'LICENSE.md']),
        (os.path.join('share', package_name, 'meshes'), ['meshes/LICENSE.md']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'meshes', 'visual'), glob('meshes/visual/*')),
        (os.path.join('share', package_name, 'meshes', 'collision'), glob('meshes/collision/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Robonine',
    maintainer_email='hello@robonine.com',
    description='SO-ARM-101 robot description with multi-simulator support',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publish_mujoco_description = '
            'so_arm_101_description.publish_mujoco_description:main',
        ],
    },
)
