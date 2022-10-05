#Plant          Regular Price   Sales Price
#Swedish Ivy    $2.25
#Boston Fern    $3.22
#Poinsetta      $6.82
#Cactus         $4.67
print("{0:<15s}{1:<15s}{2:<15s}".format("Plant", "Regular Price", "Sales Price"))
print("{0:<15s}{1:<15s}{2:<1s}{3:<15f}".format("Swedish Ivy", "$2.25", "$", -2.25*.20+2.25))
print("{0:<15s}{1:<15s}{2:<1s}{3:<15f}".format("Boston Fern", "$3.22", "$",-3.22*.20+3.22))
print("{0:<15s}{1:<15s}{2:<1s}{3:<15f}".format("Poinsettia", "$6.82", "$", -6.82*.20+6.82))
print("{0:<15s}{1:<15s}{2:<1s}{3:<15f}".format("Cactus", "$4.67", "$", -4.67*.20+4.67))