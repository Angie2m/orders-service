Orders API - Servicio de Gestión de Pedidos
Este proyecto es un microservicio para la gestión de pedidos desarrollado con FastAPI, siguiendo los principios de la Arquitectura Hexagonal y garantizando altos estándares de calidad mediante tipado estático, pruebas automatizadas y seguridad JWT.

Arquitectura del Proyecto
El sistema se divide en capas independientes para asegurar el desacoplamiento y la testabilidad:
Dominio (src/domain): Contiene las entidades de negocio (Order) y las interfaces de los repositorios.
Aplicación (src/application): Orquestación de lógica mediante casos de uso (CreateOrder, GetOrder, ListOrders).
Infraestructura (src/infrastructure): Implementaciones concretas de la base de datos (SQLAlchemy), modelos y configuración global.
Interfaces (src/interfaces): Controladores de la API, esquemas de Pydantic y dependencias de seguridad.

Tecnologías y Herramientas
Lenguaje: Python 3.13+.
Framework: FastAPI.
ORM: SQLAlchemy con migraciones de Alembic.
Gestión de Dependencias: Poetry.
Seguridad: Autenticación JWT (python-jose) y auditoría con Safety.
Calidad: Mypy (Tipado), Ruff (Linting) y Pytest (Pruebas).

Instalación y Ejecución
Requisitos Previos
Tener instalado Python 3.13 y Poetry.
Motor de Docker (opcional para contenedores).
Configuración Local
Instalar dependencias:
Ejecutar migraciones de base de datos:
Iniciar el servidor:
Ejecución con Docker
docker build -t orders-api .
docker run -p 8000:8000 orders-api

Seguridad y Autenticación
La API cuenta con protección de rutas mediante JWT.
Endpoint de Login: /token.
Credenciales de Laboratorio:
Usuario: admin
Password: password123

Calidad de Código y Pruebas
Para asegurar la robustez del servicio, ejecuta los siguientes comandos de calidad:
Pruebas Unitarias e Integración: poetry run pytest -v
Reporte de Cobertura: poetry run pytest --cov=src
Análisis de Tipado: poetry run mypy src
Linter de Estilo: poetry run ruff check .
Imports en una sola línea: poetry run isort .
Espacios Incorrectos: poetry run black .
Auditoría de Seguridad: poetry run safety scan

Documentación de la API
Una vez iniciada la aplicación, puedes acceder a la documentación interactiva en:
Swagger UI: http://localhost:8000/docs.
Redoc: http://localhost:8000/redoc.

orders-service/
├── src/
│   ├── domain/                # Capa de Negocio (Entidades y Puertos)
│   │   ├── entities/          # order.py
│   │   └── repositories/      # order_repository.py
│   ├── application/           # Casos de Uso (Orquestación)
│   │   └── use_cases/         # create_order.py, get_order.py
│   ├── infrastructure/        # Detalles Técnicos (Adaptadores)
│   │   ├── database/          # db.py, models.py
│   │   └── repositories/      # sqlalchemy_order_repository.py
│   ├── interfaces/            # Punto de Entrada (API)
│   │   └── api/               # schemas.py, order_controller.py
│   └── main.py                # Orquestador del servicio
├── tests/                     # Suite de Pruebas
├── alembic/                   # Migraciones de DB
└── README.md                  # Documentación

```mermaid
graph TD
    subgraph "Interfaces Layer (API)"
        A[order_controller.py] --> B[dependencies.py]
    end

    subgraph "Application Layer"
        B --> C[CreateOrderUseCase]
        B --> D[GetOrderUseCase]
    end

    subgraph "Domain Layer (Core)"
        C --> E((Order Entity))
        D --> E
        F{OrderRepository Interface}
    end

    subgraph "Infrastructure Layer"
        G[(SQLAlchemy / SQLite)] -- Adaptador --> F
        H[sqlalchemy_order_repository.py] -- Implementa --> F
    end

    C -.-> F

### **Pasos para actualizarlo en GitHub:**
Como ya sabes hacer el flujo de Git, solo sigue estos 3 comandos rápidos después de guardar el cambio en el `README.md`:

1.  `git add README.md`
2.  `git commit -m "Fix: renderizado de diagrama Mermaid"`
3.  `git push origin main`

**¿Por qué es importante para tu "10/10"?**
La rúbrica de **Documentación y Diagramas** exige que la arquitectura sea clara [2, 3]. Al corregir esto, tu repositorio mostrará un gráfico profesional en lugar de líneas de código, demostrando que dominas no solo la arquitectura hexagonal, sino también las herramientas de documentación técnica moderna [2].

Una vez que hagas el `push`, refresca la página de tu repositorio y verás cómo el texto se transforma en un diagrama visual de capas. ¡Dime en cuanto lo subas para verificar que ya se vea bien!
