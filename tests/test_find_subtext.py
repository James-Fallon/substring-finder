from find_subtext import find_subtext
import unittest


class TestFindSubtext(unittest.TestCase):

    def test_find_subtext_with_larger_subtext_than_text_to_search(self):
        text_to_search = 'short'
        subtext = 'a bit longer'

        with self.assertRaises(ValueError):
            find_subtext(text_to_search, subtext)

    def test_find_subtext_no_subtexts_found(self):
        text_to_search = 'Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!'
        subtext = 'vader'

        indices = find_subtext(text_to_search, subtext)
        self.assertTrue(len(indices) == 0)

    def test_find_subtext_normal_case(self):
        text_to_search = 'Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!'
        subtext = 'Peter'

        indices = find_subtext(text_to_search, subtext)
        self.assertEqual(indices, [1, 20, 75])
