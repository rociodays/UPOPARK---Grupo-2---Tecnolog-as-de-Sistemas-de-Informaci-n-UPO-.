from odoo.tools.sql import make_identifier
from psycopg2 import sql


RENOMBRES = {
    'elemento_inspeccionado': {'m2oInspeccionId': 'inspeccion_id'},
    'estado_incidencia': {},
    'incidencia': {
        'm2oTipoIncidenciaId': 'tipo_incidencia_id',
        'm2oEstadoIncidenciaId': 'estado_incidencia_id',
        'm2oContactoReportaId': 'contacto_reporta_id',
        'o2mOrdenesTrabajoIds': 'orden_trabajo_ids',
        'o2mIndisponibilidadesIds': 'indisponibilidad_ids',
    },
    'indisponibilidad': {
        'm2oRecursoId': 'recurso_id',
        'm2oIncidenciaId': 'incidencia_id',
        'o2mInspeccionesIds': 'inspeccion_ids',
    },
    'inspeccion': {
        'm2oOrdenTrabajoId': 'orden_trabajo_id',
        'm2oIndisponibilidadId': 'indisponibilidad_id',
        'm2oInspectorId': 'inspector_id',
        'm2oResultadoId': 'resultado_id',
        'o2mPuntosComprobacionIds': 'elemento_inspeccionado_ids',
    },
    'orden_trabajo': {
        'm2oIncidenciaId': 'incidencia_id',
        'm2oResponsableId': 'responsable_id',
        'o2mTareasIds': 'tarea_ids',
        'o2mInspeccionesIds': 'inspeccion_ids',
    },
    'plan_preventivo': {'m2oRecursoId': 'recurso_id'},
    'resultado': {},
    'tarea': {'m2oOrdenTrabajoId': 'orden_trabajo_id'},
    'tipo_incidencia': {},
}


def renombrar_tabla(cr, tabla_anterior, tabla_nueva, campos):
    cr.execute('SELECT to_regclass(%s)', [tabla_anterior])
    if not cr.fetchone()[0]:
        return

    cr.execute(sql.SQL('ALTER TABLE {} RENAME TO {}').format(
        sql.Identifier(tabla_anterior), sql.Identifier(tabla_nueva),
    ))
    for anterior, nuevo in campos.items():
        if not anterior.startswith('m2o'):
            continue  # One2many no tiene columna propia.
        cr.execute(sql.SQL('ALTER TABLE {} RENAME COLUMN {} TO {}').format(
            sql.Identifier(tabla_nueva), sql.Identifier(anterior), sql.Identifier(nuevo),
        ))
        cr.execute(sql.SQL('ALTER INDEX IF EXISTS {} RENAME TO {}').format(
            sql.Identifier(make_identifier(f'{tabla_anterior}__{anterior}_index')),
            sql.Identifier(make_identifier(f'{tabla_nueva}__{nuevo}_index')),
        ))

    cr.execute('SELECT conname FROM pg_constraint WHERE conrelid = %s::regclass', [tabla_nueva])
    for (restriccion,) in cr.fetchall():
        if not restriccion.startswith(tabla_anterior + '_'):
            continue
        sufijo = restriccion[len(tabla_anterior):]
        for anterior, nuevo in campos.items():
            sufijo = sufijo.replace(anterior, nuevo)
        nombre = make_identifier(tabla_nueva + sufijo)
        cr.execute(sql.SQL('ALTER TABLE {} RENAME CONSTRAINT {} TO {}').format(
            sql.Identifier(tabla_nueva), sql.Identifier(restriccion), sql.Identifier(nombre),
        ))
        cr.execute('UPDATE ir_model_constraint SET name = %s WHERE name = %s', [nombre, restriccion])
        cr.execute(
            "UPDATE ir_model_data SET name = %s WHERE module = 'upopark' AND name = %s",
            ['constraint_' + nombre, 'constraint_' + restriccion],
        )

    cr.execute(sql.SQL('ALTER SEQUENCE IF EXISTS {} RENAME TO {}').format(
        sql.Identifier(f'{tabla_anterior}_id_seq'), sql.Identifier(f'{tabla_nueva}_id_seq'),
    ))


def migrate(cr, version):
    campos_relacionales = {anterior: nuevo for campos in RENOMBRES.values() for anterior, nuevo in campos.items()}
    for entidad, campos in RENOMBRES.items():
        anterior = 'upopark.mantenimiento.' + entidad
        nuevo = 'upopark.' + entidad
        tabla_anterior = anterior.replace('.', '_')
        tabla_nueva = nuevo.replace('.', '_')
        renombrar_tabla(cr, tabla_anterior, tabla_nueva, campos)

        for campo_anterior, campo_nuevo in campos.items():
            cr.execute('UPDATE ir_model_fields SET name = %s WHERE model = %s AND name = %s',
                       [campo_nuevo, anterior, campo_anterior])
            cr.execute('UPDATE ir_model_fields SET relation_field = %s WHERE relation = %s AND relation_field = %s',
                       [campo_nuevo, anterior, campo_anterior])

        # Mantener los registros de metadatos para conservar los permisos y referencias existentes.
        for tabla, columna in (
            ('ir_model', 'model'), ('ir_model_fields', 'model'), ('ir_model_fields', 'relation'),
            ('ir_model_data', 'model'), ('ir_ui_view', 'model'), ('ir_act_window', 'res_model'),
            ('ir_act_server', 'model_name'), ('ir_attachment', 'res_model'),
            ('ir_exports', 'resource'), ('ir_filters', 'model_id'), ('ir_sequence', 'code'),
        ):
            identificador = sql.Identifier(columna)
            cr.execute(sql.SQL('UPDATE {} SET {} = %s WHERE {} = %s').format(
                sql.Identifier(tabla), identificador, identificador,
            ), [nuevo, anterior])

        cr.execute("UPDATE ir_model_data SET name = %s WHERE module = 'upopark' AND name = %s",
                   ['model_' + tabla_nueva, 'model_' + tabla_anterior])
        prefijo_anterior = f'field_{tabla_anterior}__'
        prefijo_nuevo = f'field_{tabla_nueva}__'
        cr.execute(
            "SELECT id, name FROM ir_model_data WHERE module = 'upopark' "
            "AND model = 'ir.model.fields' AND starts_with(name, %s)", [prefijo_anterior],
        )
        for registro_id, nombre in cr.fetchall():
            campo = nombre[len(prefijo_anterior):]
            cr.execute('UPDATE ir_model_data SET name = %s WHERE id = %s',
                       [prefijo_nuevo + campos.get(campo, campo), registro_id])

        for campo_anterior, campo_nuevo in campos_relacionales.items():
            cr.execute(
                "UPDATE ir_filters SET domain = replace(domain, %(anterior)s, %(nuevo)s), "
                "context = replace(context, %(anterior)s, %(nuevo)s), "
                "sort = replace(sort, %(anterior)s, %(nuevo)s) WHERE model_id = %(modelo)s "
                "AND (strpos(domain, %(anterior)s) > 0 OR strpos(context, %(anterior)s) > 0 "
                "OR strpos(sort, %(anterior)s) > 0)",
                {'anterior': campo_anterior, 'nuevo': campo_nuevo, 'modelo': nuevo},
            )
            cr.execute(
                "UPDATE ir_exports_line AS linea SET name = replace(linea.name, %s, %s) "
                "FROM ir_exports AS plantilla WHERE plantilla.id = linea.export_id "
                "AND plantilla.resource = %s AND strpos(linea.name, %s) > 0",
                [campo_anterior, campo_nuevo, nuevo, campo_anterior],
            )
