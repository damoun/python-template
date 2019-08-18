# -*- coding: utf-8 -*-

"""Console script for python_template."""
import sys

import click


@click.command()
def main(token):
    """Console script for icrawlerbot."""
    print('Hello World')
    return 0


if __name__ == "__main__":
    sys.exit(main())
