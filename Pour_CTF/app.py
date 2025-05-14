def cisco_decrypt_7(encoded):
    xlat = [
        0x64, 0x73, 0x66, 0x64, 0x3B, 0x6B, 0x66, 0x6F,
        0x41, 0x2C, 0x2E, 0x69, 0x79, 0x65, 0x77, 0x72,
        0x6B, 0x6C, 0x64, 0x4A, 0x4B, 0x44, 0x48, 0x53,
        0x55, 0x42
    ]
    seed = int(encoded[:2])
    result = ''
    for i in range(2, len(encoded), 2):
        b = int(encoded[i:i+2], 16)
        result += chr(b ^ xlat[seed % len(xlat)])
        seed += 1
    return result

# Exemples :
print("hub:", cisco_decrypt_7("025017705B3907344E"))
print("admin:", cisco_decrypt_7("10181A325528130F010D24"))
print("guest:", cisco_decrypt_7("124F163C42340B112F3830"))
print("con line:", cisco_decrypt_7("144101205C3B29242A3B3C3927"))


$1$p8Y6$MCdRLBzuGlfOs9S.hXOp0