getwd()

class(iris)

iristest = iris
save(iristest, file = "iristeste.Rdata")
rm(iristest)
iristest

load(file = "iristeste.Rdata")
iristest

#Estudo sobre estrutura de dados no R

#Vetores

X <- c(1,2,3,4,5,6)
X
X[1]

X[1] <- 10
X

#outros tipos de vetores
Y <- c("a","b","c","d")
Y

#matrizes
VADeaths
colnames(VADeaths)
rownames(VADeaths)
#ver só a coluna 1
VADeaths[,1]
#ver só a linha 1
VADeaths[1,]
#Ver linhas de 1 a 3
VADeaths[1:3,]

#Dataframes
longley


#listas
ability.cov

ability.covicov[,1:3]

#ajuda no R
help("class")



a = 10
b = 20

if (a > 10)
{
  print("a é maior")
}else
{
  print("a não é maior")
}

x = ifelse(a > 10,"a é maior","a não é maior")
x

for (i in 1:10) {
  print(i)
 }

a = 1
while(a <= 10)
{
  print(a)
  a = a+1
}








