import argparse
import time
import subprocess

def main():
    parser = argparse.ArgumentParser(
        description = 'Allows you to call the "dig" utility with dictionaries to enumerate subdomains.',
        epilog = 'EXAMPLE: subdomaindigger.py -S 1.1.1.1 -P 53 -T A -d /usr/share/wordlists/thunter/subdomains.txt -u itmo.xyz'
    )
    parser.add_argument('-S', '--dns-server', help='set a dns server')
    parser.add_argument('-P', '--dns-server-port', help='set a dns server port')
    parser.add_argument('-T', '--dns-record-type', help='set record type')
    parser.add_argument('-d', '--dictionary', help='set a dictionary of subdomains to enumerate')
    parser.add_argument('-u', '--domain-to-enumerate', help='set a domain')
    args =  parser.parse_args() 
    if None in (args.dns_server, args.dns_server_port, args.dictionary, 
                args.domain_to_enumerate, args.dns_record_type):
        print('\n[ERROR] Not enough arguments.\n')
        parser.print_help()
    else:
        try:            
            with open(args.dictionary, 'r') as f:
                lines = f.readlines()
            found_domains = 0
            total_lines_number = len(lines)
            for i, line in enumerate(lines):
                subdomain = line.strip()
                program = subprocess.run(['dig', f'@{args.dns_server}', '-p', args.dns_server_port, f'{subdomain}.{args.domain_to_enumerate}',args.dns_record_type], 
                                         capture_output=True)
                result = program.stdout.decode()
                for try_number in range(100):
                    if 'communications error' in result:
                        pass
                    else:
                        how_many_answers_in_the_result = result.splitlines()[6].split(';')[3].split(',')[1].split(':')[1].strip()
                        if how_many_answers_in_the_result == '0':
                            pass
                        else:
                            ip_address = result.splitlines()[13].split('\t')[-1]
                            found_domains += 1
                            print(f'[word:{i}/{total_lines_number},{int(i*100/total_lines_number)}%] [found:{found_domains}] {ip_address} {subdomain}.{args.domain_to_enumerate}')
                            break
        except Exception as e:
            print(f'\n[ERROR] DNS record retrieval error.\n[ERROR] Python: {e}\n')

if __name__ == '__main__':
    main()