def check_pos_neg_zero(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    return "Zero"

if __name__ == "__main__":
    print(check_pos_neg_zero(5))
    print(check_pos_neg_zero(-3))
    print(check_pos_neg_zero(0))
