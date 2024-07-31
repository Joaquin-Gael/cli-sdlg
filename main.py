import click, os, json, requests, subprocess
from components.fun import CLI
from colorama import (init, Fore, Back, Style)
import pyfiglet

init(autoreset=True)

version = '1.0.0'

msg = pyfiglet.figlet_format("CLI\nHospital-SDLG", font="slant")

@click.group()
@click.version_option(version=version, message=f"{Fore.CYAN + msg + Style.RESET_ALL}\nVersion: {Fore.YELLOW + version + Style.RESET_ALL}\nAPI: {Fore.YELLOW + 'http://127.0.0.1:8000' + Style.RESET_ALL}", show_choices=True)
def main():
    pass

@main.command()
@click.option('--nombre', '-n', type=str, required=True, help='Nombre del usuario')
@click.option('--email', '-e', type=str, required=True, help='Correo electrónico del usuario')
@click.option('--telefono', '-t', type=str, required=False, help='Teléfono del usuario')
@click.option('--dni', '-d', type=str, required=False, help='DNI del usuario')
def create_user(nombre: str, email: str, telefono: str, dni: str):
    data = {
        'nombre': nombre,
        'email': email,
        'telefono': telefono,
        'dni': dni
    }
    result = CLI.post_user(data)
    click.echo(result)

#Obtener usuarios por ID
@main.command()
@click.option('--userID', '-i', type=int, required=True, help='ID del usuario')
def get_user_by_id(id:int):
    try:
        data = CLI.get_user_by_id(id)
        click.echo(data.tabla())
    
    except Exception as e:
        click.echo(e)

@main.command()
@click.option('--userID', '-i', type=int, required=True, help='ID del usuario')
def delete_user(id: int):
    result = delete_user(id)
    click.echo(result)

@main.command()
@click.option('--userID', '-i', type=int, required=True, help='ID del usuario')
@click.option('--nombre', '-n', type=str, required=True, help='Nuevo nombre del usuario')
@click.option('--email', '-e', type=str, required=True, help='Nuevo correo electrónico del usuario')
def put_user(id: int, nombre: str, email: str):
    update_data = {'nombre': nombre, 'email': email}
    result = CLI.put_user(id, update_data)
    click.echo(result)


#Obtener todos los usuarios
@main.command()
@click.option('--limit', '-l', type=int, required=False, help='Limite de usuarios')
@click.option('--offset', '-o', type=int, required=False, help='Offset de usuarios')
def get_users(limit:int, offset:int):
    try:
        data = CLI.get_users_data({'limit':limit, 'offset':offset} if limit or offset else None)
        click.echo(data)
    
    except Exception as e:
        click.echo(e)
        
@main.command()
@click.option('--userID', '-i', type=int, required=True, help='ID del usuario')
@click.option('--nombre', '-n', type=str, required=False, help='Nuevo nombre del usuario')
@click.option('--apellido', '-a', type=str, required=False, help='Nuevo apellido del usuario')
@click.option('--fecha_nacimiento', '-f', type=str, required=False, help='Nueva fecha de nacimiento del usuario (YYYY-MM-DD)')
@click.option('--email', '-e', type=str, required=False, help='Nuevo correo electrónico del usuario')
@click.option('--telefono', '-t', type=str, required=False, help='Nuevo teléfono del usuario')
@click.option('--contraseña', '-p', type=str, required=False, help='Nueva contraseña del usuario')
@click.option('--is_admin', '-a', type=bool, required=False, help='Indica si el usuario es administrador')
def patch_user(id: int, nombre: str, apellido: str, fecha_nacimiento: str, email: str, telefono: str, contraseña: str, is_admin: bool):
    try:
        update_data = {}
        if nombre:
            update_data['nombre'] = nombre
        if apellido:
            update_data['apellido'] = apellido
        if fecha_nacimiento:
            update_data['fecha_nacimiento'] = fecha_nacimiento
        if email:
            update_data['email'] = email
        if telefono:
            update_data['telefono'] = telefono
        if contraseña:
            update_data['contraseña'] = contraseña
        if is_admin is not None:
            update_data['is_admin'] = is_admin
        
        if not update_data:
            click.echo('No se especificaron cambios para actualizar.')
            return

        response = CLI.patch_user(id, update_data)
        click.echo(f'Usuario actualizado con éxito: {response}')
    
    except Exception as e:
        click.echo(f'Error al actualizar el usuario: {e}')
        
#------------------------------------------------------------------------
@main.command()
@click.option('--userID', '-u', type=int, required=True, help='ID del usuario')
@click.option('--citaID', '-c', type=int, required=True, help='ID de la cita')
@click.option('--medicoID', '-m', type=int, required=True, help='ID del médico')
@click.option('--motivo', '-o', type=str, required=True, help='Motivo del turno')
@click.option('--estado', '-e', type=str, required=True, help='Estado del turno')
@click.option('--fecha', '-f', type=str, required=True, help='Fecha del turno en formato YYYY-MM-DD')
def create_turno(userID: int, citaID: int, medicoID: int, motivo: str, estado: str, fecha: str):
    data = {
        'userID': userID,
        'citaID': citaID,
        'medicoID': medicoID,
        'motivo': motivo,
        'estado': estado,
        'fecha': fecha
    }
    result = CLI.post_shift(data)
    click.echo(result)

@main.command()
@click.option('--turnoID', '-i', type=int, required=True, help='ID del turno')
def delete_turno(turnoID: int):
    """Elimina un turno por ID"""
    result = CLI.delete_shift(turnoID)
    click.echo(result)

@main.command()
@click.option('--turnoID', '-i', type=int, required=True, help='ID del turno')
@click.option('--motivo', '-o', type=str, required=False, help='Nuevo motivo del turno')
@click.option('--estado', '-e', type=str, required=False, help='Nuevo estado del turno')
@click.option('--fecha', '-f', type=str, required=False, help='Nueva fecha del turno en formato YYYY-MM-DD')
def patch_turno(turnoID: int, motivo: str, estado: str, fecha: str):
    update_data = {}
    if motivo:
        update_data['motivo'] = motivo
    if estado:
        update_data['estado'] = estado
    if fecha:
        update_data['fecha'] = fecha
    result = CLI.patch_shift(turnoID, update_data)
    click.echo(result)

@main.command()
@click.option('--turnoID', '-i', type=int, required=True, help='ID del turno')
@click.option('--userID', '-u', type=int, required=True, help='Nuevo ID del usuario')
@click.option('--citaID', '-c', type=int, required=True, help='Nuevo ID de la cita')
@click.option('--medicoID', '-m', type=int, required=True, help='Nuevo ID del médico')
@click.option('--motivo', '-o', type=str, required=True, help='Nuevo motivo del turno')
@click.option('--estado', '-e', type=str, required=True, help='Nuevo estado del turno')
@click.option('--fecha', '-f', type=str, required=True, help='Nueva fecha del turno en formato YYYY-MM-DD')
def put_turno(turnoID: int, userID: int, citaID: int, medicoID: int, motivo: str, estado: str, fecha: str):
    update_data = {
        'userID': userID,
        'citaID': citaID,
        'medicoID': medicoID,
        'motivo': motivo,
        'estado': estado,
        'fecha': fecha
    }
    result = CLI.put_shift(turnoID, update_data)
    click.echo(result)

@main.command()
@click.option('--turnoID', '-i', type=int, required=True, help='ID del turno')
def get_turno_by_id(id:int):
    try:
        data = CLI.get_turno_by_id(id)
        click.echo(data.tabla())
    
    except Exception as e:
        click.echo(e)

@main.command()
@click.option('--limit', '-l', type=int, required=False, help='Limite de turnos')
@click.option('--offset', '-o', type=int, required=False, help='Offset de turnos')
@click.option('--state', '-s', type=str, required=False, help='Estado del turno')
@click.option('--userID', '-u', type=int, required=False, help='ID del usuario')
def get_turnos(limit:int, offset:int, state:str, user_id:int):
    try:
        data = CLI.get_turnos_data({'limit':limit, 'offset':offset, 'state':state, 'user_id':user_id} if limit or offset or state or user_id else None)
        click.echo(data)
    
    except Exception as e:
        click.echo(e)

#------------------------------------------------------------------------

@main.command()
@click.option('--medicoID', '-m', type=int, required=True, help='ID del médico')
@click.option('--horarioID', '-h', type=int, required=True, help='ID del horario')
@click.option('--departamentoID', '-d', type=int, required=True, help='ID del departamento')
@click.option('--motivo', '-o', type=str, required=True, help='Motivo de la cita')
@click.option('--estado', '-e', type=str, required=True, help='Estado de la cita')
def create_cita(medicoID: int, horarioID: int, departamentoID: int, motivo: str, estado: str):
    data = {
        'medicoID': medicoID,
        'horarioID': horarioID,
        'departamentoID': departamentoID,
        'motivo': motivo,
        'estado': estado
    }
    result = CLI.post_appointment(data)
    click.echo(result)

@main.command()
@click.option('--citaID', '-i', type=int, required=True, help='ID de la cita')
def delete_cita(citaID: int):
    result = CLI.delete_appointment(citaID)
    click.echo(result)
    
@main.command()
@click.option('--citaID', '-i', type=int, required=True, help='ID de la cita')
@click.option('--motivo', '-o', type=str, required=False, help='Nuevo motivo de la cita')
@click.option('--estado', '-e', type=str, required=False, help='Nuevo estado de la cita')
def patch_cita(citaID: int, motivo: str, estado: str):
    update_data = {}
    if motivo:
        update_data['motivo'] = motivo
    if estado:
        update_data['estado'] = estado
    result = CLI.patch_appointment(citaID, update_data)
    click.echo(result)

@main.command()
@click.option('--citaID', '-i', type=int, required=True, help='ID de la cita')
def get_cita_by_id(id: int):
    try:
        data = CLI.get_cita_by_id(id)
        click.echo(data.tabla())
        
    except Exception as e:
        click.echo(f'Error al obtener la cita: {e}')
        
@main.command()
@click.option('--citaID', '-i', type=int, required=True, help='ID de la cita')
@click.option('--medicoID', '-m', type=int, required=True, help='Nuevo ID del médico')
@click.option('--horarioID', '-h', type=int, required=True, help='Nuevo ID del horario')
@click.option('--departamentoID', '-d', type=int, required=True, help='Nuevo ID del departamento')
@click.option('--motivo', '-o', type=str, required=True, help='Nuevo motivo de la cita')
@click.option('--estado', '-e', type=str, required=True, help='Nuevo estado de la cita')
def put_cita(citaID: int, medicoID: int, horarioID: int, departamentoID: int, motivo: str, estado: str):
    update_data = {
        'medicoID': medicoID,
        'horarioID': horarioID,
        'departamentoID': departamentoID,
        'motivo': motivo,
        'estado': estado
    }
    result = CLI.put_appointment(citaID, update_data)
    click.echo(result)

#------------------------------------------------------------------------

@main.command()
@click.option('--medicoID', '-m', type=int, required=True, help='ID del médico')
@click.option('--dia', '-d', type=str, required=True, help='Día de la semana')
@click.option('--hora_inicio', '-hi', type=str, required=True, help='Hora de inicio (formato HH:MM)')
@click.option('--hora_fin', '-hf', type=str, required=True, help='Hora de fin (formato HH:MM)')
@click.option('--especialidadID', '-e', type=int, required=True, help='ID de la especialidad')
@click.option('--departamentoID', '-dp', type=int, required=True, help='ID del departamento')
def create_horario(medicoID: int, dia: str, hora_inicio: str, hora_fin: str, especialidadID: int, departamentoID: int):
    data = {
        'medicoID': medicoID,
        'dia': dia,
        'hora_inicio': hora_inicio,
        'hora_fin': hora_fin,
        'especialidadID': especialidadID,
        'departamentoID': departamentoID
    }
    result = CLI.post_schedule(data)
    click.echo(result)

@main.command()
@click.option('--horarioID', '-i', type=int, required=True, help='ID del horario')
def delete_horario(horarioID: int):
    result = CLI.delete_schedule(horarioID)
    click.echo(result)

@main.command()
@click.option('--horarioID', '-i', type=int, required=True, help='ID del horario')
@click.option('--dia', '-d', type=str, required=False, help='Nuevo día de la semana')
@click.option('--hora_inicio', '-hi', type=str, required=False, help='Nueva hora de inicio (formato HH:MM)')
@click.option('--hora_fin', '-hf', type=str, required=False, help='Nueva hora de fin (formato HH:MM)')
@click.option('--especialidadID', '-e', type=int, required=False, help='Nuevo ID de la especialidad')
@click.option('--departamentoID', '-dp', type=int, required=False, help='Nuevo ID del departamento')
def patch_horario(horarioID: int, dia: str, hora_inicio: str, hora_fin: str, especialidadID: int, departamentoID: int):
    update_data = {}
    if dia:
        update_data['dia'] = dia
    if hora_inicio:
        update_data['hora_inicio'] = hora_inicio
    if hora_fin:
        update_data['hora_fin'] = hora_fin
    if especialidadID:
        update_data['especialidadID'] = especialidadID
    if departamentoID:
        update_data['departamentoID'] = departamentoID
    result = CLI.patch_schedule(id, update_data)
    click.echo(result)

@main.command()
@click.option('--horarioID', '-i', type=int, required=True, help='ID del horario')
@click.option('--medicoID', '-m', type=int, required=True, help='Nuevo ID del médico')
@click.option('--dia', '-d', type=str, required=True, help='Nuevo día de la semana')
@click.option('--hora_inicio', '-hi', type=str, required=True, help='Nueva hora de inicio (formato HH:MM)')
@click.option('--hora_fin', '-hf', type=str, required=True, help='Nueva hora de fin (formato HH:MM)')
@click.option('--especialidadID', '-e', type=int, required=True, help='Nuevo ID de la especialidad')
@click.option('--departamentoID', '-dp', type=int, required=True, help='Nuevo ID del departamento')
def put_horario(horarioID: int, medicoID: int, dia: str, hora_inicio: str, hora_fin: str, especialidadID: int, departamentoID: int):
    update_data = {
        'medicoID': medicoID,
        'dia': dia,
        'hora_inicio': hora_inicio,
        'hora_fin': hora_fin,
        'especialidadID': especialidadID,
        'departamentoID': departamentoID
    }
    result = CLI.put_schedule(horarioID, update_data)
    click.echo(result)

#------------------------------------------------------------------------

@main.command()
@click.option('--nombre', '-n', type=str, required=True, help='Nombre del médico')
@click.option('--apellido', '-a', type=str, required=True, help='Apellido del médico')
@click.option('--dni', '-d', type=str, required=True, help='DNI del médico')
@click.option('--especialidadID', '-e', type=int, required=True, help='ID de la especialidad')
@click.option('--telefono', '-t', type=str, required=True, help='Teléfono del médico')
@click.option('--email', '-e', type=str, required=True, help='Email del médico')
def create_medico(nombre: str, apellido: str, dni: str, especialidadID: int, telefono: str, email: str):
    """Crea un nuevo médico"""
    data = {
        'nombre': nombre,
        'apellido': apellido,
        'dni': dni,
        'especialidadID': especialidadID,
        'telefono': telefono,
        'email': email
    }
    result = CLI.post_doctor(data)
    click.echo(result)

@main.command()
@click.option('--medicoID', '-i', type=int, required=True, help='ID del médico')
def delete_medico(medicoID: int):
    result = CLI.delete_doctor(medicoID)
    click.echo(result)


@main.command()
@click.option('--medicoID', '-i', type=int, required=True, help='ID del médico')
@click.option('--nombre', '-n', type=str, required=False, help='Nuevo nombre del médico')
@click.option('--apellido', '-a', type=str, required=False, help='Nuevo apellido del médico')
@click.option('--dni', '-d', type=str, required=False, help='Nuevo DNI del médico')
@click.option('--especialidadID', '-e', type=int, required=False, help='Nuevo ID de la especialidad')
@click.option('--telefono', '-t', type=str, required=False, help='Nuevo teléfono del médico')
@click.option('--email', '-e', type=str, required=False, help='Nuevo email del médico')
def patch_medico(medicoID: int, nombre: str, apellido: str, dni: str, especialidadID: int, telefono: str, email: str):
    """Actualiza parcialmente un médico por ID"""
    update_data = {}
    if nombre:
        update_data['nombre'] = nombre
    if apellido:
        update_data['apellido'] = apellido
    if dni:
        update_data['dni'] = dni
    if especialidadID:
        update_data['especialidadID'] = especialidadID
    if telefono:
        update_data['telefono'] = telefono
    if email:
        update_data['email'] = email
    result = CLI.patch_doctor(medicoID, update_data)
    click.echo(result)
    

@main.command()
@click.option('--medicoID', '-i', type=int, required=True, help='ID del médico')
@click.option('--nombre', '-n', type=str, required=False, help='Nuevo nombre del médico')
@click.option('--apellido', '-a', type=str, required=False, help='Nuevo apellido del médico')
@click.option('--dni', '-d', type=str, required=False, help='Nuevo DNI del médico')
@click.option('--especialidadID', '-e', type=int, required=False, help='Nuevo ID de la especialidad')
@click.option('--telefono', '-t', type=str, required=False, help='Nuevo teléfono del médico')
@click.option('--email', '-e', type=str, required=False, help='Nuevo email del médico')
def patch_medico(medicoID: int, nombre: str, apellido: str, dni: str, especialidadID: int, telefono: str, email: str):
    """Actualiza parcialmente un médico por ID"""
    update_data = {}
    if nombre:
        update_data['nombre'] = nombre
    if apellido:
        update_data['apellido'] = apellido
    if dni:
        update_data['dni'] = dni
    if especialidadID:
        update_data['especialidadID'] = especialidadID
    if telefono:
        update_data['telefono'] = telefono
    if email:
        update_data['email'] = email
    result = CLI.patch_doctor(medicoID, update_data)
    click.echo(result)
    
@main.command()
@click.option('--medicoID', '-i', type=int, required=True, help='ID del médico')
@click.option('--nombre', '-n', type=str, required=True, help='Nuevo nombre del médico')
@click.option('--apellido', '-a', type=str, required=True, help='Nuevo apellido del médico')
@click.option('--dni', '-d', type=str, required=True, help='Nuevo DNI del médico')
@click.option('--especialidadID', '-e', type=int, required=True, help='Nuevo ID de la especialidad')
@click.option('--telefono', '-t', type=str, required=True, help='Nuevo teléfono del médico')
@click.option('--email', '-e', type=str, required=True, help='Nuevo email del médico')
def put_medico(medicoID: int, nombre: str, apellido: str, dni: str, especialidadID: int, telefono: str, email: str):
    update_data = {
        'nombre': nombre,
        'apellido': apellido,
        'dni': dni,
        'especialidadID': especialidadID,
        'telefono': telefono,
        'email': email
    }
    result = CLI.put_doctor(medicoID, update_data)
    click.echo(result)

@main.command()
@click.option('--nombre', '-n', type=str, required=True, help='Nombre de la ubicación')
@click.option('--descripcion', '-d', type=str, required=True, help='Descripción de la ubicación')
def create_ubicacion(nombre: str, descripcion: str):
    data = {
        'nombre': nombre,
        'descripcion': descripcion
    }
    result = CLI.post_location(data)
    click.echo(result)

@main.command()
@click.option('--ubicacionID', '-i', type=int, required=True, help='ID de la ubicación')
def delete_ubicacion(ubicacionID: int):
    result = delete_ubicacion(ubicacionID)
    click.echo(result)

@main.command()
@click.option('--ubicacionID', '-i', type=int, required=True, help='ID de la ubicación')
@click.option('--nombre', '-n', type=str, required=False, help='Nuevo nombre de la ubicación')
@click.option('--descripcion', '-d', type=str, required=False, help='Nueva descripción de la ubicación')
def patch_ubicacion(ubicacionID: int, nombre: str, descripcion: str):
    update_data = {}
    if nombre:
        update_data['nombre'] = nombre
    if descripcion:
        update_data['descripcion'] = descripcion
    result = CLI.patch_location(ubicacionID, update_data)
    click.echo(result)

@main.command()
@click.option('--ubicacionID', '-i', type=int, required=True, help='ID de la ubicación')
@click.option('--nombre', '-n', type=str, required=True, help='Nuevo nombre de la ubicación')
@click.option('--descripcion', '-d', type=str, required=True, help='Nueva descripción de la ubicación')
def put_ubicacion(ubicacionID: int, nombre: str, descripcion: str):
    update_data = {
        'nombre': nombre,
        'descripcion': descripcion
    }
    result = CLI.put_location(ubicacionID, update_data)
    click.echo(result)
    
#------------------------------------------------------------------------

@main.command()
@click.option('--userID', '-u', type=int, required=True, help='ID del usuario que realiza el testimonio')
@click.option('--content', '-c', type=str, required=True, help='Contenido del testimonio')
def create_testimonio(userID: int, content: str):
    """Crea un nuevo testimonio"""
    data = {
        'user': userID,
        'content': content
    }
    result = CLI.post_testimony(data)
    click.echo(result)

@main.command()
@click.option('--id', '-i', type=int, required=True, help='ID del testimonio')
def delete_testimonio(id: int):
    result = CLI.delete_testimony(id)
    click.echo(result)

@main.command()
@click.option('--id', '-i', type=int, required=True, help='ID del testimonio')
@click.option('--content', '-c', type=str, required=False, help='Nuevo contenido del testimonio')
def patch_testimonio(id: int, content: str):
    update_data = {}
    if content:
        update_data['content'] = content
    result = CLI.patch_testimony(id, update_data)
    click.echo(result)

@main.command()
@click.option('--id', '-i', type=int, required=True, help='ID del testimonio')
@click.option('--userID', '-u', type=int, required=True, help='ID del usuario que realiza el testimonio')
@click.option('--content', '-c', type=str, required=True, help='Contenido del testimonio')
def put_testimonio(id: int, userID: int, content: str):

    update_data = {
        'user': userID,
        'content': content
    }
    result = CLI.put_testimony(id, update_data)
    click.echo(result)

#------------------------------------------------------------------------


@main.command()
@click.option('--nombre', '-n', type=str, required=True, help='Nombre del departamento')
@click.option('--descripcion', '-d', type=str, required=True, help='Descripción del departamento')
@click.option('--ubicacionID', '-u', type=int, required=True, help='ID de la ubicación del departamento')
def create_departamento(nombre: str, descripcion: str, ubicacionID: int):
    data = {
        'nombre': nombre,
        'descripcion': descripcion,
        'ubicacionID': ubicacionID
    }
    result = CLI.post_department(data)
    click.echo(result)

@main.command()
@click.option('--departamentoID', '-i', type=int, required=True, help='ID del departamento')
def delete_departamento(departamentoID: int):
    result = CLI.delete_department(departamentoID)
    click.echo(result)

@main.command()
@click.option('--departamentoID', '-i', type=int, required=True, help='ID del departamento')
@click.option('--nombre', '-n', type=str, required=False, help='Nuevo nombre del departamento')
@click.option('--descripcion', '-d', type=str, required=False, help='Nueva descripción del departamento')
@click.option('--ubicacionID', '-u', type=int, required=False, help='Nuevo ID de la ubicación del departamento')
def patch_departamento(id: int, nombre: str, descripcion: str, ubicacionID: int):
    update_data = {}
    if nombre:
        update_data['nombre'] = nombre
    if descripcion:
        update_data['descripcion'] = descripcion
    if ubicacionID:
        update_data['ubicacionID'] = ubicacionID
    result = CLI.patch_department(id, update_data)
    click.echo(result)

@main.command()
@click.option('--departamentoID', '-i', type=int, required=True, help='ID del departamento')
@click.option('--nombre', '-n', type=str, required=True, help='Nombre del departamento')
@click.option('--descripcion', '-d', type=str, required=True, help='Descripción del departamento')
@click.option('--ubicacionID', '-u', type=int, required=True, help='ID de la ubicación del departamento')
def put_departamento(departamentoID: int, nombre: str, descripcion: str, ubicacionID: int):
    update_data = {
        'nombre': nombre,
        'descripcion': descripcion,
        'ubicacionID': ubicacionID
    }
    result = CLI.put_department(departamentoID, update_data)
    click.echo(result)

if __name__ == '__main__':
    main()

@main.command()
@click.option('--PORT', '-P', type=int, required=False, help='Port of the grafic interface Default 8000')
@click.option('--HOST', '-H', type=str, required=False, help='Host of the grafic interface Default 127.0.0.1')
def run_server(port, host):
    port = port if port else 8000
    host = host if host else "127.0.0.1"
    try:
        state = subprocess.run(
            ['streamlit', 'run', 'interface/main.py', '--server.port', str(port), '--server.address', str(host)],
            check=True
        )
        #click.echo(f'streamlit run interface/main.py --server.port {port} --server.address {host}')
        click.echo(state.stdout.decode())
        click.echo(f'\nURL: {Fore.YELLOW + f"http://{host}:{port}" + Style.RESET_ALL}')
    
    except subprocess.CalledProcessError as e:
        click.echo("Error al ejecutar Streamlit:")
        click.echo(e)
        click.echo(e.output)
    
    except KeyboardInterrupt as stop:
        click.echo(f"\n{Fore.BLUE + Style.BRIGHT}Ejecución cancelada por el usuario.{Style.RESET_ALL} {Fore.RED}Ctrl + C{Style.RESET_ALL}")

#------------------------------------------------------------------------

if __name__ == '__main__':
    main()