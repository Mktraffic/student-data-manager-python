import json
from collections import defaultdict
from datetime import date
from pathlib import Path
from pprint import pprint
from typing import Any, Dict, Iterable, List, Tuple


# ============================================================
# Actividad 1: Cargar archivo JSON
# ============================================================

def cargar_json(ruta_archivo: str) -> List[Dict[str, Any]]:
    """Carga y retorna la informacion JSON desde un archivo."""
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


# ============================================================
# Utilidades para normalizar datos de estudiantes
# ============================================================

def _extraer_nombres(valor: Any) -> List[str]:
    """Convierte nombres/apellidos en lista de tokens en minuscula."""
    if isinstance(valor, str):
        return [x.strip().lower() for x in valor.replace(",", " ").split() if x.strip()]

    if isinstance(valor, list):
        salida = []
        for item in valor:
            salida.extend(_extraer_nombres(item))
        return salida

    if isinstance(valor, dict):
        # Mantiene orden natural por clave para evitar depender del orden del diccionario.
        salida = []
        for clave in sorted(valor.keys()):
            salida.extend(_extraer_nombres(valor[clave]))
        return salida

    return []


def _primer_y_segundo_nombre(estudiante: Dict[str, Any]) -> Tuple[str, str]:
    nombres = _extraer_nombres(estudiante.get("nombres", ""))
    primer = nombres[0] if len(nombres) >= 1 else ""
    segundo = nombres[1] if len(nombres) >= 2 else ""
    return primer, segundo


def _apellidos_ordenados(estudiante: Dict[str, Any]) -> Tuple[str, str]:
    """
    Retorna (primer_apellido, segundo_apellido) usando datos normalizados.

    La metadata indica formato "segundo apellido, primer apellido" cuando es cadena.
    Si hay dos apellidos, se reorganizan como (primer, segundo).
    """
    valor = estudiante.get("apellidos", "")

    if isinstance(valor, str) and "," in valor:
        partes = [x.strip().lower() for x in valor.split(",") if x.strip()]
        if len(partes) >= 2:
            segundo_apellido = partes[0]
            primer_apellido = partes[1]
            return primer_apellido, segundo_apellido

    tokens = _extraer_nombres(valor)
    if len(tokens) >= 2:
        return tokens[0], tokens[1]
    if len(tokens) == 1:
        return tokens[0], ""
    return "", ""


# ============================================================
# Actividad 2: Nota promedio por asignatura
# ============================================================

def promedio_por_asignatura(
    estudiantes: Iterable[Dict[str, Any]], include_retiradas: bool = True
) -> Dict[str, float]:
    """Calcula promedio de nota por nombre de asignatura."""
    acumulados: Dict[str, List[float]] = defaultdict(list)

    for estudiante in estudiantes:
        for materia in estudiante.get("asignaturas", []):
            retirada = str(materia.get("retirada", "No")).strip().lower() == "si"
            if retirada and not include_retiradas:
                continue

            nombre = str(materia.get("nombre", "")).strip()
            nota = materia.get("nota")
            if nombre and isinstance(nota, (int, float)):
                acumulados[nombre].append(float(nota))

    return {
        asignatura: round(sum(notas) / len(notas), 2)
        for asignatura, notas in acumulados.items()
        if notas
    }


# ============================================================
# Actividad 3: Nota promedio por estudiante (no retiradas)
# ============================================================

def promedio_por_estudiante_no_retiradas(
    estudiantes: Iterable[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """Calcula promedio por estudiante usando solo asignaturas no retiradas y ordena por apellido."""
    resultado: List[Dict[str, Any]] = []

    for est in estudiantes:
        codigo = est.get("codigo", "")
        doc = est.get("documento", "")

        primer_nombre, segundo_nombre = _primer_y_segundo_nombre(est)
        primer_apellido, segundo_apellido = _apellidos_ordenados(est)

        notas = []
        for mat in est.get("asignaturas", []):
            retirada = str(mat.get("retirada", "No")).strip().lower() == "si"
            nota = mat.get("nota")
            if not retirada and isinstance(nota, (int, float)):
                notas.append(float(nota))

        promedio = round(sum(notas) / len(notas), 2) if notas else 0.0

        resultado.append(
            {
                "codigo": codigo,
                "documento": doc,
                "primer_nombre": primer_nombre,
                "segundo_nombre": segundo_nombre,
                "primer_apellido": primer_apellido,
                "segundo_apellido": segundo_apellido,
                "promedio": promedio,
            }
        )

    return sorted(
        resultado,
        key=lambda x: (x["primer_apellido"], x["segundo_apellido"], x["primer_nombre"]),
    )


# ============================================================
# Actividad 4: Correo institucional
# ============================================================

def generar_correo_institucional(estudiante: Dict[str, Any], dominio: str = "uptc.edu.co") -> str:
    """Genera correo institucional segun reglas del enunciado."""
    primer_nombre, segundo_nombre = _primer_y_segundo_nombre(estudiante)
    primer_apellido, segundo_apellido = _apellidos_ordenados(estudiante)

    documento = str(estudiante.get("documento", "")).strip()
    ultimos_2 = documento[-2:] if len(documento) >= 2 else documento

    if segundo_nombre:
        usuario = f"{primer_nombre[:1]}{segundo_nombre[:1]}.{primer_apellido}{ultimos_2}"
    else:
        usuario = f"{primer_nombre[:1]}{primer_apellido[:1]}.{segundo_apellido}{ultimos_2}"

    return f"{usuario.lower()}@{dominio}"


def lista_estudiantes_con_correo(estudiantes: Iterable[Dict[str, Any]]) -> List[Dict[str, str]]:
    """Retorna lista de estudiantes con su correo."""
    salida: List[Dict[str, str]] = []
    for est in estudiantes:
        primer_nombre, segundo_nombre = _primer_y_segundo_nombre(est)
        primer_apellido, segundo_apellido = _apellidos_ordenados(est)
        nombre_completo = " ".join(
            [
                x
                for x in [primer_nombre, segundo_nombre, primer_apellido, segundo_apellido]
                if x
            ]
        ).title()

        salida.append(
            {
                "codigo": str(est.get("codigo", "")),
                "nombre": nombre_completo,
                "correo": generar_correo_institucional(est),
            }
        )
    return salida


# ============================================================
# Actividad 5.1: Vocal o consonante
# ============================================================

def es_vocal(caracter: str) -> bool:
    """Retorna True si el caracter corresponde a una vocal."""
    if not caracter or len(caracter) != 1 or not caracter.isalpha():
        return False
    return caracter.casefold() in "aeiou"


# ============================================================
# Actividad 5.2: Ecuacion cuadratica
# ============================================================

def resolver_ecuacion_cuadratica(a: float, b: float, c: float) -> Tuple[complex, complex]:
    """Resuelve ax^2 + bx + c = 0 y retorna sus dos raices."""
    if a == 0:
        raise ValueError("El coeficiente 'a' no puede ser 0 en una ecuacion cuadratica.")

    discriminante = b**2 - 4 * a * c
    raiz_disc = discriminante**0.5 if discriminante >= 0 else complex(0, (-discriminante) ** 0.5)

    x1 = (-b + raiz_disc) / (2 * a)
    x2 = (-b - raiz_disc) / (2 * a)
    return x1, x2


# ============================================================
# Actividad 5.3: Histograma
# ============================================================

def histogram(valores: Iterable[int], simbolo: str = "H") -> None:
    """Imprime un histograma vertical linea por linea."""
    for numero in valores:
        if isinstance(numero, int) and numero > 0:
            print(simbolo * numero)
        else:
            print("")


# ============================================================
# Actividad 5.4: Metodos de cadena con ejemplo
# ============================================================

def ejemplos_metodos_cadena() -> Dict[str, Any]:
    texto = "  gestion de datos con python  "
    return {
        "replace": texto.replace("python", "analitica"),
        "find": texto.find("datos"),
        "count": texto.count("o"),
        "capitalize": texto.strip().capitalize(),
        "title": texto.strip().title(),
        "rstrip": texto.rstrip(),
        "index": texto.index("de"),
        "casefold": "GESTION".casefold(),
    }


# ============================================================
# Actividad 5.5: Operaciones con frase
# ============================================================

def operaciones_frase(frase: str) -> Dict[str, Any]:
    palabras = frase.split()
    letras = list(frase)
    reemplazo = frase.replace("Gestión", "Analítica").replace("Gestion", "Analitica")
    unida_guion = "-".join(palabras)
    con_separador = "-".join(letras)

    return {
        "palabras": palabras,
        "reemplazo": reemplazo,
        "letras_separadas": con_separador,
        "frase_unida_guion": unida_guion,
    }


# ============================================================
# Actividad 5.6: Fecha actual y extraccion de mes
# ============================================================

def obtener_mes_actual_como_cadena() -> str:
    fecha_actual = date.today().isoformat()  # AAAA-MM-DD
    mes = fecha_actual[5:7]
    return f"Mes {mes}"


# ============================================================
# Actividad 5.7: Empleados en formato requerido
# ============================================================

def mostrar_empleados(empleados: List[List[Any]]) -> None:
    """Recibe [nombres, edades, peso] e imprime cada empleado."""
    if len(empleados) != 3:
        raise ValueError("La estructura esperada es [nombres, edades, peso].")

    nombres, edades, pesos = empleados
    total = min(len(nombres), len(edades), len(pesos))

    for i in range(total):
        print(f"Empleado # {i + 1}: Nombre: {nombres[i]},  Edad: {edades[i]}, Peso: {pesos[i]}")


# ============================================================
# Actividad 5.8: Ejemplos copy, remove, del, clear, in, append vs extend
# ============================================================

def ejemplos_listas() -> Dict[str, Any]:
    base = [10, 20, 30]

    copia = base.copy()

    remove_demo = [1, 2, 3, 2]
    remove_demo.remove(2)  # elimina primera ocurrencia de 2

    del_demo = ["a", "b", "c", "d"]
    del del_demo[1]  # elimina elemento en indice 1

    clear_demo = [1, 2, 3]
    clear_demo.clear()

    in_demo = 20 in base

    append_demo = [1, 2]
    append_demo.append([3, 4])  # agrega una sola posicion (lista anidada)

    extend_demo = [1, 2]
    extend_demo.extend([3, 4])  # agrega cada elemento por separado

    return {
        "copy": copia,
        "remove": remove_demo,
        "del": del_demo,
        "clear": clear_demo,
        "in": in_demo,
        "append": append_demo,
        "extend": extend_demo,
    }


# ============================================================
# Actividad 5.9: Revisar duplicados sin modificar la lista
# ============================================================

def tiene_duplicados(lista: Iterable[Any]) -> bool:
    """Retorna True si existe al menos un elemento duplicado."""
    vistos = set()
    for item in lista:
        if item in vistos:
            return True
        vistos.add(item)
    return False


# ============================================================
# Actividad 5.10: Eliminar duplicados
# ============================================================

def eliminar_duplicados(lista: Iterable[Any]) -> List[Any]:
    """Elimina duplicados preservando el orden de primera aparicion."""
    vistos = set()
    salida = []
    for item in lista:
        if item not in vistos:
            vistos.add(item)
            salida.append(item)
    return salida


# ============================================================
# Actividad 5.11: Diferencia entre set y frozenset
# ============================================================

def diferencia_set_frozenset() -> Dict[str, str]:
    return {
        "set": "Mutable. Permite add/remove/update.",
        "frozenset": "Inmutable. No permite modificar elementos una vez creado.",
    }


# ============================================================
# Actividad 5.12: Operadores/metodos de conjuntos con ejemplos
# ============================================================

def ejemplos_conjuntos() -> Dict[str, Any]:
    a = {1, 2, 3, 4}
    b = {3, 4, 5}

    intersection_update_demo = a.copy()
    intersection_update_demo.intersection_update(b)

    isdisjoint_demo = {1, 2}.isdisjoint({3, 4})
    issubset_demo = {1, 2}.issubset({1, 2, 3})
    issuperset_demo = {1, 2, 3}.issuperset({1, 2})

    pop_demo_set = {7, 8, 9}
    pop_valor = pop_demo_set.pop()

    remove_demo_set = {10, 11, 12}
    remove_demo_set.remove(11)

    symmetric_difference_demo = {1, 2, 3}.symmetric_difference({3, 4, 5})

    symmetric_difference_update_demo = {1, 2, 3}
    symmetric_difference_update_demo.symmetric_difference_update({3, 4, 5})

    union_demo = {1, 2}.union({2, 3, 4})

    update_demo = {1, 2}
    update_demo.update({2, 3, 4})

    return {
        "intersection_update": intersection_update_demo,
        "isdisjoint": isdisjoint_demo,
        "issubset": issubset_demo,
        "issuperset": issuperset_demo,
        "pop": {"valor_extraido": pop_valor, "set_restante": pop_demo_set},
        "remove": remove_demo_set,
        "symmetric_difference": symmetric_difference_demo,
        "symmetric_difference_update": symmetric_difference_update_demo,
        "union": union_demo,
        "update": update_demo,
    }


# ============================================================
# Actividad 5.13: Diccionario por inicial de palabra
# ============================================================

def agrupar_palabras_por_inicial(words: Iterable[str]) -> Dict[str, List[str]]:
    """Agrupa palabras por letra inicial."""
    resultado: Dict[str, List[str]] = defaultdict(list)
    for palabra in words:
        if palabra:
            resultado[palabra[0].lower()].append(palabra)
    return dict(resultado)


# ============================================================
# Actividad 5.14: Conteo de vocales y consonantes
# ============================================================

def contar_vocales_consonantes(cadena: str) -> Dict[str, int]:
    vocales = "aeiou"
    conteo = {v: 0 for v in vocales}
    consonantes = 0

    for ch in cadena.casefold():
        if ch.isalpha():
            if ch in vocales:
                conteo[ch] += 1
            else:
                consonantes += 1

    conteo["Consonantes"] = consonantes
    return conteo


# ============================================================
# Actividad 5.15: Cadena de clientes a diccionario anidado
# ============================================================

def clientes_cadena_a_diccionario(data: str) -> Dict[str, Dict[str, str]]:
    """Convierte la cadena de clientes en un diccionario anidado por ID."""
    lineas = [linea.strip() for linea in data.split("\n") if linea.strip()]
    if not lineas:
        return {}

    encabezados = [h.strip() for h in lineas[0].split(";")]

    resultado: Dict[str, Dict[str, str]] = {}
    for linea in lineas[1:]:
        campos = [c.strip() for c in linea.split(";")]
        if len(campos) != len(encabezados):
            continue

        registro = dict(zip(encabezados, campos))
        id_cliente = registro.pop("id")
        resultado[id_cliente] = registro

    return resultado


# ============================================================
# Ejecucion demostrativa
# ============================================================

def _imprimir_titulo(texto: str) -> None:
    print("\n" + "=" * 70)
    print(texto)
    print("=" * 70)


def _imprimir_subtitulo(texto: str) -> None:
    print("\n" + texto)
    print("-" * len(texto))

def demo_actividades_json() -> None:
    ruta = Path(__file__).resolve().parent / "data" / "Unidad1_Reto.json"
    _imprimir_titulo("TALLER UNIDAD I - ENTREGA")
    _imprimir_subtitulo("Actividad 1 - Cargar el archivo JSON")
    try:
        estudiantes = cargar_json(ruta)
        print(f"Archivo cargado correctamente: {ruta.name}")
        print(f"Ruta de lectura: {ruta}")
        print(f"Cantidad de estudiantes leidos: {len(estudiantes)}")
    except FileNotFoundError:
        print(f"No se encontro '{ruta.name}'. Se omiten actividades 1 a 4.")
        print("Ruta esperada:", ruta)
        return

    _imprimir_subtitulo("Actividad 2 - Nota promedio por asignatura")
    print("Salida:")
    pprint(promedio_por_asignatura(estudiantes, include_retiradas=True))

    _imprimir_subtitulo("Actividad 3 - Nota promedio por estudiante (No retiradas, ordenado por apellido)")
    print("Salida:")
    pprint(promedio_por_estudiante_no_retiradas(estudiantes))

    _imprimir_subtitulo("Actividad 4 - Generar correo institucional")
    print("Salida:")
    pprint(lista_estudiantes_con_correo(estudiantes))


def demo_cuadernillos() -> None:
    _imprimir_titulo("Actividad 5 - Cuadernillos de la Unidad 1")

    _imprimir_subtitulo("5.1 Vocal o consonante")
    print("Entrada: 'a'  -> Salida:", es_vocal("a"))
    print("Entrada: 'b'  -> Salida:", es_vocal("b"))

    _imprimir_subtitulo("5.2 Ecuacion cuadratica")
    print("Entrada: a=1, b=-5, c=6")
    print("Salida:", resolver_ecuacion_cuadratica(1, -5, 6))

    _imprimir_subtitulo("5.3 Histograma")
    print("Entrada: [3, 5, 1]")
    print("Salida:")
    histogram([3, 5, 1])

    _imprimir_subtitulo("5.4 Funciones de cadena: replace, find, count, capitalize, title, rstrip, index, casefold")
    print("Salida:")
    pprint(ejemplos_metodos_cadena())

    _imprimir_subtitulo("5.5 Division y transformacion de frase")
    print("Entrada:")
    print("Gestión de Datos")
    resultado_55 = operaciones_frase("Gestión de Datos")
    print("Salida 1:")
    print(resultado_55["palabras"])
    print("Salida 2:")
    print(resultado_55["reemplazo"])
    print("Salida 3:")
    print(resultado_55["letras_separadas"])
    print("Salida 4:")
    print(resultado_55["frase_unida_guion"])

    _imprimir_subtitulo("5.6 Fecha actual y extraccion de mes")
    print("Salida:", obtener_mes_actual_como_cadena())

    _imprimir_subtitulo("5.7 Mostrar empleados con formato")
    nombres = ["Luis", "Pedro", "Lucia"]
    edades = [20, 18, 30]
    peso = [55.6, 60, 65.8]
    empleados = [nombres, edades, peso]
    print("Salida:")
    mostrar_empleados(empleados)

    _imprimir_subtitulo("5.8 Funciones y operadores de listas")
    print("Salida:")
    pprint(ejemplos_listas())

    _imprimir_subtitulo("5.9 Revisar duplicados")
    print("Entrada: [1, 2, 3, 2] -> Salida:", tiene_duplicados([1, 2, 3, 2]))
    print("Entrada: [1, 2, 3]    -> Salida:", tiene_duplicados([1, 2, 3]))

    _imprimir_subtitulo("5.10 Eliminar duplicados")
    print("Entrada: [1, 2, 2, 3, 1, 4]")
    print("Salida:", eliminar_duplicados([1, 2, 2, 3, 1, 4]))

    _imprimir_subtitulo("5.11 Diferencia entre set y frozenset")
    print("Salida:")
    pprint(diferencia_set_frozenset())

    _imprimir_subtitulo("5.12 Operadores de conjuntos")
    print("Salida:")
    pprint(ejemplos_conjuntos())

    _imprimir_subtitulo("5.13 Diccionario por inicial de palabra")
    words = ["apple", "bat", "bar", "atom", "book", "cat"]
    print("Entrada:", words)
    print("Salida:")
    pprint(agrupar_palabras_por_inicial(words))

    _imprimir_subtitulo("5.14 Conteo de vocales y consonantes")
    print("Entrada: Gestion de Datos")
    print("Salida:")
    pprint(contar_vocales_consonantes("Gestion de Datos"))

    _imprimir_subtitulo("5.15 Cadena de clientes a diccionario")
    cadena_clientes = (
        "id;nombre;correo;movil;salario\n"
        "3412;Pepe Perez;pepeperez@yahoo.com;300281234;150000\n"
        "45342;Maria Melo;mariamelo@yahoo.com;315434223;300000\n"
        "5673321;Fernando Jimenez;ferjim@gmail.com;312342234;230000\n"
        "4545231;Carlos Cardenas;carloscardenas@hotmail.com;3156754323;345000"
    )
    print("Salida:")
    pprint(clientes_cadena_a_diccionario(cadena_clientes))


if __name__ == "__main__":
    demo_actividades_json()
    demo_cuadernillos()
