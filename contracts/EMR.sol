// SPDX-License-Identifier: MIT

pragma solidity ^0.8;

import "@openzeppelin/contracts/access/Ownable.sol";

contract HealthRecord is Ownable {
    struct UserDetails {
        string privateKey;
        string hashData;
        bool isActive;
    }

    event RetrieveHashData(address indexed _from, string indexed _ethToken);
    event RetrievePrivateKey(address indexed _from, string indexed _ethToken);

    mapping(string => UserDetails) patient; // Unique Token to UserDetails

    function getUserKey(string memory _ehToken)
        public
        onlyOwner
        returns (string memory)
    {
        require(patient[_ehToken].isActive, "No Patient Found!");
        emit RetrievePrivateKey(msg.sender, _ehToken);
        return patient[_ehToken].privateKey;
    }

    function getUserHashData(string memory _ehToken)
        public
        returns (string memory)
    {
        require(patient[_ehToken].isActive, "No Patient Found!");
        emit RetrieveHashData(msg.sender, _ehToken);
        return patient[_ehToken].hashData;
    }

    function addUserKey(string memory _ehToken, string memory _privateKey)
        public
        onlyOwner
    {
        patient[_ehToken].privateKey = _privateKey;
        patient[_ehToken].isActive = true;
    }

    function addUserHash(string memory _ehToken, string memory _userHash)
        public
        onlyOwner
    {
        // require userHash
        require(patient[_ehToken].isActive, "No Patient Found!");
        patient[_ehToken].hashData = _userHash;
    }
}
