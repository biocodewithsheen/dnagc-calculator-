dna=input("Enter a DNA sequence :")

# Calculating length of input DNA sequence 
length=length(dna)
print("The length of DNA sequence is: ",length)

#Converting to upper case
dna=dna.upper()
print(dna)

#Counting A,T,G,C and N
a=dna.count("A")
t=dna.count("T")
g=dna.count("G")
c=dna.count("C")
n=dna.count("N")

#Printing the results
print(
      "Length=", length,"\n",
       "A=",a,"\n",
       "T=",t,"\n",
       "G=",g,"\n",
       "C=",c,"\n",
       "N=",n,"\n" )

# Calculating G+C % in the sequence 
gc=((g+c)/length)*100
print("GC content :",gc,"%")

#Calculating melting temperature of the oligo
tm=(4*(g+c)+2*(a+t))
print("The melting temperature of the given oligo is:",tm)

#Finds the first occurence of AUG from 5'end
start=dna.find("AUG")
print("The first occurence of AUG from 5'end is",start+1)



        
       
       
       
