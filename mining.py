def block_mining(self, details_miner):

            self.get_data(

            sender="0", #it implies that this node has created a new block

            receiver=details_miner,

            quantity=1, #creating a new block (or identifying the proof number) is awarded with 1

        )

        last_block = self.latest_block

        last_proof_number = last_block.proof_number

        proof_number = self.proof_of_work(last_proof_number)



        last_hash = last_block.compute_hash

        block = self.build_block(proof_number, last_hash)



        return vars(block)  
