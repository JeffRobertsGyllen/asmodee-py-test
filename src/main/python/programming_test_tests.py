import unittest
from programming_test import Genre, Collection

class GenreTest(unittest.TestCase):
    def testName_SetOnInit_ReturnedFromGetter(self):
        sut = Genre("Bobby Kennedy")
        self.assertEquals(sut.name, "Bobby Kennedy")

    def testCollection_SetOnInit_ReturnedFromGetter(self):
        collection = Collection("")
        sut = Genre("", [collection])
        self.assertEqual(sut.get_collection(), [collection])

    def testCollection_AddCollection_AddedToList(self):
        collection = Collection("")
        sut = Genre("")
        sut.add_collection(collection)
        self.assertEqual(sut.get_collection(), [collection])

    def testCollection_RemoveCollection_RemovedFromList(self):
        collection = Collection("")
        sut = Genre("", [collection])
        sut.remove_collection(collection)
        self.assertEqual(sut.get_collection(), [])

suite = unittest.TestLoader().loadTestsFromTestCase(GenreTest)
unittest.TextTestRunner(verbosity=2).run(suite)