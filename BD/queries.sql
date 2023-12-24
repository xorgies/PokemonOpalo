select count()
from Pokemon p, Pokemon_Estadisticas pe 
where p.id = pe.pokemon_id
and pe.atk>(select pe.atk 
    FROM Pokemon p, Pokemon_Estadisticas pe 
    where p.id = pe.pokemon_id
        and p.id = 900
    ORDER BY pe.atk DESC);

select p.name,pe.atk 
FROM Pokemon p, Pokemon_Estadisticas pe 
where p.id = pe.pokemon_id
ORDER BY pe.atk DESC;


-- Vistas
create view datos_pokemon_view AS
select p.*, pe.ps,pe.atk,pe.def,pe.spd,pe.atk_sp,pe.def_sp
FROM Pokemon p, Pokemon_Estadisticas pe
WHERE p.id=pe.pokemon_id;

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
select p.id,m.nombre,pm.nivel_aprender,m.nombre_esp,m.potencia,m.tipo,m.clase,m.precision,m.pp,m.descripcion
from Pokemon p,Pokemon_Movimientos pm,Movimientos m
where p.id = pm.pokemon_id
    and m.id = pm.movimiento_id;

create view pokemon_habilidades_view as
select p.id,h.nombre,ph.tipo,h.id as habilidad_id,h.nombre_esp,h.descripcion
from Pokemon p,Pokemon_Habilidades ph,Habilidades h
where p.id = ph.pokemon_id
    and h.id = ph.habilidad_id;

create view habilidad_pokemons_view as
select h.id,p.name,ph.tipo,p.id as pokemon_id
from Pokemon p,Pokemon_Habilidades ph,Habilidades h
where p.id = ph.pokemon_id
    and h.id = ph.habilidad_id;

create view movimiento_pokemons_view as
select m.id,p.name,pm.nivel_aprender,p.id as pokemon_id
from Pokemon p,Pokemon_Movimientos pm,Movimientos m
where p.id = pm.pokemon_id
    and m.id = pm.movimiento_id;

create view encuentros_lugares_view as
select e.id, e.pokemon_id, e.nombre, e.nivel_min, e.nivel_max, l.nombre as nombre_lugar from Encuentros e, Lugares l where e.lugar_id = l.id;

-- Maximo de cada estadistica
select max(pe.ps) as ps,max(pe.atk) as atk,max(pe.def) as def,max(pe.spd) as spd,max(pe.atk_sp) as atk_sp,max(pe.def_sp) as def_sp
FROM Pokemon_Estadisticas pe;

-- Maximo entre todos los maximos de las estadisticas
select max(
            max(pe.ps),
            max(pe.atk),
            max(pe.def),
            max(pe.spd),
            max(pe.atk_sp),
            max(pe.def_sp)
        )
FROM Pokemon_Estadisticas pe;