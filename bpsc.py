class Contract():
  
  def __init__(self, address, address_indexed_from, address_indexed_to, amount, execution_terms, timestamp = None):
    
    address = os.unrandom(32)
    
    self.address_indexed_from = address_indexed_from
    
    self.address_indexed_to = address_indexed_to 
    
    
