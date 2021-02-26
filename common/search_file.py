import os


class SearchFile():
    def __init__(self, path):
        self.path = path

    def search_file(self, suffix):
        list = []
        for i in os.listdir(self.path):
            if i.endswith(suffix):
                list.append(i)
        return tuple(list)


if __name__ == '__main__':
    result = SearchFile(os.getcwd()).search_file(".jar")
    print(result)
