with open('cool.webp','rb') as rf:
    with open('cool_copy.webp','wb') as wf:
        n_chunk=2024 # 2024 bits ==> 2 Bytes
        rf_chunk=rf.read(n_chunk)
        while rf_chunk:
            wf.write(rf_chunk)
            rf_chunk=rf.read(n_chunk)