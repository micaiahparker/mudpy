from distutils.core import setup

setup(name='mudpy',
      version='',
      description='A Python MUD Framework',
      author='Micaiah Parker',
      author_email='me@micaiahparker.com',
      url='https://github.com/micaiahparker/mudpy',
      packages=['mudpy.build, mudpy.server, mudpy.make'],
      package_dir={'mudpy.build': 'src/build',
                   'mudpy.server': 'src/server',
                   'mudpy.make': 'src/make'},
      package_data={'mudpy.build': ['defaults/*.xml']},
      )

