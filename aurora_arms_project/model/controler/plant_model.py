# Caminho: model/plant_model.py
import numpy as np

def run_plant_model():
    # Parâmetros físicos do AuroraArm
    R = 0.8         # Ohms[cite: 2]
    L = 1.2e-3      # Henries (1.2 mH)[cite: 2]
    Kt = 0.085      # N.m/A[cite: 2]
    Ke = 0.085      # V.s/rad[cite: 2]
    J = 4.2e-4      # kg.m^2[cite: 2]
    b = 1.5e-4      # N.m.s/rad[cite: 2]
    
    # Matrizes de Espaço de Estados (x_dot = A*x + B*u, y = C*x)
    A = np.array([[-R/L, -Ke/L],
                  [Kt/J, -b/J]])
                  
    B = np.array([[1/L],
                  [0]])
                  
    C = np.array([[0, 1]]) # Saída: velocidade angular (omega)
    D = np.array([[0]])
    
    print("Matriz A:\n", A)
    print("Matriz B:\n", B)
    
    # Cálculo dos autovalores para verificar as constantes de tempo
    eigenvalues = np.linalg.eigvals(A)
    print("Autovalores de A:", eigenvalues)
    
    tau_e = L / R
    tau_m = J / b
    print(f"Constante de tempo elétrica (tau_e): {tau_e*1000:.2f} ms")
    print(f"Constante de tempo mecânica (tau_m): {tau_m:.2f} s")

if __name__ == "__main__":
    run_plant_model()