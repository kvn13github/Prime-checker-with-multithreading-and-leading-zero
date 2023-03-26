# Prime-checker-with-multithreading-and-leading-zero
I started with the Python code, then added multithreading in V2, then translated it to Java and C++(11), the C code I have also compiled to a Linux binary.

Check the output examples on how to use it in a terminal.

So the code first asks how many digits, then prints the highest prime, then the lower primes, with a leading zero (imagine a bike lock with numbers)
then checks these for Sophie Germain and safe primes.

With the added multithreading it is capable of generating output very fast even for prime numbers several digits long.
Or so I thought...

time tests:
./primesV2 2>&1  19,73s user 0,43s system 83% cpu 24,214 total vs ( python primesV2.py; ) 2>&1  32,90s user 0,10s system 91% cpu 36,132 total vs 
( java primesV2.java; ) 2>&1  12,26s user 0,47s system 173% cpu 7,324 total SO it seems the java code is most efficient, even faster than the compiled c++ file and Python is the worst         

Tryng to optimize the java code, the language I know least for better multithreading using more cores, I have 16, and using a more efficient prime checking algorithm, such as the Sieve of Eratosthenes or the Miller-Rabin primality test. 

But chatgtp keeps giving me broken code, so this may take a while.


Created with the use of ChatGTP.
