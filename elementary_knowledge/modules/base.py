import base64


print(base64.b64encode(b'binary\x00string'))

print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))


def safe_base64_decode(s):
    elen = len(s) % 4
    print(elen)
    if elen:
        for i in range(elen):
            s += b'='
    print(s)
    return base64.b64decode(s)

safe_base64_decode('YWJjZA')
