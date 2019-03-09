def series_of_tubes(word):
  # Stage 1: Checks that the input is uppercase letters, then rot13s it.
  stage1 = list()
  for character in word:
    if not character.isupper():
      return 'Error in stage 1: %s is not all uppercase letters' % word
    stage1.append(rot13(character))

  # Stage 2: Pairs up letters in the input and checks that each pair is an ISO
  # 3166-1 alpha-2 assigned or reserved country code.
  stage2 = list()
  for index in range(0, len(stage1), 2):
    pair = ''.join(stage1[index:index + 2])
    if pair not in country_codes:
      return 'Error in stage 2: %s is not an ISO country code' % pair
    stage2.append(pair)

  # Stage 3: Treats each pair of letters as two base-36 numbers and multiplies
  # them, then checks that the product has three digits.
  stage3 = list()
  for letter1, letter2 in stage2:
    product = int(letter1, 36) * int(letter2, 36)
    if product < 100 or product >= 1000:
      return 'Error in stage 3: %s does not have three digits' % product
    stage3.append(product)

  # Stage 4: Assembles the middle digit of each three-digit product into one
  # number, and checks that it is prime.
  stage4 = ''
  for product in stage3:
    stage4 += str(product)[1]
  if not is_prime(int(stage4)):
    return 'Error in stage 4: %s is not prime' % stage4

  # Stage 5: Sums the digits of the prime and checks that the result can be
  # converted back into a letter using base-36.
  stage5 = 0
  for digit in stage4:
    stage5 += int(digit)
  if stage5 < 10 or stage5 >= 36:
    return 'Error in stage 5: %s is not a letter' % stage5

  # Here's the final answer!
  answer = alphabet[stage5 - 10]
  return 'Success!'

### HELPER FUNCTIONS: FEEL FREE TO IGNORE ###

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rot13(character):
  return alphabet[(alphabet.index(character) + 13) % 26]

country_codes = set('''
AC AD AE AF AG AI AL AM AN AO AP AQ AR AS AT AU AW AX AZ BA BB BD BE BF BG BH BI
BJ BL BM BN BO BR BS BT BU BV BW BX BY BZ CA CC CD CF CG CH CI CK CL CM CN CO CP
CR CS CU CV CX CY CZ DE DG DJ DK DM DO DY DZ EA EC EE EF EG EH EM EP ER ES ET EU
EV EW EZ FI FJ FK FL FM FO FR FX GA GB GC GD GE GF GG GH GI GL GM GN GP GQ GR GS
GT GU GW GY HK HM HN HR HT HU IB IC ID IE IL IM IN IO IQ IR IS IT JA JE JM JO JP
KE KG KH KI KM KN KP KR KW KY KZ LA LB LC LF LI LK LR LS LT LU LV LY MA MC MD ME
MF MG MH MK ML MM MN MO MP MQ MR MS MT MU MV MW MX MY MZ NA NC NE NF NG NI NL NO
NP NR NT NU NZ OA OM PA PE PF PG PH PI PK PL PM PN PR PS PT PW PY QA RA RB RC RE
RH RI RL RM RN RO RP RS RU RW SA SB SC SD SE SF SG SH SI SJ SK SL SM SN SO SR ST
SU SV SY SZ TA TC TD TF TG TH TJ TK TL TM TN TO TP TR TT TV TW TZ UA UG UK UM UN
US UY UZ VA VC VE VG VI VN VU WF WG WL WO WS WV YE YT YU YV ZA ZM ZR ZW
'''.split())

def is_prime(number):
  divisor = 2
  while divisor * divisor <= number:
    if number % divisor == 0:
      return False
    divisor += 1
  return True

import sys
print series_of_tubes(sys.argv[1])
