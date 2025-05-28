set title "Desempenho do Selection Sort"
set xlabel "Tamanho da Entrada (N)"
set ylabel "Tempo Médio de Execução (nanossegundos)"

set terminal pngcairo size 800,600 enhanced font "Verdana,10"
set output 'selection_sort_performance.png'

set grid
set key top left # Posição da legenda

plot 'selection_desempenho.txt' using 1:2 with linespoints title 'Selection Sort'
