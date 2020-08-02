import click

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
def compress_file(email):
    """Email Manager"""
    pass


@cli.command("url-checker")
@click.argument("url")
def compress_file(url):
    """Url Check For Spam"""
    pass

@cli.command("password-generator")
@click.argument("password")
def compress_file(password):
    """Generate Password"""
    pass

@cli.command("sys-stats")
@click.argument("stats")
def compress_file(stats):
    """Check system stats"""
    pass

if __name__ == "__main__":
    cli()