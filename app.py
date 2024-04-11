def parse_config(file_path):
    parsed_data = []
    external_ips = []
    interface_block = []
    in_interface_block = False
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            
            # Check for external IP addresses
            if line.startswith(' ip address'):
                ip_address = line.split()[2]
                if '.' in ip_address.split('.')[0]:
                    external_ips.append(ip_address)
            
            # Check for interface configurations
            if line.startswith('interface'):
                in_interface_block = True
                interface_block.append(line)
            elif in_interface_block:
                if line.startswith('!'):
                    in_interface_block = False
                    parsed_data.append('\n'.join(interface_block))
                    interface_block = []
                else:
                    interface_block.append(line)
            
            # Check for other important data
            if line.startswith(('Last config change', 'version', 'hostname', 'Vulnerabilities associated with version', 
                                'Encryption used/privileges level', 'Time zone', 'Routes info', 'Acts', 'banner', 
                                'ssh', 'telnet', 'Details of nap server', 'Logging info')):
                parsed_data.append(line)
                
    return parsed_data, external_ips

def write_to_file(data, external_ips):
    with open('output.txt', 'w') as f:
        f.write("External IP Addresses:\n")
        for ip in external_ips:
            f.write(ip + '\n')
        f.write("\n\n")
        
        f.write("Configuration Details:\n")
        for item in data:
            f.write("%s\n" % item)

if __name__ == '__main__':
    config_data, external_ips = parse_config('sampconf.txt')
    write_to_file(config_data, external_ips)
    print("Output written to output.txt")
