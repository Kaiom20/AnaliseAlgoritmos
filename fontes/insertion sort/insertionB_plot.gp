set title "Desempenho do Insertion Sort - Melhor Caso"
set xlabel "Tamanho da Entrada (N)"
set ylabel "Tempo Médio de Execução (nanossegundos)"

set terminal pngcairo size 800,600 enhanced font "Verdana,10"
set output 'insertion_sortB_performance.png'

set grid
set key top left # Posição da legenda

plot 'insertionB_desempenho.txt' using 1:2 with linespoints title 'Insertion Sort(Melhor caso)'
