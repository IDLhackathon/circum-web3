import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";

import 'dotenv';

require('dotenv').config()

const config: HardhatUserConfig = {
  solidity: "0.8.18",
  networks: {
    mumbai: {
      chainId: 80001,
      url: `${process.env.INFURA_MUMBAI_RPC}` || "",
      accounts:`${process.env.PRIVATE_KEY}` !== undefined ? [`${process.env.PRIVATE_KEY}`] : [],
    }
  },
  etherscan: {
    apiKey:`${process.env.POLYGONSCAN_API_KEY}`
  }

};

export default config;
