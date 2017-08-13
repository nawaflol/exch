#!/usr/bin/env python

""""A CLI application built using python to see currency exchange rates."""

import urllib.parse
import requests
import click

@click.command()
@click.option('--curr_from', '-f', default='USD', type=str,
              help='This the currency you are trying to convert from.',
              show_default=True)
@click.option('--curr_to', '-t', default='INR', type=str,
              help='This is the currency you\'re converting to.',
              show_default=True)
@click.option('--value', '-v', default=1, type=float,
              help='The amount you want to convert.')

def cli(curr_from, curr_to, value: float):
    """main function being called by Click"""

    #if curr_from == curr_to:
    #    click.echo("1.00")
    main_api = 'http://api.fixer.io/latest?'
    url = main_api + urllib.parse.urlencode({'base':curr_from})

    try:
        json_data = requests.get(url).json()
        output_ = "{} {} = {} {}".format(
            value, curr_from, json_data['rates'][curr_to] * value, curr_to)
        click.echo(output_)
    except requests.exceptions.ConnectionError:
        click.echo("Internet connection error.")
    except KeyError:
        click.echo("Unavailable currency.")
