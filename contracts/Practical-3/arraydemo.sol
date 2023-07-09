pragma solidity ^0.5.0;
contract arraydemo
{
    //Static Array
    uint[6] arr2=[10,20,30];
    function disp() public view returns(uint[6] memory)
    {
        return arr2;
    }

   
}