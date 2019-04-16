import unittest
from programming_test import Genre, Collection, Product

class GenreTest(unittest.TestCase):
    def testInit_PassedInName_ReturnedFromGetter(self):
        sut = Genre("Bobby Kennedy")
        self.assertEquals(sut.name, "Bobby Kennedy")

    def testInit_PassedInCollection_ReturnedFromGetter(self):
        collection = Collection("")
        sut = Genre("", [collection])
        self.assertEqual(sut.get_collection(), [collection])

    def testAddCollection_NewCollection_AddedToList(self):
        collection = Collection("")
        sut = Genre("")
        sut.add_collection(collection)
        self.assertEqual(sut.get_collection(), [collection])

    def testRemoveCollection_RemoveExistingCollection_RemovedFromList(self):
        collection = Collection("")
        sut = Genre("", [collection])
        sut.remove_collection(collection)
        self.assertEqual(sut.get_collection(), [])

suite = unittest.TestLoader().loadTestsFromTestCase(GenreTest)
unittest.TextTestRunner(verbosity=2).run(suite)

class CollectionTest(unittest.TestCase):
    def testSetGenre_SetNewGenreList_SetsNewListAndUpdatesAllGenresCollectionLists(self):
        sciFi = Genre("Science Fiction")
        dubFeat = Genre("Double Feature")
        sut = Collection("")

        sut.set_genres([sciFi, dubFeat])

        self.assertEqual(sut.get_genres(), [sciFi, dubFeat])
        self.assertEqual(sciFi.get_collection(), [sut])
        self.assertEqual(dubFeat.get_collection(), [sut])

    def testAddProduct_AddDuplicateProduct_DuplicateNotAddedToList(self):
        sut = Collection("Arkham Games")
        arkHrr = Product("Arkham Horror", 59.99, sut)

        sut.add_product(arkHrr)

        self.assertEqual(sut.get_products(), [arkHrr])

suite = unittest.TestLoader().loadTestsFromTestCase(CollectionTest)
unittest.TextTestRunner(verbosity=2).run(suite)