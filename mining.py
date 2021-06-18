
import time









def block_mining(self, details_miner):

            self.get_data(

            sender="0", #it implies that this node has created a new block

            receiver=details_miner,

            quantity=1, #creating a new block (or identifying the proof number) is awarded with 1

        )

        
       def mining_block(self, previous_hash):
        """
        Create a new Block in the Smart Blockchain
        :param previous_hash: Hash of previous Block
        :return: New Block
        """

        block = Block(
            
            'index': len(self.chain) + 1,
            
            'timestamp': time() or str(datetime.datetime.now()),
            
            'transactions': self.current_transactions,
            
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        )

        # Reset the current list of transactions
        
        self.current_transactions = []

        
        def sufficient_time(self):
            
            
            start = last_block.timestamp.time()
            
            end = time.time()
            
            a = (end - start)
            
            if a = 600.00000000000000000
            
            return True
            
            else 
            
            return False
            
            
            
        if new_transaction() return True:
            
            self.current_transactions.append(new_transaction)
            
            return self.current_transactions

        if len(current_transactions) = 100
            
            return new_block(self, previous_hash, current_transactions,data)
        
       elif sufficient_time() return True 

             return new_block(self, previous_hash, current_transactions,data)

        
 




        last_block = self.latest_block

        last_hash = last_block.hash

        block = self.build_block(, last_hash)



        return vars(block)  
