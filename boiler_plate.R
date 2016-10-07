# Read data from command line arguments
input <- readLines(file("stdin"))

for (i in 1:length(input)){
  # Read the first line to get no of features and training observations
  if (i == 1){
    l =  unlist(strsplit(input[i], " "))    
    train.F = as.numeric(l[1])
    train.N = as.numeric(l[2])
    # Create a dataframe of size train.N * (train.F + 1)
    data.train <- data.frame(matrix(NA, nrow = train.N, ncol = (train.F+1)))
  }
  # Extract training data
  if (i <= train.N + 1){
    l = unlist(strsplit(input[i], " "))
    for (j in 1:length(l)){
      data.train[i-1, j] = l[j]
    }
  }
  # Read the test data dimensions
  if (i == train.N+2){
    test.N =  as.numeric(unlist(strsplit(input[i], " ")))   
    test.F = train.F
    # Create a dataframe of size N * (F + 1)
    data.test <- data.frame(matrix(NA, nrow = test.N, ncol = (test.F)))
  }
  # Read the test data
  if (i > train.N + 2){
    l = unlist(strsplit(input[i], " "))
    for (j in 1:length(l)){
      data.test[i - train.N - 2, j] = l[j]
    }
  }
}

data.train <- as.data.frame(data.train)
data.test <- as.data.frame(data.test)

# fit <- lm(y ~ ., data = data.train)


# PRINT TO STDR
pred = predict(fit, newdata = data.test)
op = character()
for (i in 1:length(pred)){
  op = paste(op, as.character(unname(pred[i])), "\n", sep = "")
}

cat(op)

