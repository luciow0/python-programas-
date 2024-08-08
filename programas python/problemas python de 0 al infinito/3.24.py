ingresos = float(input("Ingrese su ingreso mensual "))
dependientes = int(input("Ingrese la cantidad de dependientes economicos que integran su familia "))

if ingresos <= 20000:
    retencion = 0
    print(f"su ingreso seguira siendo {ingresos} ya que se le aplicara una retencion de {retencion}")

if ingresos <= 40000:
    retencion = ingresos * 0.15
    print(f"su ingreso sera de {ingresos - retencion} ya que se le aplicara una retencion de {retencion}")

if ingresos <= 70000:
    retencion = ingresos * 0.25
    print(f"su ingreso sera de {ingresos - retencion} ya que se le aplicara una retencion de {retencion}")

if ingresos <= 100000:
    if dependientes < 4:
        retencion = ingresos * 0.30 - 0.02
    else:
        retencion = ingresos * 0.30
    print(f"su ingreso sera de {ingresos - retencion} ya que se le aplicara una retencion de {retencion}")

if ingresos > 100000:
    if dependientes < 4:
        retencion = ingresos * 0.35 - 0.02
    else:
        retencion = ingresos * 0.35
    print(f"su ingreso sera de {ingresos - retencion} ya que se le aplicara una retencion de {retencion}")