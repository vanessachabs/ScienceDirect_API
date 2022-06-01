import sys

# Classe que gera uma progressBar para acompanhamento da extração da API
class ProgressBar:
    def __init__(self):
        self.it = None
        self.prefix = None
        self.size = None
        self.file = None

    def progressbar(self, it, prefix="", size=60, file=sys.stdout):
        self.it = it
        self.prefix = prefix
        self.size = size
        self.file = file
        
        count = len(self.it)

        print()
        def show(j):
            x = int(self.size * j / count)
            self.file.write("%s[%s%s] %i/%i\r" % (self.prefix, "#" * x, "." * (self.size - x), j, count))
            self.file.flush()

        show(0)
        for i, item in enumerate(it):
            yield item
            show(i + 1)
        self.file.flush()
        print()