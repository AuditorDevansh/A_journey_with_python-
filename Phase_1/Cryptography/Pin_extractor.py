def pin_extractor(poems: list[str]) -> list[str]:
    """Extracts a secret PIN code from a list of poems based on word lengths.

    For each poem, it looks at each line and extracts the length of the word
    at the matching line index. If the line is too short, it appends '0'.
    """
    secret_codes = []
    for poem in poems:
        secret_code = ""
        lines = poem.split("\n")
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += "0"
        secret_codes.append(secret_code)
    return secret_codes


if __name__ == "__main__":
    # Test Data
    poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

    poem2 = (
        "The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow"
    )
    poem3 = "There\nonce\nwas\na\ndragon"

    # Execution
    results = pin_extractor([poem, poem2, poem3])
    print(results)
