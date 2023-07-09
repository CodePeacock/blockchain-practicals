pragma solidity ^0.5.0;
contract arraydemo
{
    //Static Array
    uint[6] arr2=[10,20,30];
    //Dynamic Array
    uint x=5;
    uint [] arr1;
    
    function disp() public view returns(uint[6] memory)
    {
        return arr2;
    }

    function arraydemo() public
    {
        while(x>0)
        {
            arr1.push(x);
            x=x-1;
        }
    }

    function disp() public view returns(uint[] memory)
    {
        return arr1;
    }
}