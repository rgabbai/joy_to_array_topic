from setuptools import setup

package_name = 'joy_to_array_topic'

setup(
    name=package_name,
    version='0.0.2',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Rony Gabbai',
    maintainer_email='rony.gabbai@gmail.com',
    description='Translate Joy topic to topic type:std_msgs/msg/Float64MultiArray ',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'joy_to_array_node = joy_to_array_topic.joy_to_array_node:main',
        ],
    },
)
