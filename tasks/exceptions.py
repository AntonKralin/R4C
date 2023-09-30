class ValidJSON(Exception):
    def __init__(self, message):
        super().__init__(message)


class DublicateData(Exception):
    def __init__(self, message, data):
        self.message = message
        self.data = data

    def __str__(self):
        return self.message + ': ' + ' '.join([self.data.serial,
                                              str(self.data.created)])
