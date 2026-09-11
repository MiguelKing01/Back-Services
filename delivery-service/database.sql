-- ==============================================================================
-- SCRIPT DE BASE DE DATOS PARA DELIVERY-SERVICE (ENVÍOS)
-- Motor: PostgreSQL
-- Base de datos: cooformacion_db (o delivery_db según tu configuración)
-- ==============================================================================

-- 1. Crear la base de datos si no existe (ejecutar conectado como postgres)
-- CREATE DATABASE cooformacion_db;

-- 2. Conectarse a la base de datos:
-- \c cooformacion_db;

-- 3. Crear la tabla 'envios' compatible con el modelo Django Envio
CREATE TABLE IF NOT EXISTS envios (
    id_envio SERIAL PRIMARY KEY,
    numero_guia VARCHAR(50) NOT NULL UNIQUE,
    id_usuario INTEGER NOT NULL,
    id_empresa INTEGER,
    direccion_origen VARCHAR(255) NOT NULL,
    direccion_destino VARCHAR(255) NOT NULL,
    destinatario_nombre VARCHAR(100) NOT NULL,
    destinatario_telefono VARCHAR(20) NOT NULL,
    estado VARCHAR(50) NOT NULL DEFAULT 'pendiente',
    costo_envio NUMERIC(10, 2) NOT NULL DEFAULT 0.00,
    activo INTEGER NOT NULL DEFAULT 1,
    fecha_creacion TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_entrega_estimada TIMESTAMP WITH TIME ZONE
);

-- Índices recomendados para optimizar búsquedas frecuentes
CREATE INDEX IF NOT EXISTS idx_envios_numero_guia ON envios (numero_guia);
CREATE INDEX IF NOT EXISTS idx_envios_id_usuario ON envios (id_usuario);
CREATE INDEX IF NOT EXISTS idx_envios_estado ON envios (estado);

-- ==============================================================================
-- DATOS DE PRUEBA PARA INTERACTUAR CON EL CRUD
-- ==============================================================================

INSERT INTO envios (
    numero_guia,
    id_usuario,
    id_empresa,
    direccion_origen,
    direccion_destino,
    destinatario_nombre,
    destinatario_telefono,
    estado,
    costo_envio,
    activo,
    fecha_creacion,
    fecha_entrega_estimada
) VALUES
(
    'GUIA-2026-001',
    1,
    1,
    'Calle 45 # 13-22, Bogotá',
    'Carrera 7 # 72-41, Bogotá',
    'Laura Martínez',
    '3109876543',
    'pendiente',
    15000.00,
    1,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP + INTERVAL '2 days'
),
(
    'GUIA-2026-002',
    1,
    2,
    'Avenida El Dorado # 68C-61, Bogotá',
    'Calle 100 # 15-30, Bogotá',
    'Carlos Gómez',
    '3154443322',
    'en_transito',
    22500.50,
    1,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP + INTERVAL '1 day'
),
(
    'GUIA-2026-003',
    2,
    1,
    'Transversal 23 # 85-10, Bogotá',
    'Calle 127 # 48-20, Bogotá',
    'Ana Lucía Rojas',
    '3201112233',
    'entregado',
    18000.00,
    1,
    CURRENT_TIMESTAMP - INTERVAL '3 days',
    CURRENT_TIMESTAMP - INTERVAL '1 day'
)
ON CONFLICT (numero_guia) DO NOTHING;

-- ==============================================================================
-- CONSULTAS DE EJEMPLO PARA VALIDAR EL CRUD
-- ==============================================================================

-- [READ] Listar todos los envíos activos
SELECT * FROM envios WHERE activo = 1 ORDER BY fecha_creacion DESC;

-- [READ] Consultar un envío por ID
SELECT * FROM envios WHERE id_envio = 1;

-- [READ] Consultar un envío por número de guía
SELECT * FROM envios WHERE numero_guia = 'GUIA-2026-001';

-- [CREATE] Crear un nuevo envío manualmente
-- INSERT INTO envios (numero_guia, id_usuario, direccion_origen, direccion_destino, destinatario_nombre, destinatario_telefono, estado, costo_envio)
-- VALUES ('GUIA-2026-004', 1, 'Calle 80 # 68-10', 'Carrera 15 # 93-50', 'Pedro Ruiz', '3007654321', 'pendiente', 12000.00);

-- [UPDATE] Actualizar estado o entrega
-- UPDATE envios SET estado = 'entregado', fecha_entrega_estimada = CURRENT_TIMESTAMP WHERE id_envio = 1;

-- [DELETE] Eliminación lógica (recomendada para microservicios)
-- UPDATE envios SET activo = 0 WHERE id_envio = 1;

-- [DELETE] Eliminación física directa
-- DELETE FROM envios WHERE id_envio = 1;
