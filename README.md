# DataKit (Alpha)
En el presente repositorio encontrará:
- Módulos que resuelvan problemáticas recurrentes de `Data Science`.
- Modelitos de `Deep Learning`.
- Abstracciones sobre frameworks de datos.
- El típico script que tenés anotado en una servilleta y querés tener a mano.


# Objetivos
1. Aprender sobre la marca a crear un proyecto grande y abstraido, siguiendo las mejores prácticas que conozca.
2. Crear un conjunto de herramientas que resuelvan las tareas repetitivas al trabajar con datos.
3. Crear un framework para modelos de `Deep Learning` en `PyTorch` usando `Pydantic`.
4. Manejar el guardado, carga, validación y configuración de los modelos de forma eficiente.
5. Proponer una forma `no-hardcodeada` de variar los hiperparámetros y estructura interna de los módulos.
6. Testing 100%.
7. Type-Hints.
8. Documentación automática.



# Notas:
### Como estructurar el código `dl`
- Arquitectura `base del modelo`, debe contener únicamente el `modelo a entrenar`.
- Debe traer de `modules` las capas que necesite.
```markdown
├── dl
│   ├── ...
│   ├── models
│   │   ├── name_model_1
│   │   │   └── base_name_model_1.py
│   │   ├── name_model_2
│   │   │   └── base_name_model_2.py
│   │   └── name_model_3
│   │       └── base_name_model_3.py
```


- Contiene los `nn.Module` necesarios para crear las distintas redes.
```markdown
├── dl
│   ├── ...
│   ├── modules
│   │   ├── module_1.py
│   │   ├── module_2.py
│   │   └── module_3.py
```


- Si hubiera un módulo que sirva de `backbone`, se debería introducir aquí.
```markdown
├── dl
│   ├── ...
│   ├── backbones
│   │   ├── backbone_1.py
│   │   ├── backbone_2.py
│   │   └── backbone_3.py
```




##### TODO
- Abstracción de pathlib y argparse para poder levantar los paths del proyecto.
- VER: https://pypi.org/project/zc.buildout/ lo ví en:
- config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
- https://www.ecmwf.int/en/forecasts/datasets
- https://www.meteored.com.ar/mapas-meteorologicos/
- https://github.com/luisCartoGeo/GeoAI_Plugin/tree/main


- Idea: Generar un yield con with de raster para poder abrir N rasters cerrandose al final con el src
```