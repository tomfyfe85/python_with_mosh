"CUSTOM CONTAINERS"


class TagCloud:
    def __init__(self):
        # prefix methods with __ to show it is private
        self.__tags = {}

    def add(self, tag):
        "adds a tag and shows the number of tags"
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1
        print(self.__tags)

    def __getitem__(self, tag):
        "usage: print(cloud['python'])  # Output: 3"
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):  
        return iter(self.__tags)


cloud = TagCloud()

cloud.add("Python")
cloud.add("python")
cloud.add("rodeo")