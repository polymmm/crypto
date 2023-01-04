from flask import Flask, render_template, Blueprint, redirect, url_for, flash, request
from base import alphabet, input_for_cipher_short, input_for_cipher_long, output_from_decrypted, replace_all_to, clear_text, dict, alphabet_cyrillic, word_indexes, word_by_indexes, detect_language

bp = Blueprint('RSA', __name__, url_prefix='/RSA')

encrypt_indexes=[]

def rsa_encrypt(n,e,encrypt):
    global encrypt_indexes
    encrypt_indexes=word_indexes(encrypt) #индексы в шифруемом слове
    enc_letters=[] #индексы после шифрования
    enc_word=[] #зашифрованное слово
    output=''
    for letter in encrypt_indexes:
            enc_letters.append(letter**e % n)
            output+=f'{letter} -> {letter}**{e} = {letter**e % n} (mod {n})' + '\n'
    return output

@bp.route('/1', methods=['GET', 'POST'])
def RSA_1():
    clear = ''
    encrypted = ''
    decrypted = ''
    if request.method == 'POST':
        n = int(request.form.get('n'))
        e = int(request.form.get('e'))
        clear = request.form.get('clear')
        encrypted = request.form.get('encrypted')
        decrypted = request.form.get('decrypted')
        if clear:
            encrypted = rsa_encrypt(n,e,clear)
            return render_template('RSA_1.html', clear_text=clear, encrypted_text=encrypted, decrypted_text=decrypted)
        return render_template('RSA_1.html', clear_text=clear, encrypted_text=encrypted, decrypted_text=decrypted)
    else:
        return render_template('RSA_1.html', clear_text=clear_text)
