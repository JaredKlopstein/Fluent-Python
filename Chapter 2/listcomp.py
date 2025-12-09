# without list comp
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# with list comp
codes_comp = [ord(symbol) for symbol in symbols]

print(codes_comp)