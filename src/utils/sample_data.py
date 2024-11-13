def copy_first_n_rows(n, input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for i, line in enumerate(infile):
            if i < n:
                outfile.write(line)
            else:
                break

# Example usage:
copy_first_n_rows(100000, 'data/steam_reviews.json', 'data/sample_steam_reviews.json')