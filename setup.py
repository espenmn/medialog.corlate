from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='medialog.corlate',
      version=version,
      description="Corlate theme for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Medialog theme Plone bootstrap',
      author='Espen Moe-Nilssen',
      author_email='espen@medialog.no',
      url='http://github.com/espenmn/medialog.corrolate',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['medialog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          'collective.js.bootstrap',
          'z3c.jbot',
          'diazotheme.frameworks',
          'collective.themefragments',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
