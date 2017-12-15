# Set the workspace 
getwd()
#setwd("C:/Users/1695977/Documents/Lab-1")
# helper
?logLik
help.search('log')
#data()

# Examples for manipulation

a <- 10
b <- 20
c <- a + b
ls()

d <- c (10,12,11,20)
e <- c + d

a <- "23"
b <- as.numeric(a) # casting


# variable type
print(class(c))
typeof(a)

#logyc type
a <- logical(1)
a <- T

# clean up memory
rm (euro)

###################################################################

# vector

a <- c(1,3,5,568,0,11)
a[4]
a[-4]
a[2:5]
a[4] <- 2+a[1]
a
a[c(1,4)]


b <- 10:20
b

# Sequence 

v <- seq( from = 12, to=2 , by = -0.3) 
v
y <-  rep(1:3, time=4,each=5)
y


# divide array

x <- 1:4
x / c(2,2)
length(x)


