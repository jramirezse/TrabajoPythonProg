import csv


def CalcularPuntos(equipo):
    puntos = equipo["ganados"] * 3 + equipo["empatados"]
    return puntos


def CalcularDiferenciaGoles(equipo):
    diferencia = equipo["goles_favor"] - equipo["goles_contra"]
    return diferencia


def liderTabla(equipos):
    lider = equipos[0]

    for equipo in equipos:
        if equipo["puntos"] > lider["puntos"]:
            lider = equipo
        elif equipo["puntos"] == lider["puntos"]:
            if equipo["diferencia_goles"] > lider["diferencia_goles"]:
                lider = equipo

    return lider


equipos = []
dictEquipos = {}

with open("input/equiposChampions.csv", "r") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        equipo = {
            "nombre": fila["equipo"],
            "ganados": int(fila["ganados"]),
            "empatados": int(fila["empatados"]),
            "perdidos": int(fila["perdidos"]),
            "goles_favor": int(fila["goles_favor"]),
            "goles_contra": int(fila["goles_contra"])
        }

        equipo["puntos"] = CalcularPuntos(equipo)
        equipo["diferencia_goles"] = CalcularDiferenciaGoles(equipo)

        equipos.append(equipo)

        dictEquipos[fila["equipo"]] = {
            "ganados": equipo["ganados"],
            "empatados": equipo["empatados"],
            "perdidos": equipo["perdidos"],
            "goles_favor": equipo["goles_favor"],
            "goles_contra": equipo["goles_contra"],
            "puntos": equipo["puntos"],
            "diferencia_goles": equipo["diferencia_goles"]
        }


lider = liderTabla(equipos)

print("Lider de la tabla:")
print("Equipo:", lider["nombre"])
print("Ganados:", lider["ganados"])
print("Empatados:", lider["empatados"])
print("Perdidos:", lider["perdidos"])
print("Puntos:", lider["puntos"])
print("Diferencia de goles:", lider["diferencia_goles"])


with open("output/equiposChampionsSalida.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)

    escritor.writerow(
        [
            "equipo",
            "ganados",
            "empatados",
            "perdidos",
            "goles_favor",
            "goles_contra",
            "puntos",
            "diferencia_goles"
        ]
    )

    for key, value in dictEquipos.items():
        print(key, value)

        escritor.writerow(
            [
                key,
                value["ganados"],
                value["empatados"],
                value["perdidos"],
                value["goles_favor"],
                value["goles_contra"],
                value["puntos"],
                value["diferencia_goles"]
            ]
        )