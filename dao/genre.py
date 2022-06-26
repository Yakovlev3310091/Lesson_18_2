from dao.model.genres import Genre

class GenreDAO:
    def __int__(self, session):
        self.session = session

    def get(self, gid=None):
        query = self.session.query(Genre)
        if gid:
            return query.get(gid)
        return query.all()

