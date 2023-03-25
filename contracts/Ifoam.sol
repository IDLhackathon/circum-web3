
import "./utils.sol";
pragma solidity ^0.8.10;


interface Ifoam {
    function initOracle(address _oracleAddress) external returns(bool);
    function initUserInformation(uint personId, address userAddress) external returns(bool);
    function getUserInformation(uint personId) external view returns(uint , address, bytes32 ,  uint, STATUS);
}