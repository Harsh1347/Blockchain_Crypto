import hashlib
import json


def crypto_hash(data):
    """
    Return a sha-256 hash of given data
    """
    stringified_data = json.dumps(data)

    return hashlib.sha256(data.encode('utf-8')).hexdigest()


if __name__ == "__main__":
    print(crypto_hash("testing"))
