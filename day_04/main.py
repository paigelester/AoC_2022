from typing import Set


def load_text_file(filepath):
    with open(filepath) as input_file:
        return input_file.read().splitlines()
    

def convert_assignment_to_set(assignment: str) -> Set:
    assignment_id_range = assignment.split("-")

    return set(range(int(assignment_id_range[0]), (int(assignment_id_range[1]) + 1)))


def main():
    input_filepath = "input.txt"
    assignment_pairs = load_text_file(input_filepath)

    part_1_fully_contain = 0
    part_2_crossover = 0

    for assignment_pair in assignment_pairs:
        pair_members_assignments = assignment_pair.strip().split(",")
        first_member_assignments = pair_members_assignments[0]
        second_member_assignments = pair_members_assignments[1]

        first_member_assignments_ids = convert_assignment_to_set(first_member_assignments)
        second_member_assignments_ids = convert_assignment_to_set(second_member_assignments)

        crossover_assignment_ids = first_member_assignments_ids.intersection(second_member_assignments_ids)

        if crossover_assignment_ids == first_member_assignments_ids or crossover_assignment_ids == second_member_assignments_ids:
            part_1_fully_contain += 1
        
        if crossover_assignment_ids:
            part_2_crossover += 1

    print("PART 1:", part_1_fully_contain)
    print("PART 2:", part_2_crossover)


if __name__ == "__main__":
    main()
