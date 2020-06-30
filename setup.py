import setuptools

setuptools.setup(
    name='launchd-tag',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/launchd-tag']
)
