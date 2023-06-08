from hashlib import md5 as hash
import json

# in bits
BLOCK_SIZE = 4
CHECKSUM_SIZE = 2*BLOCK_SIZE
MESSAGE_SIZE = 64*BLOCK_SIZE


def pad_msg(data: bytes, size: int):
    return data + b'\x00' * (size - len(data))

def convol_hash(data: bytes, power: int):
    acc = data
    for _ in range(power):
        acc = hash(acc).digest()
    return acc

def checksum(data: bytes, block_size: int, checksum_size: int, message_size: int):
    bindata = f'{int.from_bytes(data, "big"):0b}'.zfill(message_size)
    acc = 0
    for i in range(0, message_size, block_size):
        acc += 2**block_size - int(bindata[i:i+block_size], 2) - 1
    acc %= 2**checksum_size
    return acc.to_bytes(checksum_size // 8, 'big')

#Convertis un message en bytes en un int selon la même méthode que celle utilisée pour signer le message
def msg_to_int(data: bytes):
    len_secrets = (MESSAGE_SIZE + CHECKSUM_SIZE) // BLOCK_SIZE
    signature_size = len_secrets*BLOCK_SIZE
    data_size = signature_size - CHECKSUM_SIZE
    assert len(data) * 8 < data_size, "The message you want to sign is too long"
    padded_data = pad_msg(data, data_size // 8)
    cksum = checksum(padded_data, BLOCK_SIZE, CHECKSUM_SIZE, data_size)
    plaintext = padded_data + cksum
    binpt = f'{int.from_bytes(plaintext, "big"):0b}'.zfill(signature_size)
    return binpt

#Retrouve la clé publique utilisée à partir d'un message et de sa signature.
def find_pubkey(msg,sig):
        int_data = msg_to_int(msg)
        sign = [bytes.fromhex(x) for x in sig]

        len_secrets = (MESSAGE_SIZE + CHECKSUM_SIZE) // BLOCK_SIZE
        signature_size = len_secrets*BLOCK_SIZE
        pubkey = []

        for i in range(0, signature_size, BLOCK_SIZE):
            exp = 2**BLOCK_SIZE - int(int_data[i:i+BLOCK_SIZE], 2)
            hash = sign[i//BLOCK_SIZE]
            x = convol_hash(hash, exp)
            pubkey.append(x)
            
        return pubkey

#Génère la signature de new_msg à partir de la signature de msg , à condition qu'aucun block de new_msg ne soit plus petit que le bloc en même position dans msg.
def new_sign(new_msg, msg, sig):
    int_msg = msg_to_int(msg)
    int_new_msg = msg_to_int(new_msg)

    sign = [bytes.fromhex(x) for x in sig]

    len_secrets = (MESSAGE_SIZE + CHECKSUM_SIZE) // BLOCK_SIZE
    signature_size = len_secrets*BLOCK_SIZE

    nw_sign = []
    for i in range(0, signature_size, BLOCK_SIZE):
        exp0 = int(int_msg[i:i+BLOCK_SIZE], 2)
        exp1 = int(int_new_msg[i:i+BLOCK_SIZE], 2)
        if exp1<exp0:
            return "Erreur"
        exp = exp1-exp0
        hash = sign[i//BLOCK_SIZE]
        x = convol_hash(hash, exp)
        nw_sign.append(x)

    hex_nw_sign = [x.hex() for x in nw_sign]
    return hex_nw_sign

def main():
    
    msg = b"SALUT CA VA?"
    sign = ["732813849813580da281fb0c87634031", "3c242bdb659c447c5ff32185955b5f26", "ea6508862ee5ce3d8d42cad524553a42", "b0d9796178a006106c2235809e183825", "4a8cd908556eb2f0ff732f8c1e3b9272", "b3bfc25a0e8105166b6f92d9e5632cb2", "ae5c474843a512e1d69a3912bfdda49b", "3b8bfdace3bf9501d3b2020b618d3eb9", "5a0ef9cd50e39eede7bbfe1460b3c32f", "1960bd04bdc257c85376b85196ec4e07", "7169cd86963b2e22dedc57f20e775f17", "4a0661acdeacbf901da5896ee8609835", "e53bd849de6a463ad250cc8fd5d77800", "453a7df76a28117b1cc3360809203410", "7002d9a25fe819da8d2861bc98737563", "9752607d86dc6a62843066dec30bad42", "d5834cb9d1dad1adfec8e1f618d82918", "cd653e04a915414795d423ed25664f0a", "834c72555c22de7b169738e99304e754", "68dfaa6d21bd3d91047af759c9a3edb7", "d6866e29ca5d94e327768b84a3940e3a", "8bc59f2cd1fadbe330e75c65bd2bb0f9", "d7e786c70f2a4f2d5c8a1e287d1c29c2", "70502ed690f74e289ebfe9a5b0e1b5fb", "500c4b3a1c070f2c1e5d57e94b8a230f", "4a4942eb6d193d2a91496e087bae1277", "12d85b7b36ef6e6fb457b4b2c1035bdb", "ef3b49a7756bad1e01cec9b6887c713f", "f00aaabf348dc34c6a38017911e45a56", "7f2512ddfff15679694d97d335fb80e1", "d0879f3f96209f49b31f836f9acb7c94", "a1febd32fe50553104e2ed66fee7a629", "cd1fc8215ead41d5e38a43835acf8c37", "1302cf3132dcd8e1dbddbcb003ea7289", "4940bcae52f5d1e2920e15468b7bef23", "408168af0c27fc1d0d41d41672467d14", "a99b30510e023b39d2e468e8836194a3", "226aae2f5c1735485c65acf240c2e052", "01327780b6093f8a560f1a8a0136b30e", "734561cc4019b6ab52df30c48fa2f324", "466c86761a524c0a97c6911aadb8be50", "701f683ef3d08546d02844d35e5d3025", "b241d081169c9adb63083c4e693ebc95", "f90431a079683cf8a61f5492d3bd4249", "927e4b90b149a389e8a0475fd688226f", "dd9c5aa11e1f5fe9470d16c1d6406243", "83241fec67d95d9d2ae35034a1c6547a", "e979936bc3ccf87df4c072ce7e11004d", "728140fc5125dffd465c34033e92623c", "019d5f572e3a4f922945323cc90ba903", "96642dbfd23d3944efc4dfdf5a0f9058", "813f6f89ce6439e3204013e267911b7f", "bef867f8ef130f7c7e90d6097ebd5ec7", "4750f5144916ee2ef83ea4ed67effad3", "4631cf78e5b4933a421c93f4f533e2d7", "5c3b2c2c927e5a9409778e7a589d5ca2", "fdad84aeba6f87cd55e823468b4aa4e8", "8591c3d642f123cc9024827c2a246926", "476ad360a3c61a7b9e1f5a8508b63a12", "9d58a9756c2fa50c492ace75f5b4a122", "5a3752704531e43bf92a0d7f250f63dd", "88fae73b75bd70f8a63c34c544c7fe88", "9e5488d4c1cc76bc7e1bfe67944e6b45", "a916673d2c0b9f4dfb2e88682a0810d1", "ab193735a8d69839dad883e4736c70eb", "22485c9a69bc905ebee3621ef5460352"]
    #On calcule la clé publique utilise pour vérifier la signature de msg (inutile pour résoudre le challenge)
    pubkey = find_pubkey(msg,sign)
    print("Public key = ", pubkey,"\n")

    #On détermine le json renvoyer pour avoir le flag
    nw_msg = b"gimme flagz_aaaaazazaaaaaaabcii"
    nw_sign = new_sign(nw_msg, msg, sign)
    initial = json.dumps({"msg": nw_msg.hex(), "sig": nw_sign})
    initial += '\n'
    print(initial)

main()

