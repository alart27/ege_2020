from itertools import permutations

def array_reverse(array):
    for i in range(len(array)//2):
        t = array[i]
        array[i] = array[len(array)-1-i]
        array[len(array)-1-i] = t


def int_to_bin(num):
    array = []
    for i in range(8):
            a = num%2
            num = num // 2
            array.append(a)
    array_reverse(array)
    string = ''.join([str(a) for a in array])

    return(string)
    
    
def ip_to_bin(ip_addr):
    strings = ip_addr.split('.')
    ints = [int(s) for s in strings]
    bins = [int_to_bin(i) for i in ints]
    return ' '.join(bins)


def bin_to_int(string):
    s = 0
    pow2 = 1
    array = [int(s) for s in string]
    for i in range(7,-1, -1):
        n = array[i] * pow2
        s += n
        pow2 *= 2

    return s


def bin_to_ip(string):
    strings = string.split()
    ints = [bin_to_int(n) for n in strings]
    ints = [str(n) for n in ints]
    return '.'.join(ints)


def net_addr(ip_addr, mask):
    e = ip_addr.split('.')

    n = [int(e[i]) for i in range(4)]

    r = mask.split('.')

    k = [int(word) for word in r]

    s = [n[i] & k[i] for i in range(4)]

    string = [str(n) for n in s]

    return '.'.join(string)


def find_mask(ip_addr, net_addr):

    ip_b = ip_to_bin(ip_addr)
    net_b = ip_to_bin(net_addr)
    max_number_of_1 = 0
    i = 0

    while ip_b[i] == net_b[i]:
        if i == 8 or i == 17 or i == 26:
            i += 1
        else:
            i += 1
            max_number_of_1 += 1

    min_number_of_1 = max_number_of_1
    k = max_number_of_1

    while ip_b[k] == net_b[k]:
        if ip_b[k] == '1':
            break
        if k == 8 or k == 17 or k == 26:
            k -= 1
        else:
            k -= 1
            min_number_of_1 -= 1

    number_of_masks = max_number_of_1 - min_number_of_1

##    for i in range(min_number_of_1 - 1, max_number_of_1 + 1):
##        if i <=8:
##            return '1'*i + '0'*(8-i) + ' ' + '0'*8 + ' ' + '0'*8 + ' ' + '0'*8
##        elif i <= 16:
##            return '1'*8 + ' ' + '1'*(i-8) + '0'*(16-i) + ' ' + '0'*8 + ' ' + '0'*8
##        elif i <= 24:
##            return '1'*8 + ' ' + '1'*8 + ' ' + '1'*(i-16) + '0'*(24-i) + ' ' + '0'*8
##        else:
##            return '1'*8 + ' ' + '1'*8 + ' ' + '1'*8 + ' ' + '1'*(i-24) + '0'*(32-i)
##
##
    string = ''
    for i in range(min_number_of_1 - 1, max_number_of_1 + 1):
            if i <=8:
                string += '1'*i + '0'*(8-i) + ' ' + '0'*8 + ' ' + '0'*8 + ' ' + '0'*8 + '  '
            elif i <= 16:
                string += '1'*8 + ' ' + '1'*(i-8) + '0'*(16-i) + ' ' + '0'*8 + ' ' + '0'*8 + '  '
            elif i <= 24:
                string += '1'*8 + ' ' + '1'*8 + ' ' + '1'*(i-16) + '0'*(24-i) + ' ' + '0'*8 + '  '
            else:
                string += '1'*8 + ' ' + '1'*8 + ' ' + '1'*8 + ' ' + '1'*(i-24) + '0'*(32-i) + '  '

    return number_of_masks, string.split('  ')

def number_ip_addrs(mask):
    string = ip_to_bin(mask)

    pow2 = 1
    i = 34

    while string[i] == '0' or string[i] == ' ':
        if string[i] == ' ':
            i -= 1
        else:
            i -= 1
            pow2 *= 2
    number = pow2 - 2

    if number != 1:
        return number
    else:
        return 0


def is_correct_ip(ip):
    strings = ip.split('.')
    if len(strings) != 4:
        return False
    for s in strings:
        if len(s) == 0:
            return False
        elif s[0] == '0' and len(s) > 1:
            return False
        elif int(s) > 255:
            return False

    return True

        
def make_up_ip(parts):

    correct_ips = []

    for p in permutations(parts):
        ip = ''.join(p)
        if is_correct_ip(ip):
            correct_ips.append(ip)

    return correct_ips







##def main():
##    data_sets_1 = [
##        [
    




            
    

            
                
            

    









    



    
    
