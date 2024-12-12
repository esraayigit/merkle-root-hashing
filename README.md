# Merkle Root Calculation Script
This repository contains a Python script that calculates the Merkle Root of a set of transactions using double SHA-256 hashing. The script reads transaction hashes from a JSON file and outputs the resulting Merkle Root hash.

## Features:
### Double SHA-256 Hashing: 
Implements the sha256d function to hash concatenated transaction hashes twice.

### Endianness Handling:
Ensures correct byte order by reversing byte sequences for input and output.

### Input Flexibility:
Reads transaction hashes from an external JSON file.

## About the Example Data:

The script has been tested using data from block #542213 of the Bitcoin blockchain. The JSON file (input.json) contains the hash values of 4 transactions included in this block. The details of block #542213 can be accessed at the following link:
https://blockstream.info/block/000000000000000000143a2c56c0214236dadfd30df41d4a0345492ad6d861ec?expand

## How It Works:
- The input.json file contains the transaction hashes under the key "tx".
- The script extracts these hashes, reverses their byte order, and pairs them for hashing.
- If the number of hashes is odd, the last hash is duplicated to ensure pairing.
- The process repeats iteratively until a single hash remains—the Merkle Root.

# Merkle Root Hesaplama Scripti  
Bu depo, bir dizi işlemin Merkle Root'unu hesaplayan bir Python scripti içermektedir. Script, işlem hashlerini bir JSON dosyasından okur ve sonuç olarak Merkle Root hash değerini çıktılar.  

## Özellikler:  
### Çift SHA-256 Hashleme:  
Birleştirilen işlem hashlerini iki kez hashlemek için `sha256d` fonksiyonunu uygular.  

### Endian Desteği:  
Girdi ve çıktılar için byte sıralamasını ters çevirerek doğru sıralamayı sağlar.  

### Esnek Girdi:  
İşlem hashlerini harici bir JSON dosyasından okur.  

## Örnek Veri Hakkında:  
Script, Bitcoin blok zincirindeki #542213 numaralı bloktan alınan verilerle test edilmiştir. JSON dosyası (`input.json`), bu blokta yer alan 4 işlemin hash değerlerini içermektedir. #542213 numaralı blokla ilgili detaylara aşağıdaki bağlantıdan ulaşabilirsiniz:  
[https://blockstream.info/block/000000000000000000143a2c56c0214236dadfd30df41d4a0345492ad6d861ec?expand](https://blockstream.info/block/000000000000000000143a2c56c0214236dadfd30df41d4a0345492ad6d861ec?expand)  

## Çalışma Prensibi:  
- `input.json` dosyası, işlem hashlerini `"tx"` anahtarı altında içerir.  
- Script bu hashleri alır, byte sırasını ters çevirir ve hashleri çiftler halinde birleştirerek işlemeye başlar.  
- Eğer hash sayısı tek ise, eşleme sağlamak için son hash değeri çoğaltılır.  
- Bu süreç, tek bir hash değeri (Merkle Root) kalana kadar tekrarlanır.  
