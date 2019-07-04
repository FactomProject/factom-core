from factom_core.utils import varint


class BalanceIncrease:
    ECID = b'\x04'

    def __init__(self, ec_public_key: bytes, tx_id: bytes, index: int, quantity: int, **kwargs):
        # Required fields. Must be in every BalanceIncrease
        self.ec_public_key = ec_public_key
        self.tx_id = tx_id
        self.index = index
        self.quantity = quantity
        # TODO: assert they're all here
        # TODO: use kwargs for some optional metadata

    def marshal(self):
        """Marshals the BalanceIncrease according to the byte-level representation shown at
        https://github.com/FactomProject/FactomDocs/blob/master/factomDataStructureDetails.md#balance-increase
        """
        data = self.ec_public_key
        data += self.tx_id
        data += varint.encode(self.index)
        data += varint.encode(self.quantity)
        return data

    @classmethod
    def unmarshal(cls, raw: bytes):
        """Returns a new BalanceIncrease object, unmarshalling given bytes according to:
        https://github.com/FactomProject/FactomDocs/blob/master/factomDataStructureDetails.md#balance-increase
        """
        obj, data = BalanceIncrease.unmarshal_with_remainder(raw)
        assert len(data) == 0, 'Extra bytes remaining!'
        return obj

    @classmethod
    def unmarshal_with_remainder(cls, raw: bytes):
        """Returns a new BalanceIncrease object along with any remaining data, unmarshalling given bytes according to:
        https://github.com/FactomProject/FactomDocs/blob/master/factomDataStructureDetails.md#balance-increase

        Because BalanceIncrease is variable length, it is useful to pass a "stream" of bytes to be unmarshalled.
        This way, we don't have to know the size in advance. Just return the remainder bytes for the caller to use
        elsewhere.
        """
        ec_public_key, data = raw[:32], raw[32:]
        tx_id, data = data[:32], data[32:]
        index, data = varint.decode(data)
        quantity, data = varint.decode(data)

        return BalanceIncrease(
            ec_public_key=ec_public_key,
            tx_id=tx_id,
            index=index,
            quantity=quantity
        ), data

    def to_dict(self):
        pass  # TODO: Implement BalanceIncrease.to_dict()

    def __str__(self):
        # TODO: convert EC Public Key to its base58 address
        return '{}(tx_id={}, ec_public_key={}, quantity={})'.format(
            self.__class__.__name__, self.tx_id.hex(), self.ec_public_key.hex(), self.quantity)