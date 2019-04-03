import math
import matplotlib.pyplot as plt

n = 100

print("Com uma lista de %d elementos"%n)
print("Busca linear = %d"%n)
print("Busca binaria = %d"%(math.log2(n)+ 1))


n = list(range(1,n))
p = [math.log2(i)+1 for i in n]

plt.title("Performance busca linear x busca binaria")
plt.xlabel("Quantidade de elementos")
plt.ylabel("Quantidades de verificações")
plt.plot(n,n,label="Busca linear")
plt.plot(n,p,label="Busca binaria")
plt.legend()
plt.grid()
plt.show()
