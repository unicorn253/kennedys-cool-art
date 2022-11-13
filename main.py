@namespace
class SpriteKind:
    unicorn = SpriteKind.create()

def on_a_pressed():
    music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
            5000,
            1,
            231,
            49,
            5000,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.UNTIL_DONE)
    scene.set_background_color(2)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

mySprite = sprites.create(assets.image("""
        hearts and stars
    """),
    SpriteKind.unicorn)
scaling.scale_by_pixels(mySprite, 20, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
controller.move_sprite(mySprite, 100, 100)