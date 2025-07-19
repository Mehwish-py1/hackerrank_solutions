def merge_the_tools(string, k):

    for i in range(0, len(string), k):
        chunk = string[i:i+k]
        result = ""
        seen = set()
        for c in chunk:
            if c not in seen:
                result += c  
                seen.add(c)
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    