# 🧮 Calculadora de Rentabilidad para Mercado Libre
 
<div align="center">
  <img src="https://github.com/cristiandacontreras/Calculadora-margen-de-venta/blob/master/Screenshot_1.png" alt="Screenshot de la calculadora" width="500"/>
</div>
 
**Una herramienta de escritorio para vendedores de Mercado Libre que importan productos desde Shein.**  
Calculá el precio de venta ideal para cubrir todos tus costos y alcanzar el margen de ganancia que buscás.
 
[Ver Demo](#-demo) · [Instalación](#-instalación) · [Cómo Usar](#-cómo-usar) · [Contribuir](#-contribuir)
 
</div>
---
 
## 📋 Tabla de Contenidos
 
- [Descripción](#-descripción)
- [Demo](#-demo)
- [Funcionalidades](#-funcionalidades)
- [Tecnologías](#-tecnologías)
- [Instalación](#-instalación)
- [Cómo Usar](#-cómo-usar)
- [Fórmula de Cálculo](#-fórmula-de-cálculo)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)
---
 
## 📖 Descripción
 
Si vendés en **Mercado Libre** e importás productos desde plataformas como **Shein**, sabés lo difícil que es calcular un precio de venta que realmente te deje ganancia después de descontar:
 
- El costo del producto y su envío internacional
- La garantía de envío
- Los impuestos de tarjeta o aduana
- Tu parte del envío dentro de Mercado Libre
- La comisión que cobra Mercado Libre
Esta calculadora resuelve ese problema en segundos. Ingresás tus costos, definís tu margen esperado y obtenés el **precio de venta exacto** que necesitás publicar.
 
---
 
## 🎬 Demo
 
```
┌─────────────────────────────────────────────┐
│       Calculadora de Rentabilidad           │
├─────────────────────────────────────────────┤
│  COSTOS DE PRODUCTO                         │
│  Costo de Producto ($):        [29000     ] │
│  Envío de Producto ($):        [40000     ] │
│  Garantía de envío ($):        [1592      ] │
│  Impuestos Tarjeta/Aduana (%): [50        ] │
├─────────────────────────────────────────────┤
│  COSTOS Y VARIABLES DE VENTA (ML)           │
│  Tu parte del Envío ML ($):    [7470      ] │
│  Comisión Mercado Libre (%):   [15.5      ] │
│  Margen de Ganancia Esperado:  [30        ] │
├─────────────────────────────────────────────┤
│       [ Calcular Precio de Venta ]          │
├─────────────────────────────────────────────┤
│  Precio de Venta Ideal: $220,543.48         │
│  Tu Ganancia Limpia:    $66,163.04          │
│                                             │
│  --- Desglose ---                           │
│  Costo Total Producto (con 50% imp): ...    │
│  Costo Fijo (Producto + Envío ML):   ...    │
│  Lo que se cobra Mercado Libre:      ...    │
└─────────────────────────────────────────────┘
```
 
---
 
## ✨ Funcionalidades
 
- ✅ **Cálculo en tiempo real** del precio de venta ideal
- ✅ **Desglose detallado** de cada costo involucrado
- ✅ **Valores predeterminados** para empezar a calcular de inmediato
- ✅ **Validación de datos** con mensajes de error claros
- ✅ **Interfaz oscura** cómoda para uso prolongado
- ✅ **Liviana y sin dependencias pesadas** — solo Python y Flet
---
 
## 🛠 Tecnologías
 
| Tecnología | Versión | Uso |
|---|---|---|
| [Python](https://www.python.org/) | 3.8+ | Lenguaje base |
| [Flet](https://flet.dev/) | 1.0+ | Framework de UI de escritorio |
 
---
 
## 🚀 Instalación
 
### Prerequisitos
 
- Python 3.8 o superior instalado
- `pip` disponible en tu terminal
### Pasos
 
**1. Cloná el repositorio**
 
```bash
git clone https://github.com/tu-usuario/calculadora-rentabilidad-ml.git
cd calculadora-rentabilidad-ml
```
 
**2. (Recomendado) Creá un entorno virtual**
 
```bash
# En Windows
python -m venv venv
venv\Scripts\activate
 
# En macOS / Linux
python3 -m venv venv
source venv/bin/activate
```
 
**3. Instalá las dependencias**
 
```bash
pip install flet
```
 
**4. Ejecutá la aplicación**
 
```bash
python main.py
```
 
---
 
## 📌 Cómo Usar
 
### Sección 1: Costos de Producto
 
| Campo | Descripción | Ejemplo |
|---|---|---|
| **Costo de Producto ($)** | Precio que pagás en Shein por el artículo | `29.000` |
| **Envío de Producto ($)** | Costo del envío internacional desde Shein | `40.000` |
| **Garantía de envío ($)** | Seguro o garantía de entrega del paquete | `1.592` |
| **Impuestos Tarjeta/Aduana (%)** | Recargo por impuesto PAIS, aduana o tarjeta | `50` |
 
### Sección 2: Costos y Variables de Venta
 
| Campo | Descripción | Ejemplo |
|---|---|---|
| **Tu parte del Envío ML ($)** | Lo que vos absorbés del envío en ML | `7.470` |
| **Comisión Mercado Libre (%)** | Porcentaje que cobra ML sobre la venta | `15.5` |
| **Margen de Ganancia Esperado (%)** | La ganancia que querés obtener | `30` |
 
### Resultado
 
Hacé clic en **"Calcular Precio de Venta"** y obtendrás:
 
- 💙 **Precio de Venta Ideal**: el precio exacto a publicar en ML
- 🟠 **Tu Ganancia Limpia**: cuánto te queda en el bolsillo
- 📊 **Desglose**: detalle de cada componente del costo
> ⚠️ **Atención**: Si la suma de Comisión + Margen supera el 100%, la app te avisará del error.
 
---
 
## 🔢 Fórmula de Cálculo
 
La lógica detrás de la calculadora es la siguiente:
 
```
Costo Base Shein      = Costo Producto + Envío Shein + Garantía
Costo Total Shein     = Costo Base Shein × (1 + Impuestos%)
Costo Fijo Total      = Costo Total Shein + Envío ML
 
Divisor               = 1 - Comisión ML% - Margen%
 
Precio de Venta       = Costo Fijo Total / Divisor
Ganancia Neta         = Precio de Venta × Margen%
Comisión ML Total     = Precio de Venta × Comisión ML%
```
 
Este método garantiza que, al vender al precio calculado, tu margen quede intacto **después** de descontar comisiones y costos.
 
---
 
## 📁 Estructura del Proyecto
 
```
calculadora-rentabilidad-ml/
│
├── main.py          # Código principal de la aplicación
├── README.md        # Este archivo
└── requirements.txt # Dependencias del proyecto
```
 
### `requirements.txt`
 
```
flet>=1.0.0
```
 
---
 
## 🤝 Contribuir
 
¡Las contribuciones son bienvenidas! Si tenés ideas para mejorar la calculadora:
 
1. Hacé un **fork** del proyecto
2. Creá una rama con tu feature: `git checkout -b feature/nueva-funcionalidad`
3. Commiteá tus cambios: `git commit -m 'feat: agrego nueva funcionalidad'`
4. Pusheá la rama: `git push origin feature/nueva-funcionalidad`
5. Abrí un **Pull Request**
### Ideas para futuras mejoras
 
- [ ] Soporte para múltiples plataformas de marketplace (Tiendanube, etc.)
- [ ] Guardado de configuraciones frecuentes
- [ ] Exportación de resultados a CSV o PDF
- [ ] Historial de cálculos
- [ ] Modo claro / oscuro toggle
---
 
## 📄 Licencia
 
Este proyecto está bajo la Licencia MIT. Consultá el archivo [LICENSE](LICENSE) para más detalles.
 
---
 
<div align="center">
Hecho con 💜 para vendedores argentinos de Mercado Libre
 
⭐ Si te fue útil, ¡dejale una estrella al repo!
 
</div>
