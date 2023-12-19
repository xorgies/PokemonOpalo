select count()
from Pokemon p, Pokemon_Estadisticas pe 
where p.id = pe.pokemon_id
and pe.atk>(select pe.atk 
    FROM Pokemon p, Pokemon_Estadisticas pe 
    where p.id = pe.pokemon_id
        and p.name = 'Kartana'
    ORDER BY pe.atk DESC);

select p.name,pe.atk 
FROM Pokemon p, Pokemon_Estadisticas pe 
where p.id = pe.pokemon_id
ORDER BY pe.atk DESC;


-- Vistas
create view datos_pokemon AS
select p.*, pe.ps,pe.atk,pe.def,pe.spd,pe.atk_sp,pe.def_sp,(select p2.name from Pokemon p2,Evoluciones e2 where p2.id = e.pokemon_evolucion_id and p.id = e2.pokemon_id) as nombre_evolucion,e.forma,e.descripcion
FROM Pokemon p, Pokemon_Estadisticas pe,Evoluciones e
WHERE p.id=pe.pokemon_id
    and e.pokemon_id = p.id;

create view evoluciones_view as
select p.id,p.name, e.pokemon_evolucion_id,p2.name as name_evolucion,e.forma,e.descripcion  
FROM Pokemon p, Evoluciones e, Pokemon p2
where p.id = e.pokemon_id
    and p2.id = e.pokemon_evolucion_id;

create view pokemon_tipos_view as
select p.id,t.nombre
from Pokemon p,Pokemon_Tipos pt,Tipos t
where p.id = pt.pokemon_id
    and t.id = pt.tipo_id;

create view pokemon_movimientos_view as
select p.id,m.nombre,pm.nivel_aprender
from Pokemon p,Pokemon_Movimientos pm,Movimientos m
where p.id = pm.pokemon_id
    and m.id = pm.movimiento_id;

create view pokemon_habilidades_view as
select p.id,h.nombre,ph.tipo
from Pokemon p,Pokemon_Habilidades ph,Habilidades h
where p.id = ph.pokemon_id
    and h.id = ph.habilidad_id;