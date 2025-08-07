def devolver_distintos(n1, n2, n3):
    suma = n1 + n2 + n3
    if suma > 15:
        return max(n1, n2, n3)
    elif suma < 10:
        return min(n1, n2, n3)
    elif suma >= 10 and suma <= 15:
        if n1 < n2 and n2 < n3:
            return n2
        elif n1 > n2 and n1 < n3:
            return n1
        else:
            return n3
        
print(devolver_distintos(1, 7, 4))
        
        

