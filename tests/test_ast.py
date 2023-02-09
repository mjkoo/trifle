from trifle import *


def test_image() -> None:
    image = Image()

    command = "echo foo > /foo"

    @image.stage(from_="debian:latest")
    def final(stage: Stage) -> None:
        stage.instructions.append(RunInstruction(command=command))

    assert image.default_stage == "final"
    assert command in image.render()
