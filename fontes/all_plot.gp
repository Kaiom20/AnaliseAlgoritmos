set title "Comparação de Todos os Casos Médios"
set xlabel "Tamanho da Entrada (N)"
set ylabel "Tempo Médio de Execução (nanossegundos)"

set terminal pngcairo size 800,600 enhanced font "Verdana,10"
set output 'all_sort_performance.png'

set grid
set key top left # Posição da legenda

plot \
    'insertionM_desempenho.txt' using 1:2 with linespoints title 'Insertion Sort' dashtype 1 linewidth 2 pointtype 7 pointsize 1.0, \
    'distribution_desempenho.txt' using 1:2 with linespoints title 'Distribution Sort' dashtype 2 linewidth 2 pointtype 6 pointsize 1.0, \
    'merge_desempenho.txt' using 1:2 with linespoints title 'Merge Sort' dashtype 3 linewidth 2 pointtype 5 pointsize 1.0, \
    'quickM_desempenho.txt' using 1:2 with linespoints title 'Quick Sort' dashtype 4 linewidth 2 pointtype 4 pointsize 1.0, \
    'selection_desempenho.txt' using 1:2 with linespoints title 'Selection Sort' dashtype 5 linewidth 2 pointtype 3 pointsize 1.0