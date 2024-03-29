import unittest
from ChunkList import chunk_list


class Test_Chunck_List(unittest.TestCase):
    def test_chunk_empty_list(self):
        EMPTY_LIST = []
        CHUNK_SIZE = 1
        self.assertListEqual(chunk_list(EMPTY_LIST, CHUNK_SIZE), EMPTY_LIST)

    def test_invalid_chunk_size_(self):
        LIST = [1, 2, 3, 4]
        CHUNK_SIZE = 0
        self.assertRaises(ValueError, chunk_list, LIST, CHUNK_SIZE)
        CHUNK_SIZE = 10
        self.assertRaises(ValueError, chunk_list, LIST, CHUNK_SIZE)

    def test_list_size_one(self):
        LIST = [1]
        CHUNK_LIST = [[1]]
        self.assertListEqual(chunk_list(LIST, 1), CHUNK_LIST)

    def test_chunk_size_one(self):
        LIST = [1, 2, 3, 4]
        CHUNK_SIZE = 1
        CHUNK_LIST = [[1], [2], [3], [4]]
        self.assertListEqual(chunk_list(LIST, CHUNK_SIZE), CHUNK_LIST)

    def test_chunks(self):
        LIST = [1, 2, 3, 4]
        CHUNK_SIZE = 2
        CHUNK_LIST = [[1, 2], [3, 4]]
        self.assertListEqual(chunk_list(LIST, CHUNK_SIZE), CHUNK_LIST)

        CHUNK_SIZE = 3
        CHUNK_LIST = [[1, 2, 3], [4]]
        self.assertListEqual(chunk_list(LIST, CHUNK_SIZE), CHUNK_LIST)


if __name__ == "__main__":
    unittest.main()
