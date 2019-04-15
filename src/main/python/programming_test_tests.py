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

class CollectionTest(unittest.TestCase):
    def testGenre_SetGenre_SetsNewListAndUpdatesAllGenresCollectionLists(self):
        sciFi = Genre("Science Fiction")
        dubFeat = Genre("Double Feature")
        sut = Collection("")

        sut.set_genres([sciFi, dubFeat])

        self.assertEqual(sut.get_genres(), [sciFi, dubFeat])
        self.assertEqual(sciFi.get_collection(), [sut])
        self.assertEqual(dubFeat.get_collection(), [sut])

suite = unittest.TestLoader().loadTestsFromTestCase(CollectionTest)
unittest.TextTestRunner(verbosity=2).run(suite)