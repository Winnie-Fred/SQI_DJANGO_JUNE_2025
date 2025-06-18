def states_and_their_capitals(**states_and_capitals):
    print(states_and_capitals)
    for state, capital in states_and_capitals.items():
        print(f"The capital of {state} is {capital}")



states_and_their_capitals(oyo="Ibadan", lagos="Ikeja", abia="Umuahia")
# data = {
#     "oyo": "Ibadan",
#     "Lagos": "Ikeja",
#     "Abia": "Umuahia"
# }
# states_and_their_capitals(**data)
