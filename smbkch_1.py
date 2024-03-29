import hashlib
import json
from time import time



class Block(object):

    def __init__(self, index, proof_number, previous_hash, data, timestamp=None):

        self.index = index

        self.previous_hash = previous_hash

        self.transactions = transactions

        self.timestamp = timestamp or time.time()


 @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        
        :param block: Block
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        
        block_string = json.dumps(block, sort_keys=True).encode()
        
        return hashlib.sha256(block_string).hexdigest()
        
    def hash(transaction):
        """
        Creates a SHA-256 hash of a transaction
        
        :param block: transaction
        """
        transaction_string = json.dumps(transaction, sort_keys=True).encode()
        
        return hashlib.sha256(transaction_string).hexdigest()

@property
    
    def last_block(self):
        
        return self.chain[-1]



class Smart_Blockchain:
    
    def __init__(self):
        
        self.current_transactions = []
        
        self.chain = []
        
        self.nodes = set()

        self.build_genesis()
        
    def build_genesis(self):       # Create the genesis block
        
        self.new_block(previous_hash='1')

    def new_block(self, previous_hash):
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

        self.chain.append(block)
        
        return block
        
    @staticmethod
    
     def confirm_validity(block, previous_block):
           
           if last_block.index + 1 != block.index:

            return False

        elif last_block.hash != block.previous_hash:

            return False

        elif block.timestamp <= last_block.timestamp:

            return False

        return True
        
        
    def get_data(self, sender, receiver, amount):

        self.current_data.append({

            'sender': sender,

            'receiver': receiver,

            'amount': amount

        })

        return True
        
        
 blockchain = Smart_BlockChain()

        
        
    
          
          
           
           
    
    
    
    



    def create_node(self, address):

        self.nodes.add(address)

        return True

    @staticmethod

      
   
   
        
        

   


   
        
        

     def new_transaction(self,id ,hash,time,sender_public,sender_private,recipient,amount):
  """
        Creates a new transaction to go into the next mined Block
        :param sender: Address of the Sender
        :param amount_send: The amount sent by the sender
        :param bpsc: Address of the Smart contract (bpsc)
        :param amount_bpsc: The amount received by bpsc (Transaction fees)
        :param recipient: Address of the Recipient
        :param amount_receive: The amount received by the recipient
        :return: The index of the Block that will hold this transaction
        """
  
  
  
  
  
  transaction = {
            'id':str(os unrandom(32)),
            'hash': hash(id,data), 
            
            'data': {
                "inputs": [ #a previous  unspent transaction 
                    {
                     "transaction": previous_unspent_output_hash, # transaction hash taken from a previous unspent transaction output (64 bytes)
                     "index": previous_unspent_output_index, # index of the transaction taken from a previous unspent transaction output
                     "amount": self.amount, # amount of lios
                     "address": self.address, # from address (64 bytes)
                     "signature": signature_data(transaction_input) # transaction input hash: sha256 (transaction + index + amount + address) signed with owner address's secret key (128 bytes)
                    }
            ],
    
        
        
                "outputs": [  #Transaction outputs
                    {
                        "fees": amount * 0.0005, #amount of lios taken
                        "bpsc": 'bpsc_wallet_address', # Block Producer Smart Contract (bpsc)
                    },
                    {
                        "final_amount": amount * 0.9995, # amount of lios received
                        "address": self.recipient_address # address of the recipient
                    },
                    {
                        "refund_amount": input[amount] - output["fees"] - output["final_amount"] ,
                        "address": self.sender,
                    }
            
             ]
             
             "informations" : {
            
            'sender': self.new_address,
            'amount_send': amount,
            'bpsc': 'bpsc_wallet_address', # Block Producer Smart Contract (bpsc)
            'amount_bpsc': amount * 0.0005, # Transaction fees
            'time': str(datetime.datetime.now())
            'recipient': recipient_address,
            'amount_receive': amount * 0.9995,
            'index' : self.last_block['index'] + 1
            }
           
           
        })
   
          "crypted_transaction" : [
              'signature' : signature(data) ,
              'cipher_tras' : encrypt_aes(data, random_key),
              'cipher_key' : encrypt_rsa(random_key, recipient_address),
          ]
      
   } 
.......................


self.current_transactions.append(transaction)
      return transaction
   
      return self.last_block['index'] + 1
        
 
