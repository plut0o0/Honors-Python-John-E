1.

length = 4
width = 13
print ("The perimeter of the rectangle is",length+lenght+width+width.".")

2.

def main():
    s1=12.2
    s2=10.6
    s3=7.8
    print ("The total length os the race is",s1+s2+s3,"km.")
main()

3.

def main():
    price,num = eval(input("Enter the price of bread and the amount of loaves bought seperated by a comma: "))
    print ("The total rice of your bread is $", price*num,".")
main()

4.

def main():
    num = eval(input("Enter a two digit number: "))
    d1 = num//10
    d2 = num%10
    print ("The first digit is", d1,"and the second digit is", d2,".")
main()

5.

def main():
    g1,g2,g3,g4,g5 = eval(input("Enter your five grades eperated by a comma: "))
    print ("The average of your grades are:",(g1+g2+g3+g4+g5)/5,".")
main()

6.

def main():
    weight,height = eval(input("Enter your eight and your height seperated by comma: "))
    final = weight/height
    print ("You weigh {:.3f}".format(final),"pounds per inch.")
main()

7.

def main():
    n1,n2,n3 = eval(input("Enter three numbers with seperated by a comma: "))
    sum = n1+n2+n3
    prod = n1*n2*n3
    print ("The sum of your numbers is", sum,"and the product is", prod,".")
main()

8.



9.

def main():
    rad = eval(input("Enter the radius of your circle to find the circumference: "))
    circ = 2*3.14*rad
    print ("The circumference of your circle is {:.2f}".format(circ),".")
main()

10.

def main():
    num = eval(input("Enter a three-digit number: "))
    print ("The hundreds place of your number is", num//100,", the tens place is",(num%100)//10,", and the ones place is", str((num%100)%10) + ".")
main()

11.

def main():
    pizza = eval(input("How many slices of pizza did you eat today? "))
    print ("You must run", (pizza*375)/100,"miles.")
main()

12.

def main():
    n1,n2 = eval(input("Enter two numbers seperated by a comma: "))
    fin = n1*n2
    print ("x =",n1,"  |\ty =",n2,"  |\tx*y =",fin)
main()

13.

def main():
    n1,n2 = eval(input("Enter two numbers eperated by a comma: "))
    print (n1,"+",n2,"=",n1-n2,"  |\t",n1,"-",n2,"=",n1-n2,"  |\t",n1,"*",n2,"=",n1*n2,"  |\t",n1,"/",n2,"=",n1/n2,"  |\t",n1,"//",n2,"=",n1//n2,"  |\t",n1,"%",n2,"=",n1%n2)
main()

14.

def main():
    wage, hours = eval(input("Enter your wage and your hours worked seperated by a comma: "))
    print ("Your pay is $",wage*hours)
main()

15.

def main():
    change = eval(input("Enter the change you have in cents: "))
    quarters = change//25
    dimes = (change%25)//10
    nickles = ((change%25)%10)//5
    pennies = (((change%25)%10)%5)//1
    print (" Quarters: ",quarters,"\n Dimes: ",dimes,"\n Nickles: ",nickles,"\n Pennies: ",pennies)
main()

16.

def main():
    length,width,height = eval(input("Enter the length, width, and height seperated by a comma: "))
    print ("THe volume is", length*width*height)
main()

17.

def main():
    minutes = eval(input("Enter the time in minutes: "))
    print ("The time is " + str(minutes//60) + ":" + str((minutes/60)//10) + str(((minutes/60)%10)//1))
main()

18.

def main():
    brgs,fries,soda = eval(input("Enter the amount of fburgers, fries, and sodas that were bought. Seperate them by a comma: "))
    bt = (brgs*1.69)+(fries*1.09)+(soda*.99)
    tax = (bt*.06)
    ft = bt+tax
    print ("Total before tax: ${:.2f}" .format(bt))
    print ("Tax: ${:.2f}" .format(tax))
    print ("Final total: ${:.2f}" .format(ft))
main()

19.

def main():
    clothing,food,ent = eval(input("Enter how much you spend a month on clothing, food, and entertainment. Separate each number by a comma: "))
    budg = clothing+food+ent
    pc = (clothing/budg)*100
    pf = (food/budg)*100
    pe = (ent/budg)*100
    print ("The percentages for each of these in your monthly spending is: clothing = {:.2f}".format(pc),"food = {:.2f}".format(pf),"entertainment = {:.2f}".format(pe))
main()

20.

def main():
    local,lng = eval(input("Enter the amount of local calls and long calls seperated by a comma: "))
    total = (local*.12)*(lng*1.25)+5.83
    print ("Your bioll total is $" + str(total))
main()