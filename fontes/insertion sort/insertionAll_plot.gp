set title "Comparação do Insertion Sort - Melhor Caso, Caso Médio e Pior Caso"
set xlabel "Tamanho da Entrada (N)"
set ylabel "Tempo Médio de Execução (nanossegundos)"

set terminal pngcairo size 800,600 enhanced font "Verdana,10"
set output 'insertion_sortAll_performance.png'

set grid
set key top left # Posição da legenda

plot 'insertionB_desempenho.txt' using 1:2 with linespoints title 'Melhor Caso' linecolor rgb "green" pointtype 7, \
     'insertionM_desempenho.txt' using 1:2 with linespoints title 'Caso Médio' linecolor rgb "blue" pointtype 6, \
     'insertionW_desempenho.txt' using 1:2 with linespoints title 'Pior Caso' linecolor rgb "red" pointtype 5

