namespace SpriteKind {
    export const unicorn = SpriteKind.create()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 5000, 1, 255, 255, 5000, SoundExpressionEffect.Vibrato, InterpolationCurve.Curve), SoundExpressionPlayMode.InBackground)
    scene.setBackgroundColor(2)
})
let mySprite = sprites.create(assets.image`hearts and stars`, SpriteKind.unicorn)
scaling.scaleByPixels(mySprite, 20, ScaleDirection.Uniformly, ScaleAnchor.Middle)
controller.moveSprite(mySprite, 100, 100)
