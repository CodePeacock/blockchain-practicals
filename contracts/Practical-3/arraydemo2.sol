pragma solidity ^0.5.0;
contract arraydemo
{
    //Dynamic Array
    uint x=5;
    uint [] arr1;

    function arrayDemo() public
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