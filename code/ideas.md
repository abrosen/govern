Thinking about an abstraction of a blockchain:

A "block" is an atomic set of changes to a shared state and a reference to a previous block or state.

A "block chain" is a series of blocks such that:
  - Any system, that processed each block in order would have the same state
  - at every given moment, the criteria for deeming a new block is valid is part of the state

"Governance" in this context refers to managing authority over what new blocks can be generated and accepted by other users.

In a simple example, a blockchain with a "dictator" would establish the chain with the critera
that new blocks can only be accepted if they contain a valid signature.

Right now, the criteria for acceptable blocks is hard coded into the software that manages such block chains, we propose a superset of a blockchain system that we call a Nomic chain that contains encoded within it the critera required to accept new blocks.
