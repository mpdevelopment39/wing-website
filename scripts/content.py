"""Bilingual product copy grounded in Wing's app and AppScreens source captures."""

FEATURES = {
    'es': [
        dict(id='identify', label='Identificar', title='Ponle nombre<br>a lo que escuchas.', intro='Ese canto que vuelve cada mañana ya tiene un punto de partida. Abre Wing, graba y revisa las aves sugeridas para descubrir quién podría estar cantando.', details=[
            ('Escucha en el momento', 'Graba paseos de hasta diez minutos, marca los instantes que te interesan y revisa las sugerencias a medida que avanza la grabación.'),
            ('Recupera un sonido que ya tienes', 'Importa un archivo de audio o extrae el sonido de un vídeo para analizarlo y conservarlo junto al encuentro.'),
            ('Añade el contexto', 'La fecha y el lugar ayudan a ordenar las sugerencias. Confirma una o varias especies después de contrastar lo que has oído.')], note='El análisis se realiza en tu iPhone. Las sugerencias son una ayuda para identificar, no una confirmación automática.', alt='Pantalla Identificar de Wing: botón Escuchar e importación de audio o vídeo'),
        dict(id='widgets', label='Widgets y accesos rápidos', title='La próxima ave,<br>a un toque.', intro='Deja un poco de naturaleza en tu pantalla de inicio. Conoce otra especie a través del ave del día y ten siempre a mano el acceso para empezar a escuchar.', details=[
            ('Un ave para descubrir', 'El widget muestra una fotografía y el nombre de una especie. Tócalo para abrir su ficha y seguir explorando.'),
            ('Escucha sin dar rodeos', 'El widget de captura te lleva directamente a la grabación. También tienes accesos desde la pantalla bloqueada y la pulsación larga del icono.'),
            ('A tu manera', 'Usa Siri, Atajos o configura el botón de acción para abrir la escucha de Wing cuando oigas algo interesante.')], note='Los widgets siguen el idioma del sistema y las actualizaciones que permite iOS.', alt='Widgets reales de Wing: ave del día y acceso Escuchar en la pantalla de inicio de iPhone'),
        dict(id='guide', label='Guía de aves', title='Un mundo de aves.<br>Muchas formas de encontrarlo.', intro='Explora un catálogo de más de 11.000 especies. Busca un nombre que conoces o empieza por una familia, un grupo de aves o una región para afinar tu siguiente descubrimiento.', details=[
            ('Una búsqueda que entiende las pistas', 'Encuentra especies por nombre común o científico y busca por familia o grupo, aunque escribas las palabras en distinto orden.'),
            ('Filtros que puedes combinar', 'Acota por región, grupo, favoritos, presencia en tu diario o fotografía disponible. Ordena los resultados por relevancia o nombre.'),
            ('Escucha mientras exploras', 'Reproduce los cantos de referencia disponibles desde la lista y guarda tus favoritas para volver a ellas.')], note='La disponibilidad de fotos y cantos depende de las fuentes de cada especie.', alt='Guía de Wing con 11.201 especies, búsqueda, favoritos y filtros'),
        dict(id='species', label='Fichas de especies', title='Mira de cerca.<br>Reconoce los detalles.', intro='Una foto es solo el principio. Abre la ficha de un ave para observar sus rasgos, escuchar su voz y entender mejor lo que la hace distinta.', details=[
            ('Fotografías para observar', 'Recorre la galería y amplía una imagen para fijarte en el pico, el plumaje o la silueta sin perder detalles por el recorte.'),
            ('Plumajes que cambian', 'Compara macho, hembra o juvenil cuando hay imágenes identificadas por la fuente, y consulta la descripción y clasificación de la especie.'),
            ('Cantos y presencia a lo largo del año', 'Escucha las grabaciones disponibles y explora mapas mensuales de observaciones. Las fuentes y licencias acompañan al contenido.')], note='Los mapas muestran observaciones documentadas, no el seguimiento de aves individuales.', alt='Ficha del petirrojo europeo en Wing, con fotografía, galería y comparación de plumajes'),
        dict(id='journal', label='Diario de campo', title='Cada encuentro<br>merece un recuerdo.', intro='No guardes solo el nombre de un ave. Conserva cómo sonaba aquel lugar, la foto que hiciste y las pequeñas notas que convertirán un paseo en un recuerdo al que volver.', details=[
            ('Todo junto, con su contexto', 'Añade fotos, grabaciones, fecha, lugar, notas y número de aves. Indica si las oíste, las viste o las fotografiaste.'),
            ('Encuentra lo que has vivido', 'Busca por ave, lugar o nota, filtra tus encuentros por año o lugar y consulta tu lista de especies registradas.'),
            ('Comparte el recuerdo', 'Crea tarjetas a partir de tus encuentros. Las tarjetas para compartir omiten el lugar y las coordenadas.')], note='La captura muestra un diario de ejemplo. Tus encuentros se guardan en tu dispositivo.', alt='Diario de campo de Wing con un avistamiento de ejemplo y su lista de especies'),
        dict(id='learn', label='Aprender', title='Aprende a mirar.<br>Y a escuchar.', intro='Reconocer aves se aprende prestando atención a las pistas. Wing te acompaña con lecciones cortas, práctica y repasos que puedes llevar después al campo.', details=[
            ('Una pequeña escuela de campo', 'Seis lecciones sobre silueta, plumaje, oído, entorno, variación y observación respetuosa, con ejemplos y un reto para poner en práctica.'),
            ('Entrena la vista y el oído', 'Practica por fotografía, canto o descripción. Elige dificultad, explora colecciones por hábitat o dedica un momento a las cinco aves del día.'),
            ('Aprende también de tus encuentros', 'Practica con favoritos y especies de tu diario, reutiliza clips confirmados y repasa las aves que te han costado más.')], note='El progreso y la actividad se guardan localmente. Las colecciones iniciales de práctica se centran en aves europeas.', alt='Escuela de campo de Wing con lecciones, cinco aves del día y práctica de reconocimiento')
    ],
    'en': [
        dict(id='identify', label='Sound identification', title='Put a name<br>to what you hear.', intro='That song you hear every morning is a place to start. Open Wing, record it and review suggested birds to discover who might be singing.', details=[
            ('Listen in the moment', 'Record walks of up to ten minutes, mark moments of interest and review suggestions as the recording progresses.'),
            ('Bring a sound you already have', 'Import an audio file or extract sound from a video to analyze it and keep it with your encounter.'),
            ('Add the context', 'Date and location help rank suggestions. Confirm one or more species after checking what you heard.')], note='Analysis runs on your iPhone. Suggestions help you identify a bird; they do not automatically confirm a species.', alt='Wing identification screen with Listen button and audio or video import'),
        dict(id='widgets', label='Widgets and quick access', title='Your next bird,<br>just a tap away.', intro='Keep a little nature on your Home Screen. Meet a different species with the daily bird widget and keep a shortcut to listening close at hand.', details=[
            ('A bird to discover', 'The widget shows a photograph and species name. Tap it to open the bird’s page and keep exploring.'),
            ('Go straight to listening', 'The capture widget takes you straight to recording. Quick access is also available from the Lock Screen and by holding the app icon.'),
            ('Make it yours', 'Use Siri, Shortcuts or configure the Action button to open Wing’s listening screen when you hear something interesting.')], note='Widgets follow the system language and the update schedule allowed by iOS.', alt='Actual Wing daily bird and Listen widgets on an iPhone Home Screen'),
        dict(id='guide', label='Bird guide', title='A world of birds.<br>More ways to find them.', intro='Explore a catalog of more than 11,000 species. Search a familiar name or start with a family, bird group or region to narrow your next discovery.', details=[
            ('Search with the clues you have', 'Find birds by common or scientific name, family or group, even when you enter words in a different order.'),
            ('Combine your filters', 'Narrow by region, group, favorites, journal entries or available photography. Sort by relevance or name.'),
            ('Listen as you explore', 'Play available reference songs right from the list and save your favorites to come back to later.')], note='Photo and song availability depends on the sources for each species.', alt='Wing guide showing 11,201 species, search, favorites and filters'),
        dict(id='species', label='Species pages', title='Look closer.<br>Notice the details.', intro='A photograph is only the beginning. Open a bird’s page to study its features, listen to its voice and get to know what makes it different.', details=[
            ('Photographs worth a closer look', 'Browse the gallery and enlarge an image to study the bill, plumage or silhouette without losing detail to a crop.'),
            ('Plumage through different stages', 'Compare male, female or juvenile birds when source-labeled images are available, and read the species description and classification.'),
            ('Songs and observations through the year', 'Listen to available recordings and explore monthly observation maps. Sources and licenses accompany the content.')], note='Maps show documented observations, rather than the movements of individual birds.', alt='Wing European Robin page with photograph, gallery and plumage comparison'),
        dict(id='journal', label='Field journal', title='Every encounter<br>has a story to keep.', intro='Keep more than a bird’s name. Save the sound of a place, the photograph you took and the little notes that turn an ordinary walk into a memory you can revisit.', details=[
            ('Everything in its context', 'Add photos, recordings, date, place, notes and bird counts. Record whether you heard, saw or photographed them.'),
            ('Find your encounters again', 'Search by bird, place or note, filter by year or location and explore your list of recorded species.'),
            ('Share the memory', 'Create cards from your encounters. Shared memory cards omit places and coordinates.')], note='The screenshot shows an example journal. Your encounters are stored on your device.', alt='Wing field journal showing one example sighting and a species list'),
        dict(id='learn', label='Learning', title='Learn to look.<br>Learn to listen.', intro='Recognizing birds starts with noticing the clues. Wing helps you with short lessons, practice and reviews that you can take into the field.', details=[
            ('A pocket field school', 'Six lessons cover silhouette, plumage, listening, habitat, variation and respectful observation, with examples and a field challenge.'),
            ('Train your eyes and ears', 'Practice using photographs, songs or descriptions. Choose a difficulty, explore habitat collections or make time for five birds a day.'),
            ('Learn from your own encounters', 'Practice with favorites and journal species, reuse confirmed recording clips and revisit the birds you found harder to recognize.')], note='Progress and activity are stored locally. Initial practice collections focus on European birds.', alt='Wing field school with lessons, five daily birds and recognition practice')
    ]
}

EXTRAS = {
    'es': [
        dict(label='Explorar el entorno', title='¿Qué se ha visto cerca?', text='Busca observaciones de aves alrededor de tu ubicación o de una zona que elijas en el mapa. Ajusta el radio entre 5 y 100 km, cambia el periodo y consulta las especies y sus registros.', detail='Puedes filtrar por especie, abrir su ficha y consultar la fecha y la fuente del avistamiento. Los datos públicos de GBIF tienen cobertura parcial: son observaciones registradas, no presencia en directo.'),
        dict(label='Conservar tus recuerdos', title='Tu diario, bien cuidado.', text='Wing guarda tus encuentros en el dispositivo y ofrece copias locales. También puedes elegir una carpeta en Archivos o iCloud Drive para las copias automáticas, o exportar e importar un archivo de respaldo.', detail='La papelera permite recuperar encuentros durante 30 días. Las copias en una carpeta elegida no son sincronización en directo entre dispositivos.')],
    'en': [
        dict(label='Explore your surroundings', title='What has been seen nearby?', text='Look up bird observations around your location or an area you choose on the map. Adjust the radius from 5 to 100 km, change the time period and explore species and their records.', detail='Filter by species, open its page and check a sighting’s date and source. Public GBIF data has partial coverage: these are recorded observations, not live bird locations.'),
        dict(label='Keep your memories', title='A journal worth looking after.', text='Wing stores encounters on your device and keeps local backups. You can also choose a folder in Files or iCloud Drive for automatic backups, or export and import a backup file.', detail='Trash lets you recover encounters for 30 days. Backups to a chosen folder are not live synchronization between devices.')]
}

FAQ = {
    'es': [
        ('¿Wing identifica aves a partir de una foto?', 'La identificación automática es por sonido. Las fotos sirven para explorar especies, practicar y conservar tus avistamientos en el diario.'),
        ('¿Qué puedo usar sin conexión?', 'El análisis del canto, tu diario y el contenido que ya tengas en el dispositivo pueden funcionar sin conexión. Los mapas, las observaciones cercanas, las imágenes y los cantos remotos pueden necesitar Internet.'),
        ('¿Se envían mis grabaciones para identificarlas?', 'No. El análisis se realiza en tu iPhone. Los mapas, las consultas de aves cercanas y otros contenidos utilizan servicios externos cuando los solicitas. Encontrarás el detalle en nuestra política de privacidad.'),
        ('¿En qué idiomas está disponible?', 'La interfaz de Wing está disponible en inglés, español, francés, alemán, italiano, portugués, neerlandés, japonés, coreano, chino simplificado, árabe e hindi. Estas capturas muestran la app en español.'),
        ('¿Cómo puedo contactar?', 'Escribe a <a href="mailto:info@legal-assistant-ai.com">info@legal-assistant-ai.com</a> con el asunto «Soporte Wing».')],
    'en': [
        ('Can Wing identify a bird from a photo?', 'Automatic identification uses sound. Photos help you explore species, practice and preserve your sightings in the journal.'),
        ('What can I use offline?', 'Birdsong analysis, your journal and content already on your device can work offline. Maps, nearby observations, remote images and reference songs may require an Internet connection.'),
        ('Are my recordings uploaded for identification?', 'No. Analysis runs on your iPhone. Maps, nearby bird searches and other content use external services when you request them. Our Privacy Policy explains the details.'),
        ('Which languages are available?', 'Wing’s interface supports English, Spanish, French, German, Italian, Portuguese, Dutch, Japanese, Korean, Simplified Chinese, Arabic and Hindi. These screenshots show the app in English.'),
        ('How can I get in touch?', 'Email <a href="mailto:info@legal-assistant-ai.com">info@legal-assistant-ai.com</a> with the subject “Wing support”.')]
}
