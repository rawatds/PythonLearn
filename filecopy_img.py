
with open('dsr.jpg', 'rb') as rf,   open('dsr_copy.jpg', 'wb') as wf:
    for line in rf:
        wf.write(line)
