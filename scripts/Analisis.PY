import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/encuesta_galletas.csv", encoding="latin1")

preferencia_sexo = df.groupby("sexo")["Preferencia"].value_counts()

print("Preferencia por sexo:\n\n", preferencia_sexo)

famchocolate = df["familiaridad_chocolate"].value_counts()
famavena = df["familiaridad_avena"].value_counts()
fammani = df["familiaridad_mani"].value_counts()


print("\n\nConteo de productos probados y conocidos:\n\n", famchocolate, "\n\n", famavena, "\n\n", fammani)

map_familiaridad = {
    "Probado": 2,
    "Oido_no_probado": 1
}

df["fam_choc_num"] = df["familiaridad_chocolate"].map(map_familiaridad)
df["fam_avena_num"] = df["familiaridad_avena"].map(map_familiaridad)
df["fam_mani_num"] = df["familiaridad_mani"].map(map_familiaridad)

print("\n\n", df[["fam_choc_num", "fam_avena_num", "fam_mani_num"]].mean())

print("\n\nPreferencia general:\n\n", df["Preferencia"].value_counts())

promedios = df[
    [

        "sabor_chocolate",
        "sabor_avena",
        "sabor_mani"
    ]
].mean()

print("\n\nPromedios\n\n", promedios)

sabor_sexo = df.groupby("sexo")[
    [

        "sabor_chocolate",
        "sabor_avena",
        "sabor_mani"
    ]
].mean()

sabor_promedios = df.groupby("Preferencia")[
    [

        "sabor_chocolate",
        "sabor_avena",
        "sabor_mani"
    ]
].mean()

print("\n\nSabores por genero:\n\n", sabor_sexo)
print("\n\nSabores por Preferencia:\n\n", sabor_promedios)

sabor_sexo.plot(kind="bar")
plt.title("Promedio por genero")
plt.ylabel("Puntaje promedio")
plt.xlabel("Producto")
plt.show()

# sabor_promedios.plot(kind="bar")
# plt.title("Promedio de sabor por producto")
# plt.ylabel("Puntaje promedio")
# plt.xlabel("Producto")
# plt.show()