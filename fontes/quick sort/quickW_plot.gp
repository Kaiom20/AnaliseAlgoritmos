set title "Desempenho do Quick Sort - Pior Caso"
set xlabel "Tamanho da Entrada (N)"
set ylabel "Tempo Médio de Execução (nanossegundos)"

set terminal pngcairo size 800,600 enhanced font "Verdana,10"
set output 'quick_sortW_performance.png'

set grid
set key top left # Posição da legenda

plot 'quickW_desempenho.txt' using 1:2 with linespoints title 'Quick Sort Pior Caso'
