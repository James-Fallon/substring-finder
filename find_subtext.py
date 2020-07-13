
def find_subtext(text_to_search, subtext):

    length_of_text_to_search = len(text_to_search)
    length_of_subtext = len(subtext)

    if length_of_text_to_search < length_of_subtext:
        raise ValueError('The subtext must be smaller than the text to search! Silly goose!')

    indices_of_occurrences = []

    for x in range(length_of_text_to_search - length_of_subtext + 1):
        if subtext.lower() == text_to_search[x:x+len(subtext)].lower():
            # Adding a plus one here so that the output is indexed at 1 instead of 0 (better for humans to read)
            indices_of_occurrences.append(x + 1)

    return indices_of_occurrences


if __name__ == '__main__':

    text_to_search = input('Enter text to search: ')
    subtext = input('Enter the subtext to find: ')

    results = find_subtext(text_to_search, subtext)

    print(f'The subtext "{subtext}" can be found at the following indices: {results}')
