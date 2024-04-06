def parse_config(file_path):
    parsed_data = ""
    important_data = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(('!', 'version', 'hostname', 'interface', 'ip address', 'crypto', 'access-list')):
                important_data.append(line)
    parsed_data = '\n'.join(important_data)
    return parsed_data

def write_to_file(data):
    with open('output.txt', 'w') as f:
        f.write(data)

if __name__ == '__main__':
    config_data = parse_config('sampconf.txt')
    write_to_file(config_data)
    print("Output written to output.txt")
