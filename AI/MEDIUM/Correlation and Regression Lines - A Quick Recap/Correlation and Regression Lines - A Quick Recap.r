x = cor(c(15,  12,  8,   8,  7,   7,   7,   6,   5,   3), c(10,  25,  17,  11,  13,  17,  20,  13,  9,   15))
res = format(round(x, 3), nsmall = 3)


physics_scores = c(15,  12,  8,   8,  7,   7,   7,   6,   5,   3)
history_scores = c(10,  25,  17,  11,  13,  17,  20,  13,  9,   15)
dF = data.frame(physics_scores, history_scores)

# http://stackoverflow.com/questions/3443687/formatting-decimal-places-in-r
printDecimal <- function(x, k) cat(format(round(x, k), nsmall=k))

cor.sp = cor(physics_scores, history_scores)
printDecimal(cor.sp, 3)


fit.lin  = lm(history_scores~physics_scores, data = dF)
coef = coef(fit.lin)[2]
printDecimal(coef, 3)

new <- data.frame(physics_scores = 10)
res = predict(fit.lin, newdata = new)
printDecimal(res, 1)
