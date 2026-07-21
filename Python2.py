# Herramienta de Gestión de Redes y Ciberseguridad (Simulación)
import time

print("=" * 50)
print(" SISTEMA DE AUTOMATIZACIÓN TI - AstiChile")
print("=" * 50)

ejecutando = True

while ejecutando:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Escanear puertos (Simulación)")
    print("2. Verificar estado de Docker Swarm")
    print("3. Salir del programa")
    
    opcion = input("\nSelecciona una opción (1-3): ")

    if opcion == "1":
        ip = input("Ingresa la dirección IP a escanear: ")
        print(f"\n[+] Iniciando escaneo en {ip}...")
        time.sleep(1) # Simula una pequeña pausa de procesamiento
        print("[-] Puerto 22 (SSH)  -> ABIERTO")
        print("[-] Puerto 80 (HTTP) -> ABIERTO")
        print("[-] Puerto 443 (HTTPS)-> ABIERTO")
        print("[*] Escaneo finalizado con éxito.")
        
    elif opcion == "2":
        print("\n[*] Ejecutando: docker node ls...")
        time.sleep(1)
        print("STATUS      NAME            ROLE        AVAILABILITY")
        print("Ready       node-master-01  Leader      Active")
        print("Ready       node-worker-01  Worker      Active")
        print("[+] Entorno Docker Swarm operando con normalidad.")
        
    elif opcion == "3":
        print("\nCerrando sesión de forma segura... ¡Nos vemos, compare!")
        ejecutando = False
        
    else:
        print("\n[!] Opción no válida. Por favor, ingresa 1, 2 o 3.")

print("=" * 50)