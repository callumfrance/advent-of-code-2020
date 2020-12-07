from typing import Dict, Set, List


class HaverSack:


    def __init__(self, 
            name: str, 
            children: Dict[str, List]=None,
            parents: Set=None,
            ) -> None:
        self.name = name
        if children:
            self.children = children
        if parents:
            self.discovered_parents: Set[HaverSack] = parents
        else:
            self.discovered_parents: Set[HaverSack] = set()

    def add_parent(self, in_parent) -> None:
        self.discovered_parents.add(in_parent)

    def add_child(self, in_child: HaverSack) -> None:
        self.children[in_child.name] = in_child
