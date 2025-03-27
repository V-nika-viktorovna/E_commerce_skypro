class MyExceptions(Exception):

    def __init__(self, *args, **kwargs):

        self.message = args[0] if args else 'Товар с нулевым количеством не может быть добавлен. Товар не добавлен'

    def __str__(self):
        return self.message
