// SPDX-License-Identifier: MIT
pragma solidity 0.5.17;

contract Payment {
    address transferFrom;
    address transferTo;
    uint256 paymentAmount;

    constructor() public {
        transferFrom = msg.sender;
    }

    event TransferFund(
        address _transferTo,
        address _transferFrom,
        uint256 amount
    );

    function transferFund(address _transferTo) public payable returns (bool) {
        transferTo = _transferTo;
        address payable recipient = address(uint160(transferTo));
        recipient.transfer(msg.value);

        emit TransferFund(transferTo, transferFrom, msg.value);

        return true;
    }

    function getBalanceOfCurrentAccount() public view returns (uint256) {
        return transferFrom.balance;
    }
}
