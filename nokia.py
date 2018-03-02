#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Patricia Jesus, 46593"
__copyright__ = "Programação II, LTI, DI/FC/UL, 2016"

def teclas_para_palavra(message):
    '''
    Requires: message a string that contains only numbers (2-9) and spaces
    Ensures: decrypts the message return a string.
    O(n), where n represents the number of times that function runs.

    Regioes and Caracteristics:
    -String with spaces and different numbers
    -Stirng with spaces and without spaces, and 3/2 of the same number
    -String without anything
    -String with differnt numbers and no spaces and none repeated
    -String with different numbers and repeted
    -String where the same number is repeated differently
    '''
    
    end = 1
    splits = []
    alpha = {'2':'A', '22':'B', '222':'C', '3':'D', '33':'E', '333':'F', '4':'G', '44':'H', '444':'I', '5':'J', '55':'K', '555':'L', '6':'M', '66':'N', '666':'O', '7':'P', '77':'Q', '777':'R', '7777':'S', '8':'T', '88':'U', '888':'V', '9':'W', '99':'X', '999':'Y', '9999':'Z'}           

    while end < len(message):
        if message[end]!=message[end-1] and not (message[end]== ' ' or message[end-1]== ' '):
            splits.append(end)
        end += 1
    for i in range(len(splits)):
        message = message[:splits[i]] + ' ' + message[splits[i]:]
        if i+1 != len(splits):
            splits[i+1]+=1*(i+1)
    message=message.strip()
    l = message.split()
    m = ''
    if len(message)>0:
        for i in l:
            if i[0] in ['7','9']:
                if len(i)%4==0:
                    m+=alpha[4*''.join(set(i))]
                else:
                    m+=alpha[len(i)%4*''.join(set(i))]
            else:
                if len(i)%3==0:
                    m+=alpha[3*''.join(set(i))]
                else:
                    m+=alpha[len(i)%3*''.join(set(i))]
        return m     
    else:
        return m


if __name__ == "__main__":
    import doctest
    doctest.testmod()  
