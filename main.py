from cypher import CypherHandler
from Pass import SampleListener
import Leap, sys

def main():
    encoder = CypherHandler()
    listener = SampleListener()
    controller = Leap.Controller()
    print "\t Menu"
    print "1) Encrypt"
    print "2) Decrypt"
    choice = (int(raw_input("Enter your choice: ")))
    if choice == 1:
        message_path = raw_input("Enter file path of message to be encoded: ")
        message = open(message_path,'r')
        listener = SampleListener()
        controller = Leap.Controller()
        listener.reset()
        controller.add_listener(listener)
        try:
            sys.stdin.readline()
        except KeyboardInterrupt:
            pass
        finally:
            controller.remove_listener(listener)
        #print listener.run
        #print listener.password
        key = int(listener.password)
        enc_message = encoder.encrypt(message.read(),key)
        message.close()
        enc_message_path = raw_input("Enter file path for encrypted message: ")
        f = open(enc_message_path, 'w')
        f.write(enc_message)
        f.close()
        print 'done'

    elif choice == 2:
        enc_message_path = raw_input("Enter file path for encrypted message: ")
        enc_message = open(enc_message_path, 'r')
        listener = SampleListener()
        controller = Leap.Controller()
        listener.reset()
        controller.add_listener(listener)
        try:
            sys.stdin.readline()
        except KeyboardInterrupt:
            pass
        finally:
            controller.remove_listener(listener)
        key = int(listener.password)
        message = encoder.decrypt(enc_message.read(),key)
        dec_message_path = raw_input("Enter file path for decrypted message: ")
        dec_message = open(dec_message_path, 'w')
        dec_message.write(message)
        dec_message.close()
        print "Done"

if __name__ == "__main__":
    main()
