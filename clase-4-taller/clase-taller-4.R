# Clase 4: ejecutar desde clase-4-taller/ o con kernel R en Colab.

if (file.exists("datos/wage2.csv")) {
  original <- read.csv("datos/wage2.csv")
} else {
  if (!requireNamespace("wooldridge", quietly = TRUE)) {
    install.packages("wooldridge", repos = "https://cloud.r-project.org/")
  }
  original <- as.data.frame(wooldridge::wage2)
}
variables <- c("wage", "educ", "IQ")
print(colSums(is.na(original[variables])))
datos <- original[complete.cases(original[variables]), variables]
print(c(filas_originales = nrow(original), filas_usadas = nrow(datos)))
str(datos)
summary(datos)
head(datos)

simple <- lm(wage ~ educ, data = datos)
multiple <- lm(wage ~ educ + IQ, data = datos)
print(coef(simple))
print(coef(multiple))
comparacion <- data.frame(
  modelo = c("Simple", "Con IQ"),
  pendiente_educ = c(coef(simple)["educ"], coef(multiple)["educ"])
)
print(comparacion)
plot(wage ~ educ, data = datos, pch = 19, col = "#005F9640")
abline(simple, col = "#D6A600", lwd = 3)

nuevos <- data.frame(educ = c(12, 13), IQ = c(100, 100))
predicciones <- predict(multiple, newdata = nuevos)
print(data.frame(nuevos, salario_predicho = predicciones))
print(diff(predicciones))
print(coef(multiple)["educ"])
rejilla <- data.frame(educ = seq(9, 18, length.out = 50), IQ = 100)
plot(rejilla$educ, predict(multiple, newdata = rejilla), type = "l",
     col = "#005F96", lwd = 3, xlab = "Educación (años)",
     ylab = "Salario mensual predicho (USD)")

ejemplo <- data.frame(
  persona = c("Juan", "Pedro", "Sofía", "Caro", "Alex"),
  experiencia = c(12, 18, 14, 12, 11),
  educacion = c(93, 119, 108, 96, 74),
  salario = c(769, 808, 825, 650, 562)
)
modelo5 <- lm(salario ~ experiencia + educacion, data = ejemplo)
print(coef(modelo5))
print(data.frame(ejemplo, ajustado = fitted(modelo5), residuo = resid(modelo5)))
print(sum(resid(modelo5)^2))

X <- model.matrix(modelo5)
y <- ejemplo$salario
print(X)
print(y)
print(dim(X))
print(length(y))
print(colnames(X))
X_manual <- cbind(unos = 1, ejemplo$experiencia, ejemplo$educacion)
print(all.equal(unname(X), unname(X_manual)))

XtX <- t(X) %*% X
Xty <- t(X) %*% y
print(XtX)
print(Xty)
print(dim(XtX))
print(sum(X[, 2] * X[, 3]))
print(XtX[2, 3])
print(head(X * X))

beta_formula <- solve(XtX) %*% Xty
beta_sistema <- solve(XtX, Xty)
print(beta_formula)
print(beta_sistema)
print(coef(modelo5))
print(isTRUE(all.equal(as.numeric(beta_sistema), unname(coef(modelo5)))))
y_ajustado <- X %*% beta_sistema
print(cbind(observado = y, ajustado = y_ajustado))

u_hat <- y - as.numeric(y_ajustado)
print(round(t(X) %*% u_hat, 8))
print(c(media_y = mean(y), media_ajustada = mean(y_ajustado)))
medias <- data.frame(experiencia = mean(ejemplo$experiencia),
                     educacion = mean(ejemplo$educacion))
print(predict(modelo5, newdata = medias))
print(mean(y))

X_duplicada <- cbind(unos = 1, experiencia = ejemplo$experiencia,
                      repetida = ejemplo$experiencia)
print(c(columnas = ncol(X_duplicada), rango = qr(X_duplicada)$rank))
problema <- tryCatch(solve(t(X_duplicada) %*% X_duplicada),
                     error = function(e) conditionMessage(e))
print(problema)
ejemplo$repetida <- ejemplo$experiencia
print(coef(lm(salario ~ experiencia + repetida, data = ejemplo)))

medidas <- function(modelo) {
  s <- summary(modelo)
  c(n = nobs(modelo), R2 = s$r.squared,
    R2_ajustado = s$adj.r.squared, SSR = sum(resid(modelo)^2))
}
print(rbind(simple = medidas(simple), multiple = medidas(multiple)))
SSR <- sum(resid(multiple)^2)
SST <- sum((datos$wage - mean(datos$wage))^2)
SSE <- sum((fitted(multiple) - mean(datos$wage))^2)
n <- nobs(multiple)
k <- length(coef(multiple)) - 1
print(c(R2 = 1 - SSR/SST,
        R2_ajustado = 1 - (SSR/(n-k-1))/(SST/(n-1))))
print(c(SST = SST, SSE_mas_SSR = SSE + SSR))

set.seed(5)
n_sim <- 30
x_sim <- rnorm(n_sim)
y_sim <- 1 + 2*x_sim + rnorm(n_sim, sd = 2)
ruido <- matrix(rnorm(n_sim*10), nrow = n_sim, ncol = 10)
trayectoria <- data.frame(k_ruido = 0:10, R2 = NA, R2_ajustado = NA)
for (j in 0:10) {
  if (j == 0) {
    modelo_ruido <- lm(y_sim ~ x_sim)
  } else {
    z <- ruido[, seq_len(j), drop = FALSE]
    modelo_ruido <- lm(y_sim ~ x_sim + z)
  }
  s <- summary(modelo_ruido)
  trayectoria$R2[j+1] <- s$r.squared
  trayectoria$R2_ajustado[j+1] <- s$adj.r.squared
}
print(trayectoria)
matplot(trayectoria$k_ruido, trayectoria[, c("R2", "R2_ajustado")],
        type = "l", lty = 1, col = c("#005F96", "#D6A600"),
        xlab = "Variables de ruido añadidas", ylab = "Bondad de ajuste")
legend("bottomright", c("R²", "R² ajustado"), lty = 1,
       col = c("#005F96", "#D6A600"))

resumen5 <- summary(modelo5)
print(resumen5)
print(resumen5$coefficients)
print(anova(modelo5))
print(c(R2 = resumen5$r.squared, R2_ajustado = resumen5$adj.r.squared))
print(df.residual(modelo5))

fit <- lm(wage ~ educ + IQ, data = datos)
print(summary(fit))
print(anova(fit))
print(coef(fit))
print(predict(fit, newdata = data.frame(educ = 12, IQ = 100)))
X_real <- model.matrix(fit)
y_real <- model.response(model.frame(fit))
beta_real <- solve(t(X_real) %*% X_real, t(X_real) %*% y_real)
print(beta_real)
print(isTRUE(all.equal(as.numeric(beta_real), unname(coef(fit)))))
print(head(data.frame(observado = y_real, predicho = fitted(fit),
                      residuo = resid(fit))))

A <- t(X) %*% X
print(A)
i <- 1
j <- 2
menor <- A[-i, -j]
print(menor)
print(det(menor))
print((-1)^(i+j) * det(menor))

cofactores <- matrix(0, nrow = 3, ncol = 3)
for (i in 1:3) {
  for (j in 1:3) {
    cofactores[i, j] <- (-1)^(i+j) * det(A[-i, -j])
  }
}
adjunta <- t(cofactores)
determinante <- sum(A[1, ] * cofactores[1, ])
inversa <- adjunta / determinante
print(round(cofactores))
print(determinante)
print(round(inversa, 6))
print(isTRUE(all.equal(inversa, unname(solve(A)), check.attributes = FALSE)))
print(round(A %*% inversa, 8))

ejercicio <- data.frame(
  experiencia = c(12, 18, 14, 12, 11),
  educacion = c(93, 119, 108, 96, 74),
  salario = c(769, 808, 825, 650, 562)
)
fit_final <- lm(salario ~ experiencia + educacion, data = ejercicio)
X_final <- model.matrix(fit_final)
y_final <- ejercicio$salario
beta_final <- solve(t(X_final) %*% X_final, t(X_final) %*% y_final)
print(beta_final)
print(summary(fit_final))
print(anova(fit_final))
print(data.frame(ejercicio, ajustado = as.numeric(X_final %*% beta_final),
                 residuo = resid(fit_final)))
print(round(t(X_final) %*% resid(fit_final), 8))
