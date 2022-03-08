def pay_computation (hr,rate):
    if hr <= 40:
        pay = hr * rate
        print ('your pay is:',pay,"\n")
    else:
        pay = 40 * rate + (hr-40)*10*1.5 #subtracting the overtime from the set time(40) then multiply by the rate and the 1.5 incentive

        print ("your pay is:",pay,"\n")



pay_computation (45,10)