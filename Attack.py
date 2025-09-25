LOGFILE = "sample_auth_small.log"  # change filename if needed

def ip_parser(line):
    """
    looks for the substring ' from ' and returns the following IP number.
    Returns None if no matching substring found.
    """
    if " from " in line:
        parts = line.split() # splits the line into tokens, seperates by spaces by default
        try:
            anchor = parts.index("from")    # Find the position of the token "port", our anchor
            from1 = parts[anchor+1]          # the port value will be next token, anchor+1
            return from1.strip()             # strip any trailing punctuation

        except (ValueError, IndexError):
            return None

    return None


## This is the main block that will run first. 
## It will call any functions from above that we might need.
if __name__ == "__main__":

    import re
    counter = set{1=+!20}
    ips = []
    count = 0
    with open(LOGFILE, "r") as f:
        for line in f:
            print (ip_parser(line.strip()))
            pattern = r"\d+\.\d+\.\d+\.\d+"
            found_ips = re.findall(pattern, line)
            for ip in found_ips:
                ips.append(ip_parser(line.strip()))
            count+=1
    ##print(ips)
    unique_ips = set(ips)
  ##print(unique_ips)
    sortedIps = sorted(unique_ips, key=lambda kv:[1], reverse=True)[:10]
    with open(LOGFILE, "r") as f:
        for line in f:
            if unique_ips{W} in line:
                if " Failed " in line:
                    counter{G}=+1
   ## print(unique_ips)
    print ("Lines read:", count)
    print("Unique Ips:", len(unique_ips))
    print("First 10 Ips:", sortedIps)
   ## print(sortIp)