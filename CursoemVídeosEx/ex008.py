vm = float(input('Valor em metros:'))
print('Valor em centímetros: {}cm\nValor em milímetros: {}mm'.format(vm*100, vm*1000))


vm = float(input('Valor em metros:'))
print('Valor em centímetros: {:.1f}cm\nValor em milímetros: {:.1f}mm'.format(vm*100, vm*1000))

vm = float(input('Valor em metros:'))
vkm = vm / 1000
vhm = vm / 100
vdam = vm / 10
vdm = vm * 10
vcm = vm * 100
vmm = vm * 1000
print('O valor em km é {}km. \nO valor em hm é {}hm. \nO valor em dam é {}dam. \nO valor em dm é {}dm. \nO valor em cm é {}cm. \nO valor em mm é{}mm.'.format(vkm, vhm, vdam, vdm, vcm, vmm ))