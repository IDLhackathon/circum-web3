// SPDX-License-Identifier: GPL-2.0-or-later
pragma solidity ^0.8.10;

import "@openzeppelin/contracts/utils/Address.sol";
//import "@Openzeppelin/contracts/"
import "./utils.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";


contract foam is AccessControl {

using Address for address;

// roles

bytes32 public constant ORACLE_ROLE = keccak256("ORACLE_ROLE");
//bytes32 public constant DEFI = keccak256("DEFI");

// STATES
address oracleAddress;
//address backendAddress; 


mapping(uint => UserInformation) userAddressInformation;
uint[] registeredUser;
//MODIFIERS.

// constructor
constructor () {
    _grantRole(ORACLE_ROLE, msg.sender);
    }

function initOracle(address _oracleAddress) public returns(bool) {
    require(hasRole(ORACLE_ROLE, msg.sender), "Caller is not the owner");
    oracleAddress = _oracleAddress;
    return true;
}

function initUserInformation(uint personId, address userAddress, bytes32 _hash ) public returns(bool) {

userAddressInformation[personId].personId = personId;
userAddressInformation[personId].userAddress = userAddress;
userAddressInformation[personId].oracleLocationInformation = _hash;
userAddressInformation[personId].applicationState = STATUS.REGISTERATION;
registeredUser.(personId);
return true;

}

function getUserInformation(uint personId) public view returns(
    uint , address, bytes32 ,  uint, STATUS) 
    {
    return (
        userAddressInformation[personId].personId,
        userAddressInformation[personId].userAddress,
        userAddressInformation[personId].oracleLocationInformation,
        userAddressInformation[personId].scoringDetails,
        userAddressInformation[personId].applicationState
    );
}

function setUserScore(uint _personId, uint scoring) public  returns(bool) {
    require(hasRole(ORACLE_ROLE, msg.sender), "Caller is not the owner");
    userAddressInformation[_personId].scoringDetails = scoring;
    return true;
}

//function payUser(uint )



}