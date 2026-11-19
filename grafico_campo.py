import matplotlib.pyplot as plt

# Fórmula do módulo: E(r) = k. Q/r², com Q = 1C e r entre r entre 0,10 e 1,00 m.


# Constantes físicas (mesmos valores do relatório em LaTeX)
k = 8.99e9   # N·m²/C²
q1 = 1    # 1C

# Distâncias de 0,10 m até 1,00 m (passo de 0,01 m)
distancias = [0.10 + i * 0.01 for i in range(91)]
campos = [k * q1 / (r ** 2) for r in distancias]

plt.figure(figsize=(6, 4))
plt.plot(distancias, campos, color="tab:blue", linewidth=2)
plt.title("Campo Elétrico vs. Distância (Lei de Coulomb)")
plt.xlabel("Distância r (m)")
plt.ylabel("Campo Elétrico E (N/C)")
plt.grid(True)
plt.tight_layout()
plt.savefig("campo_coulomb.png", dpi=150)
print("Gráfico salvo em campo_coulomb.png!")