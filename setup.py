import setuptools

setuptools.setup(name='aiowrap',
                 version='0.1.1',
                 author='iceboy',
                 author_email='me@iceboy.org',
                 description=("Tools for wrapping existing synchronous "
                              "libraries into Python3's asyncio framework."),
                 license='http://www.apache.org/licenses/LICENSE-2.0',
                 keywords='asyncio greenlet wrap',
                 packages=['aiowrap'],
                 install_requires=['greenlet'])
