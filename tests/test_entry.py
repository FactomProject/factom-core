import unittest

from factom_core.block_elements import Entry


class TestEntry(unittest.TestCase):

    test_data = "00b312a0401879366b3d72a1844b3ca0da1009545ffa8e4038f80da1528cb572ab002200202140840000b4505bbb025bb7a3" \
                "2b2054eeed84a0eda2905e6272b30365abfdcd7b224f5052436861696e4944223a2244343254395842467559786872434e6e" \
                "37713336365a46644c6f3173676d5455625838586b76527a6f353367222c2244626874223a3139393435392c2257696e6e69" \
                "6e6750726576696f75734f5052223a5b22474e506f62614b674b777464396a36667265616d6f353765335363543754465234" \
                "344d7a7a5841696631594c222c22345456696b36414a35434e774c625671353458635a3972384b6b6332384d42795a395862" \
                "573771636b777831222c223756764e6b6556484734666d626a5868546579776e3862766459664d5976437644755146727366" \
                "46504c5977222c224162765970583653486b39534e4a4a4467457964645370437179504656696e37385042536a3842373537" \
                "4656222c2245743656625534673261696a654d486f777850625a5275547a6a657455687478695a656361657155566a566e22" \
                "2c22324156557a4144455a535262366f44564855434c58625a725661436b69684b694c3365773269486a6377656e222c224a" \
                "353875426e6238644541714c706159434d6a6f524247784568647864553154426677315a4e4c39444d794d222c2244765171" \
                "7574534b554a635a696d3454445242503271526268655875547a437670364d744a4b46354d59794e222c2247334b43364a36" \
                "504d4e594d707031636832717850537654754c3252737361744476356d316a37584445574d222c2246314738637650584647" \
                "4b4e316a52696a714a6d4864747a43537952785a6533587768486a674e4176437650225d2c22436f696e62617365504e5441" \
                "646472657373223a2274504e5432565365523967613538366d337138354a5772756e69526a6e706a6b6e4c7479616a31654a" \
                "345834676e457a6265373662313033222c22466163746f6d4469676974616c4944223a5b2270726f746f74797065222c2270" \
                "676d696e657231225d2c22504e54223a302c22555344223a312c22455552223a302e3838362c224a5059223a3130382e3336" \
                "31352c22474250223a302e373930372c22434144223a312e333133352c22434846223a302e393837322c22494e52223a3639" \
                "2e313737342c22534744223a312e333536322c22434e59223a362e383531382c22484b44223a372e3831352c22584155223a" \
                "31352e31312c22584147223a313338352e362c22585044223a313532382c22585054223a3833302c22584254223a31303438" \
                "322e393134352c22455448223a3239322e3830342c224c5443223a3132312e333032322c22584243223a3431362e35393835" \
                "2c22464354223a352e333837367d"

    def test_unmarshal(self):
        expected_entry_hash = "1503d1d8b8d8036ad7cb270321996c0b1f050b4ebaea79ab48d007071cf370f2"
        expected_chain_id = "b312a0401879366b3d72a1844b3ca0da1009545ffa8e4038f80da1528cb572ab"
        expected_external_ids = [
            "2140840000b4505bbb025bb7a32b2054eeed84a0eda2905e6272b30365abfdcd"
        ]
        expected_content = "7b224f5052436861696e4944223a2244343254395842467559786872434e6e37713336365a46644c6f3173676" \
                           "d5455625838586b76527a6f353367222c2244626874223a3139393435392c2257696e6e696e6750726576696f" \
                           "75734f5052223a5b22474e506f62614b674b777464396a36667265616d6f353765335363543754465234344d7" \
                           "a7a5841696631594c222c22345456696b36414a35434e774c625671353458635a3972384b6b6332384d42795a" \
                           "395862573771636b777831222c223756764e6b6556484734666d626a5868546579776e3862766459664d59764" \
                           "3764475514672736646504c5977222c224162765970583653486b39534e4a4a44674579646453704371795046" \
                           "56696e37385042536a38423735374656222c2245743656625534673261696a654d486f777850625a5275547a6" \
                           "a657455687478695a656361657155566a566e222c22324156557a4144455a535262366f44564855434c58625a" \
                           "725661436b69684b694c3365773269486a6377656e222c224a353875426e6238644541714c706159434d6a6f5" \
                           "24247784568647864553154426677315a4e4c39444d794d222c22447651717574534b554a635a696d34544452" \
                           "42503271526268655875547a437670364d744a4b46354d59794e222c2247334b43364a36504d4e594d7070316" \
                           "36832717850537654754c3252737361744476356d316a37584445574d222c22463147386376505846474b4e31" \
                           "6a52696a714a6d4864747a43537952785a6533587768486a674e4176437650225d2c22436f696e62617365504" \
                           "e5441646472657373223a2274504e5432565365523967613538366d337138354a5772756e69526a6e706a6b6e" \
                           "4c7479616a31654a345834676e457a6265373662313033222c22466163746f6d4469676974616c4944223a5b2" \
                           "270726f746f74797065222c2270676d696e657231225d2c22504e54223a302c22555344223a312c2245555222" \
                           "3a302e3838362c224a5059223a3130382e333631352c22474250223a302e373930372c22434144223a312e333" \
                           "133352c22434846223a302e393837322c22494e52223a36392e313737342c22534744223a312e333536322c22" \
                           "434e59223a362e383531382c22484b44223a372e3831352c22584155223a31352e31312c22584147223a31333" \
                           "8352e362c22585044223a313532382c22585054223a3833302c22584254223a31303438322e393134352c2245" \
                           "5448223a3239322e3830342c224c5443223a3132312e333032322c22584243223a3431362e353938352c22464" \
                           "354223a352e333837367d"

        entry = Entry.unmarshal(bytes.fromhex(expected_entry_hash), bytes.fromhex(TestEntry.test_data))
        assert entry.entry_hash.hex() == expected_entry_hash
        assert entry.chain_id.hex() == expected_chain_id
        for i, external_id in enumerate(entry.external_ids):
            assert external_id.hex() == expected_external_ids[i]
        assert entry.content.hex() == expected_content

    def test_marshal(self):
        entry_hash = "1503d1d8b8d8036ad7cb270321996c0b1f050b4ebaea79ab48d007071cf370f2"
        entry = Entry.unmarshal(bytes.fromhex(entry_hash), bytes.fromhex(TestEntry.test_data))
        assert entry.marshal().hex() == TestEntry.test_data

    def test_entry_hash_calculation(self):
        expected_entry_hash = "1503d1d8b8d8036ad7cb270321996c0b1f050b4ebaea79ab48d007071cf370f2"
        entry = Entry.unmarshal(bytes.fromhex(expected_entry_hash), bytes.fromhex(TestEntry.test_data))
        assert entry._calculate_entry_hash().hex() == expected_entry_hash