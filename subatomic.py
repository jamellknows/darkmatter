import pandas as pd 
import math 
# Define a dataset of subatomic particles and their masses
subatomic_particles = {
    'Electron': 0.511,
    'Muon': 105.7,
    'Tau': 1776.86,
    'Up Quark': 2.2,
    'Down Quark': 4.7,
    'Charm Quark': 1275,
    'Strange Quark': 95,
    'Top Quark': 173210,
    'Bottom Quark': 4180,
    'Photon': 0,
    'Z Boson': 91187.6,
    'W Boson': 80419,
    'Higgs Boson': 125.1
    # ... add more particles as needed
}

# Display the dataset
planck_length = 1.616e-35
number_of_faces = []
for particle in subatomic_particles.values():
    if particle == 0:
        particle = 1
    print(planck_length)
    value = [particle, particle/planck_length]
    nf = particle/planck_length
    gravity = 8 * math.pi * particle*((3*10**8)**2) * (6.67430*10**(-11))/((3*10**8)**4)
    point = gravity/nf
    print(f"The number of faces is {nf}")
    print(f"The force of gravity is {gravity}")
    print(f"For this particle the point nf is {point}")
    number_of_faces.append(math.sqrt(particle/planck_length))

print(number_of_faces)

    
    