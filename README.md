# Inflação e Perturbações Escalares — Mukhanov–Sasaki

Este projeto simula a evolução de perturbações escalares em um campo inflacionário no universo primordial, resolvendo numericamente a equação de **Mukhanov–Sasaki** para obter o **espectro de potência primordial** \( P_{\mathcal{R}}(k) \) e estimar o **índice espectral** \( n_s \). É um experimento computacional de cosmologia baseado nos fundamentos de teoria quântica de campos em espaço-tempo curvo.

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## Motivação

Durante a inflação, flutuações quânticas do campo escalar são amplificadas e congeladas como perturbações de densidade. Essas perturbações evoluem e deixam sua marca no **fundo cósmico de micro-ondas (CMB)** e na formação de estruturas em larga escala. A variável \( u_k \) governa essas perturbações, e sua dinâmica é determinada pela equação:

\[
u_k'' + \left( k^2 - \frac{z''}{z} \right) u_k = 0
\]

com:

\[
z = \frac{a \dot{\phi}}{H}
\]

---

## Estrutura do Projeto

```bash
inflacao_pertubacao/
├── notebooks/                  # Notebooks Jupyter com simulações
│   ├── 01_background_formalism.ipynb
│   ├── 02_mukhanov_sasaki_numeric.ipynb
│   └── 03_power_spectrum_analysis.ipynb
├── src/                        # Código-fonte em Python
│   └── perturbation_equations.py
├── figures/                    # Gráficos salvos
│   └── power_spectrum_plot.png
├── requirements.txt            # Dependências do projeto
└── README.md                   # Este arquivo


 Como Executar
1. Clone o repositório
bash
Copiar
Editar
git clone https://github.com/belemcrizan/inflacao_pertubacao.git
cd inflacao_pertubacao
2. Crie e ative o ambiente virtual
bash
Copiar
Editar
python -m venv .venv
.venv\Scripts\activate        # Windows
# ou
source .venv/bin/activate     # Linux/macOS
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Rode os notebooks
bash
Copiar
Editar
jupyter lab
Abra o notebook 03_power_spectrum_analysis.ipynb e execute as células.

 Resultados
Simulação numérica da equação de Mukhanov–Sasaki

Espectro de potência primordial 
𝑃
𝑅
(
𝑘
)
P 
R
​
 (k)

Estimativa do índice espectral 
𝑛
𝑠
n 
s
​
 


🖼 Exemplo de gráfico gerado:
![image](https://github.com/user-attachments/assets/0ab9b0cf-1902-4af4-9790-9c70d3bd1624)

 Referências
D. Baumann, Cosmology (Lecture Notes), 2022

V. Mukhanov, Physical Foundations of Cosmology, Cambridge University Press, 2005

Planck Collaboration, Planck 2018 Results. X. Constraints on Inflation, arXiv:1807.06211

 Autor
Crizan Belém Ribeiro
IFT/UNESP
📧 belemcrizan@gmail.com
🔗 linkedin.com/in/belemcrizan


