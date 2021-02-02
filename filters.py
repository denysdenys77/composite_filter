from typing import Any, List, Set


class Person:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


class CompositeFilter:

    def __init__(self):
        self.components: list = []

    def add_component(self, component: Any) -> None:
        """ Adds a component to a CompositeFilter. """
        self.components.append(component)

    def remove_component(self, component: Any) -> None:
        """ Removes a component to a CompositeFilter. """
        self.components.remove(component)

    def filter(self, iterable: List[Any], attribute: Any) -> List[Any]:
        """ Filters sequence with filters from  self.components """
        result: Set[Any] = set()

        for component in self.components:
            result.update(component.filter(iterable, attribute))

        return list(result)


class NameFilter:

    def filter(self, iterable: List[Any], attribute: Any):
        """ Filters sequence by name. """
        return [_ for _ in iterable if _.name == attribute]


class SurnameFilter:

    def filter(self, iterable: List[Any], attribute: Any):
        """ Filters sequence by surname. """
        return [_ for _ in iterable if _.surname == attribute]


def main() -> None:
    denys = Person('Denys', 'Kuznetsov')
    vasiliy = Person('Vasiliy', 'Kuznetsov')
    sergey = Person('Sergey', 'Levich')
    people = [denys, vasiliy, sergey]

    people_filter = CompositeFilter()
    people_filter.add_component(NameFilter())
    people_filter.add_component(SurnameFilter())

    print('Lets find all people whose surname is "Kuznetsov":')
    [print(f'{_.name} {_.surname}') for _ in people_filter.filter(people, 'Kuznetsov')]
    print()

    print("Let's find someone smarter:")
    [print(f'{_.name} {_.surname}') for _ in people_filter.filter(people, 'Sergey')]


if __name__ == '__main__':
    main()
