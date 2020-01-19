try:
    # raise Exception("some error occurred")
    print("123")
except Exception:
    print("woops")
else:
    print("This prints when there is no error.")
finally:
   print("Still print this out...")

