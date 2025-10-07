# Librerias
import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Configura tus credenciales de Kaggle
# Asegúrate de tener el archivo kaggle.json en la ruta correcta (~/.kaggle/kaggle.json) o especificarlo manualmente

# Especifica la ruta donde quieres guardar el dataset
#ruta_descarga = '/mnt/c/Users/jl_ve/Documents/proyecto/bd/'
ruta_descarga = os.path.dirname(os.path.abspath(__file__))

#nombre archivo
fl = 'financial_transactions.csv'
# Comprobar si el archivo existe
if os.path.exists(fl):
    # Eliminar el archivo si existe
    os.remove(fl)
    print(f"El archivo '{fl}' ha sido eliminado.")
else:
    print(f"El archivo '{fl}' no existe.")

# Nombre del dataset en Kaggle (formato 'usuario/dataset')
dataset = 'cankatsrc/financial-transactions-dataset'

# Inicializa la API de Kaggle
api = KaggleApi()
api.authenticate()

# Crea la carpeta de destino si no existe
os.makedirs(ruta_descarga, exist_ok=True)

# Descarga el dataset en la ruta especificada
api.dataset_download_files(dataset, path=ruta_descarga, unzip=True)

print(f'Dataset descargado en: {ruta_descarga}')

