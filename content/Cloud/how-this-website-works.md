Title: How this website works
Author: Giuseppe
Tags: markdown, Pelican, Docker, github

After many years on Wordpress I decided to move my website to a static website.

I decided to adopt [Pelican](http://blog.getpelican.com/): a static website builder based on python and supporting reStructuredText, Markdown, or AsciiDoc.

Moreover I decided to use [GitHub](https://pages.github.com/) pages to host the website.

The [pdf plugin](https://github.com/pbertera/www.bertera.it/blob/master/plugins/cv_pdf/__init__.py) comes from [Cyrille Rossant](http://cyrille.rossant.net/pelican-github/).

#### Docker

In order to maintain a clean approach I use a self-contained Docker container.

The Docker image is automatically build on [Docker hub] .

#### The manage script

The [manage.sh](https://github.com/pbertera/www.bertera.it/blob/master/manage.sh) is a wrapper around the `docker run` command the script accepts all the valid [Makefile] target plus the `deploy`, `build` and `update`. The first argument will deploy the website into the `gh-pages` branch, the second one creates the Docker image. The `update` argument is the same of `make html && make serve` inside of the container
