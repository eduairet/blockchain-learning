// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.13;

contract PiedraPapelTijera {

    uint public piedra = 0;
    uint public papel = 1;
    uint public tijera = 2;
    uint [3] public opciones = [piedra, papel, tijera];
    address public jugador;
    uint public seleccion;

    function hacerSeleccion(uint _seleccion) public {
        seleccion = opciones[_seleccion];
    }

    function juego() public {
        
    }

}