import numpy
from matplotlib import pyplot as plt

# length, number_of_nodes, time, time_step, left_temp, initial_temp, right_temp

def makeSimulation(s_B, dx, t_sim, dt, l_temp, T_A, p_temp):
  pass
  # Geometry of object 
  # s_B = 0.5           # m

  # Spatial grid 
  # dx = 0.01           # m
  nx = int(s_B/dx)+1
  x = numpy.linspace(0, s_B, nx) # line

  # Time grid 
  # t_sim = 300         # s all
  # dt = 0.5            # s step
  nt = int(t_sim/dt)

  # Material properties 
  rho = 2000          # kg/m^3 
  cp = 500            # J/kg/K
  lamda = 1           # W/m/K

  # Initial condition 
  # T_A = 293.15        # Kelvin temp

  # Define Result 
  T = numpy.ones(nx)*T_A  # finall grid 
  T[0] = l_temp
  T[-1] = p_temp

  # Simulation
  for n in range(1,nt):
    # Tn = T.copy()

    for i in range(1, len(T)-1):
      T[i] = T[i] + dt * lamda/(rho*cp) * ((T[i+1]-2*T[i]+T[i-1])/dx**2)


    # T[1:-1] = Tn[1:-1] + dt * lamda/(rho*cp) * (Tn[2:] - 2*Tn[1:-1]+ Tn[0:-2])/dx**2


    # T[0] = l_temp
    # T[-1] = 270
    # T[0] = 273.15
    # T[-1] = T[-2]


  plt.figure(figsize=(6,7), dpi=100)
  plt.xlabel('Długość [cm]')
  plt.ylabel('Temperatura [K]')
  plt.title('Nagrzewanie się elementu 1D')
  plt.grid(True)
  plt.plot(x,T,'k')
  plt.show()





