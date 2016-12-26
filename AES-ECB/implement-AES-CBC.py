from Crypto.Cipher import AES

KEY = "YELLOW SUBMARINE"
BLOCK_SIZE = 16


def pad(message):
    number_of_missing_bytes = BLOCK_SIZE - len(message) % BLOCK_SIZE
    for x in range(number_of_missing_bytes):
        message += str(chr(number_of_missing_bytes))
    return message


def Encrypt(pt, key):
    mode = AES.MODE_ECB
    encryptor = AES.new(key, mode)
    pt = pad(pt)
    return encryptor.encrypt(pt)

plaintext = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus sagittis leo quis malesuada sodales. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum gravida condimentum sem sit amet ultrices. Fusce porttitor non libero nec eleifend. Sed et libero vitae dui cursus fermentum. Nullam consectetur, tellus non pharetra volutpat, risus massa fringilla ipsum, nec aliquet enim mauris nec nulla. Sed dignissim mi in nulla hendrerit, placerat hendrerit risus luctus.
Nam id dui feugiat lacus rutrum tempor viverra sed mauris. Etiam ac rhoncus est. Nullam eu sapien sit amet ex fringilla vulputate in nec nulla. Morbi placerat nunc suscipit dolor blandit, id posuere sapien fringilla. Quisque sit amet tempus lacus, sit amet pharetra sem. In et ipsum eget purus posuere venenatis. Nam ante erat, rutrum eget magna quis, imperdiet cursus sapien. Fusce at massa tellus. Vivamus non orci ac est vestibulum volutpat. Donec ornare felis eu nisi iaculis, vitae sagittis neque interdum. Maecenas non est nec leo sagittis laoreet. Integer posuere interdum consequat. Maecenas congue, nunc sed pellentesque lobortis, felis libero vestibulum risus, in dignissim sapien justo quis mauris.
Suspendisse ultrices, nibh nec viverra faucibus, quam lectus faucibus risus, et auctor odio urna ac nibh. Integer ac pretium lorem. Phasellus porta sodales tincidunt. Pellentesque ut tellus urna. Nullam eget nunc pellentesque, eleifend orci ut, venenatis nisi. Aenean a libero convallis, tempus libero id, mollis diam. Integer velit justo, iaculis ut sem sit amet, egestas consectetur libero. Donec porta sollicitudin tortor, vel vulputate urna rutrum a. Morbi id tempus orci. In maximus elit vitae eleifend consequat.
Nullam pharetra, ex a laoreet malesuada, arcu nibh consequat enim, in auctor enim tellus non ligula. Aliquam iaculis ex at libero egestas, pretium ultricies ipsum molestie. Aenean et eros nec libero pretium convallis eu vitae nisi. Suspendisse at risus mauris. Praesent venenatis massa a leo fermentum, non lobortis odio elementum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse quis risus arcu. Duis malesuada massa sed luctus ullamcorper. Morbi efficitur viverra leo, vel congue nisl aliquam eget. Nulla facilisi. Donec sagittis enim eget lorem dapibus, et efficitur erat facilisis. Donec iaculis, eros eu sollicitudin tempus, eros mauris facilisis dolor, eu fringilla augue dolor vitae elit. Praesent lobortis, elit id rutrum facilisis, erat erat sollicitudin mi, sed fringilla ligula turpis eu odio. Vestibulum vel erat sodales, bibendum augue a, placerat nisl. Ut non sagittis eros. Cras sed justo vel nisi sollicitudin auctor et quis neque.
Morbi tincidunt luctus diam, a cursus velit hendrerit ac. Donec posuere erat enim, lacinia fermentum tortor viverra eget. Nam sit amet eros quis leo auctor imperdiet ut vitae erat. Proin tortor tellus, luctus id cursus pulvinar, convallis id eros. Aliquam erat volutpat. In tempus nibh turpis. Sed vehicula sit amet dolor in mattis. Duis in nisl nulla. Suspendisse quis pellentesque purus. Nunc viverra augue eu malesuada eleifend. Donec massa nisl, malesuada ut metus nec, mattis dapibus nulla. Vestibulum fringilla congue orci, nec accumsan ligula porttitor quis. Curabitur rutrum massa sit amet quam gravida, vel consectetur lectus venenatis. "
"""

print Encrypt(plaintext, KEY)
