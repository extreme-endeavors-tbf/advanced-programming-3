def compress(chars):
        i = 0  # index for all chars in the array
        count = 1  # counter for each char in chars

        # index for chars from indices i+1 to len(chars) + 1
        for j in range(1, len(chars) + 1):

            # First, check all chars after index i to see if we have a match
            if j < len(chars) and chars[j] == chars[j - 1]:
                count += 1  # if so, increment the count

            # if not, then store the char and its count in chars
            else:
                chars[i] = chars[j - 1]
                i += 1
                if count > 1:
                    for char in str(count):
                        chars[i] = char
                        i += 1
                count = 1

        # return the length of the compressed string
        return i

print(compress(["a","a","b","b","c","c","c"]))