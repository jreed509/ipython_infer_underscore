def infer_underscore(lines):
    new_lines = []
    operation_chars = "+-*/."
    numeric_chars = "0123456789"
    if not isinstance(lines, list):
        lines = [lines]
    for line in lines:
        first_char = line[0]
        try:
            second_char = line[1] 
        except IndexError:
            second_char = ""

        if first_char in operation_chars:
            if first_char == ".":
                if second_char in numeric_chars:
                    new_lines.append(line)
                    continue

            new_line = "_"+line
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    return new_lines
