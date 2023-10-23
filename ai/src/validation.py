from typing import Dict


def validate_rewards(action_rewards: Dict[str, str], external_reward_funcs: str) -> bool:
    if not external_reward_funcs:
        return not any(
            "reward =" not in value
            and "reward=" not in action_rewards[action_name]
            for action_name, value in action_rewards.items()
        )
    else:
        return True
