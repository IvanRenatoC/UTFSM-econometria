# Clase 4: ejecutar desde clase-4-taller/ o con kernel R en Colab.

demo <- data.frame(y = c(4, 6, 7, 9, 8, 11),
                   x1 = c(1, 2, 3, 4, 2, 5),
                   x2 = c(2, 1, 3, 2, 4, 3))
modelo_demo <- lm(y ~ x1 + x2, data = demo, na.action = na.exclude)
print(coef(modelo_demo))
print(fitted(modelo_demo))

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

# a) Modelo simple
simple <- lm(wage ~ educ, data = datos)
# b) Modelo múltiple
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

iq_referencia <- 100
b <- coef(multiple)
abline(a = b["(Intercept)"] + b["IQ"] * iq_referencia,
       b = b["educ"], col = "#B93E42", lwd = 3, lty = 2)
legend("topleft", legend = c("a) Solo educación", "b) Educación + IQ (IQ = 100)"),
       col = c("#D6A600", "#B93E42"), lwd = 3, lty = c(1, 2), bty = "n")

modelo_vista <- lm(wage ~ educ + IQ, data = datos)
educ_vista <- c(12, 13)
iq_vista <- c(90, 100)
rejilla_vista <- expand.grid(educ = educ_vista, IQ = iq_vista)
pred_vista <- predict(modelo_vista, newdata = rejilla_vista)
print(data.frame(rejilla_vista, salario_predicho = pred_vista))

# Filas de educación y columnas de IQ
z_vista <- matrix(pred_vista, nrow = length(educ_vista),
                  ncol = length(iq_vista))
print(z_vista)
persp(educ_vista, iq_vista, z_vista, theta = 35, phi = 25,
      xlab = "Educación", ylab = "IQ", zlab = "Salario predicho",
      col = "lightblue", ticktype = "detailed")

anova_wage <- anova(multiple)
print(anova_wage)

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

# Cinco observaciones del ejemplo
ejemplo <- data.frame(
  persona = c("Juan", "Pedro", "Sofía", "Caro", "Alex"),
  experiencia = c(12, 18, 14, 12, 11),
  educacion = c(93, 119, 108, 96, 74),
  salario = c(769, 808, 825, 650, 562)
)
modelo5 <- lm(salario ~ experiencia + educacion, data = ejemplo)
print(coef(modelo5))
print(data.frame(ejemplo, prediccion = fitted(modelo5)))

# Matriz de diseño y respuesta
X <- model.matrix(modelo5)
y <- ejemplo$salario
print(X)
print(y)
print(dim(X))
print(length(y))
print(colnames(X))
X_manual <- cbind(unos = 1, ejemplo$experiencia, ejemplo$educacion)
print(identical(as.vector(X), as.vector(X_manual)))

XtX <- t(X) %*% X
Xty <- t(X) %*% y
print(XtX)
print(Xty)
print(dim(XtX))
print(sum(X[, 2] * X[, 3]))
print(XtX[2, 3])
print(head(X * X))

# Una muestra común para todos los análisis de este tema
datos_comunes <- original[complete.cases(original), ]
campos_modelo <- setdiff(names(datos_comunes), "lwage")
datos_modelo <- datos_comunes[, campos_modelo]

modelo_completo <- lm(wage ~ ., data = datos_modelo)
print(nobs(modelo_completo))
print(anova(modelo_completo))

resumen_completo <- summary(modelo_completo)
print(resumen_completo)
coeficientes <- resumen_completo$coefficients
alfa <- 0.05
p_valores <- coeficientes[, "Pr(>|t|)"]

detalle <- data.frame(
  termino = rownames(coeficientes),
  estimacion = coeficientes[, "Estimate"],
  error_estandar = coeficientes[, "Std. Error"],
  t = coeficientes[, "t value"],
  valor_p = p_valores,
  significativo = ifelse(p_valores < alfa, "Sí", "No")
)
print(detalle, row.names = FALSE)

r2_completo <- resumen_completo$r.squared
r2_ajustado_completo <- resumen_completo$adj.r.squared
print(c(R2 = r2_completo, R2_ajustado = r2_ajustado_completo))

pairs(datos_comunes, upper.panel = NULL, pch = 16, cex = 0.25,
      col = "#005F9640", main = "wage2 · Matriz de gráficos de dispersión")
correlaciones <- cor(datos_comunes)
indices <- which(upper.tri(correlaciones) & abs(correlaciones) >= 0.50,
                 arr.ind = TRUE)
pares <- data.frame(
  variable_1 = rownames(correlaciones)[indices[, 1]],
  variable_2 = colnames(correlaciones)[indices[, 2]],
  r = round(correlaciones[indices], 3)
)
print(pares, row.names = FALSE)

significativas <- rownames(coeficientes)[p_valores < alfa]
regresores <- setdiff(significativas, "(Intercept)")
print(c(r_educ_IQ = correlaciones["educ", "IQ"],
        p_educ = p_valores["educ"], p_IQ = p_valores["IQ"]))

# Entre educación e IQ, educación tiene el menor valor p
elegidas <- setdiff(regresores, "IQ")
datos_reducidos <- datos_modelo[, c("wage", elegidas)]
modelo_reducido <- lm(wage ~ ., data = datos_reducidos)
print(elegidas)
print(summary(modelo_reducido))

resumen_reducido <- summary(modelo_reducido)
r2_reducido <- resumen_reducido$r.squared
r2_ajustado_reducido <- resumen_reducido$adj.r.squared

comparacion_ajuste <- data.frame(
  modelo = c("Completo", "Reducido"),
  observaciones = c(nobs(modelo_completo), nobs(modelo_reducido)),
  regresores = c(length(coef(modelo_completo)), length(coef(modelo_reducido))) - 1,
  R2 = c(r2_completo, r2_reducido),
  R2_ajustado = c(r2_ajustado_completo, r2_ajustado_reducido)
)
print(comparacion_ajuste, row.names = FALSE)
