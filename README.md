# BD2-T2
API de Gestión de Biblioteca con Litestar y SQLAlchemy


### Rodolfo Cifuentes 🤓
- Estudiante de Ingeniería Informática
- [Rodolfo Cifuentes](https://github.com/Fitooooooooo)
- **rcifuent@umag.cl**


### Descripción del Proyecto y Decisiones de Diseño

Este proyecto extiende una API REST base para la gestión de una biblioteca, aplicando conocimientos avanzados en el desarrollo de APIs con Litestar y SQLAlchemy.

**Principales cambios y decisiones:**

*   **Nuevos Modelos:** Se introdujeron los modelos `Category` y `Review`. Para `Category`, se implementó una relación muchos a muchos con `Book` a través de una tabla de asociación (`book_categories`), permitiendo una clasificación flexible de los libros.
*   **Actualización de Modelos Existentes:** Se enriquecieron los modelos `Book`, `User` y `Loan` con nuevos campos para añadir más detalle y lógica de negocio, como el manejo de stock, información de contacto de usuarios, y estados de préstamos (`ACTIVE`, `RETURNED`, `OVERDUE`) mediante un `Enum` para mayor robustez.
*   **Lógica de Negocio en Repositorios:** Se centralizó la lógica de negocio compleja en los repositorios correspondientes (`BookRepository` y `LoanRepository`). Esto permite mantener los controladores más limpios y enfocados en manejar las peticiones HTTP, mientras que la lógica de acceso y manipulación de datos reside en una capa separada.
*   **Validaciones y DTOs:** Se utilizaron DTOs (`Data Transfer Objects`) para cada modelo, configurando los campos a excluir o incluir en operaciones de lectura, creación y actualización. Las validaciones específicas (formato de email, rangos de valores) se implementaron a nivel de controlador para proporcionar feedback inmediato al cliente.
*   **Migraciones con Alembic:** Cada cambio en la estructura de la base de datos fue gestionado a través de migraciones generadas con Alembic, asegurando un versionado claro y la capacidad de replicar la base de datos de forma consistente.

### Cumplimiento de Requerimientos