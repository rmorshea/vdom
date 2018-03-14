from .svg import svg, polygon, g, path

def nteract(size=400):
    # TODO: We only support the purple nteract logo for now, support the others via some palette switching
    return svg(
        polygon(
            points="284.12 330 200 281.53 200 122.88 284.12 171.36 284.12 330",
            fill="#a3b7d6"),
        polygon(
            points="284.12 330 200 281.53 200 122.88 284.12 171.36 284.12 330",
            fill="#a3b7d6"),
        polygon(
            points="200 122.88 115.88 171.36 115.88 330 200 281.53 200 122.88",
            fill="#c8d4e6"),
        polygon(
            points=
            "200 70 70 144.92 92.94 158.14 200 96.44 307.06 158.14 307.06 316.78 330 303.56 330 144.92 200 70",
            fill="#5d779b"),
        polygon(
            points="92.94 158.14 70 144.92 70 303.56 92.94 316.78 92.94 158.14",
            fill="#334866"),
        polygon(
            points=
            "92.94 158.14 92.94 316.78 115.88 330 115.88 171.36 92.94 158.14",
            fill="#a3b7d6"),
        polygon(
            points=
            "92.94 158.14 200 96.44 307.06 158.14 307.06 316.78 284.12 330 284.12 171.36 200 122.88 115.88 171.36 92.94 158.14",
            fill="#edf1f7"),
        polygon(
            points=
            "200 158.13 253.53 188.98 253.53 250.68 200 281.53 146.47 250.68 146.47 188.98 200 158.13",
            fill="#ccb3ff"),
        polygon(
            points=
            "200 281.53 200 219.83 146.47 188.98 146.47 250.68 200 281.53",
            fill="#8518f2"),
        polygon(
            points=
            "200 219.83 253.53 188.98 253.53 250.68 200 281.53 200 219.83",
            fill="#af8afa"),
        xmlns="http://www.w3.org/2000/svg",
        width=str(size),
        height=str(size),
        viewBox="0 0 400 400")


def jupyter(size=40):
    width = str(size)
    # Preserve aspect ratio + spacing (note that viewBox automatically scales for us)
    height = str(round(51 / 39.) * size)

    return svg(
        g(path(
            d=
            "M5.89353 2.844c.02536.58765-.12268 1.16967-.42538 1.67245-.3027.50277-.74647.9037-1.27516 1.15206-.52869.24837-1.11855.333-1.69494.2432-.57639-.08981-1.11342-.35001-1.543152-.7477C.52517 4.76633.222056 4.24903.0839037 3.67757c-.138152-.57146-.1051337-1.1714.0948773-1.72393C.378793 1.4011.736809.920817 1.20754.573538 1.67826.226259 2.24055.0275919 2.82326.00267229 3.60389-.0307115 4.36573.249789 4.94142.782551c.57569.532759.91814 1.274209.95211 2.061449z",
            fill="#767677",
            transform="translate(31.3 .31)"),
          path(
              d=
              "M18.2646 7.13411C10.4145 7.13411 3.55872 4.2576 0 0c1.32539 3.8204 3.79556 7.13081 7.0686 9.47303 3.2731 2.34217 7.1871 3.60037 11.2004 3.60037s7.9273-1.2582 11.2004-3.60037C32.7424 7.13081 35.2126 3.8204 36.538 0c-3.5675 4.2576-10.4232 7.13411-18.2734 7.13411z",
              fill="#F37726",
              transform="translate(1.74 30.98)"),
          path(
              d=
              "M18.2733 5.93931c7.8502 0 14.706 2.87652 18.2647 7.13409-1.3254-3.82037-3.7956-7.13078-7.0686-9.473C26.1963 1.25818 22.2823 0 18.269 0S10.3417 1.25818 7.0686 3.6004C3.79556 5.94262 1.32539 9.25303 0 13.0734c3.56745-4.24877 10.4232-7.13409 18.2733-7.13409z",
              fill="#F37726",
              transform="translate(1.73 4.48)"),
          path(
              d=
              "M7.42789 3.58338c.03219.74092-.15434 1.47481-.53596 2.10875-.38162.63394-.94118 1.13943-1.60782 1.45247-.66664.31303-1.4104.41954-2.13709.30603-.7267-.11351-1.40366-.44193-1.94518-.94368C.660328 6.0052.27861 5.35268.105017 4.63202c-.1735927-.72067-.1312531-1.47708.121658-2.17346C.479587 1.76217.931697 1.15713 1.52576.720033 2.11983.282935 2.82914.0334395 3.56389.00313344 4.54667-.0374033 5.50529.316706 6.22961.987835c.72432.671125 1.15523 1.604515 1.19828 2.595545z",
              fill="#989798",
              transform="translate(1.8 42.81)"),
          path(
              d=
              "M2.27471 4.39629c-.43108.01879-.858-.09184-1.22672-.31786-.368722-.22603-.662662-.55729-.844619-.95187-.1819574-.39458-.2437508-.83473-.1775594-1.26475C.0920031 1.4318.283204 1.03126.575213.710883.867222.39051 1.24691.164708 1.66622.0620592c.41931-.1026489.85939-.0775306 1.26454.0721758.40515.149706.75716.41727 1.01146.768825.2543.35156.39947.7713.41713 1.2061.02364.58191-.18257 1.14953-.57338 1.5783-.39081.42878-.93431.6837-1.51126.70883z",
              fill="#6F7070",
              transform="translate(.36 5.06)"),
          style={"mix-blend-mode": "normal"}),
        xmlns="http://www.w3.org/2000/svg",
        width=width,
        height=height,
        viewBox="0 0 39 51"
    )