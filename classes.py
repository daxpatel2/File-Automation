import os
USER = os.getenv('USER')

class Locations:
    def __init__(self, user):
        self.user = USER

    def img(self):
        return '/Users/{}/Downloads/images/'.format(self.user)

    def documents(self):
        return '/Users/{}/Downloads/documents/'.format(self.user)

    def others(self):
        return '/Users/{}/Downloads/others/'.format(self.user)

    def software(self):
        return '/Users/{}/Downloads/softwares/'.format(self.user)

