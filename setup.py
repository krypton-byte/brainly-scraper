
from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))

setup(
  name = 'brainly_scraper',        
  packages = ['brainly_scraper'],   
  version = '0.0.1',    
  license='MIT',     
  description = 'brainly scraper', 
  author = 'Krypton Byte',                  
  author_email = 'galaxyvplus6434@gmail.com',     
  url = 'https://github.com/krypton-byte/brainly-scraper',   
  download_url = 'https://github.com/krypton-byte/brainly-scraper/archive/0.0.1.tar.gz',    
  keywords = ['brainly', 'scraper'], 
  install_requires=[           
          'requests',
          'html_text'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)