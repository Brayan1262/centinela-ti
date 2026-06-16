import psutil
import time
import json
from datetime import datetime

def obtener_metricas():
    """Obtiene las métricas actuales del sistema (CPU, RAM, Disco)."""
    # Usamos un pequeño intervalo para asegurar una lectura precisa de CPU
    cpu_usage = psutil.cpu_percent(interval=0.1)
    
    ram_info = psutil.virtual_memory()
    ram_usage = ram_info.percent
    
    # En Windows asume 'C:\' si corremos en el disco C, o la raíz actual '/'
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_percent": cpu_usage,
        "ram_percent": ram_usage,
        "disk_percent": disk_usage
    }

# def enviar_metricas_al_backend(metricas):
#     """
#     Envía las métricas recolectadas a la API REST de Spring Boot.
#     Ejemplo de implementación futura:
#     
#     try:
#         headers = {'Content-Type': 'application/json'}
#         response = requests.post(
#             url='http://localhost:8080/api/v1/metrics', 
#             json=metricas, 
#             headers=headers,
#             timeout=2
#         )
#         response.raise_for_status()
#         # print("✅ [INFO] Métricas enviadas al backend.")
#     except requests.exceptions.RequestException as e:
#         print(f"❌ [ERROR] Fallo al enviar métricas: {e}")
#     """
#     pass

def main():
    print("==================================================")
    print("🛡️  CENTINELA TI - AGENTE RECOLECTOR INICIADO   🛡️")
    print("==================================================\n")
    
    while True:
        try:
            metricas = obtener_metricas()
            
            # Formato atractivo en consola
            print(f"[{metricas['timestamp']}] 📊 NUEVA LECTURA:")
            print(f"   💻 CPU:   {metricas['cpu_percent']:>5.1f} %")
            print(f"   🧠 RAM:   {metricas['ram_percent']:>5.1f} %")
            print(f"   💽 DISCO: {metricas['disk_percent']:>5.1f} %")
            print("-" * 50)
            
            # Preparado para Fase 3:
            # enviar_metricas_al_backend(metricas)
            
            time.sleep(5)
            
        except KeyboardInterrupt:
            print("\n🛑 [INFO] Agente detenido por el usuario. Apagando Centinela...")
            break
        except Exception as e:
            print(f"\n⚠️ [ERROR] Ocurrió un fallo en la recolección: {e}")
            time.sleep(5) # Evitar un crash loop en caso de error continuo

if __name__ == "__main__":
    main()
