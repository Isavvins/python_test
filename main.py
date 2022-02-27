checklist = [
    ('name', 'John', 'John'),
    ('middle_name', '', None),
    ('last_name', 'Smith', 'Smith'),
    ('email', 'johnsmith@example.com', 'john.smith@example.com'),
    ('password', 'da342432', 'dadsa2asd')
]


def compare_fields(check_list):
    errors = list()

    for item in check_list:
        f_name = item[0]
        f_output = item[1] if item[1] else ''
        f_input = item[2] if item[2] else ''
        if f_output.strip() != f_input.strip():
            errors.append('Field \'{}\' value: \'{}\' differs from expected \'{}\''.format(f_name, f_output, f_input))
    if errors:
        return '\n'.join(errors)
    else:
        return None


def test_list():
    errors = compare_fields(checklist)
    if errors:
        print('Account verification failed:\n' + errors)
    else:
        print('Verification complete')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_list()
