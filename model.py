from functools import total_ordering


@total_ordering
class Filmek:
    cim: str
    __hossz: int
    _korhat: bool

    def __init__(self, cim, hossz, korhat):
        self.cim = cim
        self.__hossz = hossz
        self._korhat = korhat

    @property
    def hossz(self):
        return self.__hossz

    @hossz.setter
    def hossz(self, ert):
        self.__hossz = ert

    @property
    def korhat(self):
        return self._korhat

    @korhat.setter
    def korhat(self, ert):
        self._korhat = ert

    def __repr__(self):
        return f'{self.cim}, {self.__hossz}, {self._korhat}'

    def __str__(self):
        return f"{self.cim}: {self.__hossz} perces, {'korhataros' if self._korhat else 'nem korhatáros'}"

    def __eq__(self, other):
        if not isinstance(other, Filmek):
            return NotImplemented('Nem létezik ilyen!')
        return self.cim == other.cim and self.__hossz == other.__hossz and self._korhat == other._korhat

    def __lt__(self, other):
        if self.__hossz != other.__hossz:
            return self.__hossz > other.__hossz
        if self._korhat != other._korhat:
            return self._korhat < other._korhat
        return self.cim < other.cim

    @staticmethod
    def Film_L_H(filmek, hossz):
        ls = []
        for i in filmek:
            if i.__hossz == hossz:
                ls.append(i.cim)
        return ls


class Sorozatok(Filmek):
    __ep: int

    def __int__(self, cim, hossz, ep, korhat):
        super().__init__(cim, hossz, korhat)
        self.__ep = ep

    def __repr__(self):
        return f'{self.cim}, {self.__hossz}, {self._korhat}, {self.__ep}'

    def __str__(self):
        return f"{self.cim}: {self.__hossz} perces, {'korhatáros' if self._korhat else 'nem korhatáros'}, {self.__ep} részes"

