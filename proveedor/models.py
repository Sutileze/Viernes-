from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.templatetags.static import static


# ==================== CHOICES GEOGRÁFICAS SIMPLIFICADAS ====================

PAISES_CHOICES = [
    ('', 'Selecciona un país'),
    ('CL', 'Chile'),
]

# usuarios/choices.py
REGIONES_CHOICES = [
    ('', 'Selecciona una región'),
    ('CL-AP', 'Región de Arica y Parinacota'),
    ('CL-TA', 'Región de Tarapacá'),
    ('CL-AN', 'Región de Antofagasta'),
    ('CL-AT', 'Región de Atacama'),
    ('CL-CO', 'Región de Coquimbo'),
    ('CL-VS', 'Región de Valparaíso'),
    ('CL-RM', 'Región Metropolitana de Santiago'),
    ('CL-LI', 'Región del Libertador General Bernardo O\'Higgins'),
    ('CL-ML', 'Región del Maule'),
    ('CL-NB', 'Región de Ñuble'),
    ('CL-BI', 'Región del Biobío'),
    ('CL-AR', 'Región de La Araucanía'),
    ('CL-LR', 'Región de Los Ríos'),
    ('CL-LL', 'Región de Los Lagos'),
    ('CL-AI', 'Región Aysén del General Carlos Ibáñez del Campo'),
    ('CL-MA', 'Región de Magallanes y de la Antártica Chilena'),
]

COMUNAS_CHOICES = [
    ('', 'Selecciona una comuna'),
    
    # Región de Arica y Parinacota
    ('AP-Arica', 'Arica'),
    ('AP-Camarones', 'Camarones'),
    ('AP-Putre', 'Putre'),
    ('AP-General-Lagos', 'General Lagos'),
    
    # Región de Tarapacá
    ('TA-Iquique', 'Iquique'),
    ('TA-Alto-Hospicio', 'Alto Hospicio'),
    ('TA-Pozo-Almonte', 'Pozo Almonte'),
    ('TA-Camina', 'Camiña'),
    ('TA-Colchane', 'Colchane'),
    ('TA-Huara', 'Huara'),
    ('TA-Pica', 'Pica'),
    
    # Región de Antofagasta
    ('AN-Antofagasta', 'Antofagasta'),
    ('AN-Mejillones', 'Mejillones'),
    ('AN-Sierra-Gorda', 'Sierra Gorda'),
    ('AN-Taltal', 'Taltal'),
    ('AN-Calama', 'Calama'),
    ('AN-Ollague', 'Ollagüe'),
    ('AN-San-Pedro-de-Atacama', 'San Pedro de Atacama'),
    ('AN-Tocopilla', 'Tocopilla'),
    ('AN-Maria-Elena', 'María Elena'),
    
    # Región de Atacama
    ('AT-Copiapo', 'Copiapó'),
    ('AT-Caldera', 'Caldera'),
    ('AT-Tierra-Amarilla', 'Tierra Amarilla'),
    ('AT-Chanaral', 'Chañaral'),
    ('AT-Diego-de-Almagro', 'Diego de Almagro'),
    ('AT-Vallenar', 'Vallenar'),
    ('AT-Alto-del-Carmen', 'Alto del Carmen'),
    ('AT-Freirina', 'Freirina'),
    ('AT-Huasco', 'Huasco'),
    
    # Región de Coquimbo
    ('CO-La-Serena', 'La Serena'),
    ('CO-Coquimbo', 'Coquimbo'),
    ('CO-Andacollo', 'Andacollo'),
    ('CO-La-Higuera', 'La Higuera'),
    ('CO-Paihuano', 'Paiguano'),
    ('CO-Vicuna', 'Vicuña'),
    ('CO-Illapel', 'Illapel'),
    ('CO-Canela', 'Canela'),
    ('CO-Los-Vilos', 'Los Vilos'),
    ('CO-Salamanca', 'Salamanca'),
    ('CO-Ovalle', 'Ovalle'),
    ('CO-Combarbala', 'Combarbalá'),
    ('CO-Monte-Patria', 'Monte Patria'),
    ('CO-Punitaqui', 'Punitaqui'),
    ('CO-Rio-Hurtado', 'Río Hurtado'),
    
    # Región de Valparaíso
    ('VS-Valparaiso', 'Valparaíso'),
    ('VS-Casablanca', 'Casablanca'),
    ('VS-Concon', 'Concón'),
    ('VS-Juan-Fernandez', 'Juan Fernández'),
    ('VS-Puchuncavi', 'Puchuncaví'),
    ('VS-Quintero', 'Quintero'),
    ('VS-Vina-del-Mar', 'Viña del Mar'),
    ('VS-Isla-de-Pascua', 'Isla de Pascua'),
    ('VS-Los-Andes', 'Los Andes'),
    ('VS-Calle-Larga', 'Calle Larga'),
    ('VS-Rinconada', 'Rinconada'),
    ('VS-San-Esteban', 'San Esteban'),
    ('VS-La-Ligua', 'La Ligua'),
    ('VS-Cabildo', 'Cabildo'),
    ('VS-Papudo', 'Papudo'),
    ('VS-Petorca', 'Petorca'),
    ('VS-Zapallar', 'Zapallar'),
    ('VS-Quillota', 'Quillota'),
    ('VS-Calera', 'Calera'),
    ('VS-Hijuelas', 'Hijuelas'),
    ('VS-La-Cruz', 'La Cruz'),
    ('VS-Nogales', 'Nogales'),
    ('VS-San-Antonio', 'San Antonio'),
    ('VS-Algarrobo', 'Algarrobo'),
    ('VS-Cartagena', 'Cartagena'),
    ('VS-El-Quisco', 'El Quisco'),
    ('VS-El-Tabo', 'El Tabo'),
    ('VS-Santo-Domingo', 'Santo Domingo'),
    ('VS-San-Felipe', 'San Felipe'),
    ('VS-Catemu', 'Catemu'),
    ('VS-Llaillay', 'Llaillay'),
    ('VS-Panquehue', 'Panquehue'),
    ('VS-Putaendo', 'Putaendo'),
    ('VS-Santa-Maria', 'Santa María'),
    ('VS-Quilpue', 'Quilpué'),
    ('VS-Limache', 'Limache'),
    ('VS-Olmue', 'Olmué'),
    ('VS-Villa-Alemana', 'Villa Alemana'),
    
    # Región Metropolitana de Santiago
    ('RM-Santiago', 'Santiago'),
    ('RM-Cerrillos', 'Cerrillos'),
    ('RM-Cerro-Navia', 'Cerro Navia'),
    ('RM-Conchali', 'Conchalí'),
    ('RM-El-Bosque', 'El Bosque'),
    ('RM-Estacion-Central', 'Estación Central'),
    ('RM-Huechuraba', 'Huechuraba'),
    ('RM-Independencia', 'Independencia'),
    ('RM-La-Cisterna', 'La Cisterna'),
    ('RM-La-Florida', 'La Florida'),
    ('RM-La-Granja', 'La Granja'),
    ('RM-La-Pintana', 'La Pintana'),
    ('RM-La-Reina', 'La Reina'),
    ('RM-Las-Condes', 'Las Condes'),
    ('RM-Lo-Barnechea', 'Lo Barnechea'),
    ('RM-Lo-Espejo', 'Lo Espejo'),
    ('RM-Lo-Prado', 'Lo Prado'),
    ('RM-Macul', 'Macul'),
    ('RM-Maipu', 'Maipú'),
    ('RM-Nunoa', 'Ñuñoa'),
    ('RM-Pedro-Aguirre-Cerda', 'Pedro Aguirre Cerda'),
    ('RM-Penalolen', 'Peñalolén'),
    ('RM-Providencia', 'Providencia'),
    ('RM-Pudahuel', 'Pudahuel'),
    ('RM-Quilicura', 'Quilicura'),
    ('RM-Quinta-Normal', 'Quinta Normal'),
    ('RM-Recoleta', 'Recoleta'),
    ('RM-Renca', 'Renca'),
    ('RM-San-Joaquin', 'San Joaquín'),
    ('RM-San-Miguel', 'San Miguel'),
    ('RM-San-Ramon', 'San Ramón'),
    ('RM-Vitacura', 'Vitacura'),
    ('RM-Puente-Alto', 'Puente Alto'),
    ('RM-Pirque', 'Pirque'),
    ('RM-San-Jose-de-Maipo', 'San José de Maipo'),
    ('RM-Colina', 'Colina'),
    ('RM-Lampa', 'Lampa'),
    ('RM-Tiltil', 'Tiltil'),
    ('RM-San-Bernardo', 'San Bernardo'),
    ('RM-Buin', 'Buin'),
    ('RM-Calera-de-Tango', 'Calera de Tango'),
    ('RM-Paine', 'Paine'),
    ('RM-Melipilla', 'Melipilla'),
    ('RM-Alhue', 'Alhué'),
    ('RM-Curacavi', 'Curacaví'),
    ('RM-Maria-Pinto', 'María Pinto'),
    ('RM-San-Pedro', 'San Pedro'),
    ('RM-Talagante', 'Talagante'),
    ('RM-El-Monte', 'El Monte'),
    ('RM-Isla-de-Maipo', 'Isla de Maipo'),
    ('RM-Padre-Hurtado', 'Padre Hurtado'),
    ('RM-Penaflor', 'Peñaflor'),
    
    # Región del Libertador General Bernardo O'Higgins
    ('LI-Rancagua', 'Rancagua'),
    ('LI-Codegua', 'Codegua'),
    ('LI-Coinco', 'Coinco'),
    ('LI-Coltauco', 'Coltauco'),
    ('LI-Donihue', 'Doñihue'),
    ('LI-Graneros', 'Graneros'),
    ('LI-Las-Cabras', 'Las Cabras'),
    ('LI-Machali', 'Machalí'),
    ('LI-Malloa', 'Malloa'),
    ('LI-Mostazal', 'Mostazal'),
    ('LI-Olivar', 'Olivar'),
    ('LI-Peumo', 'Peumo'),
    ('LI-Pichidegua', 'Pichidegua'),
    ('LI-Quinta-de-Tilcoco', 'Quinta de Tilcoco'),
    ('LI-Rengo', 'Rengo'),
    ('LI-Requinoa', 'Requínoa'),
    ('LI-San-Vicente', 'San Vicente'),
    ('LI-Pichilemu', 'Pichilemu'),
    ('LI-La-Estrella', 'La Estrella'),
    ('LI-Litueche', 'Litueche'),
    ('LI-Marchihue', 'Marchihue'),
    ('LI-Navidad', 'Navidad'),
    ('LI-Paredones', 'Paredones'),
    ('LI-San-Fernando', 'San Fernando'),
    ('LI-Chepica', 'Chépica'),
    ('LI-Chimbarongo', 'Chimbarongo'),
    ('LI-Lolol', 'Lolol'),
    ('LI-Nancagua', 'Nancagua'),
    ('LI-Palmilla', 'Palmilla'),
    ('LI-Peralillo', 'Peralillo'),
    ('LI-Placilla', 'Placilla'),
    ('LI-Pumanque', 'Pumanque'),
    ('LI-Santa-Cruz', 'Santa Cruz'),
    
    # Región del Maule
    ('ML-Talca', 'Talca'),
    ('ML-Constitucion', 'Constitución'),
    ('ML-Curepto', 'Curepto'),
    ('ML-Empedrado', 'Empedrado'),
    ('ML-Maule', 'Maule'),
    ('ML-Pelarco', 'Pelarco'),
    ('ML-Pencahue', 'Pencahue'),
    ('ML-Rio-Claro', 'Río Claro'),
    ('ML-San-Clemente', 'San Clemente'),
    ('ML-San-Rafael', 'San Rafael'),
    ('ML-Cauquenes', 'Cauquenes'),
    ('ML-Chanco', 'Chanco'),
    ('ML-Pelluhue', 'Pelluhue'),
    ('ML-Curico', 'Curicó'),
    ('ML-Hualane', 'Hualañé'),
    ('ML-Licanten', 'Licantén'),
    ('ML-Molina', 'Molina'),
    ('ML-Rauco', 'Rauco'),
    ('ML-Romeral', 'Romeral'),
    ('ML-Sagrada-Familia', 'Sagrada Familia'),
    ('ML-Teno', 'Teno'),
    ('ML-Vichuquen', 'Vichuquén'),
    ('ML-Linares', 'Linares'),
    ('ML-Colbun', 'Colbún'),
    ('ML-Longavi', 'Longaví'),
    ('ML-Parral', 'Parral'),
    ('ML-Retiro', 'Retiro'),
    ('ML-San-Javier', 'San Javier'),
    ('ML-Villa-Alegre', 'Villa Alegre'),
    ('ML-Yerbas-Buenas', 'Yerbas Buenas'),
    
    # Región de Ñuble
    ('NB-Chillan', 'Chillán'),
    ('NB-Bulnes', 'Bulnes'),
    ('NB-Cobquecura', 'Cobquecura'),
    ('NB-Coelemu', 'Coelemu'),
    ('NB-Coihueco', 'Coihueco'),
    ('NB-Chillan-Viejo', 'Chillán Viejo'),
    ('NB-El-Carmen', 'El Carmen'),
    ('NB-Ninhue', 'Ninhue'),
    ('NB-Niquen', 'Ñiquén'),
    ('NB-Pemuco', 'Pemuco'),
    ('NB-Pinto', 'Pinto'),
    ('NB-Portezuelo', 'Portezuelo'),
    ('NB-Quillon', 'Quillón'),
    ('NB-Quirihue', 'Quirihue'),
    ('NB-Ranquil', 'Ránquil'),
    ('NB-San-Carlos', 'San Carlos'),
    ('NB-San-Fabian', 'San Fabián'),
    ('NB-San-Ignacio', 'San Ignacio'),
    ('NB-San-Nicolas', 'San Nicolás'),
    ('NB-Trehuaco', 'Trehuaco'),
    ('NB-Yungay', 'Yungay'),
    
    # Región del Biobío
    ('BI-Concepcion', 'Concepción'),
    ('BI-Coronel', 'Coronel'),
    ('BI-Chiguayante', 'Chiguayante'),
    ('BI-Florida', 'Florida'),
    ('BI-Hualqui', 'Hualqui'),
    ('BI-Lota', 'Lota'),
    ('BI-Penco', 'Penco'),
    ('BI-San-Pedro-de-la-Paz', 'San Pedro de la Paz'),
    ('BI-Santa-Juana', 'Santa Juana'),
    ('BI-Talcahuano', 'Talcahuano'),
    ('BI-Tome', 'Tomé'),
    ('BI-Hualpen', 'Hualpén'),
    ('BI-Lebu', 'Lebu'),
    ('BI-Arauco', 'Arauco'),
    ('BI-Canete', 'Cañete'),
    ('BI-Contulmo', 'Contulmo'),
    ('BI-Curanilahue', 'Curanilahue'),
    ('BI-Los-Alamos', 'Los Álamos'),
    ('BI-Tirua', 'Tirúa'),
    ('BI-Los-Angeles', 'Los Ángeles'),
    ('BI-Antuco', 'Antuco'),
    ('BI-Cabrero', 'Cabrero'),
    ('BI-Laja', 'Laja'),
    ('BI-Mulchen', 'Mulchén'),
    ('BI-Nacimiento', 'Nacimiento'),
    ('BI-Negrete', 'Negrete'),
    ('BI-Quilaco', 'Quilaco'),
    ('BI-Quilleco', 'Quilleco'),
    ('BI-San-Rosendo', 'San Rosendo'),
    ('BI-Santa-Barbara', 'Santa Bárbara'),
    ('BI-Tucapel', 'Tucapel'),
    ('BI-Yumbel', 'Yumbel'),
    ('BI-Alto-Biobio', 'Alto Biobío'),
    
    # Región de La Araucanía
    ('AR-Temuco', 'Temuco'),
    ('AR-Carahue', 'Carahue'),
    ('AR-Cunco', 'Cunco'),
    ('AR-Curarrehue', 'Curarrehue'),
    ('AR-Freire', 'Freire'),
    ('AR-Galvarino', 'Galvarino'),
    ('AR-Gorbea', 'Gorbea'),
    ('AR-Lautaro', 'Lautaro'),
    ('AR-Loncoche', 'Loncoche'),
    ('AR-Melipeuco', 'Melipeuco'),
    ('AR-Nueva-Imperial', 'Nueva Imperial'),
    ('AR-Padre-Las-Casas', 'Padre Las Casas'),
    ('AR-Perquenco', 'Perquenco'),
    ('AR-Pitrufquen', 'Pitrufquén'),
    ('AR-Pucon', 'Pucón'),
    ('AR-Saavedra', 'Saavedra'),
    ('AR-Teodoro-Schmidt', 'Teodoro Schmidt'),
    ('AR-Tolten', 'Toltén'),
    ('AR-Vilcun', 'Vilcún'),
    ('AR-Villarrica', 'Villarrica'),
    ('AR-Cholchol', 'Cholchol'),
    ('AR-Angol', 'Angol'),
    ('AR-Collipulli', 'Collipulli'),
    ('AR-Curacautin', 'Curacautín'),
    ('AR-Ercilla', 'Ercilla'),
    ('AR-Lonquimay', 'Lonquimay'),
    ('AR-Los-Sauces', 'Los Sauces'),
    ('AR-Lumaco', 'Lumaco'),
    ('AR-Puren', 'Purén'),
    ('AR-Renaico', 'Renaico'),
    ('AR-Traiguen', 'Traiguén'),
    ('AR-Victoria', 'Victoria'),
    
    # Región de Los Ríos
    ('LR-Valdivia', 'Valdivia'),
    ('LR-Corral', 'Corral'),
    ('LR-Lanco', 'Lanco'),
    ('LR-Los-Lagos', 'Los Lagos'),
    ('LR-Mafil', 'Máfil'),
    ('LR-Mariquina', 'Mariquina'),
    ('LR-Paillaco', 'Paillaco'),
    ('LR-Panguipulli', 'Panguipulli'),
    ('LR-La-Union', 'La Unión'),
    ('LR-Futrono', 'Futrono'),
    ('LR-Lago-Ranco', 'Lago Ranco'),
    ('LR-Rio-Bueno', 'Río Bueno'),
    
    # Región de Los Lagos
    ('LL-Puerto-Montt', 'Puerto Montt'),
    ('LL-Calbuco', 'Calbuco'),
    ('LL-Cochamo', 'Cochamó'),
    ('LL-Fresia', 'Fresia'),
    ('LL-Frutillar', 'Frutillar'),
    ('LL-Los-Muermos', 'Los Muermos'),
    ('LL-Llanquihue', 'Llanquihue'),
    ('LL-Maullin', 'Maullín'),
    ('LL-Puerto-Varas', 'Puerto Varas'),
    ('LL-Castro', 'Castro'),
    ('LL-Ancud', 'Ancud'),
    ('LL-Chonchi', 'Chonchi'),
    ('LL-Curaco-de-Velez', 'Curaco de Vélez'),
    ('LL-Dalcahue', 'Dalcahue'),
    ('LL-Puqueldon', 'Puqueldón'),
    ('LL-Queilen', 'Queilén'),
    ('LL-Quellon', 'Quellón'),
    ('LL-Quemalchi', 'Quemchi'),
    ('LL-Quinchao', 'Quinchao'),
    ('LL-Osorno', 'Osorno'),
    ('LL-Puerto-Octay', 'Puerto Octay'),
    ('LL-Purranque', 'Purranque'),
    ('LL-Puyehue', 'Puyehue'),
    ('LL-Rio-Negro', 'Río Negro'),
    ('LL-San-Juan-de-la-Costa', 'San Juan de la Costa'),
    ('LL-San-Pablo', 'San Pablo'),
    ('LL-Chaiten', 'Chaitén'),
    ('LL-Futaleufu', 'Futaleufú'),
    ('LL-Hualaihue', 'Hualaihué'),
    ('LL-Palena', 'Palena'),
    
    # Región Aysén del General Carlos Ibáñez del Campo
    ('AI-Coyhaique', 'Coyhaique'),
    ('AI-Lago-Verde', 'Lago Verde'),
    ('AI-Aysen', 'Aysén'),
    ('AI-Cisnes', 'Cisnes'),
    ('AI-Guaitecas', 'Guaitecas'),
    ('AI-Cochrane', 'Cochrane'),
    ('AI-OHiggins', 'O\'Higgins'),
    ('AI-Tortel', 'Tortel'),
    ('AI-Chile-Chico', 'Chile Chico'),
    ('AI-Rio-Ibanez', 'Río Ibáñez'),
    
    # Región de Magallanes y de la Antártica Chilena
    ('MA-Punta-Arenas', 'Punta Arenas'),
    ('MA-Laguna-Blanca', 'Laguna Blanca'),
    ('MA-Rio-Verde', 'Río Verde'),
    ('MA-San-Gregorio', 'San Gregorio'),
    ('MA-Cabo-de-Hornos', 'Cabo de Hornos'),
    ('MA-Antartica', 'Antártica'),
    ('MA-Porvenir', 'Porvenir'),
    ('MA-Primavera', 'Primavera'),
    ('MA-Timaukel', 'Timaukel'),
    ('MA-Natales', 'Natales'),
    ('MA-Torres-del-Paine', 'Torres del Paine'),
]

# Mapeo de regiones por país
REGIONES_POR_PAIS = {
    'CL': [
        ('CL-AP', 'Región de Arica y Parinacota'),
        ('CL-TA', 'Región de Tarapacá'),
        ('CL-AN', 'Región de Antofagasta'),
        ('CL-AT', 'Región de Atacama'),
        ('CL-CO', 'Región de Coquimbo'),
        ('CL-VS', 'Región de Valparaíso'),
        ('CL-RM', 'Región Metropolitana de Santiago'),
        ('CL-LI', 'Región del Libertador General Bernardo O\'Higgins'),
        ('CL-ML', 'Región del Maule'),
        ('CL-NB', 'Región de Ñuble'),
        ('CL-BI', 'Región del Biobío'),
        ('CL-AR', 'Región de La Araucanía'),
        ('CL-LR', 'Región de Los Ríos'),
        ('CL-LL', 'Región de Los Lagos'),
        ('CL-AI', 'Región Aysén del General Carlos Ibáñez del Campo'),
        ('CL-MA', 'Región de Magallanes y de la Antártica Chilena'),
    ],
}

# Mapeo de comunas por región
COMUNAS_POR_REGION = {
    'CL-AP': [
        ('AP-Arica', 'Arica'),
        ('AP-Camarones', 'Camarones'),
        ('AP-Putre', 'Putre'),
        ('AP-General-Lagos', 'General Lagos'),
    ],
    'CL-TA': [
        ('TA-Iquique', 'Iquique'),
        ('TA-Alto-Hospicio', 'Alto Hospicio'),
        ('TA-Pozo-Almonte', 'Pozo Almonte'),
        ('TA-Camina', 'Camiña'),
        ('TA-Colchane', 'Colchane'),
        ('TA-Huara', 'Huara'),
        ('TA-Pica', 'Pica'),
    ],
    'CL-AN': [
        ('AN-Antofagasta', 'Antofagasta'),
        ('AN-Mejillones', 'Mejillones'),
        ('AN-Sierra-Gorda', 'Sierra Gorda'),
        ('AN-Taltal', 'Taltal'),
        ('AN-Calama', 'Calama'),
        ('AN-Ollague', 'Ollagüe'),
        ('AN-San-Pedro-de-Atacama', 'San Pedro de Atacama'),
        ('AN-Tocopilla', 'Tocopilla'),
        ('AN-Maria-Elena', 'María Elena'),
    ],
    'CL-AT': [
        ('AT-Copiapo', 'Copiapó'),
        ('AT-Caldera', 'Caldera'),
        ('AT-Tierra-Amarilla', 'Tierra Amarilla'),
        ('AT-Chanaral', 'Chañaral'),
        ('AT-Diego-de-Almagro', 'Diego de Almagro'),
        ('AT-Vallenar', 'Vallenar'),
        ('AT-Alto-del-Carmen', 'Alto del Carmen'),
        ('AT-Freirina', 'Freirina'),
        ('AT-Huasco', 'Huasco'),
    ],
    'CL-CO': [
        ('CO-La-Serena', 'La Serena'),
        ('CO-Coquimbo', 'Coquimbo'),
        ('CO-Andacollo', 'Andacollo'),
        ('CO-La-Higuera', 'La Higuera'),
        ('CO-Paihuano', 'Paiguano'),
        ('CO-Vicuna', 'Vicuña'),
        ('CO-Illapel', 'Illapel'),
        ('CO-Canela', 'Canela'),
        ('CO-Los-Vilos', 'Los Vilos'),
        ('CO-Salamanca', 'Salamanca'),
        ('CO-Ovalle', 'Ovalle'),
        ('CO-Combarbala', 'Combarbalá'),
        ('CO-Monte-Patria', 'Monte Patria'),
        ('CO-Punitaqui', 'Punitaqui'),
        ('CO-Rio-Hurtado', 'Río Hurtado'),
    ],
    'CL-VS': [
        ('VS-Valparaiso', 'Valparaíso'),
        ('VS-Casablanca', 'Casablanca'),
        ('VS-Concon', 'Concón'),
        ('VS-Juan-Fernandez', 'Juan Fernández'),
        ('VS-Puchuncavi', 'Puchuncaví'),
        ('VS-Quintero', 'Quintero'),
        ('VS-Vina-del-Mar', 'Viña del Mar'),
        ('VS-Isla-de-Pascua', 'Isla de Pascua'),
        ('VS-Los-Andes', 'Los Andes'),
        ('VS-Calle-Larga', 'Calle Larga'),
        ('VS-Rinconada', 'Rinconada'),
        ('VS-San-Esteban', 'San Esteban'),
        ('VS-La-Ligua', 'La Ligua'),
        ('VS-Cabildo', 'Cabildo'),
        ('VS-Papudo', 'Papudo'),
        ('VS-Petorca', 'Petorca'),
        ('VS-Zapallar', 'Zapallar'),
        ('VS-Quillota', 'Quillota'),
        ('VS-Calera', 'Calera'),
        ('VS-Hijuelas', 'Hijuelas'),
        ('VS-La-Cruz', 'La Cruz'),
        ('VS-Nogales', 'Nogales'),
        ('VS-San-Antonio', 'San Antonio'),
        ('VS-Algarrobo', 'Algarrobo'),
        ('VS-Cartagena', 'Cartagena'),
        ('VS-El-Quisco', 'El Quisco'),
        ('VS-El-Tabo', 'El Tabo'),
        ('VS-Santo-Domingo', 'Santo Domingo'),
        ('VS-San-Felipe', 'San Felipe'),
        ('VS-Catemu', 'Catemu'),
        ('VS-Llaillay', 'Llaillay'),
        ('VS-Panquehue', 'Panquehue'),
        ('VS-Putaendo', 'Putaendo'),
        ('VS-Santa-Maria', 'Santa María'),
        ('VS-Quilpue', 'Quilpué'),
        ('VS-Limache', 'Limache'),
        ('VS-Olmue', 'Olmué'),
        ('VS-Villa-Alemana', 'Villa Alemana'),
    ],
    'CL-RM': [
        ('RM-Santiago', 'Santiago'),
        ('RM-Cerrillos', 'Cerrillos'),
        ('RM-Cerro-Navia', 'Cerro Navia'),
        ('RM-Conchali', 'Conchalí'),
        ('RM-El-Bosque', 'El Bosque'),
        ('RM-Estacion-Central', 'Estación Central'),
        ('RM-Huechuraba', 'Huechuraba'),
        ('RM-Independencia', 'Independencia'),
        ('RM-La-Cisterna', 'La Cisterna'),
        ('RM-La-Florida', 'La Florida'),
        ('RM-La-Granja', 'La Granja'),
        ('RM-La-Pintana', 'La Pintana'),
        ('RM-La-Reina', 'La Reina'),
        ('RM-Las-Condes', 'Las Condes'),
        ('RM-Lo-Barnechea', 'Lo Barnechea'),
        ('RM-Lo-Espejo', 'Lo Espejo'),
        ('RM-Lo-Prado', 'Lo Prado'),
        ('RM-Macul', 'Macul'),
        ('RM-Maipu', 'Maipú'),
        ('RM-Nunoa', 'Ñuñoa'),
        ('RM-Pedro-Aguirre-Cerda', 'Pedro Aguirre Cerda'),
        ('RM-Penalolen', 'Peñalolén'),
        ('RM-Providencia', 'Providencia'),
        ('RM-Pudahuel', 'Pudahuel'),
        ('RM-Quilicura', 'Quilicura'),
        ('RM-Quinta-Normal', 'Quinta Normal'),
        ('RM-Recoleta', 'Recoleta'),
        ('RM-Renca', 'Renca'),
        ('RM-San-Joaquin', 'San Joaquín'),
        ('RM-San-Miguel', 'San Miguel'),
        ('RM-San-Ramon', 'San Ramón'),
        ('RM-Vitacura', 'Vitacura'),
        ('RM-Puente-Alto', 'Puente Alto'),
        ('RM-Pirque', 'Pirque'),
        ('RM-San-Jose-de-Maipo', 'San José de Maipo'),
        ('RM-Colina', 'Colina'),
        ('RM-Lampa', 'Lampa'),
        ('RM-Tiltil', 'Tiltil'),
        ('RM-San-Bernardo', 'San Bernardo'),
        ('RM-Buin', 'Buin'),
        ('RM-Calera-de-Tango', 'Calera de Tango'),
        ('RM-Paine', 'Paine'),
        ('RM-Melipilla', 'Melipilla'),
        ('RM-Alhue', 'Alhué'),
        ('RM-Curacavi', 'Curacaví'),
        ('RM-Maria-Pinto', 'María Pinto'),
        ('RM-San-Pedro', 'San Pedro'),
        ('RM-Talagante', 'Talagante'),
        ('RM-El-Monte', 'El Monte'),
        ('RM-Isla-de-Maipo', 'Isla de Maipo'),
        ('RM-Padre-Hurtado', 'Padre Hurtado'),
        ('RM-Penaflor', 'Peñaflor'),
    ],
    'CL-LI': [
        ('LI-Rancagua', 'Rancagua'),
        ('LI-Codegua', 'Codegua'),
        ('LI-Coinco', 'Coinco'),
        ('LI-Coltauco', 'Coltauco'),
        ('LI-Donihue', 'Doñihue'),
        ('LI-Graneros', 'Graneros'),
        ('LI-Las-Cabras', 'Las Cabras'),
        ('LI-Machali', 'Machalí'),
        ('LI-Malloa', 'Malloa'),
        ('LI-Mostazal', 'Mostazal'),
        ('LI-Olivar', 'Olivar'),
        ('LI-Peumo', 'Peumo'),
        ('LI-Pichidegua', 'Pichidegua'),
        ('LI-Quinta-de-Tilcoco', 'Quinta de Tilcoco'),
        ('LI-Rengo', 'Rengo'),
        ('LI-Requinoa', 'Requínoa'),
        ('LI-San-Vicente', 'San Vicente'),
        ('LI-Pichilemu', 'Pichilemu'),
        ('LI-La-Estrella', 'La Estrella'),
        ('LI-Litueche', 'Litueche'),
        ('LI-Marchihue', 'Marchihue'),
        ('LI-Navidad', 'Navidad'),
        ('LI-Paredones', 'Paredones'),
        ('LI-San-Fernando', 'San Fernando'),
        ('LI-Chepica', 'Chépica'),
        ('LI-Chimbarongo', 'Chimbarongo'),
        ('LI-Lolol', 'Lolol'),
        ('LI-Nancagua', 'Nancagua'),
        ('LI-Palmilla', 'Palmilla'),
        ('LI-Peralillo', 'Peralillo'),
        ('LI-Placilla', 'Placilla'),
        ('LI-Pumanque', 'Pumanque'),
        ('LI-Santa-Cruz', 'Santa Cruz'),
    ],
    'CL-ML': [
        ('ML-Talca', 'Talca'),
        ('ML-Constitucion', 'Constitución'),
        ('ML-Curepto', 'Curepto'),
        ('ML-Empedrado', 'Empedrado'),
        ('ML-Maule', 'Maule'),
        ('ML-Pelarco', 'Pelarco'),
        ('ML-Pencahue', 'Pencahue'),
        ('ML-Rio-Claro', 'Río Claro'),
        ('ML-San-Clemente', 'San Clemente'),
        ('ML-San-Rafael', 'San Rafael'),
        ('ML-Cauquenes', 'Cauquenes'),
        ('ML-Chanco', 'Chanco'),
        ('ML-Pelluhue', 'Pelluhue'),
        ('ML-Curico', 'Curicó'),
        ('ML-Hualane', 'Hualañé'),
        ('ML-Licanten', 'Licantén'),
        ('ML-Molina', 'Molina'),
        ('ML-Rauco', 'Rauco'),
        ('ML-Romeral', 'Romeral'),
        ('ML-Sagrada-Familia', 'Sagrada Familia'),
        ('ML-Teno', 'Teno'),
        ('ML-Vichuquen', 'Vichuquén'),
        ('ML-Linares', 'Linares'),
        ('ML-Colbun', 'Colbún'),
        ('ML-Longavi', 'Longaví'),
        ('ML-Parral', 'Parral'),
        ('ML-Retiro', 'Retiro'),
        ('ML-San-Javier', 'San Javier'),
        ('ML-Villa-Alegre', 'Villa Alegre'),
        ('ML-Yerbas-Buenas', 'Yerbas Buenas'),
    ],
    'CL-NB': [
        ('NB-Chillan', 'Chillán'),
        ('NB-Bulnes', 'Bulnes'),
        ('NB-Cobquecura', 'Cobquecura'),
        ('NB-Coelemu', 'Coelemu'),
        ('NB-Coihueco', 'Coihueco'),
        ('NB-Chillan-Viejo', 'Chillán Viejo'),
        ('NB-El-Carmen', 'El Carmen'),
        ('NB-Ninhue', 'Ninhue'),
        ('NB-Niquen', 'Ñiquén'),
        ('NB-Pemuco', 'Pemuco'),
        ('NB-Pinto', 'Pinto'),
        ('NB-Portezuelo', 'Portezuelo'),
        ('NB-Quillon', 'Quillón'),
        ('NB-Quirihue', 'Quirihue'),
        ('NB-Ranquil', 'Ránquil'),
        ('NB-San-Carlos', 'San Carlos'),
        ('NB-San-Fabian', 'San Fabián'),
        ('NB-San-Ignacio', 'San Ignacio'),
        ('NB-San-Nicolas', 'San Nicolás'),
        ('NB-Trehuaco', 'Trehuaco'),
        ('NB-Yungay', 'Yungay'),
    ],
    'CL-BI': [
        ('BI-Concepcion', 'Concepción'),
        ('BI-Coronel', 'Coronel'),
        ('BI-Chiguayante', 'Chiguayante'),
        ('BI-Florida', 'Florida'),
        ('BI-Hualqui', 'Hualqui'),
        ('BI-Lota', 'Lota'),
        ('BI-Penco', 'Penco'),
        ('BI-San-Pedro-de-la-Paz', 'San Pedro de la Paz'),
        ('BI-Santa-Juana', 'Santa Juana'),
        ('BI-Talcahuano', 'Talcahuano'),
        ('BI-Tome', 'Tomé'),
        ('BI-Hualpen', 'Hualpén'),
        ('BI-Lebu', 'Lebu'),
        ('BI-Arauco', 'Arauco'),
        ('BI-Canete', 'Cañete'),
        ('BI-Contulmo', 'Contulmo'),
        ('BI-Curanilahue', 'Curanilahue'),
        ('BI-Los-Alamos', 'Los Álamos'),
        ('BI-Tirua', 'Tirúa'),
        ('BI-Los-Angeles', 'Los Ángeles'),
        ('BI-Antuco', 'Antuco'),
        ('BI-Cabrero', 'Cabrero'),
        ('BI-Laja', 'Laja'),
        ('BI-Mulchen', 'Mulchén'),
        ('BI-Nacimiento', 'Nacimiento'),
        ('BI-Negrete', 'Negrete'),
        ('BI-Quilaco', 'Quilaco'),
        ('BI-Quilleco', 'Quilleco'),
        ('BI-San-Rosendo', 'San Rosendo'),
        ('BI-Santa-Barbara', 'Santa Bárbara'),
        ('BI-Tucapel', 'Tucapel'),
        ('BI-Yumbel', 'Yumbel'),
        ('BI-Alto-Biobio', 'Alto Biobío'),
    ],
    'CL-AR': [
        ('AR-Temuco', 'Temuco'),
        ('AR-Carahue', 'Carahue'),
        ('AR-Cunco', 'Cunco'),
        ('AR-Curarrehue', 'Curarrehue'),
        ('AR-Freire', 'Freire'),
        ('AR-Galvarino', 'Galvarino'),
        ('AR-Gorbea', 'Gorbea'),
        ('AR-Lautaro', 'Lautaro'),
        ('AR-Loncoche', 'Loncoche'),
        ('AR-Melipeuco', 'Melipeuco'),
        ('AR-Nueva-Imperial', 'Nueva Imperial'),
        ('AR-Padre-Las-Casas', 'Padre Las Casas'),
        ('AR-Perquenco', 'Perquenco'),
        ('AR-Pitrufquen', 'Pitrufquén'),
        ('AR-Pucon', 'Pucón'),
        ('AR-Saavedra', 'Saavedra'),
        ('AR-Teodoro-Schmidt', 'Teodoro Schmidt'),
        ('AR-Tolten', 'Toltén'),
        ('AR-Vilcun', 'Vilcún'),
        ('AR-Villarrica', 'Villarrica'),
        ('AR-Cholchol', 'Cholchol'),
        ('AR-Angol', 'Angol'),
        ('AR-Collipulli', 'Collipulli'),
        ('AR-Curacautin', 'Curacautín'),
        ('AR-Ercilla', 'Ercilla'),
        ('AR-Lonquimay', 'Lonquimay'),
        ('AR-Los-Sauces', 'Los Sauces'),
        ('AR-Lumaco', 'Lumaco'),
        ('AR-Puren', 'Purén'),
        ('AR-Renaico', 'Renaico'),
        ('AR-Traiguen', 'Traiguén'),
        ('AR-Victoria', 'Victoria'),
    ],
    'CL-LR': [
        ('LR-Valdivia', 'Valdivia'),
        ('LR-Corral', 'Corral'),
        ('LR-Lanco', 'Lanco'),
        ('LR-Los-Lagos', 'Los Lagos'),
        ('LR-Mafil', 'Máfil'),
        ('LR-Mariquina', 'Mariquina'),
        ('LR-Paillaco', 'Paillaco'),
        ('LR-Panguipulli', 'Panguipulli'),
        ('LR-La-Union', 'La Unión'),
        ('LR-Futrono', 'Futrono'),
        ('LR-Lago-Ranco', 'Lago Ranco'),
        ('LR-Rio-Bueno', 'Río Bueno'),
    ],
    'CL-LL': [
        ('LL-Puerto-Montt', 'Puerto Montt'),
        ('LL-Calbuco', 'Calbuco'),
        ('LL-Cochamo', 'Cochamó'),
        ('LL-Fresia', 'Fresia'),
        ('LL-Frutillar', 'Frutillar'),
        ('LL-Los-Muermos', 'Los Muermos'),
        ('LL-Llanquihue', 'Llanquihue'),
        ('LL-Maullin', 'Maullín'),
        ('LL-Puerto-Varas', 'Puerto Varas'),
        ('LL-Castro', 'Castro'),
        ('LL-Ancud', 'Ancud'),
        ('LL-Chonchi', 'Chonchi'),
        ('LL-Curaco-de-Velez', 'Curaco de Vélez'),
        ('LL-Dalcahue', 'Dalcahue'),
        ('LL-Puqueldon', 'Puqueldón'),
        ('LL-Queilen', 'Queilén'),
        ('LL-Quellon', 'Quellón'),
        ('LL-Quemalchi', 'Quemchi'),
        ('LL-Quinchao', 'Quinchao'),
        ('LL-Osorno', 'Osorno'),
        ('LL-Puerto-Octay', 'Puerto Octay'),
        ('LL-Purranque', 'Purranque'),
        ('LL-Puyehue', 'Puyehue'),
        ('LL-Rio-Negro', 'Río Negro'),
        ('LL-San-Juan-de-la-Costa', 'San Juan de la Costa'),
        ('LL-San-Pablo', 'San Pablo'),
        ('LL-Chaiten', 'Chaitén'),
        ('LL-Futaleufu', 'Futaleufú'),
        ('LL-Hualaihue', 'Hualaihué'),
        ('LL-Palena', 'Palena'),
    ],
    'CL-AI': [
        ('AI-Coyhaique', 'Coyhaique'),
        ('AI-Lago-Verde', 'Lago Verde'),
        ('AI-Aysen', 'Aysén'),
        ('AI-Cisnes', 'Cisnes'),
        ('AI-Guaitecas', 'Guaitecas'),
        ('AI-Cochrane', 'Cochrane'),
        ('AI-OHiggins', 'O\'Higgins'),
        ('AI-Tortel', 'Tortel'),
        ('AI-Chile-Chico', 'Chile Chico'),
        ('AI-Rio-Ibanez', 'Río Ibáñez'),
    ],
    'CL-MA': [
        ('MA-Punta-Arenas', 'Punta Arenas'),
        ('MA-Laguna-Blanca', 'Laguna Blanca'),
        ('MA-Rio-Verde', 'Río Verde'),
        ('MA-San-Gregorio', 'San Gregorio'),
        ('MA-Cabo-de-Hornos', 'Cabo de Hornos'),
        ('MA-Antartica', 'Antártica'),
        ('MA-Porvenir', 'Porvenir'),
        ('MA-Primavera', 'Primavera'),
        ('MA-Timaukel', 'Timaukel'),
        ('MA-Natales', 'Natales'),
        ('MA-Torres-del-Paine', 'Torres del Paine'),
    ],
}

# ==================== MODELOS ====================

class CategoriaProveedor(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    icono = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'categoria_proveedor'
        verbose_name = 'Categoría de Proveedor'
        verbose_name_plural = 'Categorías de Proveedores'
    
    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    # ✅ AUTENTICACIÓN PROPIA
    email = models.EmailField(unique=True, verbose_name='Correo electrónico')
    password_hash = models.CharField(max_length=128, verbose_name='Contraseña')
    nombre_contacto = models.CharField(max_length=200, verbose_name='Nombre de contacto')
    
    # Información básica
    nombre_empresa = models.CharField(max_length=200, verbose_name='Nombre de la Empresa')
    descripcion = models.TextField(verbose_name='Descripción del negocio')
    
    # Foto/Logo
    foto = models.ImageField(upload_to='proveedores/', blank=True, null=True, verbose_name='Logo/Foto')
    
    # Categorías (un proveedor puede ofrecer múltiples rubros)
    categorias = models.ManyToManyField(CategoriaProveedor, related_name='proveedores', blank=True, verbose_name='Rubros que oferta')
    
    # Ubicación geográfica (ahora como CHOICES)
    pais = models.CharField(max_length=2, choices=PAISES_CHOICES, blank=True, null=True, verbose_name='País')
    region = models.CharField(max_length=10, blank=True, null=True, verbose_name='Región')
    comuna = models.CharField(max_length=50, blank=True, null=True, verbose_name='Comuna')
    direccion = models.CharField(max_length=255, blank=True, null=True, verbose_name='Dirección')

    foto_perfil = models.ImageField(upload_to='proveedores/fotos/', blank=True, null=True)
    modo_oscuro = models.BooleanField(default=False)
    notif_email = models.BooleanField(default=True)
    notif_mensajes = models.BooleanField(default=True)
    notif_pedidos = models.BooleanField(default=True)
    idioma = models.CharField(max_length=5, default='es')
    zona_horaria = models.CharField(max_length=50, default='America/Santiago')
    perfil_publico = models.BooleanField(default=True)
    mostrar_estadisticas = models.BooleanField(default=True)
    
    # Zona geográfica de cobertura
    COBERTURA_CHOICES = [
        ('local', 'Local'),
        ('comunal', 'Comunal'),
        ('regional', 'Regional'),
        ('nacional', 'Nacional'),
        ('internacional', 'Internacional'),
    ]
    cobertura = models.CharField(max_length=20, choices=COBERTURA_CHOICES, default='local', verbose_name='Zona geográfica')
    
    # Datos de contacto
    telefono_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="El número de teléfono debe estar en formato: '+999999999'. Hasta 15 dígitos permitidos."
    )
    telefono = models.CharField(validators=[telefono_regex], max_length=17, blank=True, null=True)
    whatsapp = models.CharField(validators=[telefono_regex], max_length=17, verbose_name='WhatsApp')
    sitio_web = models.URLField(blank=True, null=True, verbose_name='Sitio web')
    
    # Redes sociales
    facebook = models.URLField(blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    
    # Estado y validación
    activo = models.BooleanField(default=True)
    verificado = models.BooleanField(default=False, verbose_name='Proveedor verificado')
    destacado = models.BooleanField(default=False, verbose_name='Proveedor destacado')
    
    # Estadísticas
    visitas = models.IntegerField(default=0)
    contactos_enviados = models.IntegerField(default=0, verbose_name='Solicitudes de contacto enviadas')
    contactos_aceptados = models.IntegerField(default=0, verbose_name='Contactos aceptados')
    
    # Metadatos
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    ultima_conexion = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['-fecha_registro']
    
    def __str__(self):
        return self.nombre_empresa
    
    def get_profile_picture_url(self):
        if self.foto_perfil and self.foto_perfil.name:
            return self.foto_perfil.url
        return static('img/default_profile.png')
    
    def get_pais_display_name(self):
        """Retorna el nombre completo del país"""
        for codigo, nombre in PAISES_CHOICES:
            if codigo == self.pais:
                return nombre
        return self.pais
    
    def get_region_display_name(self):
        """Retorna el nombre completo de la región"""
        for codigo, nombre in REGIONES_CHOICES:
            if codigo == self.region:
                return nombre
        return self.region
    
    def get_comuna_display_name(self):
        """Retorna el nombre completo de la comuna"""
        for codigo, nombre in COMUNAS_CHOICES:
            if codigo == self.comuna:
                return nombre
        return self.comuna
    
    def incrementar_visitas(self):
        self.visitas += 1
        self.save(update_fields=['visitas'])
    
    def tasa_aceptacion(self):
        """Calcula el porcentaje de contactos aceptados"""
        if self.contactos_enviados > 0:
            return (self.contactos_aceptados / self.contactos_enviados) * 100
        return 0
    
    def get_region_display_name(self):
        """Obtiene el nombre legible de la región"""
        for codigo, nombre in REGIONES_CHOICES:
            if codigo == self.region:
                return nombre
        return self.region
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


class SolicitudContacto(models.Model):
    """
    Modelo para gestionar las solicitudes de contacto de proveedores a comercios
    """
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='solicitudes_enviadas')
    mensaje = models.TextField(verbose_name='Mensaje de presentación')
    
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
        ('cancelada', 'Cancelada'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_respuesta = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'solicitud_contacto'
        verbose_name = 'Solicitud de Contacto'
        verbose_name_plural = 'Solicitudes de Contacto'
        ordering = ['-fecha_solicitud']
    
    def __str__(self):
        return f"{self.proveedor.nombre_empresa} - {self.estado}"
    
    def aceptar(self):
        self.estado = 'aceptada'
        self.fecha_respuesta = timezone.now()
        self.save()
        
        self.proveedor.contactos_aceptados += 1
        self.proveedor.save(update_fields=['contactos_aceptados'])
    
    def rechazar(self):
        self.estado = 'rechazada'
        self.fecha_respuesta = timezone.now()
        self.save()


class ProductoServicio(models.Model):
    """Productos o servicios que ofrece el proveedor"""
    
    CATEGORIA_CHOICES = (
        ('ALIMENTOS', 'Alimentos y Comida'),
        ('BEBIDAS', 'Bebidas y Licores'),
        ('ROPA', 'Ropa y Accesorios'),
        ('HOGAR', 'Artículos para el Hogar'),
        ('SERVICIOS', 'Servicios Profesionales'),
        ('OTRO', 'Otro / Varios'),
    )
    
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE, related_name='productos_servicios')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio_referencia = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    activo = models.BooleanField(default=True)
    destacado = models.BooleanField(default=False)
    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIA_CHOICES,
        default='OTRO',
        verbose_name='Categoría del Producto/Servicio'
    )
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'producto_servicio'
        verbose_name = 'Producto/Servicio'
        verbose_name_plural = 'Productos/Servicios'
    
    def __str__(self):
        return f"{self.nombre} - {self.proveedor.nombre_empresa}"


class Promocion(models.Model):
    """Promociones que publican los proveedores"""
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='promociones')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='promociones/', blank=True, null=True)
    
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    
    activo = models.BooleanField(default=True)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'promocion'
        verbose_name = 'Promoción'
        verbose_name_plural = 'Promociones'
        ordering = ['-fecha_inicio']
    
    def __str__(self):
        return self.titulo
    
    def esta_vigente(self):
        hoy = timezone.now().date()
        return self.fecha_inicio <= hoy <= self.fecha_fin and self.activo

class SolicitudProveedor(models.Model):
    """Solicitudes de comerciantes a proveedores"""
    
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
    ]
    
    comerciante = models.ForeignKey(
        'usuarios.Comerciante',
        on_delete=models.CASCADE,
        related_name='solicitudes_enviadas'
    )
    proveedor = models.ForeignKey(
        'proveedor.Proveedor',  # ← Cambiar de 'proveedores' a 'proveedor'
        on_delete=models.CASCADE,
        related_name='solicitudes_recibidas'
    )
    mensaje = models.TextField(blank=True, null=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='pendiente'
    )
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_respuesta = models.DateTimeField(blank=True, null=True)
    mensaje_respuesta = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Solicitud a Proveedor'
        verbose_name_plural = 'Solicitudes a Proveedores'
        ordering = ['-fecha_solicitud']
        unique_together = ['comerciante', 'proveedor']
    
    def __str__(self):
        return f'{self.comerciante.nombre_apellido} → {self.proveedor.nombre_empresa} ({self.estado})'
    
    def aceptar(self, mensaje_respuesta=''):
        """Acepta la solicitud"""
        self.estado = 'aceptada'
        self.fecha_respuesta = timezone.now()
        self.mensaje_respuesta = mensaje_respuesta
        self.save()
    
    def rechazar(self, mensaje_respuesta=''):
        """Rechaza la solicitud"""
        self.estado = 'rechazada'
        self.fecha_respuesta = timezone.now()
        self.mensaje_respuesta = mensaje_respuesta
        self.save()