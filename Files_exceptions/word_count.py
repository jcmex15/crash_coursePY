def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
            " words.")
    
# filename ='Files_exceptions/alice.txt'
# count_words(filename)

filenames = ['Files_exceptions/alice.txt', 'Files_exceptions/siddhartha.txt', 'Files_exceptions/moby_dick.txt', 'Files_exceptions/little_women.txt']
for filename in filenames:
    count_words(filename)