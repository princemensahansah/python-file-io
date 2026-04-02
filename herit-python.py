#! /usr/bin/env python3

import re

herit_pattern = re.compile(r'(\w*herit\w*)', re.IGNORECASE)

def search_word(infile_name='origin.txt',outfile_name='herit_output.txt'):
    with open(infile_name, 'r') as in_stream:
        print('Opening text for search output...')
        with open(outfile_name, 'w') as out_stream:
            print('Searching for words containing "herit" in origin.txt...')
            for line_index,line in enumerate(in_stream):
                match = herit_pattern.search(line)
                if match:
                    line = line.strip()
                    print(f'{line_index}: {match.groups()[0]}')
                    out_stream.write(f'{line_index}: {match.groups()[0]}\n')


if __name__ == '__main__':
    search_word()