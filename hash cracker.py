import hashlib
var = 'b6d3aa0fb2b0b2e6732ee101c7608af8'

for i in range(0,1000):
    flag = "FS{cabbage-wait_that's_not_right_" + str(i) + "}"
    hash = hashlib.md5(flag.encode())
    if hash.hexdigest() == var:
        print(hash.hexdigest())
        print(flag)
