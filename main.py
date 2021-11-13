import csv
import dns
import dns.resolver

# Return the Hamming distance between string1 and string2.
# string1 and string2 should be the same length.
def hamming_distance(string1, string2):
    # Start with a distance of zero, and count up
    distance = 0
    # Loop over the indices of the string
    L = len(string1)
    for i in range(L):
        # Add 1 to the distance if these two characters are not equal
        if string1[i] != string2[i]:
            distance += 1
    # Return the final count of differences
    return distance


with open('real.csv') as real_file, open('FakeListTemp.csv') as fake_file:
    real_reader = csv.reader(real_file, delimiter=',')
    fake_reader = csv.reader(fake_file, delimiter=',')
    real_sites = next(real_reader)
    fake_sites = next(fake_reader)

url = 'amaz0n.com'

real = url in real_sites
fake = url in fake_sites

if real:
    print('real')
elif fake:
    print('fake')
else:
    print('does not exist')

phishing_site = None

if not real and not fake:
    current_ip = dns.resolver.resolve(url, 'A')
    for site in real_sites:
        if len(site) == len(url) and hamming_distance(url, site) == 1:
            real_ip = dns.resolver.resolve(site, 'A')
            matching_ip_count = len(set(current_ip).intersection(real_ip))
            if matching_ip_count > 0:
                print('real')
                break

