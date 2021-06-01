# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define j = Character("jhon", color="#333333")
define c = Character("chiaki", color="#DF97CB")

image c1 = "c1.png"
image background = "background2.jpg"
image ofice = "ofice.jfif"


# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene background

    # reproducimos musica de fondo
    play music "audio/intro1.mp3" loop fadein 1.0

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.



    # Presenta las líneas del diálogo.

    "Que dia el de hoy."
    "Después de un dia tan agotador solo quiero pasar a vever un café"
    "No se la verdad que estoy haciendo, quisiera poder mandar todo al diablo"
    "Odio mi trabajo y mi vida en general, no es fácil ser un adulto"
    "si me hubieran dicho que esto es en verdad ser un adulto, tener que trabajar dia y noche y ni siquiera poder disfrutar lo que gano"
    "habría preferido vivir hasta los 20"
    "..."
    "bueno, mejor no digo nada si mi madre me vendrá a tirar las patas"
    "James me recomedó esta cafetería, espero que sea buena"
    "se acerca una chica desde la mesa de al frente"

    show c1 at right:
        xzoom 0.40 yzoom 0.40

    c "Buen día señor, ¿en que le puedo ayudar?"
    show c1 at center
    "vaya, pensé que chica más linda"
    j "Hola, ¿podrías darme la carta?"
    "es como obvio eso no?, que chica tan atolondrada"
    c "Oh! lo siento señor, aqui esta la carta"
    "se puso muy nerviosa"
    j "mmm veamos"


    # MOSTRAMOS POR PANTALLA OPCIONES
    menu:
        "Café y un Struddel":
            jump escena2

label escena2:

    # cargamos backgoutn
    scene ofice

    # dialogos
    " Despues de que esta chica trajera mi pedido se vino a mi mente por un momento la imagen de la oficina"
    "Dios, no puedo descansar ni aunque trata de relajarme"
    "pensar en todo ese lugar, y cada dia partiendome el lomo trabajando, en fin mejor trato de pensar en otra cosa"

    menu:
        "me tomo la tasa de café y saboreo mi struddel":
            jump escena3

label escena3:

    # cargamos backgorund
    scene background with fade

    "la chica se acerca a mi timidamente"

    # cargamos a chiaki
    show c1 at right:
        xzoom 0.40 yzoom 0.40


    "Disculpe..."

    show c1 at center

    c "¿puedo ayudarlo en algo mas?"
    j "la verdad es que si, ¡cual es tu nombre?"
    c "disculpe?"
    "no se por qué pero tenia ganas de jugar un poco con esta chica"
    j "te pregunte cual es tu nombre, me has atendido muy bien, quisiera saber tu nombre y agradecerte"
    "lo dije en voz alta sonriendole, esto pareció coivirla un poco"
    c "me llamo chiaki señor, un gusto..."
    "su voz apena salía, que encantadora pensé para mi"
    j "chiaki eh? que lindo nombre, yo me llamo Kojiro, pero por alguna razon todos me conocen como Jhon"
    c "de verdad señor? que interesante"
    "se rio de manera muy tierna"

    menu:
        "muy bien, tengo ganas de jugar un poco más, ¿debería hacerlo?":
            jump invitacion

        "deberia dejarlo por hoy":
            jump casa

# escena invitacion
label invitacion:

    j "chiaki, te apetecería salir uno de estos dias?"
    "la pobre chica se intimidó"
    c "eh? este... bueno..."
    "mucho para ti eh?"
    c "por favor, dejame agradecerte por este excelente servicio"
    c "bueno, esta bien señor"
    j "excelente, te parece mañana?"
    "estas a punto de caer pequeña confiada"
    c "a las 3, despues de que termine mi turno"
    j "me parece bien"
    jump fin

# escena casa

label casa:

    "creo que mejor volvemos a la vida real, estoy seguro de que nunca acpetaria salir conmigo"
    j "muchas gracias por el café chiaki, estubo delicioso, un placer conocerte, pero ahora debo irme"
    c "oh... entiendo señor, esperamos volverlo a ver"
    "se fue algo cabisbaja, ¡estará esperando que la invite? no, no lo creo, quin querría salir con un salaryman"

    jump fin


label fin:

    # Finaliza el juego:

return
