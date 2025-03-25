def maxmin_select(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    elif len(arr) == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]
    else:
        mid = len(arr) // 2
        min1, max1 = maxmin_select(arr[:mid])
        min2, max2 = maxmin_select(arr[mid:])
        return (min1 if min1 < min2 else min2), (max1 if max1 > max2 else max2)

if __name__ == "__main__":
    entrada = input("Digite uma sequência de números separados por espaço: ")
    numeros = list(map(int, entrada.strip().split()))
    minimo, maximo = maxmin_select(numeros)
    print("Mínimo:", minimo)
    print("Máximo:", maximo)
