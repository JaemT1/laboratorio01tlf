from matplotlib_venn import venn3
import matplotlib.pyplot as plt
import numpy as np

# Definir los conjuntos
A = {1, 2, 3, 4,5}
B = {3, 4, 5, 6,1}
C = {4, 5, 6, 7, 9}


#A = {1, 2, 3, 4, 5}
#B = {3, 4, 5, 6, 1}
#C = {4, 5, 6, 7,9}

# Graficar el diagrama de Venn (pasar una tupla en lugar de una lista)
venn = venn3((A, B, C), ('A', 'B', 'C'))

# Ajustar el texto para cada área de intersección
venn.get_label_by_id('100').set_text('\n'.join(map(str, A - B - C)))
venn.get_label_by_id('010').set_text('\n'.join(map(str, B - A - C)))
venn.get_label_by_id('001').set_text('\n'.join(map(str, C - A - B)))
venn.get_label_by_id('110').set_text('\n'.join(map(str, A & B - C)))
venn.get_label_by_id('101').set_text('\n'.join(map(str, A & C - B)))
venn.get_label_by_id('011').set_text('\n'.join(map(str, B & C - A)))
venn.get_label_by_id('111').set_text('\n'.join(map(str, A & B & C)))

plt.title("Diagrama de Venn")
plt.show()




from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3, venn3_circles
plt.figure(figsize=(4,4))
v = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels = ('A', 'B', 'C'))
v.get_patch_by_id('100').set_alpha(1.0)
v.get_patch_by_id('100').set_color('white')
v.get_label_by_id('100').set_text('Unknown')
v.get_label_by_id('A').set_text('Set "A"')
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), linestyle='dashed')
c[0].set_lw(1.0)
c[2].set_ls('dotted')
c[2].set_alpha(0.5)

plt.title("Sample Venn diagram")
plt.annotate('Unknown set', xy=v.get_label_by_id('100').get_position() - np.array([0, 0.05]), xytext=(-70,-70),
             ha='center', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='gray', alpha=0.1),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',color='gray'))
plt.show()