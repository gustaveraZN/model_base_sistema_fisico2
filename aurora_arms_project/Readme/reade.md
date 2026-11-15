# Projeto: Model-Based Design para Sistemas Ciber-Físicos (AuroraArm)

Repositório estruturado para a modelagem matemática, simulação e verificação formal do sistema de controle de um braço robótico (AuroraArm), desenvolvido no contexto acadêmico.

## 📁 Estrutura do Repositório
- `generated_code/`: Contém os scripts principais de modelagem da planta do motor DC e o controlador PID com anti-windup.
- `tests/`: Contém os scripts de verificação formal de prazos e testes unitários/integração do sistema.

## ⚙️ Parâmetros do Sistema (Planta)
* **Resistência de armadura ($R$):** $0.8\ \Omega$
* **Indutância de armadura ($L$):** $1.2\ \text{mH}$
* **Constante de torque ($K_t$):** $0.085\ \text{Nm/A}$
* **Constante de f.c.e.m. ($K_e$):** $0.085\ \text{Vs/rad}$
* **Inércia refletida no eixo ($J$):** $4.2 \times 10^{-4}\ \text{kg}\cdot\text{m}^2$
* **Atrito viscoso ($b$):** $1.5 \times 10^{-4}\ \text{N}\cdot\text{m}\cdot\text{s/rad}$
* **Relação de redução ($N$):** $100$
* **Tensão máxima do barramento ($V_{max}$):** $48\ \text{V}$
* **Corrente máxima do driver ($I_{max}$):** $8\ \text{A}$
* **Período de amostragem ($T_s$):** $2\ \text{ms}$

## 🚀 Como Executar
1. Certifique-se de ter o Python instalado.
2. Instale as dependências necessárias:
   ```bash
   pip install numpy scipy