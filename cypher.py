class CypherHandler():
    
    def encrypt(self, message, key):
            enc_message = ""
            for line in message:
                for letter in line:
                    ind = ord(letter)
                    m = (ind ^ key)
                    #print m
                    #print unichr(m)
                    #print chr(m)
                    enc_message = enc_message + unichr(m%128)
            return enc_message

    def decrypt(self, enc_message, key):
            dire = True
            message = ""
            for line in enc_message:
                for letter in line:
                    ind = ord(letter)
                    m = (ind ^ key)
                    #print chr(m)
                    message = message + unichr(m%128)
            return bytes(message.encode('utf-8'))
