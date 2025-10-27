import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
qc = QuantumCircuit(1,1) #Quantum Circuit with 1 qubit
qc.x(0)
qc.measure(0,0)
diagram = qc.draw(output='mpl')

plt.show()
