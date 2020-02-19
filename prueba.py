import h5py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
archivos = [1,3,7,10]
filename = 'velocity_AbacusCosmos_720box_planck_00_0_FoF_vmax_300.0_sigma_{}.0_nside_360.hdf5'
divergencias = []
velocidades = []

datos_seleccionados = []
for i in archivos:
    with h5py.File(filename.format(i), 'r') as f:
        #divergence = list(f.keys())[0]
        vel_x = list(f.keys())[1]
        vel_y = list(f.keys())[2]
        vel_z = list(f.keys())[3]

        #dataDivergence = list(f[divergence])
        data_vel_x = np.array(f[vel_x])
        data_vel_y = np.array(f[vel_y])
        data_vel_z = np.array(f[vel_z])
    velocidades.append(np.sqrt(data_vel_x**2 + data_vel_y**2 + data_vel_z**2))
    #divergencias.append(dataDivergence)

    #aleatorio = np.random.randint(0,360)
    #datos_seleccionados.append(np.array(dataDivergence[aleatorio])[:120,:120])

#lt.figure(figsize = (10,10))
#for i in range(4):
#    plt.subplot(2,2,i+1)
#    plt.imshow(datos_seleccionados[i])
#    plt.colorbar()
#    plt.title(r"$\sigma_(V_(ox)) $ = {}vx".format( archivos[i]))

#plt.savefig("grafica.png")

plt.figure(figsize = (10,10))
for i in range(4):
    #vel_actual = []
    #inicio = 0
    #for j in velocidades[i]:
    #    if(inicio == 0):
    #        vel_actual = j
    #        inicio += 1
    #    else:
    #        vel_actual = np.concatenate((vel_actual,j))
    plt.subplot(2,2,i+1)
    plt.hist(velocidades[i][180], bins = 1000)
    plt.title(r"$\sigma_(V_(ox)) $ = {}vx".format(archivos[i]))

plt.savefig("grafica2.png")