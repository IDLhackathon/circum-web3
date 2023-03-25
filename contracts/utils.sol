// SPDX-License-Identifier: GPL-2.0-or-later
pragma solidity ^0.8.10;

import "@openzeppelin/contracts/utils/Base64.sol";

enum STATUS {REGISTERATION, ORACLE_UPDATION}

struct UserInformation {
uint personId;
address userAddress;
bytes32 oracleLocationInformation;
address dataNFTAddress;
uint scoringDetails;
STATUS applicationState;
}

