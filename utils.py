def print_paragraph(para):
    para_lines = para.split('\n')
    para_lengths = map(len, para_lines)
    max_line = max(para_lengths)

    message = []
    start_string = '#'
    end_string = '#'
    fill_string = '*'
    header = [
          start_string + (max_line + 2) * fill_string + end_string
        , start_string + (max_line + 2) * ' ' + end_string
    ]

    footer = copy.copy(header)
    footer.reverse()

    message.extend(header)

    for line in para_lines:
        spaces = max_line - len(line)
        message.append(start_string + ' ' + line + (spaces + 1) * ' ' + end_string)

    message.extend(footer)
    print '\n'.join(message)
