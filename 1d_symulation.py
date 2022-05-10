import numpy
from matplotlib import pyplot 

# Geometry of object 
s_B = 0.5           # m

# Spatial grid 
dx = 0.01           # m
nx = int(s_B/dx)+1
x = numpy.linspace(0, s_B, nx) # line

# Time grid 
t_sim = 300         # s all
dt = 0.5            # s step
nt = int(t_sim/dt)

# Material properties 
rho = 2000          # kg/m^3 
cp = 500            # J/kg/K
lamda = 1           # W/m/K

# Initial condition 
T_A = 303.15        # Kelvin temp

# Define Result 
T = numpy.ones(nx)*T_A  # finall grid 

# Simulation
for n in range(1,nt):
  Tn = T.copy()

  T[1:-1] = Tn[1:-1] + dt * lamda/(rho*cp) * (Tn[2:] - 2*Tn[1:-1]+ Tn[0:-2])/dx**2

  # T[0] = 293.15
  T[0] = 273.15
  T[-1] = T[-2]


pyplot.figure(figsize=(6,7), dpi=100)
pyplot.xlabel('Długość [M]')
pyplot.ylabel('Temperatura [C]')
pyplot.title('Nagrzewanie się elementu 1D')
pyplot.grid(True)
pyplot.plot(x,T-273.15,'k')
pyplot.show()






