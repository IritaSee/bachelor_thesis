# Read values from tab-delimited autos.dat 
autos_data <- read.csv("result_AR100.csv")

# Graph autos with adjacent bars using rainbow colors
plot<-barplot(as.matrix(autos_data), main="Result: AR max 100", ylab= "Total",
        beside=TRUE, col=rainbow(5))

# Place the legend at the top-left corner with no frame  
# using rainbow colors
legend("topleft", c("10 Epochs","20 Epochs", "30 Epochs", "40 Epochs", "50 Epochs"), cex=0.6, 
       bty="n", fill=rainbow(5));
#text(plot, 0, autos_data,cex=0.3,pos=3) 
