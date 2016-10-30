def convert_to_mandarin(num):
    '''
    * the following is how numbers for Mandarin are arranged
    - there are words for each of the digits from 0 to 10
    - for numbers 11-19  the number is pronounced
    - For numbers between 20 and 99, the number is pronounced as digit ten digit  so for example
      37 would be pronounced (using Mandarin) as three ten seven  If the digit is a zero it is not included
    num = string representing a number between 0 and 99
    returns = the string mandarin representation of num using trans_dict
    '''

    trans_dict = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si',
                  '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu', '10': 'shi'}





