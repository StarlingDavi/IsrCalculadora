""# Programa para el cálculo del sueldo neto en República Dominicana
# Basado en los descuentos de Seguridad Social (TSS), Impuesto sobre la Renta (ISR) y Bonificación.


TSS_PERCENTAGE = 0.0304  
ISR_PERCENTAGE = 0.15    
BONIFICATION_PERCENTAGE = 0.10  


def calcular_sueldo_neto(sueldo_bruto, otros_descuentos=0):
    if sueldo_bruto <= 0:
        raise ValueError("El sueldo bruto debe ser mayor que cero.")
    if otros_descuentos < 0:
        raise ValueError("Los otros descuentos no pueden ser negativos.")
    
  
    descuento_tss = sueldo_bruto * TSS_PERCENTAGE
    retencion_isr = sueldo_bruto * ISR_PERCENTAGE
    
  
    bonificacion = sueldo_bruto * BONIFICATION_PERCENTAGE
    
 
    sueldo_neto = sueldo_bruto - descuento_tss - retencion_isr - otros_descuentos + bonificacion
    
   
    print("----- Detalle del Cálculo -----")
    print(f"Sueldo Bruto: RD${sueldo_bruto:.2f}")
    print(f"Descuento por Seguridad Social (TSS): RD${descuento_tss:.2f}")
    print(f"Retención ISR: RD${retencion_isr:.2f}")
    print(f"Otros Descuentos: RD${otros_descuentos:.2f}")
    print(f"Bonificación: RD${bonificacion:.2f}")
    print(f"Sueldo Neto: RD${sueldo_neto:.2f}")


try:
    sueldo_bruto = float(input("Ingrese el sueldo bruto (RD$): "))
    otros_descuentos = float(input("Ingrese otros descuentos (RD$): "))
    calcular_sueldo_neto(sueldo_bruto, otros_descuentos)
except ValueError as e:
    print(f"Error: {e}")
""
