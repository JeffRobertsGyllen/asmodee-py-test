import unittest
from programming_test import Genre, Collection, Product, TaxableProduct

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

    def testAddGenre_AddDuplicateGenre_DuplicateNotAddedToList(self):
        sut = Collection("Descent Games")
        dungeon = Genre("Dungeon Crawl", [sut])

        sut.add_genre(dungeon)

        self.assertEqual(sut.get_genres(), [dungeon])

    def testAddChild_AddDuplicateChild_DuplicateNotAddedToList(self):
        sut = Collection("Star Wars")
        starWarsMinis = Collection("Star Wars Miniature", [], [], sut)

        sut.add_child(starWarsMinis)

        self.assertEqual(sut.get_children(), [starWarsMinis])

class TaxableProductTest(unittest.TestCase):
    def testInit_TaxValue_TaxAddedToPrice(self):
        collection = Collection("")
        sut = TaxableProduct("Eldritch Horror", 69.99, collection, 6.75)

        self.assertEqual(sut.get_price(), 74.71)