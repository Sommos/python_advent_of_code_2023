def sum_calibration_values(calibration_document):
    total_sum = 0
    number_dict = {"one": "1", "two": "2", "three": "3", "four": "4",
                   "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for line in calibration_document:
        digits = []
        for word in line.split():
            if word.isdigit():
                digits.append(word)
            elif word in number_dict:
                digits.append(number_dict[word])
        if digits:
            calibration_value = int(digits[0] + digits[-1])
            total_sum += calibration_value

    return total_sum


def read_calibration_document(file_path):
    with open(file_path, 'r') as file:
        calibration_document = [line.strip() for line in file.readlines()]

    return calibration_document


file_path = 'input.txt'

calibration_document = read_calibration_document(file_path)

result = sum_calibration_values(calibration_document)
print("The sum of calibration values is:", result)
