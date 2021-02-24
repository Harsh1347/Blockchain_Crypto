from backend.util.crypto_hash import crypto_hash


def test_crypto_hash():
    # It should create same hash for different order
    assert crypto_hash(1, [2], "three") == crypto_hash([2], "three", 1)
    assert crypto_hash(
        "foo") == "b2213295d564916f89a6a42455567c87c3f480fcd7a1c15e220f17d7169a790b"
