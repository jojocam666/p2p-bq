Wallet=[
    {
        "id": os unrandom(32), # random id (64 bytes)
        "passwordHash": hash(password), # hash taken from password: sha256 (password) (64 bytes)
        "secret": hash2(salt, passwordHash, random_factor) # pbkdf2 secret taken from password hash: sha512 (salt + passwordHash + random factor)
        "keyPairs": [
            {
                "index": 1,
                "secretKey": "6acb83e364...ee6bcdbc73", # EdDSA secret key generated from the secret (1024 bytes)
                "publicKey": "dda3ce5aa5...b409bf3fdc" # EdDSA public key generated from the secret (64 bytes) (also known as address)
            },
            {
                "index": 2,
                "secretKey": "072ab010ed...246ed16d26", # EdDSA secret key generated from pbkdf2 (sha512 (salt + passwordHash + random factor)) over last address secret key (1024 bytes)
                "publicKey": "4f8293356d...b53e8c5b25"  # EdDSA public key generated from the secret (64 bytes) (also known as address)
            }     
        ]
    }
]








class Wallet:
     def __init__(self, private_key = None):

        if private_key == None:

            self.private_key = self.new_private_key()

        else:

            self.private_key = private_key

        self.address_uncompressed = None

        self.address_compressed = None

        self.wif_uncompressed = None

        self.wif_compressed = None
        
    def new_private_key(self):

        return os.urandom(32)
 
    def sha256(data):

        digest = hashlib.new("sha256")

        digest.update(data)

        return digest.digest()

    def ripemd160(data):

        digest = hashlib.new("ripemd160")

        digest.update(data)

        return digest.digest()
        
def b58(data):

    B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    if data[0] == 0:

        return "1" + b58(data[1:])

    x = sum([v * (256 ** i) for i, v in enumerate(data[::-1])])

    ret = ""

    while x > 0:

        ret = B58[x % 58] + ret

        x = x // 58

    return ret

 class ECDSAPoint:

    def __init__(self,

        x=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,

        y=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,

        p=2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1):

        self.x = x

        self.y = y

        self.p = p



    def __add__(self, other):

        return self.__radd__(other)



    def __mul__(self, other):

        return self.__rmul__(other)



    def __rmul__(self, other):

        n = self

        q = None

        for i in range(256):

            if other & (1 << i):

                q = q + n

            n = n + n

        return q



    def __radd__(self, other):

        if other is None:

            return self

        x1 = other.x

        y1 = other.y

        x2 = self.x

        y2 = self.y

        p = self.p

        if self == other:

            l = pow(2 * y2 % p, p-2, p) * (3 * x2 * x2) % p

        else:

            l = pow(x1 - x2, p-2, p) * (y1 - y2) % p

        newX = (l ** 2 - x2 - x1) % p

        newY = (l * x2 - l * newX - y2) % p

        return ECDSAPoint(newX, newY)



    def toBytes(self, compressed):

        x = self.x.to_bytes(32, "big")

        y = self.y.to_bytes(32, "big")

        if compressed:

            if (self.y % 2) == 0:

                return b"x02" + x

            else:

                return b"x03" + x

        else:

            return b"x04" + x + y

   def get_address(self, compressed):

        SPEC256k1 = ECDSAPoint()

        pk = int.from_bytes(self.private_key, "big")

        hash160 = ripemd160(sha256((SPEC256k1 * pk).toBytes(compressed)))

        address = b"x00" + hash160

        address = b58(address + sha256(sha256(address))[:4])

        return address


    def get_address_uncompressed(self):

        if self.address_uncompressed == None:

            self.address_uncompressed = self.get_address(compressed = False)

        return self.address_uncompressed
        
    def get_address_compressed(self):

        if self.address_compressed == None:

            self.address_compressed = self.get_address(compressed = True)

        return self.address_compressed
        
   def get_wif(self, compressed):

        if compressed:

            wif = b"x80" + self.private_key + b"x01"

        else:

            wif = b"x80" + self.private_key

        wif = b58(wif + sha256(sha256(wif))[:4])

        return wif
  
   def get_wif_uncompressed(self):

        if self.wif_uncompressed == None:

            self.wif_uncompressed = self.get_wif(compressed = False)

        return self.wif_uncompressed
 
 
 def get_wif_compressed(self):

        if self.wif_compressed == None:

            self.wif_compressed = self.get_wif(compressed = True)

        return self.wif_compressed
        
   
  
   
   
   
 
       
       
 ......................
 
  wallet = Wallet;
 
    def node_get_public_key(self):
       
       if self.node_public_key == None     
       
          self.node_public_key = address
       
       return self.node_public_key
       
  def get_new_spend_address(self):
    
    random_seed = os.unrandom(32)
    
    spend_address = b58(address + sha256(sha256(random_seed))[:4])
    
    return spend_address

  
  def get_spend_key(self):
  
    spend_key = self.private_key
    
    return spend_key
    
  def get_view_key(self):
    
    view_key = self.address
    
    return view_key
    
 def get_key_ring(self, address, private_key, view_key) :
   
    a = self.get_private_key
    
    b = self.get_address
    
    key_ring= [a,b]
    
    return key_ring


def new_wallet(self):
    
    return get_key_ring()

...........................................



