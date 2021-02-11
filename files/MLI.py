# assumes emissivity=1, no reflection.
# there's something wrong with this.

import numpy as np
import math

specific_heat = 451 # J / kg K
thermal_conductivity = 30 # W/(m-k)
support_cross_section_area = 0

stefan_boltzmann_constant = 5.670e-8



num_layers = 4

layer_height = 0.115

layer_thickness = 0.001
layer_gap = 0.001
start_radius = (0.07/2.0)

def radius(n):
	return start_radius + (layer_thickness+layer_gap)*n

input_power = 1000.0
temperature = [273.5]*num_layers

timestep = 0.0001
end_time = 5

volume = []
for layer in range(0, num_layers):
	volume.append(((math.pi*((radius(layer)+layer_thickness)**2))-(math.pi*(radius(layer)**2.0)))*layer_height)

print(volume)
for t in np.arange(0, end_time, timestep):
	for layer in range(0, num_layers):

		surface_area = 2.0*math.pi*(radius(layer))*layer_height

		radiated_power = stefan_boltzmann_constant*surface_area*(temperature[layer]**4.0)
		print(radiated_power)

		if(not layer):
			temperature[layer+1] += (1*(radiated_power)*timestep)/(specific_heat*volume[layer+1])
		else:
			if(layer > 0):
				#delta_t = (temperature[layer-1]-temperature[layer])
				#conducted_power = delta_t*thermal_conductivity*support_cross_section_area/layer_gap

				#temperature[layer] -= conducted_power

				temperature[layer-1] += (0.5*(radiated_power)*timestep)/(specific_heat*volume[layer-1])

			if(layer < num_layers-1 and layer):
				#delta_t = (temperature[layer+1]-temperature[layer])
				#conducted_power = delta_t*thermal_conductivity*support_cross_section_area/layer_gap

				#temperature[layer] -= conducted_power

				temperature[layer+1] += (0.5*(radiated_power)*timestep)/(specific_heat*volume[layer+1])

		if(not layer):
			temperature[layer] += (input_power*timestep)/(specific_heat*volume[layer])

		temperature[layer] -= (radiated_power*timestep)/(specific_heat*volume[layer])

	print("Frame ", t, temperature)
