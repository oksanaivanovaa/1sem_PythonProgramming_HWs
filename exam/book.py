import sys


def main(args):

    pbook = "book-Ivanova.ph"
    cmdtokens = args[1:]
    while True:
        if not cmdtokens:
            print('Have no arguments. Please, specify the command')
            break
        cmd = cmdtokens[0]
        cmdargs = cmdtokens[1:]

        '''Make a list of contacts from pbook'''
        with open(pbook) as f:
            contacts = f.readlines()

        if cmd == 'add':
            if len(cmdargs) < 4 or len(cmdargs) % 2 != 0:
                print("Error in arguments: the structure should be "
                      "'add <Last name> <First name> <Tag-1> "
                      "<Phone-1> <Tag-2> <Phone-2> ... ' ")
                break

            name = ' '.join(cmdargs[:2])

            '''Checking unique tag names and phone numbers'''
            t = False
            for i in range(2, len(cmdargs)):
                k = i % 2
                cmdargs_i = cmdargs[:i]+cmdargs[i+1:]

                if cmdargs[i] in set(cmdargs_i):
                    if k == 0:
                        print('Error: you have identical tags %s for '
                              'one person. Please, change tags' % cmdargs[i])
                    else:
                        print('Error: you have identical phone numbers %s '
                              'for one person. Please, change phone '
                              'numbers' % cmdargs[i])
                    t = True
                    break
            if t:
                break

            summ = name + ' '
            for i in range(2, len(cmdargs), 2):
                summ += cmdargs[i]+':' + cmdargs[i+1]+' '

            with open(pbook, 'a') as f:
                f.write(summ[:-1] + '\n')
            print("Phonebook was succesfully updated")

        elif cmd == 'remove':

            if len(cmdargs) < 2:
                print("Error in arguments: the structure should be "
                      "<Last name> <First name> [Tag] ")
                break

            laname = cmdargs[0]
            finame = cmdargs[1]
            intag = cmdargs[2]

            '''Make a list with update contacts without one chosen'''
            new_contacts = []
            p = False
            for con in contacts:
                '''Read the components of contact'''
                c = con.split(' ')
                lname = c[0]
                fname = c[1]
                tags = [c[i].split(':')[0] for i in range(2, len(c))]
                phones = [c[i].split(':')[1] for i in range(2, len(c))]

                if lname == laname and fname == finame:
                    i = 0
                    p = True

                    for t in tags:
                        if t == intag:
                            break
                        else:
                            p = False
                        i += 1

                    '''Make a new contact-string without tag'''
                    if len(tags) == 1:
                        continue
                    snew = laname+' '+fname+' '
                    for k in range(len(tags)):
                        if k != i:
                            snew += tags[k] + ':' + phones[k]+' '
                    snew += '\n'
                    new_contacts.append(snew)
                    continue
                new_contacts.append(con)

            if p is False:
                print('There is no such name or tag in the phonebook')

            else:
                with open(pbook, 'w') as f:
                    f.writelines(new_contacts)
                print('Phonebook was successfully updated: '
                      'phone number %s %s %s removed'
                      % (laname, finame, intag))

        elif cmd == 'get':

            if len(cmdargs) < 2:
                print("Error in arguments: the structure should be "
                      "<Last name> <First name> [Tag]")
                break

            laname = cmdargs[0]
            finame = cmdargs[1]
            intag = cmdargs[2]

            p = False
            for con in contacts:
                '''Read the components of contact'''
                c = con.split(' ')
                lname = c[0]
                fname = c[1]
                tags = [c[i].split(':')[0] for i in range(2, len(c))]
                phones = [c[i].split(':')[1] for i in range(2, len(c))]

                if lname == laname and fname == finame:
                    i = 0
                    p = True

                    for t in tags:
                        if t == intag:
                            break
                        i += 1
                    print('Contact %s %s %s phone: '
                          % (laname, finame, intag), phones[i])
                    break
            if not p:
                print('There is no such name or tag in the phonebook')

        elif cmd == 'mod':

            if len(cmdargs) != 4:
                print("Error in arguments: the structure should be "
                      "<Last name> <First name> <Tag> <New number> ")
                break

            laname = cmdargs[0]
            finame = cmdargs[1]
            intag = cmdargs[2]
            new_phone = cmdargs[3]

            new_contacts = []
            p = False
            for con in contacts:
                '''Read the components of contact'''
                c = con.split(' ')
                lname = c[0]
                fname = c[1]
                tags = [c[i].split(':')[0] for i in range(2, len(c))]
                phones = [c[i].split(':')[1] for i in range(2, len(c))]

                if lname == laname and fname == finame:
                    i = 0
                    p = True

                    for t in tags:
                        if t == intag:
                            break
                        else:
                            p = False
                        i += 1
                    '''Make a new contact-string with modified tag'''
                    snew = laname+' '+fname+' '+intag + ':' + new_phone+' '
                    for k in range(len(tags)):
                        if k != i:
                            snew += tags[k] + ':' + phones[k]+' '

                    new_contacts.append(snew[:-1])
                    continue
                new_contacts.append(con)

            if p is False:
                print('There is no such name or tag in the phonebook')

            else:
                with open(pbook, 'w') as f:
                    f.writelines(new_contacts)
                print('Phonebook was successfully modified')

        elif cmd == 'view':

            with open(pbook, 'r') as f:
                print('Phonebook %s:' % pbook)
                for line in sorted(f.readlines()):
                    print(line[:-1] if line[-1] == '\n' else line)

        else:
            print('Unknown command: {cmd}'.format(cmd=cmd))

        break


if __name__ == '__main__':
    main(sys.argv)
