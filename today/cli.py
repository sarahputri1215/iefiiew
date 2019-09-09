import click
from today import __version__ as VERSION

def login():
    email = click.prompt("Enter Email:")
    password = click.prompt("Enter Passowrd:")
    
    

@click.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--version', is_flag=True, help="Gives the installed version of Today")
def main(verbose,version):
    if verbose:
        print('This is in verbose mode')
    if version:
        print(VERSION)
    remote_path = click.prompt("Enter UserName")
    login()
if __name__ == "__main__":
    main()