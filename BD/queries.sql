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

create view datos_pokemon AS
select p.*, pe.ps,pe.atk,pe.def,pe.spd,pe.atk_sp,pe.def_sp,(select p2.name from Pokemon p2,Evoluciones e2 where p2.id = e.pokemon_evolucion_id and p.id = e2.pokemon_id) as nombre_evolucion,e.forma,e.descripcion
FROM Pokemon p, Pokemon_Estadisticas pe,Evoluciones e
WHERE p.id=pe.pokemon_id
    and e.pokemon_id = p.id;