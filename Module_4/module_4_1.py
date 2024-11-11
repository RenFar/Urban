import fake_math as fa
import true_math as ta

def fake_divide(first, second):
    print(fa.divide(first,second))

def true_divide(first, second):
    print(ta.divide(first, second))

fake_divide(69, 3)
fake_divide(3, 0)
true_divide(49, 7)
true_divide(15, 0)