from setuptools import setup, find_packages

setup(
    name='translator',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'translator.Web_Interface': ['templates/*', 'static/*'],
    },
    entry_points={
        'console_scripts': [
            'translator_transform=translator.command_line:run_transform_command',
            'translator_launch=translator.Web_Interface.web_interface:run_web_interface',
        ],
    },
    install_requires=[
        'flask'
        # Add other dependencies here
    ],
)