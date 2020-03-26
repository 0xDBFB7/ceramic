# assumes emissivity=1, no reflection.

import numpy as np
import math

specific_heat = 451 # J / kg K
thermal_conductivity = 30 # W/(m-k)
support_cross_section_area = 0.5

stefan_boltzmann_constant = 5.670e-8


num_layers = 4

layer_height = 0.115

layer_thickness = 0.001
layer_gap = 0.001
start_radius = (0.07/2.0)

def radius(n):
	return start_radius + (layer_thickness+layer_gap)*n


temperature = [1600.0,273.0,273.0,273.0]

timestep = 0.01
end_time = 4

volume = []
for layer in range(0, num_layers):
	volume.append(((math.pi*((radius(layer)+layer_thickness)**2))-(math.pi*(radius(layer)**2.0)))*layer_height)

for t in np.arange(0, end_time, timestep):
	for layer in range(0, num_layers):

		surface_area = 2.0*math.pi*(radius(layer))*layer_height


		radiated_power = stefan_boltzmann_constant*surface_area*(temperature[layer]**4.0)

		if(layer):
			delta_t = (temperature[layer-1]-temperature[layer])
			conducted_power = delta_t*thermal_conductivity*surface_area/layer_gap

			temperature[layer-1] += (0.5*(radiated_power+conducted_power)*timestep)/(specific_heat*volume[layer-1])

		if(layer < num_layers-1):
			delta_t = (temperature[layer+1]-temperature[layer])
			conducted_power = delta_t*thermal_conductivity*surface_area/layer_gap

			temperature[layer+1] += (0.5*(radiated_power+conducted_power)*timestep)/(specific_heat*volume[layer+1])

		temperature[layer] -= (radiated_power)/(specific_heat*volume[layer])

	print(temperature)





