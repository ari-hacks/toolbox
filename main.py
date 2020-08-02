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
def email_manager():
    """Email Manager"""
    pass


@cli.command("url-checker")
@click.argument("url")
def url_checker(url):
    """Url Check For Spam"""
    pass

@cli.command("password-generator")
def pass_gen():
    """Generate Password"""
    #Add args for diff lengths 
    generated_password = base64.b64encode(os.urandom(65)).decode('utf-8')
    clipboard.copy(generated_password)
    return print(generated_password)

@cli.command("sys-stats")
@click.argument("stats")
def sys_stats(stats):
    """Check system stats"""
    pass

if __name__ == "__main__":
    cli()