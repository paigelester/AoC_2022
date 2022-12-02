def load_text_file(filepath):
    with open(filepath) as input_file:
        return input_file.read().splitlines()

def main():
    input_filepath = "input.txt"
    calorie_data = load_text_file(input_filepath)

    calorie_count_by_elf = []
    current_calorie_count = 0

    for item_calorie_count in calorie_data:
        if item_calorie_count.strip() == "":
            calorie_count_by_elf.append(current_calorie_count)
            current_calorie_count = 0
        else:
            current_calorie_count += int(item_calorie_count)
    
    calorie_count_by_elf.sort(reverse=True)
    
    print("Top calorie count:", calorie_count_by_elf[0])
    print("Top 3 calorie counts:", calorie_count_by_elf[:3])
    print("Total top 3 calorie count:", sum(calorie_count_by_elf[:3]))

if __name__ == "__main__":
    main()