chunk_size = 9

with open('fruits.txt') as f:

    txt = f.read(chunk_size)

    while len(txt) > 0:
        print(f"*, {f.tell()} [{txt}]" )
        txt = f.read(chunk_size)


