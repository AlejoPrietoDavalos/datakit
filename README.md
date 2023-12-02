## Data Science Toolkit (super alpha)
- Sentite libre de chorear o aportar cualquier contenido.


# Notas:
### Como estructurar el código
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




#### Que encontrarás en este repositorio:
- Pequeños módulos que resuelvan problemáticas de `data science`.
- Modelitos de `Deep Learning`.
- Abstracciones para manipular algún framework.
- Objetos contenedores de datos personalizados.
- El típico script que tenés anotado en una servilleta y querés tener a mano.


##### TODO
- Abstracción de pathlib y argparse para poder levantar los paths del proyecto.
- VER: https://pypi.org/project/zc.buildout/ lo ví en:
- config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
- https://www.ecmwf.int/en/forecasts/datasets
- https://www.meteored.com.ar/mapas-meteorologicos/
- https://github.com/luisCartoGeo/GeoAI_Plugin/tree/main


- Idea: Generar un yield con with de raster para poder abrir N rasters cerrandose al final con el src
