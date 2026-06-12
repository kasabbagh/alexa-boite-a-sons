"""
Alexa Skill - Boîte à Sons
Joue des sons d'animaux, transports, nature, etc.
"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Mapping des mots-clés français vers (audio tag, durée estimée en secondes)
# On répète chaque son pour atteindre ~5 secondes
TARGET_DURATION = 5  # secondes

SOUNDS = {
    # Animaux
    "ours": ("soundbank://soundlibrary/animals/amzn_sfx_bear_groan_roar_01", 3),
    "oiseau": ("soundbank://soundlibrary/animals/amzn_sfx_bird_forest_01", 4),
    "chat": ("soundbank://soundlibrary/animals/amzn_sfx_cat_meow_1x_01", 2),
    "chaton": ("soundbank://soundlibrary/animals/amzn_sfx_cat_purr_01", 4),
    "poulet": ("soundbank://soundlibrary/animals/amzn_sfx_chicken_cluck_01", 2),
    "poule": ("soundbank://soundlibrary/animals/amzn_sfx_chicken_cluck_01", 2),
    "corbeau": ("soundbank://soundlibrary/animals/amzn_sfx_crow_caw_1x_01", 2),
    "chien": ("soundbank://soundlibrary/animals/amzn_sfx_dog_med_bark_1x_02", 2),
    "éléphant": ("soundbank://soundlibrary/animals/amzn_sfx_elephant_01", 3),
    "elephant": ("soundbank://soundlibrary/animals/amzn_sfx_elephant_01", 3),
    "cheval": ("soundbank://soundlibrary/animals/amzn_sfx_horse_neigh_01", 3),
    "galop": ("soundbank://soundlibrary/animals/amzn_sfx_horse_gallop_4x_01", 4),
    "lion": ("soundbank://soundlibrary/animals/amzn_sfx_lion_roar_01", 3),
    "singe": ("soundbank://soundlibrary/animals/amzn_sfx_monkey_chimp_01", 3),
    "rat": ("soundbank://soundlibrary/animals/amzn_sfx_rat_squeaks_01", 2),
    "souris": ("soundbank://soundlibrary/animals/amzn_sfx_rat_squeaks_01", 2),
    "coq": ("soundbank://soundlibrary/animals/amzn_sfx_rooster_crow_01", 3),
    "mouton": ("soundbank://soundlibrary/animals/amzn_sfx_sheep_baa_01", 2),
    "dinde": ("soundbank://soundlibrary/animals/amzn_sfx_turkey_gobbling_01", 3),
    "loup": ("soundbank://soundlibrary/animals/amzn_sfx_wolf_howl_01", 4),
    # Transports
    "avion": ("soundbank://soundlibrary/transportation/amzn_sfx_airplane_takeoff_whoosh_01", 4),
    "vélo": ("soundbank://soundlibrary/transportation/amzn_sfx_bicycle_bell_ring_01", 2),
    "velo": ("soundbank://soundlibrary/transportation/amzn_sfx_bicycle_bell_ring_01", 2),
    "bus": ("soundbank://soundlibrary/transportation/amzn_sfx_bus_drive_past_01", 4),
    "voiture": ("soundbank://soundlibrary/transportation/amzn_sfx_car_accelerate_01", 3),
    "klaxon": ("soundbank://soundlibrary/transportation/amzn_sfx_car_honk_1x_01", 2),
    "moto": ("soundbank://soundlibrary/transportation/amzn_sfx_motorcycle_engine_rev_01", 3),
    "métro": ("soundbank://soundlibrary/transportation/amzn_sfx_subway_passing_01", 4),
    "metro": ("soundbank://soundlibrary/transportation/amzn_sfx_subway_passing_01", 4),
    # Nature
    "tremblement de terre": ("soundbank://soundlibrary/nature/amzn_sfx_earthquake_rumble_01", 4),
    "éclair": ("soundbank://soundlibrary/nature/amzn_sfx_lightning_strike_01", 3),
    "océan": ("soundbank://soundlibrary/nature/amzn_sfx_ocean_wave_1x_01", 4),
    "ocean": ("soundbank://soundlibrary/nature/amzn_sfx_ocean_wave_1x_01", 4),
    "vague": ("soundbank://soundlibrary/nature/amzn_sfx_ocean_wave_on_rocks_1x_01", 4),
    "pluie": ("soundbank://soundlibrary/nature/amzn_sfx_rain_01", 5),
    "orage": ("soundbank://soundlibrary/nature/amzn_sfx_rain_thunder_01", 5),
    "tonnerre": ("soundbank://soundlibrary/nature/amzn_sfx_thunder_rumble_01", 4),
    "rivière": ("soundbank://soundlibrary/nature/amzn_sfx_stream_01", 5),
    "riviere": ("soundbank://soundlibrary/nature/amzn_sfx_stream_01", 5),
    "vent": ("soundbank://soundlibrary/nature/amzn_sfx_strong_wind_whistling_01", 5),
    # Maison
    "porte": ("soundbank://soundlibrary/home/amzn_sfx_door_open_01", 2),
    "sonnette": ("soundbank://soundlibrary/home/amzn_sfx_doorbell_chime_01", 3),
    "cheminée": ("soundbank://soundlibrary/home/amzn_sfx_fireplace_crackle_01", 5),
    "cheminee": ("soundbank://soundlibrary/home/amzn_sfx_fireplace_crackle_01", 5),
    "aspirateur": ("soundbank://soundlibrary/home/amzn_sfx_vacuum_on_01", 4),
    # Humains
    "bébé": ("soundbank://soundlibrary/human/amzn_sfx_baby_big_cry_01", 3),
    "bebe": ("soundbank://soundlibrary/human/amzn_sfx_baby_big_cry_01", 3),
    "applaudissements": ("soundbank://soundlibrary/human/amzn_sfx_crowd_applause_01", 5),
    "bravo": ("soundbank://soundlibrary/human/amzn_sfx_crowd_applause_01", 5),
    "huées": ("soundbank://soundlibrary/human/amzn_sfx_crowd_boo_01", 4),
    "rire": ("soundbank://soundlibrary/human/amzn_sfx_laughter_01", 3),
    "toux": ("soundbank://soundlibrary/human/amzn_sfx_cough_01", 2),
    "éternuement": ("soundbank://soundlibrary/human/amzn_sfx_sneeze_01", 2),
    # Divers
    "feux d'artifice": ("soundbank://soundlibrary/impacts/amzn_sfx_fireworks_01", 4),
    "fantôme": ("soundbank://soundlibrary/magic/amzn_sfx_ghost_spooky_01", 4),
    "fantome": ("soundbank://soundlibrary/magic/amzn_sfx_ghost_spooky_01", 4),
    "trompette": ("soundbank://soundlibrary/musical/amzn_sfx_trumpet_bugle_01", 3),
    "tambour": ("soundbank://soundlibrary/musical/amzn_sfx_drum_comedy_01", 2),
    "guitare": ("soundbank://soundlibrary/musical/amzn_sfx_electric_guitar_01", 3),
}


def get_sound_ssml(sound_name):
    """Génère le SSML avec répétition du son pour atteindre ~5 secondes."""
    src, duration = SOUNDS[sound_name]
    # Calcule combien de fois répéter pour atteindre TARGET_DURATION
    import math
    repeats = max(1, math.ceil(TARGET_DURATION / duration))
    audio_tag = f'<audio src="{src}"/>'
    return audio_tag * repeats


def build_response(speech, should_end_session=False, reprompt=None):
    """Construit la réponse JSON pour Alexa."""
    response = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "SSML",
                "ssml": f"<speak>{speech}</speak>",
            },
            "shouldEndSession": should_end_session,
        },
    }
    if reprompt:
        response["response"]["reprompt"] = {
            "outputSpeech": {
                "type": "SSML",
                "ssml": f"<speak>{reprompt}</speak>",
            }
        }
    return response


def handle_launch(event):
    """Quand l'utilisateur dit 'Alexa, ouvre Boîte à Sons'."""
    speech = "Boîte à sons ouverte ! Dis le nom d'un animal ou d'un son. Par exemple : cheval, voiture, ou lion."
    reprompt = "Quel son veux-tu entendre ?"
    return build_response(speech, should_end_session=False, reprompt=reprompt)


def handle_sound_intent(event):
    """Quand l'utilisateur demande un son."""
    try:
        slots = event["request"]["intent"]["slots"]
        sound_name = slots["son"]["value"].lower().strip()
    except (KeyError, TypeError):
        speech = "Je n'ai pas compris. Dis le nom d'un animal ou d'un véhicule."
        return build_response(speech, should_end_session=False, reprompt="Quel son veux-tu ?")

    if sound_name in SOUNDS:
        audio = get_sound_ssml(sound_name)
        speech = f"{audio}"
        reprompt = "Quel autre son veux-tu ?"
        return build_response(speech, should_end_session=False, reprompt=reprompt)
    else:
        speech = f"Je ne connais pas le son {sound_name}. Essaie cheval, chat, voiture ou lion."
        reprompt = "Quel son veux-tu ?"
        return build_response(speech, should_end_session=False, reprompt=reprompt)


def handle_help(event):
    """Intent d'aide."""
    speech = (
        "Tu peux me demander n'importe quel son. "
        "Par exemple dis : cheval, chien, voiture, lion, pluie, ou tonnerre. "
        "Quel son veux-tu entendre ?"
    )
    return build_response(speech, should_end_session=False, reprompt="Quel son veux-tu ?")


def handle_stop(event):
    """Quand l'utilisateur dit stop ou annuler."""
    speech = "À bientôt !"
    return build_response(speech, should_end_session=True)


def lambda_handler(event, context):
    """Point d'entrée Lambda."""
    logger.info(f"Event: {event}")

    request_type = event["request"]["type"]

    if request_type == "LaunchRequest":
        return handle_launch(event)

    elif request_type == "IntentRequest":
        intent_name = event["request"]["intent"]["name"]

        if intent_name == "PlaySoundIntent":
            return handle_sound_intent(event)
        elif intent_name == "AMAZON.HelpIntent":
            return handle_help(event)
        elif intent_name in ("AMAZON.StopIntent", "AMAZON.CancelIntent"):
            return handle_stop(event)
        elif intent_name == "AMAZON.FallbackIntent":
            speech = "Je n'ai pas compris. Dis le nom d'un animal ou d'un son."
            return build_response(speech, should_end_session=False, reprompt="Quel son veux-tu ?")
        else:
            return handle_sound_intent(event)

    elif request_type == "SessionEndedRequest":
        return build_response("", should_end_session=True)

    return build_response("Une erreur est survenue.", should_end_session=True)
