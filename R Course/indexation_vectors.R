# Init vector
v <- 1:100

####################################
# Indexement with positive numbers #
####################################

v[1] # The first element
v[c(1,1,3,4,5)] # Select two times the first, third, four, five element index
v[20:30] # Get elements between 20 and 30
v[70:100] <- 0 # Set 0 at elements between 70 and 100
v[which(v == 30)] # Select the indexes of elements > 30


####################################
# Indexement with negative numbers #
####################################

v[-1] # Select all elements excluding the first element
v[-c(1,2,3)] # Select all elements excluding the first, second and third element
v[-length(v)] # All elements excluding the last element


########################################
# Indexement with booleans expressions #
########################################
v0 <- v[1:5]
v0[c(TRUE,FALSE,TRUE,FALSE)] # Select the first and third element
v[v>30] # All > 30
v[v>20 & v<=50] # All > 20 and <= 50
v[v==0] # All ceros
v[v %in% c(10,20,30)] # Select the 10, 20 and 30


#######################
# Indexement by names #
#######################

names(v0) <- c("alpha", "beta", "gamma", "delta", "omega")
v0["alpha"]
v0["beta"] <- 500
v0[c("delta", "omega")]
print("aasdasdasad")
v0[names(v0) %in% c("alpha", "beta")] # exactly this elements
v0[!(names(v0) %in% c("alpha", "beta"))] # diferents of this elements
