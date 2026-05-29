import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("datos/ventas.csv")
df["fecha"] = pd.to_datetime(df["fecha"])
df["total_venta"] = df["cantidad"] * df["precio"]
df["mes"] = df["fecha"].dt.to_period("M")

ventas_totales = df["total_venta"].sum()
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()
ventas_por_mes = df.groupby("mes")["total_venta"].sum()

print("=" * 45)
print("   ANÁLISIS DE VENTAS - INDICADORES")
print("=" * 45)
print(f"Ventas totales:        $ {ventas_totales:,.2f}")
print(f"Producto más vendido:  {producto_mas_vendido}")
print("\nVentas por mes:")
for mes, total in ventas_por_mes.items():
    print(f"  {mes}: $ {total:,.2f}")

fig, ax = plt.subplots(figsize=(10, 5))
ventas_por_mes.plot(kind="bar", ax=ax, color="#4C72B0", edgecolor="white")
ax.set_title("Evolución de ventas por mes", fontsize=14, fontweight="bold")
ax.set_xlabel("Mes")
ax.set_ylabel("Total de ventas ($)")
ax.tick_params(axis="x", rotation=45)
plt.tight_layout()
os.makedirs("resultados", exist_ok=True)
plt.savefig("resultados/grafico_ventas.png", dpi=150)
plt.show()
print("\nGráfico guardado en resultados/grafico_ventas.png")
