#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Giuseppe Perrone'
SITENAME = 'Giuseppe Perrone\'s Blog'
SITEURL = 'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = 'Something about ...'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
SITELOGO = '//s.gravatar.com/avatar/f64fc3d41c2a8368feff0b7672ca7571?s=120'
BROWSER_COLOR = '#ff3333'
PYGMENTS_STYLE = 'default'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

THEME = 'Flex'

STATIC_PATHS = ['static', 'pdfs', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

PLUGIN_PATHS = ['pelican-plugins', 'plugins']

# Organise the posts in folders per category
USE_FOLDER_AS_CATEGORY = True

# Pelican plugins:
PLUGINS = [# These plugins are part of the official `pelican-plugins` repo:
           #'summary',
           #'neighbors',
           # This one is a custom plugin:
           'cv_pdf',
           ]

DISQUS_SITENAME = "gperrone-it"

LINKS = ()

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/giuseppeperrone'),
          ('github', 'https://github.com/giuseppeperrone'),
          ('twitter', 'https://twitter.com/giuseppeperrone'),
          ('rss', '//bertera.it/feeds/all.atom.xml'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

DEFAULT_PAGINATION = 10
COPYRIGHT_YEAR = 2024

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
