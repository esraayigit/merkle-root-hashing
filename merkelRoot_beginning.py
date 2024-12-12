#Quelle: https://bitcoin.stackexchange.com/questions/79747/how-do-i-calculate-the-witness-commitment-hash-for-a-given-block

from hashlib import sha256

def reverse_HEX(strinput):
    # 0x224466 -> 664422
    #print strinput
    return strinput.rstrip("L").decode('hex')[::-1].encode('hex')

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
tx = [ ] #{version: "", inputs: ["UnspendTX:Index", "SCRIPTSIG (HEX)"], output: [Amount in BTC, "SCRIPTPUBKEY (HEX)"], witness: ["Signature","PubKey"], locktime: int}
i = 0 

tx.append({"version":None, "inputs":[], "outputs":[], "witness":[], "locktime":None})
tx[len(tx)-1]["version"] = "00000001"
tx[len(tx)-1]["inputs"].append(["0:4294967295", "03054608174d696e656420627920416e74506f6f6c393b205ba350dffabe6d6d3a3e92d9efff857664de632e89fa3182f1e793d00be2e71a117b273145945a810400000000000000db250000acba0500", "ffffffff"])
tx[len(tx)-1]["outputs"].append([12.50004874, "76a914edf10a7fac6b32e24daa5305c723f3de58db1bc888ac"])
tx[len(tx)-1]["outputs"].append([0, "6a24aa21a9ed4a657fcaa2149342376247e2e283a55a6b92dcc35d4d89e4ac7b74488cb63be2"])
tx[len(tx)-1]["witness"].append(["0000000000000000000000000000000000000000000000000000000000000000"])
tx[len(tx)-1]["locktime"] = 0

tx.append({"version":None, "inputs":[], "outputs":[], "witness":[], "locktime":None})
tx[len(tx)-1]["version"] = "00000001"
tx[len(tx)-1]["inputs"].append(["db636bb7d1c79b38b496766dcf37fbc215edb1fd4f19b5ec9993d4983f2798b8:1", "483045022100e2e9bc1f6bae2deed086e935bb49fd6ac1e13dc3a44c36cd8b9a6f4257efb70d022076537c7021f12d761e1202796029f13798503bc22ab8c2ee8cb98207cbfeb414012102071c2c88e4560b47a03c033c736149a2ddd6071aea54ab85c5169cee156712f8", "ffffffff"])
tx[len(tx)-1]["outputs"].append([0.0075, "76a914849a95fc65eeaa2ac47b6b6fc1f1883edb2c6c9788ac"])
tx[len(tx)-1]["outputs"].append([0.1924887, "76a9142964198f7ae9f7b920a2ab7c0b96b90e4ec9b14d88ac"])
#tx[len(tx)-1]["witness"].append()
tx[len(tx)-1]["locktime"] = 0

tx.append({"version":None, "inputs":[], "outputs":[], "witness":[], "locktime":None})
tx[len(tx)-1]["version"] = "00000001"
tx[len(tx)-1]["inputs"].append(["88a7846ff8f618cd70c9ee0cf1be9bbbb7b3b0a12434f640355b0560265e4052:0", "160014dde2f1a9a4bfda011ba9ec4062990c7e1a531585", "ffffffff"])
tx[len(tx)-1]["outputs"].append([0.01627238, "a914adc5ec550548f087371e645047170864d5fbdc0387"])
tx[len(tx)-1]["outputs"].append([0.0000115, "001441f6746110cc0fec102e83053d4c0ae56fab1bdd"])
tx[len(tx)-1]["witness"].append(["3045022100f93bd5d3529418f60dddd477f169c32ea5ab340c99573438ee7c40d705db9ba20220323f1b4d8840098b1271c95365cdc7e8f81d0bf1fcc568c68fc7de8b871b4bee01","03211d047d92547bca4aa116bc51ec4b09188e5991f69f0432fe1b5dfd89478597"])
tx[len(tx)-1]["locktime"] = 0

tx.append({"version":None, "inputs":[], "outputs":[], "witness":[], "locktime":None})
tx[len(tx)-1]["version"] = "00000001"
tx[len(tx)-1]["inputs"].append(["21e78cdeb8e642c3617104a9517cb56f01fcf7b98ed096ae9227b9e55498a1c1:0", "483045022100fa00a6651015ac807b03d8d54559831db40d80329f46a886b93ca6b3996daf9b02201d0fafccc88c4654a9c3d205ef0828e32376ecb42f79587615203f23fc8f2d42012102a2cda42f6954605e40cbc5601f65673621c057f8c12f16149fbbf632e8be8ed8", "ffffffff"])
tx[len(tx)-1]["inputs"].append(["5fc2e2941b3da3c969f53df56c42dfe98d1640a7d4e5d5168ff724734aff16da:0", "4730440220167b4777a23db304f50ac75febfae5db0b1578c90d85769bc76e0f5458484319022023f763e95ea7771c15ea0df91c17519014b2223cd726a3b0a8b1a6f67f99b2bf012103b9492a823f03b70a1750e0fac44f58f5c81e09f4c18d0b28755b44c911ffab5f", "ffffffff"])
tx[len(tx)-1]["inputs"].append(["701be2ca7a438771484515919c38d45a10d65968bb5be02b9d854ba32e3f53f1:0", "483045022100be0b8dc174f4136e3fb4f3ccf1a2be67a44d2086179c5726c61a1af010d5232f02205c0fb4cdd7c9cb8698ceed05e688e10a0cbdd0ee5db1a0a2ef92f322e1a60e9f0121020b9f404317cc6ab5a699f607a9bb0acd0bf5588777672f8f7f4c1a13304e9f76", "ffffffff"])
tx[len(tx)-1]["inputs"].append(["72951146c456f5857a0f5a798a8e197dda6b6d9da7c24cfa1c5baa3718199513:0", "483045022100ef3c61b5ba155b94fd02a96bf788e9a9be2de0ee53e3fe1fa6c24dd9d9aaee12022044c07be54a9c59fed96dfb778da0079f6753ab634d1920bf0fac25ebf7ac49d0012103f93e29be8b393773228f704151964662a91df4c1a3e15364e4cfb38a8cacbda9", "ffffffff"])
tx[len(tx)-1]["inputs"].append(["7cfdf540f7d74367f36b908fdc409fc26fe434d78c19d05f84bb5f4d680f1255:0", "4730440220421aef290bbd39a18d1281ecfbb420b43daf2cc1c315b6bb44c895f88cb3cfcc022007a512c65b7768b1505f789b6d78479063d04ffb243072f2061eeb66fb1ade81012102712eea19c72fd644b2698c5480ebe77ce6face0bed64238a34a32085567f2f8e", "ffffffff"])
tx[len(tx)-1]["inputs"].append(["a62b4710ba33b2aaebe2d6ca6cb1019d9d0f26a506fa9c4e465631ce193d55f3:0", "483045022100a29aea775d2c46028f40dceb1707b23e720bb314cef455854313569200c83162022009d0cdcef2e1f0a9217794991fa838fe6ce2bdc6e3c04ad490343c7e4a0ee7d3012102ed59ec6d98f9c2a4dd1324d46d74c56ff7e15935925f69799e547969a523ea98", "ffffffff"])
tx[len(tx)-1]["inputs"].append(["b63dfef28758e3a02bce39512538a66cbefe83e9cb12fb9b66830d5fd9b60a53:0", "483045022100fad9f10989ab4ab019da4f6e430f9fe9ebe76941a9200d7346447358e93b1dce0220756c864b029a64ed9d6eedc13cf8b7d602572fcd7a3d3cb528350bb032d7e3ec012102e3e0c78d034627b1616cf196aa69bfaf20009ba9ebf09cf069453cc0423239e2", "ffffffff"])
tx[len(tx)-1]["inputs"].append(["d8e47e4abae931f98f529e0240c09bf7bcfaadac3c7099df65d9414982708e4b:0", "48304502210095f37fb2700c9f96d5e5c02d4b043a7cd804f79dd071d8b221b7ae781f0f5b4e02200ae3135b8bebf813449956ae19e7c02db5eff2472da023afa8b8d4e9baba0cdd01210226cc53dfc0a41cc0cf7117dfd406db2b87161e89e2bab9908a2382173fc6dbe1", "ffffffff"])
tx[len(tx)-1]["inputs"].append(["dfab9fae87944c4947c69b3be2d953ee832bed82487e7f212b7281989e126252:0", "473044022032361f724fe006079cf37b3df61cb6c51cb0c5fd77f29b61a318134ca4948d0e02202fbe6d484a78730899230244f3662fd5578b87e9eaaccdf9bf8f05d23917de8301210254e84223b3d7f7cfd14315be8fa0c7d7eb1a1a34a672f08e2b8ec134472a66d4", "ffffffff"])
tx[len(tx)-1]["inputs"].append(["f4b9d1b9075f753ccaa73eb1584498c949081305b7b75dbe2e288832e0407006:0", "483045022100b78b9c24f5f3e950aba637b827d5b11615c17ae2f43105941d172cc4a8b73c80022064998c17becd06abbcfde47c91b9d87da5ac67873ed9a412010b08b954e0b5cd01210329a0acc2b0d60dd243eef46073a672ed0caf467c92f63ef7293f2036a3851a1e", "ffffffff"])
tx[len(tx)-1]["outputs"].append([0.00032514, "76a914c6a396ae979670eeaa6929df3dd1c2d8fba31c3d88ac"])
tx[len(tx)-1]["outputs"].append([0.43753861, "a914409dbd0e9a1ab27853186367130e6aab2509e47f87"])
#tx[len(tx)-1]["witness"].append()
tx[len(tx)-1]["locktime"] = 0