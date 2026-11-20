"""Bilingual product copy grounded in Wing 1.3 native captures."""

FEATURES = {'es': [{'id': 'photo',
         'label': 'Identificar por foto',
         'title': 'Una foto.<br>Una nueva pista.',
         'intro': 'En Wing 1.3 podrás hacer una foto o elegir una de tu fototeca y consultar las especies sugeridas. '
                  'Compara sus rasgos y abre la ficha para conocer mejor el ave.',
         'details': [('Desde la cámara o tu fototeca',
                      'Elige una imagen donde el ave se vea con claridad. Revisa la foto antes de enviarla.'),
                     ('Compara las coincidencias',
                      'Consulta las posibles especies y contrasta el plumaje, la forma y el contexto. La sugerencia no '
                      'confirma por sí sola una identificación.'),
                     ('Conserva el encuentro', 'Abre la ficha de la especie y guarda el avistamiento en tu diario.')],
         'note': 'Requiere Internet y tu permiso para enviar la foto, sin metadatos de ubicación, a Firebase y OpenAI. '
                 'Puede haber límites de uso.',
         'alt': 'Wing en español: foto de un mirlo y posibles coincidencias para comparar'},
        {'id': 'identify',
         'label': 'Identificar',
         'title': 'Ponle nombre<br>a lo que escuchas.',
         'intro': 'Ese canto que vuelve cada mañana ya tiene un punto de partida. Abre Wing, graba y revisa las aves '
                  'sugeridas para descubrir quién podría estar cantando.',
         'details': [('Escucha en el momento',
                      'Graba paseos de hasta diez minutos, marca los instantes que te interesan y revisa las '
                      'sugerencias a medida que avanza la grabación.'),
                     ('Recupera un sonido que ya tienes',
                      'Importa un archivo de audio o extrae el sonido de un vídeo para analizarlo y conservarlo junto '
                      'al encuentro.'),
                     ('Añade el contexto',
                      'La fecha y el lugar ayudan a ordenar las sugerencias. Confirma una o varias especies después de '
                      'contrastar lo que has oído.')],
         'note': 'El análisis se realiza en tu iPhone. Las sugerencias son una ayuda para identificar, no una '
                 'confirmación automática.',
         'alt': 'Pantalla Identificar de Wing: botón Escuchar e importación de audio o vídeo'},
        {'id': 'widgets',
         'label': 'Widgets y accesos rápidos',
         'title': 'La próxima ave,<br>a un toque.',
         'intro': 'El ave del día, la escucha y la identificación por foto, directamente desde tus widgets. Wing 1.3 '
                  'amplía los accesos para empezar a descubrir sin buscar la app.',
         'details': [('Naturaleza en tu pantalla de inicio',
                      'Combina el ave del día con los accesos para escuchar e identificar por foto.'),
                     ('También en la pantalla bloqueada',
                      'Añade los widgets compatibles a la pantalla bloqueada para tener tus acciones a mano.'),
                     ('Siri, Atajos y botón de Acción',
                      'Configura las acciones de Wing con la guía paso a paso de Captura rápida en Ajustes. El botón '
                      'de Acción requiere un iPhone compatible.')],
         'note': 'Los widgets usan el estado de acceso de Wing. Abre la app para configurar la suscripción, los '
                 'permisos y el idioma.',
         'alt': 'Pantalla de inicio con los widgets de Wing para el ave del día, escuchar e identificar por foto, '
                'junto al icono de Wing'},
        {'id': 'discover',
         'label': 'Descubrir',
         'title': 'Tu próxima ave<br>empieza aquí.',
         'intro': 'La pantalla Descubrir de Wing 1.3 reúne la escucha y la identificación por foto con la guía, las '
                  'observaciones cercanas y el ave del día.',
         'details': [('Elige cómo empezar',
                      'Escucha un canto o identifica desde una foto con los dos accesos de la pantalla principal.'),
                     ('Explora lo que te rodea',
                      'Abre el mapa de observaciones cercanas o entra en la guía para seguir una nueva pista.'),
                     ('Vuelve a tus descubrimientos',
                      'Consulta el ave del día y retoma tu último encuentro cuando ya tengas registros en el diario.')],
         'note': 'Las observaciones del mapa proceden de registros públicos y no indican presencia en directo. Las '
                 'funciones en línea requieren conexión.',
         'alt': 'Pantalla Descubrir actualizada de Wing en español con accesos a escuchar, identificar por foto, aves '
                'cercanas y guía'},
        {'id': 'guide',
         'label': 'Guía de aves',
         'title': 'Un mundo de aves.<br>Muchas formas de encontrarlo.',
         'intro': 'Explora un catálogo de más de 11.000 especies. Busca un nombre que conoces o empieza por una '
                  'familia, un grupo de aves o una región para afinar tu siguiente descubrimiento.',
         'details': [('Una búsqueda que entiende las pistas',
                      'Encuentra especies por nombre común o científico y busca por familia o grupo, aunque escribas '
                      'las palabras en distinto orden.'),
                     ('Filtros que puedes combinar',
                      'Acota por región, grupo, favoritos, presencia en tu diario o fotografía disponible. Ordena los '
                      'resultados por relevancia o nombre.'),
                     ('Escucha mientras exploras',
                      'Reproduce los cantos de referencia disponibles desde la lista y guarda tus favoritas para '
                      'volver a ellas.')],
         'note': 'La disponibilidad de fotos y cantos depende de las fuentes de cada especie.',
         'alt': 'Guía de Wing con 11.201 especies, búsqueda, favoritos y filtros'},
        {'id': 'species',
         'label': 'Fichas de especies',
         'title': 'Mira de cerca.<br>Reconoce los detalles.',
         'intro': 'Una foto es solo el principio. Abre la ficha de un ave para observar sus rasgos, escuchar su voz y '
                  'entender mejor lo que la hace distinta.',
         'details': [('Fotografías para observar',
                      'Recorre la galería y amplía una imagen para fijarte en el pico, el plumaje o la silueta sin '
                      'perder detalles por el recorte.'),
                     ('Plumajes que cambian',
                      'Compara macho, hembra o juvenil cuando hay imágenes identificadas por la fuente, y consulta la '
                      'descripción y clasificación de la especie.'),
                     ('Cantos y presencia a lo largo del año',
                      'Escucha las grabaciones disponibles y explora mapas mensuales de observaciones. Las fuentes y '
                      'licencias acompañan al contenido.')],
         'note': 'Los mapas muestran observaciones documentadas, no el seguimiento de aves individuales.',
         'alt': 'Ficha del petirrojo europeo en Wing, con fotografía, galería y comparación de plumajes'},
        {'id': 'journal',
         'label': 'Diario de campo',
         'title': 'Cada encuentro<br>merece un recuerdo.',
         'intro': 'No guardes solo el nombre de un ave. Conserva cómo sonaba aquel lugar, la foto que hiciste y las '
                  'pequeñas notas que convertirán un paseo en un recuerdo al que volver.',
         'details': [('Todo junto, con su contexto',
                      'Añade fotos, grabaciones, fecha, lugar, notas y número de aves. Indica si las oíste, las viste '
                      'o las fotografiaste.'),
                     ('Encuentra lo que has vivido',
                      'Busca por ave, lugar o nota, filtra tus encuentros por año o lugar y consulta tu lista de '
                      'especies registradas.'),
                     ('Comparte el recuerdo',
                      'Crea tarjetas a partir de tus encuentros. Las tarjetas para compartir omiten el lugar y las '
                      'coordenadas.')],
         'note': 'La captura muestra un diario de ejemplo. Tus encuentros se guardan en tu dispositivo.',
         'alt': 'Diario de campo de Wing con un avistamiento de ejemplo y su lista de especies'},
        {'id': 'learn',
         'label': 'Aprender',
         'title': 'Aprende a mirar.<br>Y a escuchar.',
         'intro': 'Reconocer aves se aprende prestando atención a las pistas. Wing te acompaña con lecciones cortas, '
                  'práctica y repasos que puedes llevar después al campo.',
         'details': [('Una pequeña escuela de campo',
                      'Seis lecciones sobre silueta, plumaje, oído, entorno, variación y observación respetuosa, con '
                      'ejemplos y un reto para poner en práctica.'),
                     ('Entrena la vista y el oído',
                      'Practica por fotografía, canto o descripción. Elige dificultad, explora colecciones por hábitat '
                      'o dedica un momento a las cinco aves del día.'),
                     ('Aprende también de tus encuentros',
                      'Practica con favoritos y especies de tu diario, reutiliza clips confirmados y repasa las aves '
                      'que te han costado más.')],
         'note': 'El progreso y la actividad se guardan localmente. Las colecciones iniciales de práctica se centran '
                 'en aves europeas.',
         'alt': 'Escuela de campo de Wing con lecciones, cinco aves del día y práctica de reconocimiento'},
        {'id': 'share',
         'label': 'Compartir tus encuentros',
         'title': 'Ese momento<br>merece contarse.',
         'intro': 'Convierte un encuentro de tu diario en una tarjeta para compartir. Wing 1.3 incorpora formatos para '
                  'publicaciones e historias, con la especie y el recuerdo que quieres conservar.',
         'details': [('El formato que necesitas',
                      'Elige publicación 4:5 o historia 9:16 y ajusta el encuadre de la imagen.'),
                     ('El ave, protagonista',
                      'La tarjeta reúne la foto, el nombre de la especie y los datos del encuentro. Las imágenes de '
                      'referencia conservan sus créditos.'),
                     ('Tú eliges el destino',
                      'Comparte la tarjeta mediante la hoja de iOS con la app o persona que elijas.')],
         'note': 'Revisa la tarjeta antes de compartir. Las fotos y notas del diario permanecen en tu dispositivo '
                 'hasta que decidas exportarlas.',
         'alt': 'Editor de tarjetas de Wing en español con un petirrojo, formatos de publicación e historia y botón de '
                'compartir'}],
 'en': [{'id': 'photo',
         'label': 'Identify from a photo',
         'title': 'One photo.<br>A new clue.',
         'intro': 'In Wing 1.3, take a photo or choose one from your library to explore suggested species. Compare '
                  'their features and open a species page to get to know the bird.',
         'details': [('Camera or photo library',
                      'Choose a clear image of the bird. Review it before sending it for identification.'),
                     ('Compare possible matches',
                      'Check the suggested species against the plumage, shape and context. A suggestion does not '
                      'confirm an identification on its own.'),
                     ('Keep the encounter', 'Open the species page and save the sighting to your journal.')],
         'note': 'Requires Internet and permission to send the photo, with location metadata removed, through Firebase '
                 'to OpenAI. Usage limits may apply.',
         'alt': 'Wing in English: a blackbird photo and possible species matches to compare'},
        {'id': 'identify',
         'label': 'Sound identification',
         'title': 'Put a name<br>to what you hear.',
         'intro': 'That song you hear every morning is a place to start. Open Wing, record it and review suggested '
                  'birds to discover who might be singing.',
         'details': [('Listen in the moment',
                      'Record walks of up to ten minutes, mark moments of interest and review suggestions as the '
                      'recording progresses.'),
                     ('Bring a sound you already have',
                      'Import an audio file or extract sound from a video to analyze it and keep it with your '
                      'encounter.'),
                     ('Add the context',
                      'Date and location help rank suggestions. Confirm one or more species after checking what you '
                      'heard.')],
         'note': 'Analysis runs on your iPhone. Suggestions help you identify a bird; they do not automatically '
                 'confirm a species.',
         'alt': 'Wing identification screen with Listen button and audio or video import'},
        {'id': 'widgets',
         'label': 'Widgets and quick access',
         'title': 'Your next bird,<br>just a tap away.',
         'intro': 'The bird of the day, listening and photo identification, straight from your widgets. Wing 1.3 '
                  'expands quick actions so you can start discovering without searching for the app.',
         'details': [('Nature on your Home Screen',
                      'Combine the bird of the day with actions to listen or identify from a photo.'),
                     ('On your Lock Screen too',
                      'Add supported widgets to your Lock Screen to keep Wing actions close.'),
                     ('Siri, Shortcuts and Action button',
                      'Set up Wing actions with the step-by-step Quick capture guide in Settings. The Action button '
                      'requires a compatible iPhone.')],
         'note': 'Widgets use Wing’s access status. Open the app to configure your subscription, permissions and '
                 'language.',
         'alt': 'Home Screen showing only Wing widgets for bird of the day, listening and photo identification '
                'alongside the Wing app icon'},
        {'id': 'discover',
         'label': 'Discover',
         'title': 'Your next bird<br>starts here.',
         'intro': 'Wing 1.3 brings listening and photo identification together with the guide, nearby observations and '
                  'bird of the day on the Discover screen.',
         'details': [('Choose where to start',
                      'Listen to a song or identify from a photo using the two actions on the main screen.'),
                     ('Explore around you',
                      'Open the map of nearby observations or browse the guide to follow a new clue.'),
                     ('Return to your discoveries',
                      'Meet the bird of the day and revisit your latest encounter once you have journal records.')],
         'note': 'Map observations are public records, not live bird locations. Online features require a connection.',
         'alt': 'Updated Wing Discover screen in English with listening, photo identification, nearby birds and guide '
                'actions'},
        {'id': 'guide',
         'label': 'Bird guide',
         'title': 'A world of birds.<br>More ways to find them.',
         'intro': 'Explore a catalog of more than 11,000 species. Search a familiar name or start with a family, bird '
                  'group or region to narrow your next discovery.',
         'details': [('Search with the clues you have',
                      'Find birds by common or scientific name, family or group, even when you enter words in a '
                      'different order.'),
                     ('Combine your filters',
                      'Narrow by region, group, favorites, journal entries or available photography. Sort by relevance '
                      'or name.'),
                     ('Listen as you explore',
                      'Play available reference songs right from the list and save your favorites to come back to '
                      'later.')],
         'note': 'Photo and song availability depends on the sources for each species.',
         'alt': 'Wing guide showing 11,201 species, search, favorites and filters'},
        {'id': 'species',
         'label': 'Species pages',
         'title': 'Look closer.<br>Notice the details.',
         'intro': 'A photograph is only the beginning. Open a bird’s page to study its features, listen to its voice '
                  'and get to know what makes it different.',
         'details': [('Photographs worth a closer look',
                      'Browse the gallery and enlarge an image to study the bill, plumage or silhouette without losing '
                      'detail to a crop.'),
                     ('Plumage through different stages',
                      'Compare male, female or juvenile birds when source-labeled images are available, and read the '
                      'species description and classification.'),
                     ('Songs and observations through the year',
                      'Listen to available recordings and explore monthly observation maps. Sources and licenses '
                      'accompany the content.')],
         'note': 'Maps show documented observations, rather than the movements of individual birds.',
         'alt': 'Wing European Robin page with photograph, gallery and plumage comparison'},
        {'id': 'journal',
         'label': 'Field journal',
         'title': 'Every encounter<br>has a story to keep.',
         'intro': 'Keep more than a bird’s name. Save the sound of a place, the photograph you took and the little '
                  'notes that turn an ordinary walk into a memory you can revisit.',
         'details': [('Everything in its context',
                      'Add photos, recordings, date, place, notes and bird counts. Record whether you heard, saw or '
                      'photographed them.'),
                     ('Find your encounters again',
                      'Search by bird, place or note, filter by year or location and explore your list of recorded '
                      'species.'),
                     ('Share the memory',
                      'Create cards from your encounters. Shared memory cards omit places and coordinates.')],
         'note': 'The screenshot shows an example journal. Your encounters are stored on your device.',
         'alt': 'Wing field journal showing one example sighting and a species list'},
        {'id': 'learn',
         'label': 'Learning',
         'title': 'Learn to look.<br>Learn to listen.',
         'intro': 'Recognizing birds starts with noticing the clues. Wing helps you with short lessons, practice and '
                  'reviews that you can take into the field.',
         'details': [('A pocket field school',
                      'Six lessons cover silhouette, plumage, listening, habitat, variation and respectful '
                      'observation, with examples and a field challenge.'),
                     ('Train your eyes and ears',
                      'Practice using photographs, songs or descriptions. Choose a difficulty, explore habitat '
                      'collections or make time for five birds a day.'),
                     ('Learn from your own encounters',
                      'Practice with favorites and journal species, reuse confirmed recording clips and revisit the '
                      'birds you found harder to recognize.')],
         'note': 'Progress and activity are stored locally. Initial practice collections focus on European birds.',
         'alt': 'Wing field school with lessons, five daily birds and recognition practice'},
        {'id': 'share',
         'label': 'Share your encounters',
         'title': 'A moment<br>worth sharing.',
         'intro': 'Turn a journal encounter into a card to share. Wing 1.3 adds post and story formats, with the '
                  'species and the memory you want to keep.',
         'details': [('Choose your format', 'Select a 4:5 post or 9:16 story and adjust the image framing.'),
                     ('Put the bird first',
                      'Bring together the photo, species name and encounter details. Reference photographs keep their '
                      'attribution.'),
                     ('Choose where it goes',
                      'Use the iOS share sheet to send the card to an app or person of your choice.')],
         'note': 'Review the card before sharing. Journal photos and notes stay on your device until you choose to '
                 'export them.',
         'alt': 'Wing card editor in English showing a robin, post and story formats and the share button'}]}

EXTRAS = {'es': [{'label': 'Explorar el entorno',
         'title': '¿Qué se ha visto cerca?',
         'text': 'Busca observaciones de aves alrededor de tu ubicación o de una zona que elijas en el mapa. Ajusta el '
                 'radio entre 5 y 100 km, cambia el periodo y consulta las especies y sus registros.',
         'detail': 'Puedes filtrar por especie, abrir su ficha y consultar la fecha y la fuente del avistamiento. Los '
                   'datos públicos de GBIF tienen cobertura parcial: son observaciones registradas, no presencia en '
                   'directo.'},
        {'label': 'Conservar tus recuerdos',
         'title': 'Tu diario, bien cuidado.',
         'text': 'Wing guarda tus encuentros en el dispositivo y ofrece copias locales. También puedes elegir una '
                 'carpeta en Archivos o iCloud Drive para las copias automáticas, o exportar e importar un archivo de '
                 'respaldo.',
         'detail': 'La papelera permite recuperar encuentros durante 30 días. Las copias en una carpeta elegida no son '
                   'sincronización en directo entre dispositivos.'}],
 'en': [{'label': 'Explore your surroundings',
         'title': 'What has been seen nearby?',
         'text': 'Look up bird observations around your location or an area you choose on the map. Adjust the radius '
                 'from 5 to 100 km, change the time period and explore species and their records.',
         'detail': 'Filter by species, open its page and check a sighting’s date and source. Public GBIF data has '
                   'partial coverage: these are recorded observations, not live bird locations.'},
        {'label': 'Keep your memories',
         'title': 'A journal worth looking after.',
         'text': 'Wing stores encounters on your device and keeps local backups. You can also choose a folder in Files '
                 'or iCloud Drive for automatic backups, or export and import a backup file.',
         'detail': 'Trash lets you recover encounters for 30 days. Backups to a chosen folder are not live '
                   'synchronization between devices.'}]}

FAQ = {'es': [('¿Wing identifica aves a partir de una foto?',
         'La versión 1.3 incorpora identificación desde la cámara o la fototeca. Con tu permiso, la foto se envía sin '
         'metadatos de ubicación a través de Firebase a OpenAI. Requiere Internet; revisa las coincidencias antes de '
         'confirmar una especie. Las capturas de esta página son un adelanto de esa actualización.'),
        ('¿Qué puedo usar sin conexión?',
         'El análisis del canto, tu diario y el contenido que ya tengas en el dispositivo pueden funcionar sin '
         'conexión. Los mapas, las observaciones cercanas, las imágenes y los cantos remotos pueden necesitar '
         'Internet. La identificación por foto requiere conexión.'),
        ('¿Se envían mis grabaciones para identificarlas?',
         'No. El análisis se realiza en tu iPhone. Los mapas, las consultas de aves cercanas y otros contenidos '
         'utilizan servicios externos cuando los solicitas. Encontrarás el detalle en nuestra política de privacidad.'),
        ('¿En qué idiomas está disponible?',
         'La interfaz de Wing está disponible en inglés, español, francés, alemán, italiano, portugués, neerlandés, '
         'japonés, coreano, chino simplificado, árabe e hindi. Estas capturas muestran la app en español.'),
        ('¿Cómo puedo contactar?',
         'Escribe a <a href="mailto:info@legal-assistant-ai.com">info@legal-assistant-ai.com</a> con el asunto '
         '«Soporte Wing».')],
 'en': [('Can Wing identify a bird from a photo?',
         'Version 1.3 adds identification from the camera or photo library. With your permission, the photo is sent '
         'with location metadata removed through Firebase to OpenAI. Internet is required; compare the matches before '
         'confirming a species. The screenshots on this page preview that update.'),
        ('What can I use offline?',
         'Birdsong analysis, your journal and content already on your device can work offline. Maps, nearby '
         'observations, remote images and reference songs may require an Internet connection. Photo identification '
         'requires a connection.'),
        ('Are my recordings uploaded for identification?',
         'No. Analysis runs on your iPhone. Maps, nearby bird searches and other content use external services when '
         'you request them. Our Privacy Policy explains the details.'),
        ('Which languages are available?',
         'Wing’s interface supports English, Spanish, French, German, Italian, Portuguese, Dutch, Japanese, Korean, '
         'Simplified Chinese, Arabic and Hindi. These screenshots show the app in English.'),
        ('How can I get in touch?',
         'Email <a href="mailto:info@legal-assistant-ai.com">info@legal-assistant-ai.com</a> with the subject “Wing '
         'support”.')]}
