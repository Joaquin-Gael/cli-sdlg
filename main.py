import click, os, json, requests, subprocess
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
    
    except KeyboardInterrupt as stop:
        click.echo(f"\n{Fore.BLUE + Style.BRIGHT}Ejecución cancelada por el usuario.{Style.RESET_ALL} {Fore.RED}Ctrl + C{Style.RESET_ALL}")
    
    except Exception as e:
        click.echo(e)

@main.command()
@click.option('--limit', '-l', type=int, required=False, help='Limite de usuarios')
@click.option('--offset', '-o', type=int, required=False, help='Offset de usuarios')
def get_users(limit:int, offset:int):
    try:
        data = CLI.get_users_data({'limit':limit, 'offset':offset} if limit or offset else None)
        click.echo(data)
    
    except KeyboardInterrupt as stop:
        click.echo(f"\n{Fore.BLUE + Style.BRIGHT}Ejecución cancelada por el usuario.{Style.RESET_ALL} {Fore.RED}Ctrl + C{Style.RESET_ALL}")
    
    except Exception as e:
        click.echo(e)

@main.command()
@click.option('--id', '-i', type=int, required=True, help='ID del turno')
def get_turno_by_id(id:int):
    try:
        data = CLI.get_turno_by_id(id)
        click.echo(data.tabla())
    
    except KeyboardInterrupt as stop:
        click.echo(f"\n{Fore.BLUE + Style.BRIGHT}Ejecución cancelada por el usuario.{Style.RESET_ALL} {Fore.RED}Ctrl + C{Style.RESET_ALL}")
    
    except Exception as e:
        click.echo(e)

@main.command()
@click.option('--limit', '-l', type=int, required=False, help='Limite de turnos')
@click.option('--offset', '-o', type=int, required=False, help='Offset de turnos')
@click.option('--state', '-s', type=str, required=False, help='Estado del turno')
@click.option('--user_id', '-u', type=int, required=False, help='ID del usuario')
def get_turnos(limit:int, offset:int, state:str, user_id:int):
    try:
        data = CLI.get_turnos_data({'limit':limit, 'offset':offset, 'state':state, 'user_id':user_id} if limit or offset or state or user_id else None)
        click.echo(data)
    
    except KeyboardInterrupt as stop:
        click.echo(f"\n{Fore.BLUE + Style.BRIGHT}Ejecución cancelada por el usuario.{Style.RESET_ALL} {Fore.RED}Ctrl + C{Style.RESET_ALL}")
    
    except Exception as e:
        click.echo(e)

@main.command()
@click.option('--PORT', '-P', type=int, required=False, help='Port of the grafic interface Default 8000')
@click.option('--HOST', '-H', type=str, required=False, help='Host of the grafic interface Default 127.0.0.1')
def run_server(port, host):
    port = port if port else 8000
    host = host if host else "127.0.0.1"
    try:
        click.echo(f'\nURL: {Fore.YELLOW + f"http://{host}:{port}" + Style.RESET_ALL}')
        state = subprocess.run(
            ['streamlit', 'run', 'interface/main.py', '--server.port', str(port), '--server.address', str(host)],
            check=True
        )
        #click.echo(f'streamlit run interface/main.py --server.port {port} --server.address {host}')
        click.echo(state.stdout.decode())
    
    except subprocess.CalledProcessError as e:
        click.echo("Error al ejecutar Streamlit:")
        click.echo(e)
        click.echo(e.output)
    
    except KeyboardInterrupt as stop:
        click.echo(f"\n{Fore.BLUE + Style.BRIGHT}Ejecución cancelada por el usuario.{Style.RESET_ALL} {Fore.RED}Ctrl + C{Style.RESET_ALL}")
        

if __name__ == '__main__':
    main()