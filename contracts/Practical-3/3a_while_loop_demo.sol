pragma solidity ^0.5.0;

contract whileDemo{
    uint[] data;
    uint8 j = 0;

    function loopDemo() public {
        while(j<5){
            j++;
            data.push(j);
        }
    }
    function display() public view returns(uint[] memory){
        return data;
    }
}