import string
from typing import List
from abc import ABC, abstractmethod


def load_text_file(filepath):
    with open(filepath) as input_file:
        return input_file.read().splitlines()


class ISupplyGrouper(ABC):
    @abstractmethod
    def group_supplies(self, rucksacks: List[str]) -> List[str]:
        raise NotImplementedError


class RucksackCompartmentsSupplyGrouper(ISupplyGrouper):
    def group_supplies(self, rucksacks: List[str]) -> List[str]:
        return [
            [
                rucksack[:int(len(rucksack) / 2)],
                rucksack[int(len(rucksack) / 2):]
            ]
            for rucksack in rucksacks
        ]


class RucksackGroupsSupplyGrouper(ISupplyGrouper):
    def group_supplies(self, rucksacks: List[str]) -> List[str]:
        chunk_size = 3
        return [
            rucksacks[i:i + chunk_size]
            for i in range(0, len(rucksacks), chunk_size)
        ]


class RucksackSupplyPrioritiser:
    def __init__(self, supply_grouper: ISupplyGrouper):
        self._supply_grouper = supply_grouper

        self._item_index_bump = 1 # required to ensure indexing starts from 1 instead of 0
        self._alphabet_length = 26 # requiured to ensure upper and lower case have different indexes

    def get_total_priority(self, rucksacks: List[str]) -> int:
        grouped_supplies = self._supply_grouper.group_supplies(rucksacks)

        grouped_duplicate_supplies = [
            self._find_duplicates_in_supplies(supply_group)
            for supply_group in grouped_supplies
        ]

        total_priority = sum([
            self._get_item_priority(supply)
            for duplicate_group_supplies in grouped_duplicate_supplies
            for supply in duplicate_group_supplies
        ])

        return total_priority
    
    def _get_item_priority(self, item: str) -> int:
        return (
            (string.ascii_lowercase.index(item) + self._item_index_bump)
            if item.islower() else
            (string.ascii_uppercase.index(item) + self._item_index_bump + self._alphabet_length)
        )

    def _find_duplicates_in_supplies(self, supplies: List[str]) -> List[str]:
        if len(supplies) <= 1:
            raise Exception("Not enough supplies provided")
        
        supplies_in_all = []
        for supplies_index in range(len(supplies)):
            clean_supplies = set(supplies[supplies_index].strip())

            if supplies_index == 0:
                supplies_in_all = clean_supplies
                continue
            
            supplies_in_all = supplies_in_all.intersection(clean_supplies)

        supplies_in_all = list(supplies_in_all)
        if not supplies_in_all:
            raise Exception("No supplies found")

        return supplies_in_all


def main():
    input_filepath = "input.txt"
    rucksacks = load_text_file(input_filepath)

    part_1_supply_grouper = RucksackCompartmentsSupplyGrouper()
    part_1_priority_total = RucksackSupplyPrioritiser(part_1_supply_grouper).get_total_priority(rucksacks)
    print("PART 1 PRIORITY TOTAL:", part_1_priority_total)

    part_2_supply_grouper = RucksackGroupsSupplyGrouper()
    part_2_priority_total = RucksackSupplyPrioritiser(part_2_supply_grouper).get_total_priority(rucksacks)
    print("PART 2 PRIORITY TOTAL:", part_2_priority_total)


if __name__ == "__main__":
    main()
