# @version ^0.3.1

'''
Contrato inteligente para el juego «Piedra, papel o tijera».
Gana o pierde faucet ether jugando.
'''

jugador: public(address)
juegoComienzo: public(uint256)
resultado: public(uint256)
finalizado: public(bool) 

@external
def __init__(_jugador: address, _juegoComienzo: uint256, _tiempoDeJuego: uint256):
    self.jugador = _jugador
    self.juegoComienzo = _juegoComienzo
    self.juegoFinal = self.juegoComienzo + _tiempoDeJuego

@external
@payable
def apuesta():
    assert block.timestamp >= self.juegoComienzo
    assert block.timestamp < self.juegoFinal