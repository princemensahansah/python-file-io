print('Opening dummy.txt for reading...')

with open('dummy.txt', 'r') as in_stream:
    
    print('Opening output.txt for writing...')
    with open('output.txt', 'w') as out_stream:
        print('Copying contents of dummy.txt to output.txt...')
        for line_index, line in enumerate(in_stream):
            line.strip()
            word_list = line.split()
            for word in word_list:
                out_stream.write(f'{line_index}\t{word}\n')   

print('Done!')
print('In_stream closed:', in_stream.closed)
print('Out_stream closed:', out_stream.closed)