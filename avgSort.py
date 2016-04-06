##
# Algoritmo di ordinamento che utlizza un algoritmo basato
# sul calcolo del valore medio un array di n-lunghezza
#

## Determina il valore medio di un insieme di numeri
#  @param numbers l'insieme di valori
#  @return il valore medio
#
def avg(numbers):
    return sum(numbers) / len(numbers)

## Algoritmo di ordinamento per media ricorsivo
#  @param values l'insieme di valori
#  @return una lista con i valori ordinato
#
def avgSort(values):
    if values.count(values[0]) == len(values): return [values[0]]
    vm = avg(values)
    first, second = [], []
    for i in values:
        if i <= vm:
            first.append(i)
        else:
            second.append(i)
    return avgSort(first) + avgSort(second)

