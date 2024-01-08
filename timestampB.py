import re


# 1.create a pattern
pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>.*?)\] "(?P<request>.*?)" (?P<status>\d+) (?P<bytes>\d+) "(?P<referrer>.*?)" "(?P<user_agent>.*?)"')
def parse_log_file(file_path):
    with open (file_path, 'r') as file:
        for line in file:
            match = pattern.match(line)
            if match:
                log_info = match.groupdict()
            ## Extract specific information using named groups

                print(f"ip : {log_info["ip"]}, timestamp: {log_info ['timestamp']}]")
            else:
                print('No match')

def parse_and_compare(file_path1, file_path2, output_file_path):
    with open(file_path1, 'r') as file1:
        data1 = {match['ip']: match for line in file1 if (match := pattern.match(line))}
    
    with open(file_path2, 'r') as file2:
        with open(output_file_path, 'w') as outfile:
            for line in file2:
                match = pattern.match(line)
                if match:
                    log_info = match.groupdict()
                    ip_address = log_info["ip"]

                    if ip_address in data1:
                        # Match found, write your data to the output file
                        outfile.write(f"Match found for IP: {ip_address}\n")
                        # You can write more data based on log_info or other requirements



    

    
    


#parse_log_file('time.txt')
parse_and_compare("time.txt", "time1.txt", "output_file.txt")



