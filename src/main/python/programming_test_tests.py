import unittest
from programming_test import Genre, Collection, Product, TaxableProduct, print_tree

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

class PrintTreeTest(unittest.TestCase):
    def testPrintTree_EmptyCollection_PrintsNameOnly(self):
        collection = Collection("Named Collection")

        expected = "Named Collection\n"

        self.assertEqual(print_tree(collection), expected)

    def testPrintTree_CollectionWithProducts_PrintsAll(self):
        collection = Collection("Named Collection")
        product1 = Product("First Product", 5.99, collection)
        product2 = Product("Second Product", 12.50, collection)

        expected = ("Named Collection\n"
                    "    First Product ($5.99)\n"
                    "    Second Product ($12.50)\n")

        self.assertEqual(print_tree(collection), expected)

    def testPrintTree_NestedEmptyCollections_PrintsAll(self):
        collectionRoot = Collection("Root Collection")
        collectionLeaf1 = Collection("First Leaf Collection", [], [], collectionRoot)
        collectionLeaf2 = Collection("Second Leaf Collection", [], [], collectionRoot)

        expected = ("Root Collection\n"
                    "    First Leaf Collection\n"
                    "    Second Leaf Collection\n")

        self.assertEqual(print_tree(collectionRoot), expected)

    def testPrintTree_NestedCollectionsWithProducts_PrintsAll(self):
        collectionRoot = Collection("Root Collection")
        rootProduct = Product("Root First Product", 9.99, collectionRoot)
        collectionLeaf1 = Collection("First Leaf Collection", [], [], collectionRoot)
        leaf1product1 = Product("First Leaf First Product", 8.12, collectionLeaf1)
        leaf1product2 = Product("First Leaf Second Product", 1847.99, collectionLeaf1)
        collectionLeaf2 = Collection("Second Leaf Collection", [], [], collectionRoot)
        leaf2product1 = Product("Second Leaf First Product", 0.01, collectionLeaf2)
        collectionLeaf2Leaf1 = Collection("Second Leaf First Leaf Collection", [], [], collectionLeaf2)
        collectionLeaf2Leaf1Leaf1 = Collection("Second Leaf First Leaf First Leaf Collection", [], [], collectionLeaf2Leaf1)
        leaf2leaf1leaf1product1 = TaxableProduct("Second Leaf First Leaf First Leaf First Product", 9.99, collectionLeaf2Leaf1Leaf1, 5.77)

        expected = ("Root Collection\n"
                    "    First Leaf Collection\n"
                    "        First Leaf First Product ($8.12)\n"
                    "        First Leaf Second Product ($1847.99)\n"
                    "    Second Leaf Collection\n"
                    "        Second Leaf First Leaf Collection\n"
                    "            Second Leaf First Leaf First Leaf Collection\n"
                    "                Second Leaf First Leaf First Leaf First Product ($10.57)\n"
                    "        Second Leaf First Product ($0.01)\n"
                    "    Root First Product ($9.99)\n")

        self.assertEqual(print_tree(collectionRoot), expected)