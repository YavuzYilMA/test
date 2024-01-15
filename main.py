import itertools
import string

def generate_complex_passwords(name):
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~"
    all_characters = f"{name}{special_characters}{string.ascii_letters}{' '}"
    
    # Tüm klavye tuşlarını içeren karakter seti
    character_sets = [all_characters]

    # itertools.product ile karakter setlerinin tüm kombinasyonları elde edilir
    for variation in itertools.product(*character_sets, repeat=len(name)):
        # Her kombinasyon birleştirilerek yeni bir şifre oluşturulur
        password = ''.join(variation)
        print(password)

# Örnek kullanım
name = "sifre"
generate_complex_passwords(name)