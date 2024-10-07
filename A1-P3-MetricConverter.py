#Program 3 – Imperial to Metric Conversion
#Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Firstly we need to recieve inputs for tons, stone, pounds and ounces
    #Next we need to calculate the total ounces , total kilos and metric tons in that order
    #after these calculations we calculate our leftover kilos and finally leftover ounces and convert them to grams
    #finally we make a properly formatted print statement with our values

    tons = int(input("Enter the amount of tons: "))
    stones = int(input("Enter the amount of stones: "))
    pounds = int(input("Enter the amount of pounds: "))     
    ounces = int(input("Enter the amount of ounces: "))  #INPUTS ^^^^

    totalOunces = 35840 * tons + 224 * stones + 16 * pounds + ounces    #converting our inputs to ounces using the formula 
    totalKilos = totalOunces / 35.274 #converting our ounces to kilos
    metTonsTotal = int(totalKilos/1000) #our total metric tons
    kilosLeft =  int(totalKilos - (metTonsTotal * 1000))  #calculating the difference of our total metric tons and total kilos to get leftover kilos   
    gramsLeft =  28.3495231 * (totalOunces - ((metTonsTotal * 35274) + (kilosLeft * 35.274))) # converting our metric tons and leftover kilos to ounces and subtracting it from our total ounces before converting our leftover ounces to grams


    print("The metric weight is {0} metric tons, {1} kilos, and {2:.1f} grams".format(metTonsTotal,kilosLeft,gramsLeft))  #Formatted print statement with our calculations






    # YOUR CODE ENDS HERE

main()