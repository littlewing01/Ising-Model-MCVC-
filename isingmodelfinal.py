import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap


def Matrix(n):
    spin = [-1, 1]
    og_matrix = np.random.choice(spin, size=(n, n))
    return og_matrix


def delA(M, i, j, J):
  #we use %n so that we can model a larger grid and not worry about the edges of the lattice
  Eij= J*(M[i,j]*(M[(i+1)%n,j]+M[(i-1)%n,j]+M[i,(j+1)%n]+M[i,(j-1)%n]))
  return 2*Eij


def Probability(delA, Kb, T):
    P = np.exp(-delA / (Kb * T))
    return min(1, P)


def Energy(M, J):
    energy = 0
    for i in range(n):
        for j in range(n):
            energy += -J * M[i, j] * (M[(i+1) % n, j] + M[i, (j+1) % n])
    return energy


Kb = 1
T = np.linspace(0.1, 4, 100)
J = 1
sweep = 1000

n = int(input("Enter size of matrix"))
M = Matrix(n)
temp_mag = []
temp_energy = []
temp_susceptibility = []
temp_heat = []


for temp in T:

    Magnetisation = []
    Energies = []

    for s in range(sweep):

        
        for x in range(n**2):

            i = np.random.randint(0, n)
            j = np.random.randint(0, n)

            P = Probability(delA(M, i, j, J), Kb, temp)

            if np.random.random() < P:
                M[i, j] *= -1

        
        magnetisation = np.sum(M)
        m = magnetisation / n**2
        Magnetisation.append(m)

        energy = Energy(M, J)
        e = energy / n**2

        Energies.append(e)
        
    Magnetisation = np.array(Magnetisation)
    Energies = np.array(Energies)

    temp_mag.append(np.mean(np.abs(Magnetisation)))
    temp_energy.append(np.mean(Energies))

    susceptibility = (n**2 / (Kb * temp)* (np.mean(Magnetisation**2)- np.mean(np.abs(Magnetisation))**2))
    temp_susceptibility.append(susceptibility)

    specific_heat = (n**2 / (Kb * temp**2) * (np.mean(Energies**2) - np.mean(Energies)**2))
    temp_heat.append(specific_heat)

fig, ax = plt.subplots(2, 2, figsize=(12, 9))

ax[0, 0].plot(T, temp_mag, linestyle="-")
ax[0, 0].axvline(x=2.269,linestyle="--",label="Theoretical $T_c$")
ax[0, 0].set_xlabel("Temperature")
ax[0, 0].set_ylabel("Magnetisation per spin")
ax[0, 0].set_title("Magnetisation vs Temperature")


ax[0, 1].plot(T, temp_energy)
ax[0, 1].axvline(x=2.269, linestyle="--",label="Theoretical critical temperature")
ax[0, 1].set_xlabel("Temperature")
ax[0, 1].set_ylabel("Energy per spin")
ax[0, 1].set_title("Energy vs Temperature")



ax[1, 0].plot(T, temp_susceptibility)
ax[1, 0].axvline(x=2.269,linestyle="--", label="Theoretical critical temperature")
ax[1, 0].set_xlabel("Temperature")
ax[1, 0].set_ylabel("Magnetic Susceptibility")
ax[1, 0].set_title("Magnetic Susceptibility vs Temperature")



ax[1, 1].plot(T, temp_heat)
ax[1, 1].axvline(x=2.269,linestyle="--", label="Theoretical critical temperature")
ax[1, 1].set_xlabel("Temperature")
ax[1, 1].set_ylabel("Specific Heat")
ax[1, 1].set_title("Specific Heat vs Temperature")


plt.tight_layout()
plt.show()


fig, ax = plt.subplots()

cmap = ListedColormap(["cyan", "magenta"])

image = ax.imshow(M,cmap=cmap,vmin=-1,vmax=1,interpolation="nearest")

Temperature = float(input("Enter a temperature for animation: "))

def animate(sweep):
  for x in range(n**2):
        
        i = np.random.randint(0, n)
        j = np.random.randint(0, n)
        P = Probability(delA(M, i, j, J), Kb, Temperature)
        
        if np.random.random() < P:
          M[i,j] *= -1
  image.set_data(M)
  return (image,)

anim = FuncAnimation(fig,animate,frames=200,interval=50,blit=True)

plt.show()