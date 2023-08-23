# subdomaindigger
Allows you to call the "dig" utility with dictionaries to enumerate subdomains.

## Requirements
* python
* dig

## How to install
No installation required.

## How to run
1. `git clone https://github.com/vadimmugalimov/subdomaindigger.git`
2. `cd subdomaindigger`
3. `python3 subdomaindigger.py -h`

## Documentation
`python3 subdomaindigger.py -h`

## Example 
`subdomaindigger.py -S 1.1.1.1 -P 53 -T A -d /usr/share/wordlists/thunter/subdomains.txt -u itmo.xyz`
