# TODO 3: Implementa bubble sort O(n^2)
def bubble_sort(xs:List[int]) -> List[int]:
    xs = xs[:]  # no mutar entrada
    n = len(xs)
    for i in range(n):
        for j in range(0, n-i-1):
            if xs[j] > xs[j+1]:
                xs[j], xs[j+1] = xs[j+1], xs[j]
    return xs

# Tests rápidos
arr = [5,1,4,2,8]
assert bubble_sort(arr) == sorted(arr)
xs = list(range(10))
assert binary_search(xs, 7) == 7
assert linear_search(xs, 7) == 7
print("OK: funciones base listas.")
# Experimento: medir tiempos para distintos n
sizes = [1_000, 5_000, 10_000, 20_000]
print("== Búsqueda lineal vs binaria ==")
for n in sizes:
    data = sorted(rand_list(n, unique=True))
    target = data[-1]  # peor caso aprox. para lineal
    mean_lin, s_lin = timeit(linear_search, data, target, repeat=7)
    mean_bin, s_bin = timeit(binary_search, data, target, repeat=7)
    print(f"n={n:>7}  linear≈{mean_lin:.6f}s  binary≈{mean_bin:.6f}s")


print("\n== Bubble sort (n^2) vs sort nativo (≈n log n) ==")
sizes2 = [500, 1_000, 2_000]  # bubble es costoso
for n in sizes2:
    data = rand_list(n, unique=True)
    mean_bub, _ = timeit(bubble_sort, data, repeat=3)
    mean_timsort, _ = timeit(sorted, data, repeat=3)  # Timsort de Python: O(n log n) en promedio
    print(f"n={n:>7}  bubble≈{mean_bub:.6f}s  sorted()≈{mean_timsort:.6f}s")
# Datos de ejemplo obtenidos de la celda anterior (ajusta si tienes otros valores):
sizes2 = [1000, 5000, 10000, 20000]#sizes = [1_000, 5_000, 10_000, 20_000]
mean_bub = []
mean_timsort = []
for n in sizes2:
    data = sorted(rand_list(n, unique=True))
    print(f"\nLista ordenada de {n} elementos")
    target = data[-1]  # peor caso aprox. para lineal
    mean_lin, s_lin = timeit(linear_search, data, target, repeat=7)
    mean_bin, s_bin = timeit(binary_search, data, target, repeat=7)
    mean_bub.append(mean_lin)
    mean_timsort.append(mean_bin)

fig = go.Figure()
fig.add_trace(go.Scatter(x=sizes2, y=mean_bub, mode='lines+markers', name='lineal (O(n))'))
fig.add_trace(go.Scatter(x=sizes2, y=mean_timsort, mode='lines+markers', name='binario (O(log n))'))
fig.update_layout(title='Comparación de tiempos: Búsqueda Lineal vs Búsqueda Binaria',
                  xaxis_title='Tamaño de la lista (n)',
                  yaxis_title='Tiempo promedio (s)',
                  legend=dict(x=0.01, y=0.99))    