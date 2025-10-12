# 📊 CLASE 9: INTRODUCCIÓN A POWER BI DESKTOP
## Analítica de Datos - Universidad Cooperativa de Colombia

**Modalidad:** Práctica guiada con ejercicios en clase

---

## 🎯 OBJETIVOS DE LA CLASE

Al final de esta sesión serás capaz de:
- ✅ Navegar la interfaz de Power BI Desktop
- ✅ Importar y transformar datos con Power Query
- ✅ Crear relaciones entre tablas
- ✅ Construir visualizaciones básicas e intermedias
- ✅ Crear medidas DAX fundamentales
- ✅ Implementar interactividad (filtros, drill-through, bookmarks)
- ✅ Diseñar un dashboard funcional

---

## 📋 ESTRUCTURA DE LA CLASE

| Actividad | Tipo |
|-----------|------|
| Instalación y configuración | Setup |
| Tour de interfaz | Demostración |
| Importar y transformar datos | Práctica guiada |
| Modelo de datos y relaciones | Práctica guiada |
| Visualizaciones básicas | Ejercicio 1 |
| Medidas DAX | Ejercicio 2 |
| Diseño profesional | Práctica guiada |
| Interactividad avanzada | Ejercicio 3 |
| Publicar y compartir | Demostración |

---

## 📥 PARTE 1: INSTALACIÓN Y SETUP

### Descarga Power BI Desktop

1. Ir a: https://powerbi.microsoft.com/es-es/desktop/
2. Click en "Descargar gratis"
3. Instalar (requiere Windows 10 u 11)
4. Abrir Power BI Desktop por primera vez

> **💡 Alternativa para Mac:** Usar Parallels, VMware Fusion, o acceder a máquina virtual en la nube

### Configuración Inicial

```
Archivo > Opciones y configuración > Opciones

Configurar:
- Regional > Español (Colombia)
- Vista previa de características > Activar todas
- Autoguardado > Cada 5 minutos
- Seguridad > Desactivar advertencias de privacidad (solo para práctica)
```

### Datasets para la Clase

**Fuente:** datos.gov.co

Vamos a trabajar con 2 datasets de políticas públicas colombianas:

#### Dataset 1: Ejecución del Presupuesto de Ingresos
- **Archivo:** `Ejecución_del_Presupuesto_de_Ingresos_20251012.csv`
- **Descripción:** Seguimiento mensual de ingresos presupuestales
- **Campos principales:**
  - VIGENCIA (año)
  - MES
  - RUBRO (código)
  - CONCEPTO (Ingresos Corrientes, Recursos de Capital)
  - PRESUPUESTO VIGENTE
  - RECAUDOS
  - RS/PV (porcentaje ejecución)

#### Dataset 2: Nacidos Vivos en Miranda, Cauca
- **Archivo:** `Nacidos_Vivos_por_Residencia,_en_el_Municipio_de_Miranda_Cauca_20251012.csv`
- **Descripción:** Registros de nacimientos en Miranda, Cauca 2024
- **Campos principales:**
  - Fecha Nacimiento
  - Sexo
  - Peso, Talla
  - Edad Madre, Edad Padre
  - Área Residencia
  - Régimen Seguridad Social
  - Tipo Parto
  - Número Consultas Prenatales

---

## 🗺️ PARTE 2: TOUR DE LA INTERFAZ

### Las 3 Vistas Principales

#### 📊 Vista de INFORME (Report View)
**Para qué:** Diseñar visualizaciones y dashboards

**Componentes:**
- **Lienzo de trabajo** (centro): Donde se colocan los gráficos
- **Panel de visualizaciones** (derecha): Tipos de gráficos disponibles
- **Panel de campos** (derecha abajo): Campos de las tablas
- **Panel de filtros** (derecha arriba): Filtros por visualización/página/informe

**Shortcut:** `Ctrl + Alt + 1`

---

#### 📋 Vista de DATOS (Data View)
**Para qué:** Ver tablas crudas y crear columnas calculadas

**Componentes:**
- Tabla completa visible (como Excel)
- Barra de fórmulas (arriba)
- Lista de tablas (izquierda)

**Shortcut:** `Ctrl + Alt + 2`

---

#### 🔗 Vista de MODELO (Model View)
**Para qué:** Crear relaciones entre tablas

**Componentes:**
- Diagrama entidad-relación
- Tablas con sus campos
- Líneas que muestran relaciones

**Shortcut:** `Ctrl + Alt + 3`

---

### Barra de Herramientas Superior

```
┌─────────────────────────────────────────────┐
│ Inicio:     Importar datos, publicar       │
│ Insertar:   Formas, imágenes, botones      │
│ Modelado:   Nueva medida, columna, tabla   │
│ Optimizar:  Rendimiento y diagnósticos     │
│ Ver:        Temas, reglas, cuadrícula      │
│ Ayuda:      Documentación y comunidad      │
└─────────────────────────────────────────────┘
```

---

## 📂 PARTE 3: IMPORTAR Y TRANSFORMAR DATOS

### 3.1 Importar Datos desde CSV

**Vamos a importar el primer dataset: Ejecución del Presupuesto**

**Paso a paso:**

```
1. Inicio > Obtener datos > Texto/CSV
2. Navegar a la carpeta clase9
3. Seleccionar: Ejecución_del_Presupuesto_de_Ingresos_20251012.csv
4. Vista previa automática de datos
5. ⚠️ IMPORTANTE: Click "Transformar datos" (NO "Cargar")
```

**¿Por qué "Transformar"?**
- Permite limpiar datos antes de cargarlos
- Abre Power Query Editor (la herramienta mágica)
- Este dataset tiene valores con comas en números que debemos limpiar

---

### 3.2 Power Query: Limpieza de Datos

**Se abre Power Query Editor** - Ventana separada

#### Exploración Inicial

```
✓ Observar columnas y tipos de datos
✓ Ver panel "Pasos aplicados" (derecha)
✓ Cada acción queda registrada y es reversible
✓ Buscar errores (banderas rojas) o valores nulos
```

---

#### Transformaciones Comunes

**1. Quitar columnas innecesarias**
```
- Click derecho en columna > Quitar
- O seleccionar varias columnas > Quitar columnas
```

**Criterio:** Eliminar columnas que no aportan al análisis

---

**2. Cambiar tipos de datos**
```
- Click en ícono ABC/123 del encabezado de columna
- Elegir: Texto, Número entero, Decimal, Fecha, etc.
```

**Común:**
- Códigos (ej: código DANE) → Texto
- Cantidades → Número entero
- Valores monetarios → Decimal
- Fechas → Fecha

---

**3. Renombrar columnas**
```
- Doble click en nombre de columna
- Usar nombres descriptivos sin espacios
```

**Ejemplos:**
- ❌ `Col1` → ✅ `departamento`
- ❌ `TOTAL EST` → ✅ `total_estudiantes`
- ❌ `Año` → ✅ `anio`

---

**4. Filtrar valores nulos o errores**
```
- Click en flecha desplegable del encabezado
- Desmarcar (null) o (error)
- O: Inicio > Quitar filas > Quitar errores
```

---

**5. Reemplazar valores**
```
- Click derecho en columna > Reemplazar valores
- Buscar: "N/A"
- Reemplazar por: (dejar vacío para null)
```

**Casos comunes:**
- "NA" → null
- "No aplica" → null
- Espacios extra → (trimming automático)

---

**6. Dividir columnas**
```
Si tienes: "Bogotá D.C. - Cundinamarca"

- Transformar > Dividir columna > Por delimitador
- Delimitador: " - "
- Resultado: 2 columnas separadas
```

---

**7. Agrupar datos (Group By)**
```
- Transformar > Agrupar por
- Similar a GROUP BY en SQL
```

**Ejemplo:**
```
Agrupar por: departamento
Nueva columna: total_estudiantes
Operación: Suma de estudiantes
```

---

### 🎓 EJERCICIO EN CLASE 1: Limpieza del Dataset de Presupuesto

**Con el dataset de Ejecución del Presupuesto:**

```
✅ Tareas a realizar:

1. Limpiar columnas numéricas:
   - PRESUPUESTO VIGENTE (PV): tiene comas, debe ser número
   - RECAUDOS (RS): tiene comas, debe ser número
   - Reemplazar comas (,) por vacío y cambiar tipo a Decimal

2. Cambiar tipos de datos:
   - VIGENCIA: cambiar a Texto (es un código, no número)
   - MES: cambiar a Número entero
   - RS/PV: cambiar a Texto (ya viene con %)

3. Renombrar columnas con nombres claros:
   - VIGENCIA → vigencia
   - MES → mes
   - CONCEPTO → tipo_ingreso
   - PRESUPUESTO VIGENTE (PV) → presupuesto_vigente
   - RECAUDOS (RS) → recaudos
   - RS/PV → porcentaje_ejecucion

4. Verificar el panel "Pasos aplicados"

🎯 Objetivo: Dataset limpio, sin errores, con tipos correctos
```

**Validación:**
- No debe haber errores visibles
- Todas las columnas numéricas suman correctamente
- Nombres de columnas son descriptivos sin espacios ni símbolos

---

### 3.3 Finalizar Transformación

```
Inicio > Cerrar y aplicar
```

**Qué sucede:**
- Cierra Power Query Editor
- Carga datos al modelo de Power BI
- Aparecen tablas en panel de campos

---

## 🔗 PARTE 4: MODELO DE DATOS Y RELACIONES (20 min)

### 4.1 ¿Por qué necesitamos relaciones?

**Escenario en nuestra clase:**

Ya tenemos el dataset de **Presupuesto** cargado. Ahora vamos a importar el segundo dataset de **Nacidos Vivos**.

**¿Cómo se relacionan?**
Por ahora, trabajaremos con cada dataset por separado para aprender visualizaciones. En un caso real, podríamos crear una tabla calendario para relacionarlos por fecha.

---

### 4.2 Importar Segunda Tabla

**Vamos a importar: Nacidos Vivos en Miranda, Cauca**

```
1. Inicio > Obtener datos > Texto/CSV
2. Seleccionar: Nacidos_Vivos_por_Residencia,_en_el_Municipio_de_Miranda_Cauca_20251012.csv
3. Click "Transformar datos"
```

**Transformaciones necesarias:**
```
1. Cambiar tipos de datos:
   - Fecha Nacimiento: tipo Fecha
   - Peso: tipo Número entero
   - Talla: tipo Número entero
   - Edad Madre: tipo Número entero (limpiar "SIN INFORMACIÓN")
   - Edad Padre: tipo Número entero (limpiar "SIN INFORMACIÓN")

2. Renombrar columnas principales:
   - Fecha Nacimiento → fecha_nacimiento
   - Sexo → sexo
   - Peso → peso_gramos
   - Talla → talla_cm
   - Edad Madre → edad_madre
   - Tipo Parto → tipo_parto
   - Área Residencia → area_residencia

3. Reemplazar valores:
   - "SIN INFORMACIÓN" → null

4. Cerrar y aplicar
```

---

### 4.3 Modelo de Datos - Vista de Modelo

**Ir a Vista de Modelo** (`Ctrl + Alt + 3`)

**Qué verás:**
```
- Tabla: Presupuesto (izquierda)
  Campos: vigencia, mes, rubro, tipo_ingreso,
          presupuesto_vigente, recaudos

- Tabla: NacidosVivos (derecha)
  Campos: fecha_nacimiento, sexo, peso_gramos,
          edad_madre, tipo_parto, area_residencia
```

**En esta clase:**
- Trabajaremos con ambas tablas de forma independiente
- No crearemos relaciones entre ellas (no tienen campos comunes)
- Cada una representa una política pública diferente

**Concepto de relaciones:**
```
Cardinalidad común:
  Uno a muchos (1:*) → MÁS USADO
    Ejemplo: 1 departamento → muchos municipios

  Muchos a muchos (*:*) → EVITAR
    Requiere tabla puente

  Uno a uno (1:1) → RARO
    Mejor fusionar las tablas
```

**Para crear relaciones (cuando sea necesario):**
```
Método: Drag & drop desde campo de una tabla hasta
        campo compatible en otra tabla
```

---

## 📊 PARTE 5: VISUALIZACIONES BÁSICAS

### 5.1 Primera Visualización: Tarjeta KPI

**Dataset:** Presupuesto
**Objetivo:** Mostrar total recaudado

```
1. Ir a Vista de Informe (Ctrl + Alt + 1)
2. Panel de visualizaciones > Tarjeta (Card) 📇
3. Arrastrar campo "recaudos" a "Campos"
4. Formatear:
   - Formato > Etiqueta de datos
   - Tamaño texto: 48
   - Formato de número: Moneda, sin decimales
   - Formato > Etiqueta de categoría
   - Texto: "Total Recaudado"
```

**Resultado esperado:**
```
┌─────────────────────┐
│  Total Recaudado    │
│                     │
│  $55,495,944,368    │
└─────────────────────┘
```

---

### 5.2 Gráfico de Barras Horizontales

**Dataset:** Presupuesto
**Objetivo:** Comparar Ingresos Corrientes vs Recursos de Capital

```
1. Insertar > Gráfico de barras horizontales
2. Configurar campos:
   - Eje Y: tipo_ingreso
   - Eje X: recaudos (agregación: Suma)
3. Formato:
   - Título: "Recaudos por Tipo de Ingreso"
   - Etiquetas de datos: Activar
   - Colores: Azul (Ingresos Corrientes), Verde (Recursos Capital)
```

---

### 5.3 Gráfico de Línea Temporal

**Dataset:** Presupuesto
**Objetivo:** Evolución mensual de recaudos

```
1. Gráfico de líneas
2. Configurar:
   - Eje X: mes
   - Eje Y: recaudos (Suma)
   - Leyenda: tipo_ingreso
3. Activar:
   - Marcadores de datos
   - Etiquetas de datos
4. Formato:
   - Título: "Evolución Mensual de Recaudos 2024"
   - Colores diferenciados por tipo de ingreso
```

---

### 5.4 Gráfico de Columnas Agrupadas

**Dataset:** Nacidos Vivos
**Objetivo:** Nacimientos por tipo de parto

```
1. Visualización: Gráfico de columnas agrupadas
2. Configurar:
   - Eje X: tipo_parto
   - Eje Y: Contar de registros
   - Leyenda: sexo
3. Formato:
   - Título: "Nacimientos por Tipo de Parto y Sexo"
   - Colores: Azul (Masculino), Rosa (Femenino)
```

---

### 5.5 Gráfico de Dispersión

**Dataset:** Nacidos Vivos
**Objetivo:** Relación entre edad de la madre y peso del bebé

```
1. Visualización: Gráfico de dispersión
2. Configurar:
   - Eje X: edad_madre
   - Eje Y: peso_gramos
   - Leyenda: sexo
3. Ajustes:
   - Filtrar edades válidas (quitar null)
   - Filtrar pesos válidos (2000-5000g)
4. Formato:
   - Título: "Peso del Bebé según Edad de la Madre"
```

---

### 5.6 Tabla con Formato Condicional

**Dataset:** Presupuesto
**Objetivo:** Detalle de ejecución presupuestal

```
1. Visualización: Tabla
2. Arrastrar campos:
   - mes
   - tipo_ingreso
   - presupuesto_vigente
   - recaudos
   - porcentaje_ejecucion
3. Formato condicional:
   - Click derecho en "recaudos"
   - Formato condicional > Barras de datos
   - Gradiente: Verde
4. Ordenar por mes ascendente
```

---

### 🎓 EJERCICIO EN CLASE 2: Dashboard de Presupuesto

**Crear en el lienzo una página: "Presupuesto 2024"**

```
┌─────────────────────────────────────────────┐
│  [Total Recaudado]  [Total Presupuesto]    │  ← KPIs arriba
│  [Porcentaje Ejecución]                     │
├──────────────────┬──────────────────────────┤
│                  │                          │
│  Gráfico Barras  │   Gráfico Línea         │  ← Centro
│  (Ingresos vs    │   (Evolución Mensual)   │
│   Capital)       │                          │
│                  │                          │
├─────────────────────────────────────────────┤
│  Tabla con detalle mensual                  │  ← Abajo
└─────────────────────────────────────────────┘

✅ Checklist:
- 3 tarjetas KPI con totales (arriba)
- Gráfico de barras: Tipo de ingreso vs Recaudos
- Gráfico de línea: Evolución temporal
- Tabla: Detalle por mes con formato condicional
- Todos alineados con cuadrícula
- Títulos descriptivos en cada visualización
```

**Página 2: "Nacidos Vivos Miranda"**

```
┌─────────────────────────────────────────────┐
│  [Total Nacidos]  [Peso Promedio]          │  ← KPIs
├──────────────────┬──────────────────────────┤
│  Gráfico Columnas│   Gráfico Dispersión    │
│  (Tipo Parto)    │   (Edad vs Peso)        │
├──────────────────┴──────────────────────────┤
│  Tabla: Estadísticas por área residencia   │
└─────────────────────────────────────────────┘

✅ Checklist:
- 2 páginas diferentes (pestañas abajo)
- Cada página tiene tema coherente
- Visualizaciones alineadas
```

---

## 🧮 PARTE 6: MEDIDAS DAX (30 min)

### 6.1 ¿Qué es DAX?

**Data Analysis Expressions:** Lenguaje de fórmulas para Power BI

**Características:**
- Similar a Excel pero más potente
- Se evalúa en contexto de filtros dinámicos
- Permite cálculos complejos

---

### 6.2 Diferencia: Columna Calculada vs Medida

#### Columna Calculada
```
- Se calcula UNA VEZ al cargar datos
- Ocupa espacio en memoria
- Visible en Vista de Datos
- Usa contexto de fila

Ejemplo:
categoria = IF([total_estudiantes] > 10000, "Grande", "Pequeño")
```

#### Medida (Measure) ⭐ **LAS MÁS IMPORTANTES**
```
- Se calcula DINÁMICAMENTE según filtros
- No ocupa espacio adicional
- Solo visible en visualizaciones
- Usa contexto de filtro

Ejemplo:
Total Estudiantes = SUM(Tabla[total_estudiantes])
```

**🎯 Preferir siempre MEDIDAS sobre columnas calculadas**

---

### 6.3 Crear tu Primera Medida

**Dataset:** Presupuesto
**Objetivo:** Calcular total de recaudos

```
1. Click derecho en tabla "Presupuesto" > Nueva medida
2. Aparece barra de fórmulas arriba
3. Escribir:

Total Recaudos = SUM(Presupuesto[recaudos])

4. Presionar Enter
5. La medida aparece con ícono de calculadora ƒx
```

**Usar en visualización:**
- Arrastrar la medida [Total Recaudos] a cualquier gráfico
- Se calcula automáticamente según filtros activos
- Prueba: Úsala en una tarjeta KPI

---

### 6.4 Medidas DAX Esenciales

#### 1. Totales y Agregaciones (Presupuesto)

```dax
Total Recaudos = SUM(Presupuesto[recaudos])

Total Presupuesto = SUM(Presupuesto[presupuesto_vigente])

Promedio Recaudos = AVERAGE(Presupuesto[recaudos])

Máximo Recaudo = MAX(Presupuesto[recaudos])

Total Registros = COUNTROWS(Presupuesto)
```

**Para Nacidos Vivos:**

```dax
Total Nacidos = COUNTROWS(NacidosVivos)

Peso Promedio = AVERAGE(NacidosVivos[peso_gramos])

Edad Promedio Madre = AVERAGE(NacidosVivos[edad_madre])
```

---

#### 2. Porcentajes (Presupuesto)

**% de Ejecución Presupuestal:**
```dax
% Ejecución =
    DIVIDE(
        [Total Recaudos],
        [Total Presupuesto],
        0
    )
```

**Explicación:**
- `DIVIDE`: División segura (maneja división por cero)
- Tercer parámetro (0): valor si hay división por cero
- Formatear como porcentaje en el visual

---

**% del Total por Tipo de Ingreso:**
```dax
% del Total =
    DIVIDE(
        [Total Recaudos],
        CALCULATE(
            [Total Recaudos],
            ALL(Presupuesto[tipo_ingreso])
        )
    )
```

**Explicación:**
- `CALCULATE`: Modifica contexto de filtro
- `ALL`: Ignora filtros de tipo_ingreso
- Útil para ver participación de cada tipo

---

**Para Nacidos Vivos:**

```dax
% Cesáreas =
    VAR TotalNacidos = [Total Nacidos]
    VAR TotalCesareas = CALCULATE(
        [Total Nacidos],
        NacidosVivos[tipo_parto] = "CESÁREA"
    )
    RETURN
        DIVIDE(TotalCesareas, TotalNacidos)
```

**Explicación:**
- `VAR`: Variables para cálculos intermedios
- `RETURN`: Resultado final
- Más legible y fácil de debuggear

---

#### 3. Comparaciones Temporales (Avanzado)

**Requiere tabla calendario:**

```dax
Total Año Anterior =
    CALCULATE(
        [Total Estudiantes],
        SAMEPERIODLASTYEAR(Calendario[Fecha])
    )

Diferencia YoY =
    [Total Estudiantes] - [Total Año Anterior]
```

**Nota:** Para esto funcione necesitas una tabla Calendario relacionada.

---

#### 4. Filtros en Medidas

**Presupuesto:**

```dax
Ingresos Corrientes =
    CALCULATE(
        [Total Recaudos],
        Presupuesto[tipo_ingreso] = "INGRESOS CORRIENTES"
    )

Recursos Capital =
    CALCULATE(
        [Total Recaudos],
        Presupuesto[tipo_ingreso] = "RECURSOS DE CAPITAL"
    )

Recaudos Primer Semestre =
    CALCULATE(
        [Total Recaudos],
        Presupuesto[mes] <= 6
    )
```

**Nacidos Vivos:**

```dax
Nacidos Masculinos =
    CALCULATE(
        [Total Nacidos],
        NacidosVivos[sexo] = "MASCULINO"
    )

Nacidos Zona Rural =
    CALCULATE(
        [Total Nacidos],
        NacidosVivos[area_residencia] = "RURAL DISPERSO"
    )

Peso Bajo =
    CALCULATE(
        [Total Nacidos],
        NacidosVivos[peso_gramos] < 2500
    )
```

---

### 🎓 EJERCICIO EN CLASE 3: Crear Medidas DAX

**Para dataset Presupuesto, crear:**

```dax
1. Total Recaudos
Total Recaudos = SUM(Presupuesto[recaudos])

2. Total Presupuesto Vigente
Total Presupuesto = SUM(Presupuesto[presupuesto_vigente])

3. % Ejecución
% Ejecución = DIVIDE([Total Recaudos], [Total Presupuesto], 0)

4. Brecha Presupuestal
Brecha = [Total Presupuesto] - [Total Recaudos]

5. Ingresos Corrientes Únicamente
Ingresos Corrientes =
    CALCULATE(
        [Total Recaudos],
        Presupuesto[tipo_ingreso] = "INGRESOS CORRIENTES"
    )
```

**Para dataset Nacidos Vivos, crear:**

```dax
6. Total Nacimientos
Total Nacidos = COUNTROWS(NacidosVivos)

7. Peso Promedio
Peso Promedio = AVERAGE(NacidosVivos[peso_gramos])

8. % Cesáreas
% Cesáreas =
    DIVIDE(
        CALCULATE([Total Nacidos], NacidosVivos[tipo_parto] = "CESÁREA"),
        [Total Nacidos]
    )
```

**Usar estas medidas en:**
- Tarjetas KPI en tus páginas
- Gráficos existentes
- Nueva tabla comparativa

---

### 6.5 Funciones DAX Más Usadas - Referencia Rápida

```dax
/* AGREGACIONES */
SUM, AVERAGE, MIN, MAX, COUNT, COUNTROWS, DISTINCTCOUNT

/* FILTROS */
CALCULATE   → Modifica contexto de filtro
FILTER      → Filtra tabla
ALL         → Ignora filtros
ALLEXCEPT   → Ignora todos excepto...
VALUES      → Valores únicos de columna

/* TIEMPO */
SAMEPERIODLASTYEAR  → Mismo período año anterior
DATEADD             → Agregar días/meses/años
TOTALYTD            → Total acumulado del año

/* LÓGICA */
IF        → Condicional simple
SWITCH    → Múltiples condiciones
AND, OR   → Operadores lógicos

/* RELACIONALES */
RELATED       → Traer campo de tabla relacionada (lado "1")
RELATEDTABLE  → Traer tabla relacionada (lado "muchos")

/* ITERADORES (fila por fila) */
SUMX      → Suma iterando cada fila
AVERAGEX  → Promedio iterando
COUNTX    → Contar iterando
```

---

## 🎨 PARTE 7: DISEÑO PROFESIONAL (25 min)

### 7.1 Aplicar Tema

```
Vista > Temas > Elegir tema predefinido

O personalizar:
Vista > Temas > Personalizar tema actual

Configurar:
- Colores de datos: 5-7 colores armoniosos
- Color de fondo: Blanco o gris claro
- Fuentes: Títulos (Segoe UI Bold), Texto (Calibri)
```

**Paletas recomendadas:**
- Corporativo: Azules y grises
- Educación: Azules y verdes
- Alertas: Verde, Amarillo, Rojo

---

### 7.2 Formato de Visualizaciones

**Para CADA visualización:**

```
Formato (pincel) > Configurar:

GENERAL:
- Título: Activar, tamaño 14-16, negrita
- Fondo: Color sutil, opacidad 90%
- Borde: 1px, color gris claro
- Sombra: Ligera

ETIQUETAS DE DATOS:
- Tamaño: 10-11pt
- Color: Contraste alto
- Posición: Fuera de punto/barra

EJES:
- Títulos: Descriptivos
- Valores: Formato numérico con separadores
```

---

### 7.3 Layout y Composición

#### Jerarquía Visual

```
┌─────────────────────────────────────────┐
│  ARRIBA: KPIs (grandes, 3-4 tarjetas)  │
├─────────────────────────────────────────┤
│                                         │
│  CENTRO: Visualizaciones principales    │
│         (2-3 gráficos importantes)      │
│                                         │
├─────────────────────────────────────────┤
│  ABAJO: Detalles y tablas              │
├─────────────────────────────────────────┤
│  LATERAL: Filtros y segmentaciones     │
└─────────────────────────────────────────┘
```

---

#### Alineación y Espaciado

```
Ver > Mostrar:
- ✓ Líneas de cuadrícula
- ✓ Ajustar a cuadrícula
- ✓ Reglas

Seleccionar múltiples objetos (Ctrl + Click):
- Formato > Alinear > Alinear izquierda
- Formato > Distribuir > Horizontalmente
- Formato > Distribuir > Verticalmente
```

**🎯 Regla de oro:** Todo debe estar alineado

---

### 7.4 Segmentaciones (Slicers) - Filtros visuales

**Crear filtro interactivo:**

```
1. Visualizaciones > Segmentación de datos
2. Arrastrar campo: departamento, año, sector
3. Formato:
   - Estilo: Lista, desplegable, o azulejos
   - Selección múltiple: Activar
   - Botón "Seleccionar todo": Mostrar
   - Orientación: Vertical u horizontal
```

**Ejemplo de layout con slicers:**
```
┌──────────────┬──────────────────────────┐
│  Filtros:    │                          │
│  □ Año       │   Gráficos principales   │
│  □ Depto     │                          │
│  □ Sector    │                          │
└──────────────┴──────────────────────────┘
```

---

## 🚀 PARTE 8: INTERACTIVIDAD AVANZADA (30 min)

### 8.1 Niveles de Filtros

```
1. Filtros de VISUALIZACIÓN
   → Solo afecta ese gráfico

2. Filtros de PÁGINA
   → Afecta toda la página actual

3. Filtros de INFORME
   → Afecta todo el dashboard
```

**Configurar:**
- Panel de filtros (derecha)
- Arrastrar campo al nivel deseado
- Configurar tipo: Básico, Avanzado, Top N

---

### 8.2 Interacción entre Visualizaciones

**Por defecto:** Click en barra → Filtra otros gráficos

**Personalizar interacciones:**
```
1. Seleccionar visualización origen
2. Formato > Editar interacciones
3. En otras visualizaciones aparecen íconos:
   - 🎯 Filtrar: Aplica filtro
   - 📍 Resaltar: Resalta datos
   - 🚫 Ninguno: No interactúa
```

**Ejemplo:** Click en departamento del mapa → Filtra gráfico de barras

---

### 8.3 Drill-Through (Navegar a Detalle)

**Objetivo:** Click en punto de datos → Ver página de detalle

#### Configurar página de destino:

```
1. Crear nueva página: "Detalle Departamento"
2. En esta página:
   - Panel de filtros > Área de Drill-through
   - Arrastrar campo: departamento
   - Activar: "Mantener todos los filtros"
3. Agregar visualizaciones detalladas:
   - Tabla con colegios
   - Gráfico de evolución
   - KPIs específicos
```

#### Usar drill-through:

```
En página principal:
- Click derecho en barra/punto
- Drill through > Detalle Departamento
- Aparece página filtrada automáticamente
- Botón "Atrás" generado automáticamente
```

---

### 8.4 Bookmarks (Marcadores) - Data Storytelling

**Objetivo:** Guardar estados del dashboard para contar una historia

#### Crear marcador:

```
1. Configurar filtros y selecciones deseadas
2. Vista > Marcadores > Agregar
3. Renombrar: "Panorama Nacional"
4. Opciones (clic derecho):
   - Datos: ✓ (guarda filtros)
   - Mostrar: ✓ (guarda visibilidad)
   - Página actual: ✓
```

---

#### Storytelling con bookmarks:

**Ejemplo: Dashboard de Crisis Educativa**

```
MARCADOR 1: "Situación General"
- Mapa nacional completo
- Sin filtros aplicados
- KPIs generales visibles

MARCADOR 2: "Departamentos Críticos"
- Filtrado a Bottom 5 departamentos
- Gráfico de barra resaltado en rojo
- Tabla de brechas visible

MARCADOR 3: "Evolución Temporal"
- Gráfico de línea ampliado
- Años 2015-2024 visibles
- Proyección futura visible
```

#### Crear botones de navegación:

```
Insertar > Botones > Botón en blanco

Configurar:
1. Formato > Acción
   - Tipo: Marcador
   - Marcador: "Situación General"
2. Formato > Estilo
   - Texto: "Ver Panorama"
   - Ícono: ▶
   - Estados: Normal, Al pasar, Al presionar
```

---

### 🎓 EJERCICIO EN CLASE 4: Interactividad

**Implementar en tu dashboard de Presupuesto:**

```
✅ 1. Crear segmentaciones (slicers)
   - Por mes (1-12)
   - Por tipo_ingreso (Ingresos Corrientes / Recursos Capital)
   - Ubicarlos en la parte superior o lateral izquierda

✅ 2. Configurar interacciones
   - Gráfico de barras filtra línea temporal
   - Tabla NO filtra otros gráficos (desactivar interacción)
   - Slicers filtran TODO el dashboard

✅ 3. Crear bookmarks para storytelling
   - "Vista Completa": Sin filtros, todo visible
   - "Ingresos Corrientes": Filtrado solo a Ingresos Corrientes
   - "Recursos de Capital": Filtrado solo a Recursos de Capital

✅ 4. Agregar botones de navegación
   - Botón 1: "Ver Ingresos Corrientes" → Bookmark correspondiente
   - Botón 2: "Ver Recursos Capital" → Bookmark correspondiente
   - Botón 3: "Ver Todo" → Bookmark Vista Completa

✅ 5. Personalizar tooltip (opcional avanzado)
   - Crear página pequeña de tooltip
   - Mostrar detalle al pasar sobre punto de datos
```

**Para dashboard de Nacidos Vivos:**

```
✅ 1. Crear segmentaciones
   - Por sexo
   - Por tipo_parto
   - Por area_residencia

✅ 2. Crear bookmark comparativo
   - "Comparar por Sexo": Resaltar diferencias M vs F
   - "Análisis Rural vs Urbano": Filtrado por área
```

---

## 📤 PARTE 9: PUBLICAR Y COMPARTIR (15 min)

### 9.1 Guardar Archivo Local

```
Archivo > Guardar como
Formato: .pbix (Power BI Desktop file)
Ubicación: Carpeta clase9
Nombre sugerido: clase9_politicas_publicas.pbix
```

**💾 Guardar frecuentemente:** `Ctrl + S`

**Tu archivo incluye:**
- Los 2 datasets (Presupuesto y Nacidos Vivos)
- Todas las transformaciones de Power Query
- Las medidas DAX creadas
- Las visualizaciones y páginas
- Los bookmarks y configuraciones

---

### 9.2 Publicar en Power BI Service (Nube)

**Requisitos:** Cuenta Microsoft 365 o cuenta Power BI gratuita

```
Inicio > Publicar

Pasos:
1. Iniciar sesión (si no lo has hecho)
2. Seleccionar workspace: "Mi área de trabajo"
3. Esperar carga (puede tardar 1-2 min)
4. Click en "Abrir en Power BI"
5. Se abre en navegador
```

**Beneficios:**
- Acceso desde cualquier dispositivo
- Compartir con URL
- Actualización automática de datos
- Colaboración en tiempo real

---

### 9.3 Compartir Dashboard

#### Opción 1: Compartir Enlace (Power BI Service)

```
En Power BI Service (web):
1. Abrir dashboard publicado
2. Compartir > Crear vínculo
3. Configurar permisos:
   - ✓ Permitir que los destinatarios compartan
   - ✓ Permitir que los destinatarios creen contenido
4. Copiar enlace
5. Enviar por correo/Teams
```

---

#### Opción 2: Exportar a PDF

```
Archivo > Exportar a PDF

Configurar:
- Páginas: Actual o todas
- Orientación: Horizontal (recomendado)
- Tamaño: A4 o Carta

Usar para:
- Presentaciones impresas
- Reportes estáticos
- Archivo adjunto en correo
```

---

#### Opción 3: Exportar a PowerPoint

```
Archivo > Exportar a PowerPoint

Resultado:
- Cada página = 1 diapositiva
- Imágenes estáticas (no interactivas)
- Ideal para presentaciones ejecutivas

Editar luego en PowerPoint:
- Agregar texto explicativo
- Insertar logotipos
- Crear narrativa
```

---

### 9.4 Compartir Archivo .pbix

```
Enviar archivo .pbix por:
- Correo electrónico
- OneDrive / Google Drive
- USB

⚠️ Consideraciones:
- Receptor necesita Power BI Desktop instalado
- Datos quedan embebidos en el archivo
- No se actualiza automáticamente
```

---

## ⚡ BUENAS PRÁCTICAS Y TIPS

### 🎯 Rendimiento

```
✅ HACER:
- Usar medidas en lugar de columnas calculadas
- Importar solo columnas necesarias
- Filtrar filas innecesarias en Power Query
- Usar tipos de datos correctos

❌ EVITAR:
- Columnas calculadas pesadas
- Relaciones muchos a muchos
- Imágenes de alta resolución (>200KB)
- Visualizaciones innecesarias
```

---

### 📝 Convenciones de Nombres

```
MEDIDAS (con corchetes):
✓ [Total Estudiantes]
✓ [% Crecimiento]
✓ [Promedio Calificación]

COLUMNAS (snake_case):
✓ nombre_columna
✓ departamento_codigo
✓ fecha_registro

TABLAS (PascalCase):
✓ MatriculaEscolar
✓ Departamentos
✓ Calendario
```

---

### 🗂️ Organización

```
Carpetas de medidas:
- Click derecho en medida > Nueva carpeta
- Carpetas: KPIs, Cálculos Temporales, Porcentajes

Descripción de medidas:
- Click derecho > Propiedades > Descripción
- Aparece como tooltip al pasar cursor
```

---

## 🛠️ TROUBLESHOOTING

### ❌ "No se pueden cargar los datos"

```
✓ Verificar que el archivo existe
✓ Cerrar archivo si está abierto en Excel
✓ Comprobar permisos de lectura
✓ Cambiar a "Importar" si usaste DirectQuery
```

---

### ❌ "Relación no se crea automáticamente"

```
✓ Verificar tipos de datos compatibles
✓ Buscar duplicados en columna del lado "1"
✓ Crear relación manual en Vista de Modelo
✓ Verificar nombres de columnas (espacios, mayúsculas)
```

---

### ❌ "Medida DAX da error"

```
✓ Verificar nombres de tablas y campos
✓ Usar [corchetes] para medidas
✓ Usar Tabla[columna] para campos
✓ Revisar sintaxis: comas y paréntesis
✓ Verificar contexto de filtros
```

---

### ❌ "Dashboard es muy lento"

```
✓ Reducir número de visualizaciones por página (max 6-8)
✓ Limitar filas en Power Query (filtrar años antiguos)
✓ Usar agregaciones previas
✓ Ejecutar Analizador de rendimiento:
   Vista > Analizador de rendimiento > Iniciar
```

---

## 📚 RECURSOS ADICIONALES

### Documentación Oficial
- **Power BI Docs:** https://docs.microsoft.com/power-bi/
- **DAX Guide:** https://dax.guide/
- **Power Query M:** https://docs.microsoft.com/powerquery-m/

### Comunidad y Aprendizaje
- **Power BI Community:** https://community.powerbi.com/
- **YouTube:**
  - Guy in a Cube
  - Curbal
  - SQLBI
- **Cursos gratuitos:** Microsoft Learn

### Datasets de Práctica
- **datos.gov.co** (Colombia)
- **Kaggle Datasets**
- **World Bank Open Data**
- **Sample datasets de Microsoft**


---

## 🎯 PREPARACIÓN PARA PRÓXIMA CLASE

**Semana 10: Data Storytelling y Análisis Avanzado**

**Traer preparado:**
1. Tu archivo .pbix de la clase 9
2. Ideas de insights encontrados en los datos
3. Preguntas sobre DAX o visualizaciones

**Temas próxima clase:**
- Data storytelling: contar historias con datos
- Análisis de patrones y tendencias
- Presentación efectiva de dashboards
- Técnicas avanzadas de DAX

---

**¿Preguntas? ¿Necesitas ayuda?**

👉 Revisa este manual paso a paso
👉 Consulta la documentación oficial
👉 Pregunta al profesor durante o después de clase

**¡A crear dashboards impactantes! 📊✨**
