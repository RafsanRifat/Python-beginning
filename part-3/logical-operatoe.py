# In python there are 3 logical operator---->>  and, or, not

high_income = False
good_credit = True
student = False

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

# ###########################################################################

if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

# ###########################################################################
if not student:
    print("Eligible")
else:
    print("Not eligible")

# ###########################################################################
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("not eligible")

# ###########################################################################
message = "Eligible" if (high_income and good_credit) or not student else "NOT eligible"

print(message)