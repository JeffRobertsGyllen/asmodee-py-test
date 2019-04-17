# vim: ts=4:sw=4:expandtabs

__author__ = 'zmott@asmodeena.com'
__doc__ = """
Asmodee North America Web Application programming test
v0.1.3 2017-05-11
"""

# +----------------------------------------------------------------------------+
# |                                                                            |
# |  The following classes represent a simple application for managing a       |
# |  product catalog.  They form the basis for this coding test, so consider   |
# |  them carefully.                                                           |
# |                                                                            |
# |  Please submit your solutions to questions 1 through 4 in a single file    |
# |  named 'programming_test_solutions.py'. This file must contain valid       |
# |  Python 2.7 code. That is, it must not raise any SyntaxErrors while being  |
# |  parsed by the Python 2.7 interpreter.                                     |
# |                                                                            |
# |  You may submit your answers to questions 5 and 6 in whatever format is    |
# |  is most convenient to you. Plain text, PDF, and Word or Pages documents   |
# |  are preferred.                                                            |
# |                                                                            |
# +----------------------------------------------------------------------------+


class Product(object):
    def __init__(self, name, price, collection):
        self.name = name
        
        # Attribute names that begin with __ (double underscores)
        # are inaccessible from outside the class.
        self.__price = price

        self.collection = collection
        self.collection.add_product(self)

    def __unicode__(self):
        return u"{name} (${price:.2f})".format(name=self.name, price=self.get_price())

    def get_price(self):
        return self.__price


class Genre(object):
    """
    Q1-1. Certain users prefer to browse the product catalog by genre (e.g. 
          "Science Fiction") instead of title. Because of this use case, we
          need to represent genre-related information in our product catalog.

          Implement the Genre class. Genres must be instantiated with a name,
          but they may also receive a list of Collections which will be associated
          with the new Genre. Genres must keep track of which Collections they're
          associated with. Additionally, the Genre class must also know how to add
          and remove Collections from itself.

          A Collection may be a associated with any number of Genres, and a Genre
          may be associated with any number of Collections.
    """
    def __init__(self, name, collections=None):
        # A list of collections associated with this genre
        self.__collections = []

        self.name = name

        # Make sure this new genre is added to all the given collections
        if collections:
            self.__collections = collections
            for collection in collections:
                collection.add_genre(self)

    # Accessors

    def get_collection(self):
        return self.__collections

    # Adders

    def add_collection(self, collection):
        self.__collections.append(collection)

    # Removers

    def remove_collection(self, collection):
        self.__collections.remove(collection)


class Collection(object):
    def __init__(self, name, genres=None, products=None, parent=None):
        # A list of products which are children of this collection
        self.__products = []

        # A list of collections which are children of this collection
        self.__children = []

        # A list of genres this collection is a part of.
        self.__genres = []

        self.name = name
        self.parent = None

        if products:
            self.__products.extend(products)

        if parent:
            self.parent = parent
            self.parent.add_child(self)

        if genres:
            self.__genres.extend(genres)

    #
    # Accessor methods.
    #

    def get_children(self):
        return self.__children
        
    def get_products(self):
        return self.__products
        
    def get_genres(self):
        return self.__genres

    #
    # Adder methods. These add the given value to the corresponding list.
    #

    def add_child(self, child):
        if child not in self.__children:
            self.__children.append(child)

    def add_product(self, product):
        if product not in self.__products:
            self.__products.append(product)

    def add_genre(self, genre):
        if genre not in self.__genres:
            self.__genres.append(genre)

    #
    # Remover methods. These raise a ValueError if the given
    # value isn't a member of the corresponding list.
    #

    def remove_child(self, child):
        self.__children.remove(child)

    def remove_product(self, product):
        self.__products.remove(product)
        
    def remove_genre(self, genre):
        self.__genres.remove(genre)

    #
    # Setter methods. We're only worried about genres here.
    #
    
    def set_genres(self, genres):
        """
        Q1-2. Implement this method, which takes a list of Genres to which
              this collection will be attached. This method REPLACES
              all Genre associations, so be sure to update each Genre's
              internal representation of associated Collections appropriately.
        """
        self.__genres = genres
        for newGenre in self.__genres:
            newGenre.add_collection(self)


# +----------------------------------------------------------------------------+
# |                                                                            |
# | Q2-1. After reviewing your work on Q1, your manager provides you with      |
# |       a new requirement: The 'products', 'genres', and 'children'          |
# |       attributes of the Collection class must never contain duplicate      |
# |       values. Write a test suite to illustrate that the current            |
# |       implementation of the Collection class does not satisfy this         |
# |       requirement.                                                         |
# |                                                                            |
# | Q2-2. Modify the Collection class (and your answers to Q1, if necessary)   |
# |       so that it passes the tests you wrote in Q2-1.                       |
# |                                                                            |
# +----------------------------------------------------------------------------+


# +----------------------------------------------------------------------------+
# |                                                                            |
# |  Q3. Create a new kind of product, called a TaxableProduct, that behaves   |
# |      exactly like a product, but takes an additional argument "tax_rate"   |
# |      during initialization. The tax rate is a percentage expressed as a    |
# |      float. E.g. a tax rate of 5.67% will be provided as 5.67. When asked  |
# |      for its price, a TaxableProduct must provide the price INCLUDING tax. |
# |                                                                            |
# +----------------------------------------------------------------------------+

class TaxableProduct(Product):
    def __init__(self, name, price, collection, tax_rate):
        Product.__init__(self, name, price, collection)
        self.__tax_rate = tax_rate

    def get_price(self):
        return round(Product.get_price(self) * (1 + (self.__tax_rate / 100 )), 2)

# +----------------------------------------------------------------------------+
# |                                                                            |
# |  Q4. Implement the following function "print_tree".  This function must    |
# |      take a collection as input, though you may modify its signature to    |
# |      take other parameters as well. This function prints all of its        |
# |      subcollections and products (and their subcollections and products,   |
# |      and so on), visually indicating the parent/child relationships.       |
# |      Products must be differentiated from collections by the inclusion of  |
# |      their price.                                                          |
# |                                                                            |
# +----------------------------------------------------------------------------+


def print_tree(collection, depth=1):
    """ In the example output below, "Twilight Imperium" is the root collection,
    "Base Game" and "Expansions" are subcollections belonging to the root
    collection, and "Twilight Imperium Third Edition ($89.95)", "Shattered
    Empire ($59.95)", and "Shards of the Throne ($59.95)" are products belonging
    to their respective subcollections.

    > print_tree(twilight_imperium)
    Twilight Imperium
        Base Game
            Twilight Imperium Third Edition ($89.95)
        Expansions
            Shattered Empire ($59.95)
            Shards of the Throne ($59.95)
    """

    # Print name of this collection
    output = collection.name + "\n"

    # Process child collections and fully print their trees
    for child in collection.get_children():
        output += ("\t" * depth) + print_tree(child, depth + 1)

    # Print direct child products of this collection
    for product in collection.get_products():
        output += ("\t" * depth) + unicode(product) + "\n"

    return output


# +----------------------------------------------------------------------------+
# |                                                                            |
# |  Q5-1. Devise a SQL schema that could be used to persist the data          |
# |        represented by the Product, Genre, and Collection classes above.    |
# |        Make sure to preserve relationships between the classes as well as  |
# |        the data contained within each class.                               |
# |                                                                            |
# |  Q5-2. Write a SQL statement that uses the schema you devised in Q5-1 to   |
# |        fetch name, price, collection name, and names of related genres for |
# |        all of the products that are immediate children of the collection   |
# |        named "Descent Second Edition".                                     |
# |                                                                            |
# +----------------------------------------------------------------------------+
#SELECT Product.Name AS 'Product Name', Product.Price, Collection.Name AS 'Collection Name',
#    (SELECT Genre.Name + ','
#    FROM Genre
#    INNER JOIN GenreCollection ON Genre.Id = GenreCollection.GenreId
#    INNER JOIN Collection ON Collection.Id = GenreCollection.CollectionId
#    WHERE Collection.Name = 'Descent Second Edition'
#    FOR XML PATH ('')) [Genre Names]
#FROM Product
#INNER JOIN Collection ON Product.CollectionId = Collection.Id
#WHERE Collection.Name = 'Descent Second Edition'


# +----------------------------------------------------------------------------+
# |                                                                            |
# |  Q6.  Consider www.fantasyflightgames.com. As a web developer, from both            |
# |       technical and aesthetic perspectives, how would you improve the home |
# |       page?                                                                |
# |                                                                            |
# +----------------------------------------------------------------------------+
# I think the homepage looks pretty great. I'm not sure how I would improve on it asthetically.
# I think it does a good job of presenting recent news stories above the fold and splashing them
# with eye-catching art from the games. It looks great on mobile too.
# From the technical side, I have to admit that I don't have enough experience with angular.js
# to evaluate if it's coded well. The page always seems to work smoothly when I visit the site.