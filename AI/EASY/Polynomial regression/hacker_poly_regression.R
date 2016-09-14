# https://www.hackerrank.com/challenges/predicting-office-space-price

conn <- file("input.txt", "r", blocking = FALSE)
input<- readLines(conn)

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

close(conn)


colnames(data.train) = c("f1", "f2", "y")
colnames(data.test) = c("f1", "f2")

data.train <- sapply(data.train, as.numeric)
data.test <- sapply(data.test, as.numeric)

data.train <- as.data.frame(data.train)
data.test <- as.data.frame(data.test)

printOP <- function(pred){
  op = character()
  for (i in 1:length(pred)){
    op = paste(op, as.character(unname(pred[i])), "\n", sep = "")
  }
  
  cat(op)
}

analyzeModel<- function(model){
  
  print(summary(model))
  
  #Plot of fitted vs residuals. No clear pattern should show in the residual plot if the model is a good fit
  plot(fitted(model),residuals(model))
}


# Linear regression : 0.9380093812942505 score | test case 1 n 2 failed
fit.1 <- lm(y ~ ., data = data.train)
analyzeModel(fit.1)

pred.1 = predict(fit.1, newdata = data.test) 
printOP(pred.1)


# Quadratic : 1.0 score| 5.5 
fit.2 <- lm(y ~ f1 + f2 + I(f1^2)+I(f1*f2)+ I(f2^2), data = data.train)
analyzeModel(fit.2)

pred.2 = predict(fit.2, newdata = data.test) 
printOP(pred.2)


# Quadratic : 
fit.22 <- lm(y ~ polym(f1, f2, degree = 2, raw = TRUE), data = data.train)
analyzeModel(fit.22)

pred.22 = predict(fit.22, newdata = data.test) 
printOP(pred.22)


# Cubic http://www.statmethods.net/stats/regression.html : 1 score| 5.5
fit.3 <- lm(y ~ poly(f1, degree = 3) + poly(f2, degree = 3)+ poly(f1*f2, degree = 2), data = data.train)
analyzeModel(fit.3)

pred.3 = predict(fit.3, newdata = data.test) # 0.93 score
printOP(pred.3)


# Cubic
polym(x1, x2, degree=, raw=TRUE)
fit.33 <- lm(y ~ polym(f1, f2, degree = 3, raw = TRUE), data = data.train)
analyzeModel(fit.33)

pred.33 = predict(fit.33, newdata = data.test) # 0.93 score
printOP(pred.33)