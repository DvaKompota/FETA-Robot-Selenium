def sentence_to_snake(text):
    """Return a string of text, converted to snake_case format

    Accepts text in 'Regular sentence' or 'Capitalized Sentence' case format

    :param text:                String of text in 'Regular sentence' or 'Capitalized Sentence' case

    :return:                    String of text, converted to snake_case format

    Usage examples:
        sentence_to_snake("Submit button") -> "submit_button"
        sentence_to_snake("Customer Name") -> "customer_name"
    """
    return text.replace(' ', '_').lower()
