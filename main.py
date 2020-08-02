import os 
import base64
import click
import subprocess
from pandas.io import clipboard


@click.group()
def cli():
    """ToolBox"""
    pass

@cli.command("compress-file")
@click.argument("file")
def compress_file(file):
    """Compress file"""
    print('test')
    pass

@cli.command("email-manager")
@click.argument("email")
def compress_file():
    """Email Manager"""
    pass


@cli.command("url-checker")
@click.argument("url")
def compress_file(url):
    """Url Check For Spam"""
    pass

@cli.command("password-generator")
def compress_file():
    """Generate Password"""
    generated_password = base64.b64encode(os.urandom(65)).decode('utf-8')
    clipboard.copy(generated_password)
    return print(generated_password)

@cli.command("sys-stats")
@click.argument("stats")
def compress_file(stats):
    """Check system stats"""
    pass

if __name__ == "__main__":
    cli()