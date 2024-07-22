class Account():
    def __init__(self, **kwargs):
        self.username = kwargs['username']
        self.password = kwargs['password']
        self.role = kwargs['role']