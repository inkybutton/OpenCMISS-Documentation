#set title "Legendre Polynomials"
set nokey
set xlabel "$\xi$"
set xlabel "$\fnof{P_{n}}{\xi}$"
set xtics  -1.0,0.25,1.0
set ytics -1.0,0.25,1.0
P0(x)=1
P1(x)=x
P2(x)=(1.0/2.0)*(3.0*x*x-1.0)
P3(x)=(1.0/2.0)*(5.0*x*x*x-3.0*x)
P4(x)=(1.0/8.0)*(35.0*x*x*x*x-30.0*x*x+3.0)
P5(x)=(1.0/8.0)*(63.0*x*x*x*x*x-70.0*x*x*x+15.0*x)
P6(x)=(1.0/16.0)*(231.0*x*x*x*x*x*x-315.0*x*x*x*x+105.0*x*x-5.0)
P7(x)=(1.0/16.0)*(429.0*x*x*x*x*x*x*x-693.0*x*x*x*x*x+315.0*x*x*x-35.0*x)
P8(x)=(1.0/128.0)*(6435.0*x*x*x*x*x*x*x*x-12012.0*x*x*x*x*x*x+6930.0*x*x*x*x-1260.0*x*x+35.0)
P9(x)=(1.0/128.0)*(12155.0*x*x*x*x*x*x*x*x*x-25740.0*x*x*x*x*x*x*x+18018.0*x*x*x*x*x-4620.0*x*x*x+315.0*x)
P10(x)=(1.0/256.0)*(46189.0*x*x*x*x*x*x*x*x*x*x-109395.0*x*x*x*x*x*x*x*x+90090.0*x*x*x*x*x*x-30030.0*x*x*x*x+3465.0*x*x-63.0)
plot[-1.0:1.0] P0(x),P1(x),P2(x),P3(x),P4(x),P5(x),P6(x),P7(x),P8(x),P9(x),P10(x)
