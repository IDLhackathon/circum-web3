# circum-web3
implementation concerning the smart contract side of project.  These contract will work primarily on: 

1.  FOAM proof of location, where user will submit the picture (represented by their address with hash) along with the location,

2. And then based on the prediction of the DL, we will be updating the score from the model corresponding to the each submission, thus giving crediblity to the submitters information.

3. Also it uses the ocean protocol in order to create datamarkets and adding of the user images as NFT.

## setup 

1. set `.env` parameters 


TODO: 

```mermaid

stateDiagram
    User --> application: registers the account 




```


# deployment of the  contracts 

following are the configuration of the contracts (ocean along with ) : 

```json
{
  "mumbai": {
    "chainId": 80001,
    "Ocean": "0xd8992Ed72C445c35Cb4A2be468568Ed1079357c8",
    "OPFCommunityFeeCollector": "0x7F50f017a431a2e8Fffbdf8689fE79A8E05921ac",
    "veOCEAN": "0x13B6c0655c549CFb974B26F06D474fa57d0705b6",
    "veAllocate": "0xc838F968F3b1bFF9c11dD6bC9490524ae77FF2aA",
    "veDelegation": "0xE47e917CD1EFB49b04f1e5F8D74FEBFDB77ad46C",
    "veFeeDistributor": "0x9A069D299929a28488Dd707eB7C729e5AE4535DB",
    "veDelegationProxy": "0xE2fb0e1f7348a54cfD9795d5c65D36DFD33A04FA",
    "veFeeEstimate": "0x54f9fF36DAddd4DAC2454b33B3BE459d1149c0bf",
    "SmartWalletChecker": "0xBe717A349f2187B8B3ddBe8a6cA9a66c4ac13257",
    "DFRewards": "0xf278a4b9F486DDF112ed68821A30B498e7318cA1",
    "DFStrategyV1": "0x609B5d0352A7BAC121059972454DB3F2A697D1F7",
    "foam": "0xeb1C79E2632acf0c699C27c58e4e7D4557A60cF7"
  }
}
```