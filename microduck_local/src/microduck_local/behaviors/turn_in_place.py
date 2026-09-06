from .core import *

_lifted_foot_up, _stance_foot_planted, _one_leg_hold = _one_leg("right", "left")

def _both_feet_penalty(env) -> float:
    return -float(_both_feet_down(env))

_register(Behavior(
    id="turn_in_place",
    emoji="🎯",
    title="Turn in place with one foot",
    description=("Rotate on one foot without translating or falling"),
    how_it_learns=(
        "The duck earns a little for staying upright the whole time, more "
        "as it continually rotates at a steady pace, and achieves the biggest "
        "payout when it fully finishes rotating. "
        "The duck is penalized for placing the other foot on the ground. "
    ),
    keywords=("turn on one foot", "spin on one foot", "rotate on one foot"),
    terms=(
        RewardTerm("spin_fast", "Points for yaw speed", 2.5, _spin_rate),
        RewardTerm("one_leg_hold", "Points for one leg", 1.0, _one_leg_hold),
        RewardTerm("stay_upright", "Points for staying upright", 0.6, _upright),
        RewardTerm("both_feet_down", "Negative points for having both feet on the ground", 1.0, _both_feet_penalty, is_penalty=True),
        RewardTerm("stay_home", "Penalty for wandering away from the starting spot",
                        1.0, _stay_home_pen, is_penalty=True),
        ),
    default_steps=3_000_000,
    success_metric="spinning around on one foot",
    episode_s=15.0,
    scene="walk",
    terminate_on_fall=True,
    # The turn direction is command-conditioned, but the recipe still fixes
    # the left foot as the stance foot and the right foot as lifted.
    symmetric=False,
))
