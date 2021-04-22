class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)
    def __setitem__(self, tag, count):


cloud = TagCloud()
cloud["python"]
cloud.add("Python")
cloud.add("python")
cloud.add("python")

print(cloud.tags)