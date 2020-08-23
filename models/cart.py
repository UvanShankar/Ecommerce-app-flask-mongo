# mongo-engine packages
from mongoengine import Document, StringField,ListField
class Cart(Document):
    """
    Template for a mongoengine document, which represents a user's favorite Product.

    :param name: required string value
    :param description: optional string value, fewer than 120 characters
    :param price: optional float value
    :param image_url: optional string image url
    :Example:

    >>> import mongoengine
    >>> from app import default_config

    >>> mongoengine.connect(**default_config['MONGODB_SETTINGS'])
    MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, read_preference=Primary())

    >>> new_Product = Products(name= "Vegetable Spring Rolls", \
                        description= "These crisp veggie rolls are filled with"  \
                                     "cabbage, peppers, cucumber, and home-made peanut sauce.")
    >>> new_Product.save()
    <Product: Product object>

    """

    products = ListField(StringField(max_length=50))