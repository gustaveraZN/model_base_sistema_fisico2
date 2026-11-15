# Caminho: formal_verification/safety_supervisor.py

def verify_safety_deadline():
    # Parâmetros de tempo definidos no desafio
    sensor_delay_max = 20.0   # ms (atraso máximo do sensor de proximidade)
    rtos_jitter_max = 2.0     # ms (perda de ciclo por jitter do RTOS)
    control_cycle = 0.2       # ms (orçamento de tempo de execução por ciclo)
    
    # Prazo limite exigido pela ISO/TS 15066 (REQ-SAFE-AA-001)
    deadline_limit = 100.0    # ms[cite: 3]
    
    # Pior caso possível (Worst-Case Execution Time - WCET)
    worst_case_time = sensor_delay_max + rtos_jitter_max + control_cycle
    
    print(f"--- VERIFICAÇÃO FORMAL DE PRAZO (REQ-SAFE-AA-001) ---")
    print(f"Atraso máximo do sensor: {sensor_delay_max} ms")
    print(f"Jitter máximo do RTOS: {rtos_jitter_max} ms")
    print(f"Tempo de execução do ciclo: {control_cycle} ms")
    print(f"Tempo total de resposta no pior caso: {worst_case_time} ms")
    print(f"Prazo limite exigido: {deadline_limit} ms")
    
    if worst_case_time <= deadline_limit:
        print("[SUCESSO] O requisito formal de segurança foi ATENDIDO com margem segura.")
    else:
        print("[FALHA] O prazo foi violado.")

if __name__ == "__main__":
    verify_safety_deadline()
    