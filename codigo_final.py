

import sqlite3
from abc import ABC, abstractmethod

conn = sqlite3.connect('hotel.db')
cursor = conn.cursor()

def crear_tablas():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hotel (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            direccion TEXT,
            calificacion REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS habitacion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero INTEGER,
            tipo TEXT,
            precio REAL,
            hotel_id INTEGER,
            FOREIGN KEY (hotel_id) REFERENCES hotel (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reserva (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            huesped TEXT,
            fecha_entrada TEXT,
            fecha_salida TEXT,
            habitacion_id INTEGER,
            hotel_id INTEGER,
            FOREIGN KEY (habitacion_id) REFERENCES habitacion (id),
            FOREIGN KEY (hotel_id) REFERENCES hotel (id)
        )
    ''')
    conn.commit()

crear_tablas()

class HotelAbstracto(ABC):
    @abstractmethod
    def agregar_habitacion(self, habitacion):
        pass

    @abstractmethod
    def listar_habitaciones(self):
        pass

class Hotel(HotelAbstracto):
    def __init__(self, id, nombre, direccion, calificacion):
        self.id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__calificacion = calificacion
        self.habitaciones = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, nueva_direccion):
        self.__direccion = nueva_direccion

    @property
    def calificacion(self):
        return self.__calificacion

    @calificacion.setter
    def calificacion(self, nueva_calificacion):
        if 0 <= nueva_calificacion <= 5:
            self.__calificacion = nueva_calificacion
        else:
            print("Calificación no válida.")

    def agregar_habitacion(self, habitacion):
        cursor.execute('''
            INSERT INTO habitacion (numero, tipo, precio, hotel_id)
            VALUES (?, ?, ?, ?)
        ''', (habitacion.numero, habitacion.tipo, habitacion.precio, self.id))
        conn.commit()

    def listar_habitaciones(self):
        cursor.execute('SELECT numero, tipo, precio FROM habitacion WHERE hotel_id = ?', (self.id,))
        habitaciones_db = cursor.fetchall()
        if not habitaciones_db:
            print("No hay habitaciones disponibles.")
        for habitacion in habitaciones_db:
            print(f'Habitación {habitacion[0]}: {habitacion[1]}, Precio: {habitacion[2]}')

    def actualizar_datos(self, nuevo_nombre=None, nueva_direccion=None, nueva_calificacion=None):
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nueva_direccion:
            self.direccion = nueva_direccion
        if nueva_calificacion:
            self.calificacion = nueva_calificacion

        cursor.execute('''
            UPDATE hotel SET nombre = ?, direccion = ?, calificacion = ? WHERE id = ?
        ''', (self.nombre, self.direccion, self.calificacion, self.id))
        conn.commit()

    def eliminar_habitacion(self, numero_habitacion):
        cursor.execute('DELETE FROM habitacion WHERE numero = ? AND hotel_id = ?', (numero_habitacion, self.id))
        conn.commit()

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio

    def actualizar_datos(self, nuevo_tipo=None, nuevo_precio=None):
        if nuevo_tipo:
            self.tipo = nuevo_tipo
        if nuevo_precio:
            self.precio = nuevo_precio

    def __str__(self):
        return f'Habitación {self.numero}: {self.tipo}, Precio: {self.precio}'

class Reserva:
    def __init__(self, hotel, habitacion, huesped, fecha_entrada, fecha_salida):
        self.hotel = hotel
        self.habitacion = habitacion
        self.huesped = huesped
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida

    def guardar_reserva(self):
        cursor.execute('''
            INSERT INTO reserva (huesped, fecha_entrada, fecha_salida, habitacion_id, hotel_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.huesped, self.fecha_entrada, self.fecha_salida, self.habitacion.numero, self.hotel.id))
        conn.commit()

    def actualizar_datos(self, nueva_fecha_entrada=None, nueva_fecha_salida=None):
        if nueva_fecha_entrada:
            self.fecha_entrada = nueva_fecha_entrada
        if nueva_fecha_salida:
            self.fecha_salida = nueva_fecha_salida

    def __str__(self):
        return f'Reserva de {self.huesped} en {self.hotel.nombre}, Habitación {self.habitacion.numero}, desde {self.fecha_entrada} hasta {self.fecha_salida}'

def menu_principal():
    hoteles = obtener_hoteles()
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear hotel")
        print("2. Listar hoteles")
        print("3. Seleccionar hotel")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_hotel(hoteles)
        elif opcion == "2":
            listar_hoteles(hoteles)
        elif opcion == "3":
            seleccionar_hotel(hoteles)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def crear_hotel(hoteles):
    nombre = input("Ingrese el nombre del hotel: ")
    direccion = input("Ingrese la dirección: ")
    calificacion = float(input("Ingrese la calificación del hotel (0-5): "))
    cursor.execute('''
        INSERT INTO hotel (nombre, direccion, calificacion)
        VALUES (?, ?, ?)
    ''', (nombre, direccion, calificacion))
    conn.commit()
    hoteles.append(Hotel(cursor.lastrowid, nombre, direccion, calificacion))
    print("Hotel creado con éxito.")

def listar_hoteles(hoteles):
    if not hoteles:
        print("No hay hoteles disponibles.")
        return

    for idx, hotel in enumerate(hoteles):
        print(f"{idx + 1}. {hotel.nombre} - {hotel.direccion} - Calificación: {hotel.calificacion}")

def seleccionar_hotel(hoteles):
    if not hoteles:
        print("No hay hoteles disponibles.")
        return

    listar_hoteles(hoteles)
    seleccion = int(input("Seleccione un hotel por número: ")) - 1

    if 0 <= seleccion < len(hoteles):
        menu_hotel(hoteles[seleccion])
    else:
        print("Selección no válida.")

def menu_hotel(hotel):
    while True:
        print(f"\n--- Menú de {hotel.nombre} ---")
        print("1. Agregar habitación")
        print("2. Listar habitaciones")
        print("3. Actualizar hotel")
        print("4. Eliminar habitación")
        print("5. Crear reserva")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_habitacion(hotel)
        elif opcion == "2":
            hotel.listar_habitaciones()
        elif opcion == "3":
            actualizar_hotel(hotel)
        elif opcion == "4":
            eliminar_habitacion(hotel)
        elif opcion == "5":
            crear_reserva(hotel)
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")

def agregar_habitacion(hotel):
    numero = int(input("Ingrese el número de habitación: "))
    tipo = input("Ingrese el tipo de habitación: ")
    precio = float(input("Ingrese el precio de la habitación: "))
    habitacion = Habitacion(numero, tipo, precio)
    hotel.agregar_habitacion(habitacion)
    print("Habitación agregada con éxito.")

def actualizar_hotel(hotel):
    nuevo_nombre = input(f"Ingrese nuevo nombre (Actual: {hotel.nombre}) o deje en blanco para mantener: ")
    nueva_direccion = input(f"Ingrese nueva dirección (Actual: {hotel.direccion}) o deje en blanco para mantener: ")
    nueva_calificacion = input(f"Ingrese nueva calificación (Actual: {hotel.calificacion}) o deje en blanco para mantener: ")

    hotel.actualizar_datos(nuevo_nombre or None, nueva_direccion or None, float(nueva_calificacion) if nueva_calificacion else None)
    print("Datos del hotel actualizados con éxito.")

def eliminar_habitacion(hotel):
    numero_habitacion = int(input("Ingrese el número de habitación a eliminar: "))
    hotel.eliminar_habitacion(numero_habitacion)
    print("Habitación eliminada con éxito.")

def crear_reserva(hotel):
    huesped = input("Ingrese el nombre del huésped: ")
    fecha_entrada = input("Ingrese la fecha de entrada (YYYY-MM-DD): ")
    fecha_salida = input("Ingrese la fecha de salida (YYYY-MM-DD): ")

    hotel.listar_habitaciones()
    numero_habitacion = int(input("Seleccione el número de habitación para la reserva: "))
    
    cursor.execute('SELECT id, numero, tipo, precio FROM habitacion WHERE numero = ? AND hotel_id = ?', (numero_habitacion, hotel.id))
    habitacion_db = cursor.fetchone()

    if habitacion_db:
        habitacion = Habitacion(habitacion_db[1], habitacion_db[2], habitacion_db[3])
        reserva = Reserva(hotel, habitacion, huesped, fecha_entrada, fecha_salida)
        reserva.guardar_reserva()
        print("Reserva creada con éxito.")
    else:
        print("Habitación no encontrada.")

def obtener_hoteles():
    cursor.execute('SELECT id, nombre, direccion, calificacion FROM hotel')
    hoteles_db = cursor.fetchall()
    hoteles = [Hotel(hotel[0], hotel[1], hotel[2], hotel[3]) for hotel in hoteles_db]
    return hoteles

if __name__ == "__main__":
    menu_principal()
