class Women:
    title = "value title"
    photo = "value photo"
    ordering = "value ordering"

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + "@" + psw)

    class Meta:
        ordering = ["id"]

        def __init__(self, access):
            self._access = access
            self._t = Women.title


if __name__ == '__main__':
    print(Women.ordering)
    print(Women.Meta.ordering)
    print("*" * 200)

    w = Women("test", "123")
    print(w.ordering)
    print(w.Meta.ordering)
    print(w.__dict__)
    print("*" * 200)
    print(w.meta.__dict__)
