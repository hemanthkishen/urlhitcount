# urlhitcount
This program reads the data from the text file and determines the URL Hit Count with respect to the date in epoch which is converted to MM/DD/YYYY GMT.

Big-O Analysis:-

sorted fuction is used. This describes an adaptive, stable, natural mergesort, modestly called
timsort.
Best Case:- O(n)
Average Case:- O(n log n)
Worst Case:- O(n log n)

for loop is used. There is a for loop in a for loop.
Best Case:- O(2n)
Average Case:- O(2n)
Worst Case:- O(2n)

Therefore, the final Big-O is:-
Best Case:- O(2n)
Average Case:- O(2n)
Worst Case:- O(2n)

input.txt:-

1407564301|www.nba.com
1407478021|www.facebook.com
1407478022|www.facebook.com
1407481200|news.ycombinator.com
1407478028|www.google.com
1407564301|sports.yahoo.com 
1407564300|www.cnn.com
1407564300|www.nba.com
1407564300|www.nba.com
1407564301|sports.yahoo.com
1407478022|www.google.com
1407648022|www.twitter.com

Output:-

08/08/2014 GMT
www.facebook.com 2
www.google.com 2
news.ycombinator.com 1


08/09/2014 GMT
www.nba.com 3
sports.yahoo.com 2
www.cnn.com 1


08/10/2014 GMT
www.twitter.com 1
