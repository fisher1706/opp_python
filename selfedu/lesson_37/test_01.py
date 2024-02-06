class Meta(type):
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, bases, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


"""
    class Meta reformat class Women to:

    class Women(metaclass=Meta):
    class_attrs = {
        "title": "way title",
        "content": "way content",
        "photo": "way photo"
    }
    title = "way title"
    content = "way content"
    photo = "way photo"
    
    def __init__(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value
"""


class Women(metaclass=Meta):
    title = "way title"
    content = "way content"
    photo = "way photo"


if __name__ == '__main__':
    w = Women()
    print(w.__dict__)
