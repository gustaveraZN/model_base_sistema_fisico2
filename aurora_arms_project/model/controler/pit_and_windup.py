# Caminho: controller/pid_anti_windup.py
import numpy as np

class PIDControllerWithAntiWindup:
    def __init__(self, kp, ki, kd, ts, v_max, i_max):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.ts = ts
        self.v_max = v_max
        self.i_max = i_max
        self.integral = 0.0
        self.prev_error = 0.0

    def compute(self, setpoint, measurement):
        error = setpoint - measurement
        
        # Termo proporcional
        p_term = self.kp * error
        
        # Termo integral com Anti-Windup condicional
        potential_integral = self.integral + error * self.ts
        
        # Termo derivativo
        d_term = self.kd * (error - self.prev_error) / self.ts
        
        # Saída prévia de controle (tensão)
        u_unconstrained = p_term + self.ki * potential_integral + d_term
        
        # Saturação do atuador (Barramento de 48V)
        if u_unconstrained > self.v_max:
            u_constrained = self.v_max
            # Congela o integrador (Anti-Windup)
        elif u_unconstrained < -self.v_max:
            u_constrained = -self.v_max
            # Congela o integrador (Anti-Windup)
        else:
            u_constrained = u_unconstrained
            self.integral = potential_integral  # Atualiza apenas se não saturoteu
            
        self.prev_error = error
        return u_constrained

if __name__ == "__main__":
    # Teste rápido do controlador no ponto de operação
    pid = PIDControllerWithAntiWindup(kp=1.2, ki=15.0, kd=0.01, ts=0.002, v_max=48.0, i_max=8.0)
    control_signal = pid.compute(setpoint=450.0, measurement=0.0)
    print(f"Sinal de controle inicial gerado: {control_signal:.2f} V")