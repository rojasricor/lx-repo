# vectors of fixed length
v1 <- vector(mode="logical", length=4)
v1
v2 <- vector(mode="integer", length=5)
v2
numeric(4)
character(4)

# Using the sequency operator
v3 <- 1:5
v3
v4 <- 1.3:5.4
v4
v5 <- seq(from=0, to=1, by=0.1)
v5

# Using the combination function
v6 <- c(TRUE, FALSE)
v6
v7 <- c(1,2,3,5,6/3)
v7
v8 <- c("black", "white")
v8
v9 <- c(v1,v3)
v9

# Vector with names
v10 <- c(a=1, b=2, c=3, d=4)
v10['a']

# Operations between vectors
sum(v10, v7)
max(v10)
mean(v10)

v_total <- v3 + v4
v_total
