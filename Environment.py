from models import Observation, Action, Reward
from tasks import get_random_task
from grader import grade_classification, grade_response, grade_resolution

MAX_STEPS = 5

class SupportEnv:

    def __init__(self):
        self.reset()

    def reset(self):
        self.task = get_random_task()
        self.steps = 0
        self.done = False

        self.state_data = {
            "classified": False,
            "replied": False,
            "category_pred": None
        }

        return self._get_observation()

    def _get_observation(self):
        return Observation(
            ticket_id=self.task["id"],
            customer_message=self.task["message"],
            customer_history=[],
            priority=self.task["priority"],
            category_hint=None,
            time_elapsed=self.steps
        )

    def step(self, action: Action):
        if self.done:
            return self._get_observation(), Reward(score=0, breakdown={}), True, {}

        self.steps += 1
        reward_score = 0
        breakdown = {}

        # Classification
        if action.action_type == "classify_ticket":
            self.state_data["classified"] = True
            self.state_data["category_pred"] = action.content

            class_score = grade_classification(
                action.content, self.task["category"]
            )

            reward_score += 0.3 * class_score
            breakdown["classification"] = class_score

        # Reply
        elif action.action_type == "reply_to_customer":
            self.state_data["replied"] = True

            response_score = grade_response(
                action.content, self.task["solution_keywords"]
            )

            reward_score += 0.7 * response_score
            breakdown["response"] = response_score

        # Close
        elif action.action_type == "close_ticket":
            self.done = True

            class_score = grade_classification(
                self.state_data["category_pred"],
                self.task["category"]
            )

            response_score = grade_response(
                action.content or "",
                self.task["solution_keywords"]
            )

            final_score = grade_resolution(class_score, response_score)
            reward_score = final_score
            breakdown["final"] = final_score

        # Penalty for too many steps
        if self.steps >= MAX_STEPS:
            self.done = True
            reward_score -= 0.2

        return self._get_observation(), Reward(score=reward_score, breakdown=breakdown), self.done, {}

    def state(self):
        return self.state_data
