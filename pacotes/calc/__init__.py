from pacote1.modulo1 import soma
from pacote2.modulo1 import subtracao as sub

# Implementação do design pattern façade em python

# O all permite expor as funcionalidades do pacote aqui dentro do init
# assim, quem chamar o pacote calc pode chamar diretamente as funções
# soma e sub, que são implementadas em outros subpacotes

__all__ = ['soma', 'sub']
