import click, os, json, requests
from components.fun import CLI
from colorama import (init, Fore, Back, Style)
import pyfiglet

init(autoreset=True)

version = '1.0.0'

msg = pyfiglet.figlet_format("CLI\nHospital-SDLG", font="slant")

@click.group()
@click.version_option(version=version, message=f"{Fore.CYAN + msg + Style.RESET_ALL}\nVersion: {Fore.YELLOW + version + Style.RESET_ALL}\nAPI: {Fore.YELLOW + 'http://localhost:8000' + Style.RESET_ALL}", show_choices=True)
def main():
    pass

@main.command()
@click.option('--id', '-i', type=int, required=True, help='ID del usuario')
def get_user_by_id(id:int):
    try:
        data = CLI.get_user_by_id(id)
        click.echo(data.tabla())
    
    except Exception as e:
        click.echo(e)

@main.command()
@click.option('--limit', '-l', type=int, required=False, help='Limite de usuarios')
@click.option('--offset', '-o', type=int, required=False, help='Offset de usuarios')
def get_users(limit:int, offset:int):
    try:
        data = CLI.get_users_data({'limit':limit, 'offset':offset} if limit and offset else None)
        click.echo(data)
    
    except Exception as e:
        click.echo(e)
        

if __name__ == '__main__':
    main()