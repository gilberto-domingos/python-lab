'Implementar um script em linguagem R baseado no conjunto de dados USArrests, que deve calcular as
médias das prisões por assaltos, assassinatos e estupros para as 5 maiores e as 5 menores populações urbanas.
Utilizar o conhecimento adquirido até o momento. Por exemplo, evitar funções de filtro e média.
Identificar manualmente a quantidade de registros ou observações do conjunto de dados e realizar os demais cálculos
via script.'

# Carregar o conjunto de dados USArrests
data(USArrests)

# Inspecionar o conjunto de dados
head(USArrests)
str(USArrests)

# Ordenar os dados pela coluna UrbanPop (População Urbana)
sorted_data <- USArrests[order(USArrests$UrbanPop),]

# Verificar as 5 menores populações urbanas
lowest_urban_pop <- sorted_data[1:5,]
lowest_urban_pop

# Verificar as 5 maiores populações urbanas
highest_urban_pop <- sorted_data[(nrow(sorted_data)-4):nrow(sorted_data),]
highest_urban_pop

# Calcular as médias para as 5 menores populações urbanas
mean_lowest_assault <- mean(lowest_urban_pop$Assault)
mean_lowest_murder <- mean(lowest_urban_pop$Murder)
mean_lowest_rape <- mean(lowest_urban_pop$Rape)

# Calcular as médias para as 5 maiores populações urbanas
mean_highest_assault <- mean(highest_urban_pop$Assault)
mean_highest_murder <- mean(highest_urban_pop$Murder)
mean_highest_rape <- mean(highest_urban_pop$Rape)

# Exibir os resultados
cat("Médias para as 5 menores populações urbanas:\n")
cat("Assaltos:", mean_lowest_assault, "\n")
cat("Assassinatos:", mean_lowest_murder, "\n")
cat("Estupros:", mean_lowest_rape, "\n\n")

cat("Médias para as 5 maiores populações urbanas:\n")
cat("Assaltos:", mean_highest_assault, "\n")
cat("Assassinatos:", mean_highest_murder, "\n")
cat("Estupros:", mean_highest_rape, "\n")
