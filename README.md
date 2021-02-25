# :heavy_dollar_sign: :moneybag: Blockchain and Cryptocurrency using Python :moneybag: :heavy_dollar_sign:

**Create Virtual Environment**
```
python -m venv <env_name>
```

**Activate Virtual Env**
```
<env_name>\scripts\activate
```

**Install Required Packages**
```
pip install -r requirements.txt
```

**Run The Tests**
Make sure virtural environment is activated

```
python -m pytest backend/tests
```

<hr>

## Concepts

- The ***blockchain*** is list of blocks where each block represents a unit of storage for data. The list is called a chain because each block references the block before it, creating (chain) links between between blocks. In a blockchain that supports a cryptocurrency, blocks store transactions.

- ***Mining blocks*** refers to the process of running a computationally expensive algorithm in order to create new blocks for the blockchain. We'll expand on this in the section on Proof of Work.

- The ***genesis block*** is the first block in the blockchain. Since all blocks must reference the block that came before it, the genesis block serves as a hardcoded starter block for the chain.

- A ***hashing algorithm*** generates a unique output for every unique output. In the case of this project, we're using the **sha-256 algorithm**, which produces a unique 256 character hash in binary, and a 64 character hash in hexadecimal.

- ***Proof of work*** is a mechanism that requires miners to solve a computational puzzle in order to create valid blocks. Solving the puzzle requires a brute-force algorithm that demands CPU power (hence, the analogy of mining the block).

- The ***leading 0's requirement*** is the standard proof of work implementation for finding valid blocks. By adjusting a nonce value in the block, the miner has an infinite number of tries at generating new hashes. Once the miner finds a hash with a matching number of leading 0's as the block difficulty, the fields for valid new block have been found.

- ***Dynamic difficulty*** is a mechanism that increases or decreases the difficulty of the next block based on how long it's taking to mine the new block. If the time is exceeding an established mining rate for the system, the difficulty decreases. Likewise, if the time is still before the mine rate, the difficulty increases. This allows the blockchain to control the rate at which blocks are added.

- ***Chain validation*** is the process of ensuring that the data of an external blockchain is formatted correctly. For the blockchain to be valid, there are multiple rules to enforce. For starters, every block must be valid, with a proper hash based on the block fields, correctly adjusted difficulty, acceptable number of leading 0's in the hash for the proof of work requirement, and more. Likewise, in the blockchain itself must start with the genesis block, and every block's last hash must reference the hash of the block that came before it.

- ***Chain replacement*** is the process of substituting the current blockchain data for the data of an incoming blockchain. If the incoming blockchain is longer, and valid, then it should replace the current blockchain. This will allow a valid blockchain, with new blocks, to spread across the eventual blockchain network, becoming the true blockchain that all nodes in the blockchain network agree upon.