#############################
# Automathic type coertions #
#############################
x <- c(5, 'a') # Convert 5 to "5"
x
c <- 1:3
c
x[3] <- 'a' # Convert a "1", "2" y "a"
x
typeof(1:2) == typeof(c(1,2))

#############################################################
# Booleans operations "vectorizateds and not vectorizateds" #
#############################################################
c(T,F,T) && c(T,F,F) # True !Vectorizated
c(T,F,T) & c(T,F,F) # TRUE, FALSE, FALSE
