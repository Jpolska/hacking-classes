from hashlib import sha256


def get_f(SIZE=4):
    def f(x):
        """ Concantinate string 'Hacking classes' with x then hash it and return
            SIZE first characters of it
        """
        return sha256("tHacking classes" + x).hexdigest()[:SIZE]
    return f
