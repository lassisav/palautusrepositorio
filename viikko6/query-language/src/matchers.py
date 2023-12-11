class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class All:
    def __init__(self):
        pass

    def test(self, player):
        return True

class Not:
    def __init__(self, func):
        self._func = func

    def test(self, player):
        value = self._func.test(player)
        if value:
            return False
        return True

class Or:
    def __init__(self, *conditions):
        self._conditions = conditions

    def test(self, player):
        for condition in self._conditions:
            if condition.test(player):
                return True
        return False

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value