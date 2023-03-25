import { ethers } from "hardhat";
import {Foam} from '../typechain-types/contracts/Foam'
async function main() {
  
  const foam = await ethers.getContractFactory("foam");
  const Foam = await foam.deploy();

  await Foam.deployed();

  console.log(
    `Foam deployed to ${Foam.address}`
  );
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
